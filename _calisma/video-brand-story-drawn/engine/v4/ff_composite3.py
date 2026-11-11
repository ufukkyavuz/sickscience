# Opening, simple and clean (no per-pixel motion masks):
#  - pure AI video while the notebook opens;
#  - when the turned page lands, ONE rectangle over the two pages (left of the hand) switches to the real photo, so the
#    AI never re-draws the writing;
#  - once the hand has gone, the whole frame dissolves slowly into the photo (= first frame of the film).
# usage: python ff_composite3.py ALIGNED.mp4 PHOTO.png OUT.mp4 DESK_LAYER.png
import sys, subprocess, numpy as np, cv2
IN, PH, OUT = sys.argv[1:4]
from PIL import Image
DL = np.asarray(Image.open(sys.argv[4]).convert('RGBA').resize((1080, 1920), Image.LANCZOS)).astype(np.float32)
DA = DL[..., 3:4] / 255; DC = DL[..., :3]   # founders' photos on the desk: there from the first frame
W, H = 1080, 1920
ref = cv2.cvtColor(cv2.imread(PH), cv2.COLOR_BGR2RGB).astype(np.float32)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-t', '6.9', '-i', IN, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
F = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
PG = np.zeros((H, W), np.float32); PG[598:1342, 0:990] = 1; PG = cv2.GaussianBlur(PG, (0, 0), 5)[..., None]
LP = np.zeros((H, W), np.float32); LP[598:1342, 0:505] = 1; LP = cv2.GaussianBlur(LP, (0, 0), 4)[..., None]   # left page: still once the cover has landed
PINK = np.array([238, 158, 232], np.float32)
def unyellow(f):   # the AI clip still has the old yellow highlighter on the turning sheet -> our pink
    r, g, b = f[..., 0], f[..., 1], f[..., 2]
    y = np.clip((np.minimum(r, g) - b - 40) / 60, 0, 1) * np.clip((g - 120) / 60, 0, 1)
    y[:560] = 0; y[1380:] = 0                       # notebook only (the pineapple stays yellow)
    y = cv2.GaussianBlur(y, (0, 0), 1.2)[..., None]
    lum = (0.3 * r + 0.59 * g + 0.11 * b)[..., None] / 215
    return f * (1 - y) + np.clip(PINK * lum, 0, 255) * y
def ss(x): x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '30', '-i', '-',
                      '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', OUT], stdin=subprocess.PIPE)
for i, fr in enumerate(F):
    t = i / 30; f = fr.astype(np.float32); f = f * (1 - DA) + DC * DA
    if 1.5 < t < 3.0: f = unyellow(f)
    a_pg = np.maximum(PG * ss((t - 2.88) / 0.10), LP * ss((t - 2.34) / 0.06))   # left page early, both pages when the sheet has landed
    a_all = ss((t - 5.85) / 0.75)                 # everything -> photo after the hand has left
    a = np.maximum(a_pg, a_all)
    out = f * (1 - a) + ref * a
    p.stdin.write(np.clip(out, 0, 255).astype(np.uint8).tobytes())
p.stdin.close(); p.wait(); print('done', OUT, len(F))
