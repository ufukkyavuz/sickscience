"""Batch 27 — DropOff free-trial UGC test (9:16, 1080x1920, 24 fps).
Kling 3.0 selfie clip (raw_kling.mp4, speech included) + PIL overlays/cards + ffmpeg.
The clip's tube is redrawn badly between ~4.95 and 6.75 s, so that stretch is covered by the checklist card (real PNG).
usage: python render27.py -> out/u27_dropoff_trial.mp4"""
import os, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import shutil

HERE = os.path.dirname(os.path.abspath(__file__)); SS = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
W, H, FPS = 1080, 1920, 24
FD = os.path.expanduser('~/Library/Fonts/')
FB, FR = FD + 'FoundersGrotesk-Bold.otf', FD + 'FoundersGrotesk-Regular.otf'
FF = shutil.which("ffmpeg")
COBALT = (18, 40, 150); SKY = (150, 200, 255); WHITE = (255, 255, 255)

# timeline (s)
HOOK_END, CARD_END, CLIP_END, TOTAL = 3.45, 6.80, 8.70, 11.2
CHECKS = [(3.54, 'Pay shipping only.'), (4.92, 'Try it for 21 days.'), (6.54, 'Love it or return it.')]

def f(p, s): return ImageFont.truetype(p, s)

def read_clip():
    cmd = [FF, '-v', 'error', '-i', os.path.join(HERE, 'raw_kling.mp4'), '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}',
           '-r', str(FPS), '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    raw = subprocess.run(cmd, capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)

def cobalt_bg(cy=930):
    y, x = np.mgrid[0:H, 0:W]; r = np.sqrt((x - W / 2) ** 2 + ((y - cy) * 0.8) ** 2); g = np.clip(1 - r / 900, 0, 1) ** 2
    a = np.full((H, W, 3), COBALT, float) + g[..., None] * np.array([30, 45, 90])
    return Image.fromarray(a.clip(0, 255).astype(np.uint8))

TUBE = Image.open(os.path.join(SS, 'Products/png/ERH_7488.png')).convert('RGBA'); TUBE = TUBE.crop(TUBE.split()[-1].getbbox())
def tube(h): return TUBE.resize((round(TUBE.width * h / TUBE.height), h), Image.LANCZOS)
LOGO = Image.open(os.path.join(HERE, 'assets/logo_white.png'))

def shadow(im, cx, by, w):
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).ellipse((cx - w, by - 14, cx + w, by + 16), fill=150); sh = sh.filter(ImageFilter.GaussianBlur(12))
    return Image.composite(Image.new('RGB', (W, H), (8, 18, 70)), im, sh)

def ease(t): t = max(0, min(1, t)); return 1 - (1 - t) ** 3

# ---- static layers
CARD = cobalt_bg(1000); T1 = tube(700); CARD = shadow(CARD, 870, 1230, 115); CARD.paste(T1, (870 - T1.width // 2, 1230 - 700), T1)
d = ImageDraw.Draw(CARD); d.text((65, 300), '$0 TODAY.', font=f(FB, 150), fill=WHITE)
END = Image.open(os.path.join(HERE, 'assets/endcard.png')).convert('RGB')

def hook_overlay(img, t):
    d = ImageDraw.Draw(img, 'RGBA'); a = ease(t / 0.35)
    txt = 'I PAID $0 FOR THIS.'; fo = f(FB, 104); w = d.textlength(txt, font=fo)
    x = (W - w) / 2; y = 300 + 30 * (1 - a)
    pad = 28; d.rounded_rectangle((x - pad, y - 18, x + w + pad, y + 112), 22, fill=(255, 255, 255, int(235 * a)))
    d.text((x, y), txt, font=fo, fill=(18, 40, 150, int(255 * a)))
    return img

def card_frame(t):
    img = CARD.copy(); d = ImageDraw.Draw(img, 'RGBA')
    for i, (ts, s) in enumerate(CHECKS):
        a = ease((t - ts) / 0.3)
        if a <= 0: continue
        y = 620 + i * 190; x = 65 + 40 * (1 - a)
        d.ellipse((x, y + 4, x + 72, y + 76), fill=(*SKY, int(255 * a)))
        d.line([(x + 18, y + 42), (x + 31, y + 56), (x + 55, y + 28)], fill=(18, 40, 150, int(255 * a)), width=9, joint='curve')
        lines = {'Pay shipping only.': 'Pay shipping\nonly.', 'Try it for 21 days.': 'Try it for\n21 days.', 'Love it or return it.': 'Love it or\nreturn it.'}[s]
        d.multiline_text((x + 96, y - 2), lines, font=f(FB, 64), fill=(255, 255, 255, int(255 * a)), spacing=4)
    return img

def end_frame(t):
    s = 1.0 + 0.03 * ease(t / (TOTAL - CLIP_END))
    im = END.resize((round(W * s), round(H * s)), Image.LANCZOS)
    return im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H))

def main():
    clip = read_clip(); n = round(TOTAL * FPS)
    p = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-i', os.path.join(HERE, 'raw_kling.mp4'), '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-pix_fmt', 'yuv420p',
                          '-crf', '18', '-c:a', 'aac', '-b:a', '192k', '-af', f'apad=whole_dur={TOTAL}', '-t', str(TOTAL),
                          os.path.join(OUT, 'u27_dropoff_trial.mp4')], stdin=subprocess.PIPE)
    for k in range(n):
        t = k / FPS
        if t < HOOK_END: img = hook_overlay(Image.fromarray(clip[min(k, len(clip) - 1)]), t)
        elif t < CARD_END: img = card_frame(t)
        elif t < CLIP_END: img = Image.fromarray(clip[min(k, len(clip) - 1)])
        else: img = end_frame(t - CLIP_END)
        p.stdin.write(np.asarray(img.convert('RGB')).tobytes())
    p.stdin.close(); p.wait(); print('ok', n)

if __name__ == '__main__':
    main()
