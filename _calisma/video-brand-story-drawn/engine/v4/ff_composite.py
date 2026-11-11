# Opening clip: wherever the AI video shows the same thing as the real photo (desk, props, the settled spread), show the
# PHOTO; keep the video only where something really moves (hand, sleeve, cover, page). Props stop drifting, and by the
# time the notebook lies open the frame is already the sharp photo, so the cut to the film cannot be seen.
# usage: python ff_composite.py ALIGNED.mp4 PHOTO.png OUT.mp4
import sys, subprocess, numpy as np, cv2
IN, PH, OUT = sys.argv[1:4]
W, H = 1080, 1920
ref = cv2.cvtColor(cv2.imread(PH), cv2.COLOR_BGR2RGB).astype(np.float32)
rb = cv2.GaussianBlur(ref, (0, 0), 5)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', IN, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
F = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '30', '-i', '-',
                      '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', OUT], stdin=subprocess.PIPE)
NB = np.zeros((H, W), np.float32); NB[500:1430, :] = 1               # the notebook (in the settled frame)
NB = cv2.GaussianBlur(NB, (0, 0), 30)
TL0, TL1 = 2.88, 2.98                                                # the turned page has landed
PG = np.zeros((H, W), np.float32); PG[600:1340, 0:995] = 1; PG = cv2.GaussianBlur(PG, (0, 0), 6)
STRIP = np.zeros((H, W), np.float32); STRIP[:, 930:] = 1; STRIP = cv2.GaussianBlur(STRIP, (0, 0), 20)
T0, T1 = 5.35, 5.85                                                  # hand gone from the pages: the whole notebook dissolves to the photo
vb = cv2.GaussianBlur(F[int(6.5 * 30)].astype(np.float32), (0, 0), 5)          # last frame of the clip: hand gone, everything settled
prev = None
for i, fr in enumerate(F):
    t = i / 30; f = fr.astype(np.float32)
    d = np.abs(cv2.GaussianBlur(f, (0, 0), 5) - vb).max(2)          # vs the video's OWN settled frame: props never count as motion
    m = (d > 16).astype(np.float32)                                  # desk: video only where something really moves (hand, sleeve, shadow)
    m = cv2.GaussianBlur(cv2.dilate(m, np.ones((25, 25), np.uint8)), (0, 0), 5)
    if prev is not None: m = np.maximum(m, prev * 0.45)
    prev = m
    k = 1 - np.clip((t - T0) / (T1 - T0), 0, 1); k = k * k * (3 - 2 * k)
    kp = 1 - np.clip((t - TL0) / (TL1 - TL0), 0, 1); kp = kp * kp * (3 - 2 * kp)
    # the pages: the AI video re-draws (garbles) the writing, so once the turned page has landed the page area is the photo;
    # only the strip at the right edge where the hand still holds the page stays video until the hand has gone
    pages = PG * (1 - kp)                                            # 0..1 share of the photo inside the pages
    nb_video = NB * np.maximum(k, 0) if t < T1 else NB * 0
    nb_video = np.where(PG > 0, np.minimum(nb_video, 1 - pages + m * STRIP), nb_video)
    m = np.maximum(m * (1 - NB), nb_video)
    out = ref * (1 - m[..., None]) + f * m[..., None]
    p.stdin.write(np.clip(out, 0, 255).astype(np.uint8).tobytes())
p.stdin.close(); p.wait(); print('done', OUT, len(F))
