# Slightly angled camera: every frame of the finished film gets the same gentle perspective (top farther, bottom nearer,
# like a photographer standing at the desk) plus shallow depth of field at the far top and the near bottom edge.
# usage: python tilt.py IN.mp4 OUT.mp4   (audio is copied)   |   python tilt.py IN.png OUT.png
import sys, subprocess, numpy as np, cv2
IN, OUT = sys.argv[1:3]
W, H = 1080, 1920
D = 0.13 * W                                     # bottom edge inset: how far the near side is magnified
src = np.float32([[0, 0], [W, 0], [W - D, H - 0.03 * H], [D, H - 0.03 * H]])
dst = np.float32([[0, 0], [W, 0], [W, H], [0, H]])
M = cv2.getPerspectiveTransform(src, dst)
R = cv2.getRotationMatrix2D((W / 2, H / 2), 1.6, 1.07)                  # the camera is also turned a little, as held by hand
M = np.vstack([R, [0, 0, 1]]) @ M
y = np.linspace(0, 1, H, dtype=np.float32)[:, None, None]
far = np.clip((0.16 - y) / 0.16, 0, 1) ** 1.5     # top 16 %: softening toward the far edge
near = np.clip((y - 0.90) / 0.10, 0, 1) ** 1.5    # bottom 10 %: a touch soft, nearest to the lens
def tilt(fr):
    o = cv2.warpPerspective(fr, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    b = cv2.GaussianBlur(o, (0, 0), 2.6)
    w = np.maximum(far, near * 0.7)
    return (o * (1 - w) + b * w).astype(np.uint8)
if IN.endswith('.png') or IN.endswith('.jpg'):
    cv2.imwrite(OUT, tilt(cv2.imread(IN).astype(np.float32))); sys.exit()
dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', IN, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '30', '-i', '-', '-i', IN,
                        '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '22', '-preset', 'slow', '-pix_fmt', 'yuv420p', '-c:a', 'copy', OUT], stdin=subprocess.PIPE)
n = 0
while True:
    buf = dec.stdout.read(W * H * 3)
    if len(buf) < W * H * 3: break
    enc.stdin.write(tilt(np.frombuffer(buf, np.uint8).reshape(H, W, 3).astype(np.float32)).tobytes()); n += 1
enc.stdin.close(); enc.wait(); print('done', OUT, n)
