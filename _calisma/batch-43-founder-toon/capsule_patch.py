"""Track the (near-static) capsule in a Veo clip and composite the sharp capsule from the clip's own first-frame still.
Veo re-renders small product labels illegibly at 720p; the still has the corrected white label.
Two passes: (1) multi-scale template tracking per frame, (2) the track is fitted with a smooth low-order curve
and the patch is warped at sub-pixel precision, so it never jitters (user 2026-10-13: "titriyomuş gibi duruyo").
usage: capsule_patch.py clip.mp4 still.png x0 y0 x1 y1 out.mp4   (box = capsule bbox in still pixels)"""
import sys, subprocess, numpy as np, cv2
from PIL import Image, ImageDraw, ImageFilter
clip, still, x0, y0, x1, y1, out = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7]), sys.argv[7]
probe = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=width,height,r_frame_rate', '-of', 'csv=p=0', clip], capture_output=True, text=True).stdout.strip().split(',')
W, H = int(probe[0]), int(probe[1]); fps = probe[2]
st = Image.open(still).convert('RGB'); s = W / st.width; sh = round(st.height * s)
st = st.resize((W, sh), Image.LANCZOS); off = (sh - H) // 2
px0, py0, px1, py1 = round(x0 * s) - 2, round(y0 * s) - off - 2, round(x1 * s) + 2, round(y1 * s) - off + 2
patch = np.asarray(st.crop((px0, py0 + off, px1, py1 + off))).astype(np.float32)
pw, ph = patch.shape[1], patch.shape[0]
m = Image.new('L', (pw * 4, ph * 4), 0); d = ImageDraw.Draw(m)
d.rounded_rectangle((6, 6, pw * 4 - 6, ph * 4 - 6), radius=pw * 2 - 8, fill=255)
alpha = np.asarray(m.resize((pw, ph), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.8))).astype(np.float32) / 255.0

def frames():
    dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', clip, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    while True:
        b = dec.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        yield np.frombuffer(b, np.uint8).reshape(H, W, 3)

# pass 1: track centre + scale
pg = cv2.cvtColor(patch.astype(np.uint8), cv2.COLOR_RGB2GRAY)
cx, cy, cs = px0 + pw / 2, py0 + ph / 2, 1.0; track = []
for f in frames():
    g = cv2.cvtColor(f, cv2.COLOR_RGB2GRAY); best = None
    for sc in np.arange(max(0.9, cs - 0.03), min(1.25, cs + 0.031), 0.005):
        tw, th = round(pw * sc), round(ph * sc); tg = cv2.resize(pg, (tw, th), interpolation=cv2.INTER_AREA)
        sx0, sy0 = int(max(0, cx - tw / 2 - 40)), int(max(0, cy - th / 2 - 40))
        win = g[sy0:min(H, sy0 + th + 80), sx0:min(W, sx0 + tw + 80)]
        if win.shape[0] < th or win.shape[1] < tw: continue
        res = cv2.matchTemplate(win, tg, cv2.TM_CCOEFF_NORMED); _, v, _, loc = cv2.minMaxLoc(res)
        if best is None or v > best[0]: best = (v, sx0 + loc[0] + tw / 2, sy0 + loc[1] + th / 2, sc)
    _, cx, cy, cs = best; track.append((cx, cy, cs))
tr = np.array(track); t = np.arange(len(tr))
# pass 2: smooth low-order fit (camera drift is slow and continuous)
fit = np.stack([np.polyval(np.polyfit(t, tr[:, k], 3), t) for k in range(3)], 1)
print('raw jitter px', round(float(np.abs(np.diff(tr[:, 0])).mean()), 2), '-> fitted residual', round(float(np.abs(tr[:, 0] - fit[:, 0]).mean()), 2))
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', fps, '-i', '-',
                        '-i', clip, '-map', '0:v', '-map', '1:a?', '-c:v', 'libx264', '-crf', '14', '-pix_fmt', 'yuv420p', '-c:a', 'copy', '-shortest', out], stdin=subprocess.PIPE)
gains = []
for i, f in enumerate(frames()):
    cx, cy, sc = fit[i]
    M = np.float32([[sc, 0, cx - pw * sc / 2], [0, sc, cy - ph * sc / 2]])   # sub-pixel scale + translate
    P = cv2.warpAffine(patch, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT)
    A_ = cv2.warpAffine(alpha, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)[..., None]
    F = f.astype(np.float32); msk = A_[..., 0] > 0.5
    gains.append((F[msk].mean() + 1) / (P[msk].mean() + 1))
    gain = float(np.clip(np.mean(gains[-12:]), 0.94, 1.06))                 # smoothed brightness match
    enc.stdin.write((P * gain * A_ + F * (1 - A_)).clip(0, 255).astype(np.uint8).tobytes())
enc.stdin.close(); enc.wait(); print('frames', len(tr))
