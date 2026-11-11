"""Dark vertical lettering on chrome -> white, background estimated per column.
usage: whiten_col.py in out x0 y0 x1 y1"""
import sys
import numpy as np
from PIL import Image
src, dst, x0, y0, x1, y1 = sys.argv[1], sys.argv[2], *map(int, sys.argv[3:7])
a = np.asarray(Image.open(src).convert("RGB")).astype(float)
box = a[y0:y1, x0:x1]
lum = box.mean(axis=2)
bg = np.percentile(lum, 85, axis=0)            # per column
bgc = np.stack([np.percentile(box[..., c], 85, axis=0) for c in range(3)], -1)
alpha = np.clip((0.75 * bg - lum) / np.maximum(0.75 * bg, 1), 0, 1) ** 0.6

white = np.array([248, 248, 250.0])
a2 = np.clip(alpha * 1.6, 0, 1)[..., None]; out = box * (1 - a2) + white * a2
keep = alpha == 0
out[keep] = box[keep]
a[y0:y1, x0:x1] = np.clip(out, 0, 255)
Image.fromarray(a.astype(np.uint8)).save(dst)
