# Opening, simple and clean (no per-pixel motion masks):
#  - pure AI video while the notebook opens;
#  - when the turned page lands, ONE rectangle over the two pages (left of the hand) switches to the real photo, so the
#    AI never re-draws the writing;
#  - once the hand has gone, the whole frame dissolves slowly into the photo (= first frame of the film).
# usage: python ff_composite2.py ALIGNED.mp4 PHOTO.png OUT.mp4
import sys, subprocess, numpy as np, cv2
IN, PH, OUT = sys.argv[1:4]
W, H = 1080, 1920
ref = cv2.cvtColor(cv2.imread(PH), cv2.COLOR_BGR2RGB).astype(np.float32)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-t', '6.9', '-i', IN, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
F = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
PG = np.zeros((H, W), np.float32); PG[598:1342, 0:990] = 1; PG = cv2.GaussianBlur(PG, (0, 0), 5)[..., None]
def ss(x): x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '30', '-i', '-',
                      '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', OUT], stdin=subprocess.PIPE)
for i, fr in enumerate(F):
    t = i / 30; f = fr.astype(np.float32)
    a_pg = ss((t - 2.88) / 0.10)                  # pages -> photo when the page has landed
    a_all = ss((t - 5.85) / 0.75)                 # everything -> photo after the hand has left
    a = np.maximum(PG * a_pg, a_all)
    out = f * (1 - a) + ref * a
    p.stdin.write(np.clip(out, 0, 255).astype(np.uint8).tobytes())
p.stdin.close(); p.wait(); print('done', OUT, len(F))
