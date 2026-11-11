# v6 (2026-11-10): STORY-first rebuild after reading both OneSkin carousels slide by slide.
# Ref 1 (DU3c4OHFEnV): cover microscope circle "Target the system, not just the symptom" -> comparison (anti-aging vs longevity)
#   -> "From the OneSkin Lab" lab photo -> peptide 3D animation ("Mask the past / Protect your future").
# Ref 2 (DZ_Ro4bgi2R): hook "Collagen is like gluten in bread (hear us out)" (bread) -> "Your skin's structural framework" (crumb close-up)
#   -> "Don't forget the salt" (salt close-up) -> "The OS-01 Peptide effect" (microscope cells white -> green).
# Ours: A = skin-care vs cell signalling (microscope cover, comparison, SickScience lab, glass-3D exosome). B = exosomes are like SEEDS
#   (plant-derived): dandelion hook -> seed carries instructions -> don't forget the soil -> NX35 effect (3D cell white -> mint).
import os, subprocess, glob
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_slides3.py')).read()
exec(src[:src.index("INK = (255, 255, 255, 255)\n# ---------------- A:")])
Image.MAX_IMAGE_PIXELS = None
OUT = os.path.join(R, 'out6'); os.makedirs(OUT, exist_ok=True)
ST = os.path.join(R, 'stock'); G3 = os.path.join(R, 'glass3d', 'glass3d_loop.mp4')
LABJ = os.path.join(BA, 'Images', 'All Products - Old Image', 'SS0606.jpg')
INK = (18, 18, 22, 255); WHITE = (255, 255, 255, 255)
def center(d, txt, f, y, fill):
    w = d.textlength(txt, font=f); d.text(((W - w) / 2, y), txt, font=f, fill=fill)
def run(out, fl, inputs):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', fl, '-map', '[o]', '-t', '8', '-r', '30', '-c:v', 'libx264', '-crf', '14', '-preset', 'slow',
                    '-pix_fmt', 'yuv420p', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-movflags', '+faststart', out], check=True); print(out)
def vid(name, clip, ss, crop, layout, ov, grade='', loop=False, scale_extra=''):
    band = 470
    if layout == 'v2': ov, band = ov
    ovp = os.path.join(OUT, name + '_text.png'); ov.save(ovp)
    base = f'[0:v]crop={crop},scale={W}:{H}:flags=lanczos,fps=30,setsar=1{grade}[v]'
    if layout == 'v2':
        fl = base + f';[v]split[a][b];[b]crop=1080:{band}:0:0,gblur=sigma=30,drawbox=x=0:y=0:w=1080:h={band}:color=white@0.42:t=fill[bd];[a][bd]overlay=0:0[c];[c][1:v]overlay=0:0,format=yuv420p[o]'
        ins = ['-ss', str(ss), '-t', '8', '-i', clip, '-loop', '1', '-t', '8', '-i', ovp]
    else:
        fl = base + ';[v][1:v]overlay=0:0,format=yuv420p[o]'; ins = ['-ss', str(ss), '-t', '8', '-i', clip, '-loop', '1', '-t', '8', '-i', ovp]
    if loop: ins = ['-stream_loop', '-1'] + ins
    run(os.path.join(OUT, name + '.mp4'), fl, ins)
# ---------- A1 cover: microscope circle ----------
def cover():
    lay = Image.new('RGBA', (W, H), (14, 37, 42, 255)); hole = Image.new('L', (W, H), 0); d = ImageDraw.Draw(hole); d.ellipse([20, 150, 1060, 1190], fill=255)
    hole = hole.filter(ImageFilter.GaussianBlur(26)); lay.putalpha(hole.point(lambda v: 255 - v))
    top = Image.new('RGBA', (W, H), (0, 0, 0, 0)); t = ImageDraw.Draw(top)
    scr = Image.new('L', (W, H), 0); ImageDraw.Draw(scr).ellipse([120, 520, 960, 780], fill=150); top.paste((8, 24, 28), (0, 0), scr.filter(ImageFilter.GaussianBlur(60)))
    f = font('Medium', 66)
    for k, ln in enumerate(['Skip the surface.', 'Speak to the cell.']): center(t, ln, f, 565 + k * 84, WHITE)
    f2 = font('Medium', 32); s = 'EXOSOMES  >  “SKINCARE”'; sw = t.textlength(s, font=f2) + len(s) * 3
    x = (W - sw) / 2
    for ch in s: t.text((x, 1262), ch, font=f2, fill=(225, 236, 236, 255)); x += t.textlength(ch, font=f2) + 3
    lay.alpha_composite(top); return lay
ovc = cover(); ovc.save(os.path.join(OUT, 'A1_text.png'))
grade = ',hue=s=0.15,colorbalance=rs=-0.08:gs=0.05:bs=0.12:rm=-0.06:gm=0.04:bm=0.1,eq=brightness=-0.04:contrast=1.05'
fl = f'[0:v]crop=1080:1080:400:0,scale=1080:1080:flags=lanczos,fps=30,setsar=1{grade},pad={W}:{H}:0:150:color=0x0e252a[v];[v][1:v]overlay=0:0,format=yuv420p[o]'
run(os.path.join(OUT, 'A1_cover.mp4'), fl, ['-ss', '1', '-t', '8', '-i', os.path.join(ST, '4178359.mp4'), '-loop', '1', '-t', '8', '-i', os.path.join(OUT, 'A1_text.png')])
# ---------- A2 comparison (static) ----------
def tile(img, size=300):
    img = img.convert('RGB'); s = min(img.size); img = img.crop(((img.width - s) // 2, (img.height - s) // 2, (img.width + s) // 2, (img.height + s) // 2)).resize((size, size), Image.LANCZOS)
    m = Image.new('L', (size, size), 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, size - 1, size - 1], 26, fill=255); img.putalpha(m); return img
skin = os.path.join(OUT, 'skin.png'); subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', '3', '-i', os.path.join(ST, '7477545.mp4'), '-frames:v', '1', '-vf', 'crop=2160:2160:0:800,scale=900:900', skin], check=True)
scalp_img = Image.open(os.path.join(SC, 'Scalp 18 - Day 56.jpg'))
bg = Image.new('RGBA', (W, H), (243, 242, 238, 255)); d = ImageDraw.Draw(bg)
cols = [(270, 'TOPICAL', 'How actives work', ['sit on the', 'surface', 'of the skin'], tile(Image.open(skin))), (810, 'EXOSOMES', 'How NX35™ works', ['communicate with', 'cells at the', 'molecular level'], tile(scalp_img))]
for cx, head, sub, lines, im in cols:
    bg.alpha_composite(im, (cx - 150, 330)); center_x = lambda txt, f, y, fill: d.text((cx - d.textlength(txt, font=f) / 2, y), txt, font=f, fill=fill)
    center_x(head, font('Bold', 58), 690, INK); center_x(sub, font('Regular', 38), 775, INK)
    d.ellipse([cx - 22, 842, cx + 22, 886], outline=INK, width=3); d.line([cx, 853, cx, 874], fill=INK, width=3); d.line([cx - 8, 866, cx, 875, cx + 8, 866], fill=INK, width=3)
    for k, ln in enumerate(lines): center_x(ln, font('Regular', 40), 925 + k * 54, INK)
bg.convert('RGB').save(os.path.join(OUT, 'A2_comparison.png'), quality=95)
# ---------- A3 lab photo ----------
lab = Image.open(LABJ).convert('RGB'); print('lab', lab.size)
w0, h0 = lab.size; ch = h0; cw = int(ch * 4 / 5); x0 = int(w0 * 0.38)
lab = lab.crop((x0, 0, x0 + cw, ch)).resize((W, H), Image.LANCZOS).convert('RGBA')
lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); ft, fb = font('Bold', 47), font('Regular', 37)
d.text((60, 70), 'FROM THE SICKSCIENCE LAB', font=ft, fill=WHITE); y = 142
for ln in wrap(d, 'NX35 is SickScience’s proprietary plant-based biomimetic exosome technology, engineered to mimic the body’s natural cellular communication system.', fb, 960): d.text((60, y), ln, font=fb, fill=WHITE); y += 49
sh = Image.new('RGBA', (W, 520), (0, 0, 0, 0)); g = Image.new('L', (1, 520)); g.putdata([int(150 * (1 - i / 520) ** 1.2) for i in range(520)]); sh.putalpha(g.resize((W, 520)))
shade = Image.new('RGBA', (W, H), (0, 0, 0, 0)); shade.alpha_composite(Image.merge('RGBA', [Image.new('L', (W, 520), 0)] * 3 + [g.resize((W, 520))]), (0, 0))
lab.alpha_composite(shade); lab.alpha_composite(lay); lab.convert('RGB').save(os.path.join(OUT, 'A3_lab.png'), quality=95)
# ---------- A4 glass 3D (V1) ----------
if os.path.exists(G3):
    INK = (18, 18, 22, 255)
    vid('A4_exosome3d', G3, 0, '1080:1350:0:0', 'v1', text_v1([('x', 'SKIP THE SURFACE'), ('v', 'SPEAK TO THE CELL')], 'NX35™ is our plant exosome technology: carriers that deliver specific coded messages to cells at a molecular level.'), loop=True)
# ---------- B ----------
D = os.path.join(ST, '8121602.mp4')
lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = font('Medium', 66)
sc_ = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sc_).rectangle([0, 0, W, H], fill=(0, 0, 0, 70)); lay.alpha_composite(sc_)
for k, ln in enumerate(['Exosomes in your skin', 'are like seeds in', 'a garden']): center(d, ln, f, 470 + k * 84, WHITE)
center(d, '(hear us out)', font('Regular', 40), 470 + 3 * 84 + 14, WHITE)
vid('B1_hook', D, 6, '1728:2160:1000:0', 'v1', lay)
vid('B2_seed', D, 12, '1100:1375:1500:560', 'v2', text_v2('A Seed Carries the Instructions', 'A seed is tiny, yet it holds the message that tells a plant how to grow.\n\nSeed = a tiny carrier of instructions\nExosome = a tiny carrier of coded messages'))
vid('B3_soil', os.path.join(ST, '31145801.mp4'), 2, '1728:2160:1000:0', 'v2', text_v2('Don’t Forget the Soil', 'A seed on concrete never grows. It needs the right ground. Exosomes find targeted cells and deliver signals where it’s needed most.'))
if os.path.exists(G3):
    vid('B4_effect3d', G3, 0, '720:900:180:180', 'v2', text_v2('The NX35™ Effect', 'Our NX35™ technology targets specific cells and delivers “coded” messages. 100% plant-derived and vegan.', True), loop=True)
