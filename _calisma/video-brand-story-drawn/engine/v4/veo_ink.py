# Put the finished notebook's ink into the Veo opening, so the drawings are on the pages while the notebook opens.
# Ink = ratio (finished cover frame / blank cover frame), multiplied onto each Veo frame ONLY where that frame shows the
# page itself: a local correlation of the grid texture against the settled blank page says where paper is visible
# (cover, hand and sleeve have no matching grid, so the ink stays hidden under them; hand shadows keep it, darkened).
# usage: python veo_ink.py VEO_ALIGNED.mp4 BLANK.png FULL.png OUT.mp4
import sys, subprocess, numpy as np, cv2
VEO, BLANK, FULL, OUT = sys.argv[1:5]
W, H = 1080, 1920
rd = lambda p: cv2.cvtColor(cv2.imread(p), cv2.COLOR_BGR2RGB).astype(np.float32)
blank, full = rd(BLANK), rd(FULL)
R = np.clip((full + 1) / (blank + 1), 0, 1.05)
inkmask = cv2.GaussianBlur((np.abs(full - blank).max(2) > 10).astype(np.float32), (0, 0), 2) > 0.02
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', VEO, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
F = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
ref = F[-1].astype(np.float32)                                   # settled, aligned blank spread
Hm = np.load(VEO.replace('.mp4', '_H.npy'))
def Hk_of(t):
    k = np.clip((t - 1.3) / 2.1, 0, 1); k = k * k * (3 - 2 * k)
    return np.eye(3) * (1 - k) + Hm * k                              # same ramp as veo_align.py
def to_frame(img, t, interp=cv2.INTER_LINEAR):                       # settled coords -> where the (static) notebook sits in frame t
    M = Hk_of(t) @ np.linalg.inv(Hm)
    return cv2.warpPerspective(img, M, (W, H), flags=interp, borderMode=cv2.BORDER_REPLICATE)
def hp(img):
    g = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
    return g - cv2.GaussianBlur(g, (0, 0), 2.5)
K = (41, 41)
def ss(x, a, c): x = np.clip((x - a) / (c - a), 0, 1); return x * x * (3 - 2 * x)
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '30', '-i', '-',
                      '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', OUT], stdin=subprocess.PIPE)
for i, fr in enumerate(F):
    t = i / 30
    f = fr.astype(np.float32); a = hp(f)
    ref_t = to_frame(ref, t); Rt = to_frame(R, t); im_t = (to_frame(inkmask.astype(np.uint8), t, cv2.INTER_NEAREST) > 0).astype(np.uint8)
    if t >= 1.7:                                                     # each page settles on its own: refine its position by ECC on the grid texture
        for (x0, x1) in ((20, 540), (540, 1070)):
            roi = (slice(600, 1330), slice(x0, x1))
            A = hp(ref_t)[roi]; B = a[roi]
            wm = np.eye(3, dtype=np.float32)
            try:
                _, wm = cv2.findTransformECC(A, B, wm, cv2.MOTION_HOMOGRAPHY, (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 60, 1e-5), None, 5)
            except cv2.error:
                continue
            T = np.array([[1, 0, -x0], [0, 1, -600], [0, 0, 1]], np.float32); M = np.linalg.inv(T) @ wm @ T
            if abs(M[0, 2]) > 40 or abs(M[1, 2]) > 40: continue
            for img in (ref_t, Rt):
                img[:, x0:x1] = cv2.warpPerspective(img, M, (W, H), flags=cv2.INTER_LINEAR | cv2.WARP_INVERSE_MAP, borderMode=cv2.BORDER_REPLICATE)[:, x0:x1]
            im_t[:, x0:x1] = cv2.warpPerspective(im_t, M, (W, H), flags=cv2.INTER_NEAREST | cv2.WARP_INVERSE_MAP)[:, x0:x1]
    im_t = im_t > 0
    b = hp(ref_t); mb = cv2.blur(b, K); vb = cv2.blur(b * b, K) - mb * mb
    ma = cv2.blur(a, K); va = cv2.blur(a * a, K) - ma * ma
    ncc = (cv2.blur(a * b, K) - ma * mb) / np.sqrt(np.maximum(va * vb, 1e-3))
    vis = ss(ncc, 0.18, 0.42)
    vis = cv2.morphologyEx(vis, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
    vis = cv2.GaussianBlur(cv2.erode(vis, np.ones((7, 7), np.uint8)), (0, 0), 4)
    vis = np.where(im_t, vis, 0)[..., None]
    out = f * (1 + (Rt - 1) * vis)
    p.stdin.write(np.clip(out, 0, 255).astype(np.uint8).tobytes())
    if i % 20 == 0: print(i, float(vis.mean()), flush=True)
p.stdin.close(); p.wait(); print('done', OUT)
