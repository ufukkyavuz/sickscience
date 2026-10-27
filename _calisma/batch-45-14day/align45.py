"""Align the day-by-day profile stills: mirror left-facing shots, then a similarity transform that puts the ear and
the nose tip on the same two points in every frame (removes head tilt / distance, keeps the jaw-neck line honest)."""
import cv2, numpy as np, os, sys
SRC = sys.argv[1]; OUTD = sys.argv[2]
# key: (file, flip, ear(x,y), nose(x,y)) in 2160x3840 source pixels, read off grid overlays
# client day numbering (their edit): d3 = IMG_2417 pink pyjamas, d5 = IMG_2458, d8 = IMG_2602 glasses,
# d10 = IMG_2638 white tee, d14 = IMG_8738 (user, 2026-10-14: the result is at 14 days)
P = {'d0': (False, (670, 1550), (1246, 1590)), 'd3': (True, (1280, 1580), (736, 1560)),
     'd5': (False, (890, 1530), (1436, 1560)), 'd8': (False, (920, 1520), (1440, 1520)),
     'd10': (False, (965, 1470), (1480, 1580)), 'd14': (True, (1040, 1680), (510, 1660))}
def warp(img, ear, nose, dst_ear, dst_nose, size):
    s = np.array(nose, float) - ear; d = np.array(dst_nose, float) - dst_ear
    sc = np.linalg.norm(d) / np.linalg.norm(s); ang = np.arctan2(d[1], d[0]) - np.arctan2(s[1], s[0])
    ang = float(np.clip((ang + np.pi) % (2 * np.pi) - np.pi, -np.radians(4), np.radians(4)))   # never tilt the room
    c, si = sc * np.cos(ang), sc * np.sin(ang); M = np.array([[c, -si, 0], [si, c, 0]])
    M[:, 2] = np.array(dst_ear) - M[:, :2] @ np.array(ear, float)
    return cv2.warpAffine(img, M, size, flags=cv2.INTER_LANCZOS4, borderMode=cv2.BORDER_REPLICATE)
for k, (flip, ear, nose) in P.items():
    im = cv2.imread(os.path.join(SRC, k + '.png'))
    if flip:
        im = im[:, ::-1].copy(); ear = (2159 - ear[0], ear[1]); nose = (2159 - nose[0], nose[1])
    full = warp(im, ear, nose, (330, 900), (730, 900), (1080, 1920))            # full-frame jump cut
    half = warp(im, ear, nose, (130, 900), (430, 900), (540, 1920))             # one half of the split
    cv2.imwrite(os.path.join(OUTD, k + '_full.png'), full); cv2.imwrite(os.path.join(OUTD, k + '_half.png'), half)
print('ok')
