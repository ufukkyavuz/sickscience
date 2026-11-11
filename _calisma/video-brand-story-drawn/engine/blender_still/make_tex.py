# page textures (paper + grid + ink) and print textures (photo with white border)
from PIL import Image, ImageDraw, ImageChops, ImageFilter
import numpy as np, json, random
ink = Image.open('ink.png').convert('RGB').point(lambda v: int(255 * (v / 255) ** 1.7))
SW, SH = ink.size
GRID = (205, 214, 226)
paper = Image.new('RGB', (SW, SH), (252, 251, 247)); d = ImageDraw.Draw(paper)
rng = np.random.default_rng(3)
for x0, x1 in ((0, 1020), (1020, 2040)):
    for x in range(x0 + 60, x1 - 30, 28): d.line((x, 120, x, 1430), fill=GRID, width=2)
    for y in range(130, 1430, 28): d.line((x0 + 60, y, x1 - 30, y), fill=GRID, width=2)
# paper fibre noise
n = rng.normal(0, 2.2, (SH, SW, 1)); a = np.clip(np.asarray(paper).astype(float) + n, 0, 255).astype(np.uint8)
paper = Image.fromarray(a)
page = ImageChops.multiply(paper, ink)
page = page.resize((SW * 2, SH * 2), Image.LANCZOS)
page.crop((0, 0, SW, SH * 2)).save('tex_left.png'); page.crop((SW, 0, SW * 2, SH * 2)).save('tex_right.png')
# prints: (year, centre px on spread, width px, rotation deg)
PR = [(2009, (780, 480), 280, -3), (2013, (545, 600), 150, 5), (2020, (865, 1188), 182, -3)]
DESK = [2018, 2024, 2025]
from PIL import ImageEnhance
def soften(im):   # printed-photo look in this room: a little less saturation/contrast, lifted blacks, fine grain
    im = ImageEnhance.Color(im).enhance(0.85); im = ImageEnhance.Contrast(im).enhance(0.9)
    a = np.asarray(im).astype(float); a = 14 + a * (236 - 14) / 255 + np.random.default_rng(5).normal(0, 3, a.shape)
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
out = []
for y, c, w, r in PR:
    ph = Image.open(f'ph_{y}.jpg').convert('RGB'); pw, phh = ph.size
    b = int(pw * 0.06); bb = int(pw * 0.06)
    ph = soften(ph); card = Image.new('RGB', (pw + 2 * b, phh + b + bb), (238, 240, 242)); card.paste(ph, (b, b))
    card.save(f'print_{y}.jpg', quality=95)
    out.append(dict(y=y, c=c, w=w, r=r, aspect=card.size[1] / card.size[0]))
for y in DESK:
    ph = Image.open(f'ph_{y}.jpg').convert('RGB'); pw, phh = ph.size; b = int(pw * 0.06)
    ph = soften(ph); card = Image.new('RGB', (pw + 2 * b, phh + 2 * b), (238, 240, 242)); card.paste(ph, (b, b)); card.save(f'print_{y}.jpg', quality=95)
json.dump(out, open('prints.json', 'w'), indent=1)
print(out)
