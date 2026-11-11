# Make the Veo opening land exactly on the notebook film's first frame: geometry (homography) and colour are eased in
# over the second half of the clip, so the cut to the photo is invisible.  usage: python veo_align.py VEO.mp4 FIRST_FRAME.png OUT.mp4
import sys, subprocess, numpy as np, cv2
VEO, REF, OUT = sys.argv[1:4]
import os
W, H = 1080, 1920; TEND = float(os.environ.get('TEND', 3.7)); TCUT = float(os.environ.get('TCUT', 3.4)); R0 = float(os.environ.get('R0', 1.3))
ref = cv2.cvtColor(cv2.imread(REF), cv2.COLOR_BGR2RGB)
raw = subprocess.run(['ffmpeg', '-v', 'error', '-t', str(TEND), '-i', VEO, '-vf', f'fps=30,scale={W}:{H}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
F = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
end = F[min(len(F) - 1, int(TCUT * 30))]                                   # frame that sits under the cross-fade
g1, g2 = cv2.cvtColor(end, cv2.COLOR_RGB2GRAY), cv2.cvtColor(ref, cv2.COLOR_RGB2GRAY)
orb = cv2.SIFT_create(6000)
k1, d1 = orb.detectAndCompute(g1, None); k2, d2 = orb.detectAndCompute(g2, None)
m = cv2.BFMatcher().knnMatch(d1, d2, k=2); good = [a for a, b in m if a.distance < 0.7 * b.distance]
Hm, inl = cv2.findHomography(np.float32([k1[a.queryIdx].pt for a in good]), np.float32([k2[a.trainIdx].pt for a in good]), cv2.RANSAC, 3.0)
print('matches', len(good), 'inliers', int(inl.sum())); print(np.round(Hm, 4)); np.save(OUT.replace('.mp4', '_H.npy'), Hm)
# colour: per-channel mean/std in Lab, measured on the aligned end frame
we = cv2.warpPerspective(end, Hm, (W, H), borderMode=cv2.BORDER_REPLICATE)
la, lb = cv2.cvtColor(we, cv2.COLOR_RGB2LAB).astype(np.float32), cv2.cvtColor(ref, cv2.COLOR_RGB2LAB).astype(np.float32)
ma, sa, mb, sb_ = la.mean((0, 1)), la.std((0, 1)), lb.mean((0, 1)), lb.std((0, 1))
def ss(a): a = min(1, max(0, a)); return a * a * (3 - 2 * a)
p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', '30', '-i', '-',
                      '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', OUT], stdin=subprocess.PIPE)
for i, fr in enumerate(F):
    t = i / 30; k = ss((t - R0) / (TCUT - R0))
    Hk = np.eye(3) * (1 - k) + Hm * k
    o = cv2.warpPerspective(fr, Hk, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    if k > 0:
        L = cv2.cvtColor(o, cv2.COLOR_RGB2LAB).astype(np.float32)
        L2 = (L - ma) / np.maximum(sa, 1e-3) * sb_ + mb
        o = cv2.cvtColor(np.clip(L * (1 - k) + L2 * k, 0, 255).astype(np.uint8), cv2.COLOR_LAB2RGB)
    z = 1.0                  # the camera starts a slow push that the notebook film continues
    if z > 1: o = cv2.warpAffine(o, np.float32([[z, 0, W / 2 * (1 - z)], [0, z, H / 2 * (1 - z)]]), (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    p.stdin.write(np.ascontiguousarray(o).tobytes())
p.stdin.close(); p.wait(); print('done', OUT)
