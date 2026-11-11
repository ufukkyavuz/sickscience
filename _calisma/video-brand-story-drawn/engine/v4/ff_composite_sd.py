# Seedance opening (aligned): pure video while the hand opens the notebook, then a soft whole-frame dissolve into the
# film's first frame once the hand has left. usage: python ff_composite_sd.py ALIGNED.mp4 PHOTO.png OUT.mp4 T0 DUR
import sys, subprocess, numpy as np, cv2
IN, PH, OUT, T0, DUR = sys.argv[1], sys.argv[2], sys.argv[3], float(sys.argv[4]), float(sys.argv[5])
W, H = 1080, 1920
ref = cv2.cvtColor(cv2.imread(PH), cv2.COLOR_BGR2RGB).astype(np.float32)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', IN, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
F = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
def ss(x): x = min(1.0, max(0.0, x)); return x * x * (3 - 2 * x)
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '30', '-i', '-',
                      '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', OUT], stdin=subprocess.PIPE)
for i, fr in enumerate(F):
    a = ss((i / 30 - T0) / DUR)
    p.stdin.write(np.clip(fr.astype(np.float32) * (1 - a) + ref * a, 0, 255).astype(np.uint8).tobytes())
p.stdin.close(); p.wait(); print('done', OUT, len(F))
