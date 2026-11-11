"""Enlarge a generated bottle in place from its own pixels, keeping its base line.
Usage: python bottle_grow.py in.png out.png '<json>'
json: {"x0":..,"y0":..,"x1":..,"base":..,"scale":..,"reflect":0}
  x0,x1,y0 = bottle's left, right, top in px; base = y where it stands.
  reflect = px of floor reflection under the base to scale too (fades out).
The bottle is cut with a capsule-shaped soft mask, so the wall, plinth and shadow stay."""
import json, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

src, dst, c = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])
img = Image.open(src).convert("RGB")
x0, x1, y0, base, k = c["x0"], c["x1"], c["y0"], c["base"], c["scale"]
ref = c.get("reflect", 0)
cx = (x0 + x1) / 2
pad = 6
box = (x0 - pad, y0 - pad, x1 + pad, base + ref + pad)
crop = img.crop(box)
W, H = round(crop.width * k), round(crop.height * k)
big = crop.resize((W, H), Image.LANCZOS)
left = round(cx - (cx - box[0]) * k)
top = round(base - (base - box[1]) * k)
mask = Image.new("L", (W, H), 0)
d = ImageDraw.Draw(mask)
bw, bh = (x1 - x0) * k, (base - y0) * k
mx = (W - bw) / 2
my = base - top - bh
d.rounded_rectangle((mx, my, mx + bw, my + bh), radius=bw * 0.42, fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(1.6))
if ref:
    r = Image.new("L", (W, H), 0)
    a = np.zeros((H, W), np.uint8)
    y = round(base - top)
    n = H - y
    a[y:, int(mx):int(mx + bw)] = np.linspace(200, 0, n).astype(np.uint8)[:, None]
    r = Image.fromarray(a).filter(ImageFilter.GaussianBlur(10))
    mask = Image.fromarray(np.maximum(np.array(mask), np.array(r)))
img.paste(big, (left, top), mask)
img.save(dst)
print("ok", left, top, W, H, "new h", round(bh), "new w", round(bw))
