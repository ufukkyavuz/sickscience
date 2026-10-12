"""Replace an oversized generated bottle with the real product PNG at true scale.
Usage: python bottle_rescale.py in.png out.png x0 y0 x1 y1 src_dy png_path new_h cx base_y
  (x0,y0,x1,y1) = box around the generated bottle (incl. its contact shadow), filled with the wall patch from src_dy px above;
  the bottom 30 px of the box are blended by inpainting so the plinth edge stays clean.
  png_path = real product PNG (transparent); new_h = target height in px; (cx, base_y) = where it stands."""
import sys, cv2, numpy as np
from PIL import Image, ImageFilter, ImageEnhance
src, dst = sys.argv[1], sys.argv[2]
x0, y0, x1, y1, dy = map(int, sys.argv[3:8]); png = sys.argv[8]; nh, cx, by = map(int, sys.argv[9:12])
im = cv2.imread(src); H, W = im.shape[:2]
out = im.copy()
import os
dx = int(os.environ.get('DX', '0'))
patch = (im[y0:y1, x0 - dx:x1 - dx] if dx else im[y0 - dy:y1 - dy, x0:x1]).copy().astype(np.float32)
# per-row tone match: shift each patch row so its edges match the real wall next to the box
ref = np.median(patch.reshape(-1, 3), 0)
shift = np.zeros((y1 - y0, 3), np.float32); last = np.zeros(3, np.float32)
for i, y in enumerate(range(y0, y1)):
    nb = np.concatenate([im[y, max(0, x0 - 30):x0], im[y, x1:x1 + 30]]).astype(np.float32)
    sat = (nb.max(1) - nb.min(1)); ok = nb[(np.abs(nb - ref).sum(1) < 90) & (sat < 90)]
    if len(ok) > 6:
        last = ok.mean(0) - np.concatenate([patch[i, :12], patch[i, -12:]]).mean(0)
    shift[i] = last
shift = cv2.GaussianBlur(shift[:, None, :], (1, 0), sigmaX=0, sigmaY=25)[:, 0, :] if False else cv2.blur(shift, (1, 41))
patch = np.clip(patch + shift[:, None, :], 0, 255).astype(np.uint8)
m = np.zeros((H, W), np.float32); m[y0:y1, x0:x1] = 1; m = cv2.GaussianBlur(m, (0, 0), 6)[..., None]
full = im.copy(); full[y0:y1, x0:x1] = patch
out = (im * (1 - m) + full * m).astype(np.uint8)
band = np.zeros((H, W), np.uint8); band[max(y1 - 40, y0):y1 + 10, x0 - 10:x1 + 10] = 255
plinth = out.copy(); plinth = cv2.inpaint(plinth, band, 7, cv2.INPAINT_TELEA)
bm = cv2.GaussianBlur((band > 0).astype(np.float32), (0, 0), 3)[..., None]
out = (out * (1 - bm) + plinth * bm).astype(np.uint8)
bg = Image.fromarray(cv2.cvtColor(out, cv2.COLOR_BGR2RGB))
p = Image.open(png).convert('RGBA'); p = p.crop(p.split()[-1].getbbox())
nw = round(p.width * nh / p.height); p = p.resize((nw, nh), Image.LANCZOS)
rgb = ImageEnhance.Contrast(p.convert('RGB')).enhance(0.94)
a = np.asarray(rgb).astype(np.float32); warm = np.asarray(bg.crop((x0, y0, x1, y1)).resize((1, 1))).reshape(3).astype(np.float32)
a = a * 0.95 + warm * 0.05; rgb = Image.fromarray(a.clip(0, 255).astype(np.uint8))
p = Image.merge('RGBA', (*rgb.split(), p.split()[-1]))
sh = Image.new('L', bg.size, 0)
from PIL import ImageDraw
ImageDraw.Draw(sh).ellipse((cx - nw * 0.6, by - 8, cx + nw * 0.6, by + 10), fill=130); sh = sh.filter(ImageFilter.GaussianBlur(6))
bg = Image.composite(Image.new('RGB', bg.size, (110, 90, 95)), bg, sh.point(lambda v: int(v * 0.5)))
bg.paste(p, (cx - nw // 2, by - nh), p)
g = np.asarray(bg).astype(np.float32); reg = g[by - nh - 10:by + 10, cx - nw // 2 - 10:cx - nw // 2 + nw + 10]; reg += np.random.normal(0, 2.0, reg.shape[:2] + (1,))
Image.fromarray(g.clip(0, 255).astype(np.uint8)).save(dst); print('ok', dst, nw, nh)
