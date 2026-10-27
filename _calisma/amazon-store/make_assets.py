"""Amazon Store redesign (2026-10-19) — flat image backgrounds, all text added in Figma (Founders Grotesk, editable).
Sources: client-approved colour series (batch-47 'renkli'), real launch-event frame of both founders, official product PNGs."""
import os
from PIL import Image, ImageFilter, ImageDraw
S = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience")
SEC = os.path.join(S, '_calisma/batch-47-characters/secim'); PNG = os.path.join(S, 'Products/png'); O = os.path.expanduser('~/sickscience-work/amazon/assets')
SER = {'pc': 'renkli_1_PowerCycle_Kiara.png', 'nw': 'renkli_2_NetWork_Ama.png', 'ss': 'renkli_3_ShapeShift_Leila.png', 'do': 'renkli_5_DropOff_Zara.png'}
def edge_color(im, x0, x1):
    px = [im.getpixel((x, y)) for x in range(x0, x1, 6) for y in range(40, 600, 20)]
    return tuple(sum(p[i] for p in px) // len(px) for i in range(3))
# 1) hero strips 450x600 (face + product), 4 colours
for k, f in SER.items():
    im = Image.open(os.path.join(SEC, f)).convert('RGB')
    w = im.width; h = round(w * 600 / 450); y0 = 380
    im.crop((0, y0, w, y0 + h)).resize((450, 600), Image.LANCZOS).save(os.path.join(O, f'hero_{k}.jpg'), quality=94)
# 2) product tiles 1500x1500: photo at full height on the right, colour field extended to the left (no crop of the person)
for k, f in SER.items():
    im = Image.open(os.path.join(SEC, f)).convert('RGB'); ph = im.resize((round(im.width * 1500 / im.height), 1500), Image.LANCZOS)
    bg = edge_color(ph, 0, 60); tile = Image.new('RGB', (1500, 1500), bg)
    # soft blend of the photo's left edge into the field
    tile.paste(ph, (1500 - ph.width, 0))
    m = Image.new('L', (160, 1500), 0); d = ImageDraw.Draw(m)
    for x in range(160): d.line((x, 0, x, 1500), fill=round(255 * x / 159))
    fieldstrip = Image.new('RGB', (160, 1500), bg); seam = tile.crop((1500 - ph.width, 0, 1500 - ph.width + 160, 1500))
    tile.paste(Image.composite(seam, fieldstrip, m), (1500 - ph.width, 0))
    tile.save(os.path.join(O, f'tile_{k}.jpg'), quality=94); print(k, bg)
# 3) founders: real launch-night frame (Merve + Polen at the Welcome wall), square crop
import subprocess
ev = os.path.join(S, '_calisma/batch-53-launch-montage/src-event-reel-revised.mp4'); fr = os.path.join(O, 'founders_frame.png')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', '9.2', '-i', ev, '-frames:v', '1', fr], check=True)
fi = Image.open(fr).convert('RGB'); s = fi.width; fi.crop((0, 300, s, 300 + s)).resize((1500, 1500), Image.LANCZOS).save(os.path.join(O, 'founders.jpg'), quality=94)
# 4) NX35 lineup: four official product PNGs on white, real proportions, soft contact shadow
fronts = [('ERH_7477C.png', 1.0), ('ERH_7470B.png', 1.0), ('ERH_7460B.png', 14 / 12), ('ERH_7488.png', 20 / 12)]
canvas = Image.new('RGB', (1500, 1500), (255, 255, 255)); base_h = 620; gap = 60; items = []
for f, rel in fronts:
    p = Image.open(os.path.join(PNG, f)).convert('RGBA'); p = p.crop(p.getbbox()); h = round(base_h * rel); p = p.resize((round(p.width * h / p.height), h), Image.LANCZOS); items.append(p)
tw = sum(p.width for p in items) + gap * 3; x = (1500 - tw) // 2; floor = 1180
for p in items:
    sh = Image.new('L', (p.width + 120, 70), 0); ImageDraw.Draw(sh).ellipse((20, 10, p.width + 100, 60), fill=110); sh = sh.filter(ImageFilter.GaussianBlur(14))
    canvas.paste((205, 200, 210), (x - 60, floor - 35), sh); canvas.paste(p, (x, floor - p.height), p); x += p.width + gap
canvas.save(os.path.join(O, 'lineup.jpg'), quality=95)
print('ok')
