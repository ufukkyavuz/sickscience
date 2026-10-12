"""Replace a model-drawn 'ULTA' word on a generated shopping bag with the official Ulta Beauty logo (white, from ulta.com SVG).
Usage: python ulta_logo_swap.py in.png out.png x0 y0 x1 y1 logo_width_px [cx cy]
  (x0,y0,x1,y1) = box around the drawn text; logo is centred on the box centre (or cx,cy) at logo_width_px.
Steps: white-text mask -> cv2 inpaint with bag colour -> logo tinted by local bag shading -> occluders (handles, bottles) restored on top."""
import sys, cv2, numpy as np
from PIL import Image
ROOT = "/Users/ufo/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/"
src, dst = sys.argv[1], sys.argv[2]
x0, y0, x1, y1, lw = map(int, sys.argv[3:8])
im = cv2.imread(src, cv2.IMREAD_COLOR)
H, W = im.shape[:2]
hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
# 1. text mask: bright, low-saturation pixels inside the box
box = np.zeros((H, W), np.uint8); box[y0:y1, x0:x1] = 1
white = ((hsv[..., 2] > 170) & (hsv[..., 1] < 90)).astype(np.uint8) & box
white = cv2.dilate(white, np.ones((7, 7), np.uint8))
import os
if os.environ.get('NOCLEAN'): white[:] = 0  # plain bag: nothing to erase
clean = cv2.inpaint(im, white * 255, 9, cv2.INPAINT_TELEA)
# smooth the inpainted area a little so no letter ghosts remain
blur = cv2.GaussianBlur(clean, (0, 0), 6)
m3 = cv2.GaussianBlur(white.astype(np.float32), (0, 0), 3)[..., None]
clean = (clean * (1 - m3) + blur * m3).astype(np.uint8)
# 2. bag (magenta) mask = pixels the logo may cover
hsv2 = cv2.cvtColor(clean, cv2.COLOR_BGR2HSV)
h, s, v = hsv2[..., 0].astype(int), hsv2[..., 1].astype(int), hsv2[..., 2].astype(int)
bag = (((h >= 150) | (h <= 6)) & (s > 110) & (v > 70)).astype(np.float32)
bag = cv2.GaussianBlur(bag, (0, 0), 1.2)
import os
if os.environ.get('NOMASK'): bag = np.ones_like(bag)
# 3. logo
logo = Image.open(ROOT + 'Ulta/logo/ulta_logo_white.png').convert('RGBA')
lh = round(logo.height * lw / logo.width)
logo = np.asarray(logo.resize((lw, lh), Image.LANCZOS)).astype(np.float32) / 255
cx = int(sys.argv[8]) if len(sys.argv) > 8 else (x0 + x1) // 2
cy = int(sys.argv[9]) if len(sys.argv) > 9 else (y0 + y1) // 2
lx, ly = cx - lw // 2, cy - int(lh * 0.42)
out = clean.astype(np.float32)
reg = out[ly:ly + lh, lx:lx + lw]
lum = cv2.cvtColor(clean, cv2.COLOR_BGR2GRAY).astype(np.float32)[ly:ly + lh, lx:lx + lw]
shade = np.clip((lum / max(lum.mean(), 1)) ** 0.6, 0.78, 1.12)[..., None]
ink = np.clip(np.array([248, 248, 250], np.float32) * shade, 0, 255)
a = logo[..., 3:4] * 0.96 * bag[ly:ly + lh, lx:lx + lw, None]
out[ly:ly + lh, lx:lx + lw] = reg * (1 - a) + ink * a
cv2.imwrite(dst, np.clip(out, 0, 255).astype(np.uint8))
print('ok', dst, (lx, ly, lw, lh))
