"""Cut products out of a photo shot on a white seamless (OpenCV grabCut).

Usage: python cutout.py in.png out.png x0 y0 x1 y1
The box (pixels of the source) must contain all the products. Output is an RGBA
PNG the same size as the source: use it as a layer above giant type in Figma,
so the type appears to sit behind the products. Contact shadows stay in the
photo layer underneath.
"""
import sys
import cv2
import numpy as np

src, dst = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = map(int, sys.argv[3:7])
img = cv2.imread(src)
mask = np.zeros(img.shape[:2], np.uint8)
bgd, fgd = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
cv2.grabCut(img, mask, (x0, y0, x1 - x0, y1 - y0), bgd, fgd, 6, cv2.GC_INIT_WITH_RECT)
fg = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 255, 0).astype(np.uint8)
# drop soft floor-shadow blobs: keep pixels that differ from the white backdrop
diff = cv2.absdiff(img, cv2.GaussianBlur(img, (0, 0), 60)).max(axis=2)
sat = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)[..., 1]
keep = ((sat > 25) | (diff > 18) | (img.min(axis=2) < 200)).astype(np.uint8) * 255
fg = cv2.bitwise_and(fg, cv2.dilate(keep, np.ones((9, 9), np.uint8)))
n, lab, stats, _ = cv2.connectedComponentsWithStats(fg)
big = np.zeros_like(fg)
for i in range(1, n):
    if stats[i, cv2.CC_STAT_AREA] > 4000:
        big[lab == i] = 255
big = cv2.morphologyEx(big, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))
alpha = cv2.GaussianBlur(big, (0, 0), 1.2)
out = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
out[..., 3] = alpha
cv2.imwrite(dst, out)
