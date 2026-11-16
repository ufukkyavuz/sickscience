"""Real customer review scene (white science background, brand typography). Review text is verbatim minus the duration sentence."""
import math, subprocess, os
from PIL import Image, ImageDraw, ImageFont
W, H, FPS = 1080, 1920, 30; SC_ = float(os.environ.get('RC_SCALE', '1')); DUR = 4.6 * SC_; OUTF = os.environ.get('RC_OUT', 'src/review/review_card.mp4')
FB = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Bold.otf'); FM = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Medium.otf')
SRC = '/Users/ufo/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive\'ım/SickScience/_calisma/batch-126-testimonial/src/'
MAG = (169, 33, 192); INK = (20, 20, 24); GOLD = (247, 189, 52)
def ease(p): p = max(0.0, min(1.0, p)); return 1 - (1 - p) ** 3
def back(p):
    p = max(0.0, min(1.0, p)); c1 = 1.9; c3 = c1 + 1; return 1 + c3 * (p - 1) ** 3 + c1 * (p - 1) ** 2
def crop_img(n):
    im = Image.open(SRC + n).convert('RGB'); w, h = im.size; im = im.crop((0, 0, w, int(h * 0.94))); return im
imgs = [crop_img('collage_front.jpeg'), crop_img('collage_profile.jpeg')]
QUOTE = "I'm blown away with the results so far! I wouldn't have believed it if I didn't take a picture of before and after."
fq = ImageFont.truetype(FM, 56); d0 = ImageDraw.Draw(Image.new('RGB', (1, 1)))
words = QUOTE.split(); lines = []; cur = ''
for w_ in words:
    t = (cur + ' ' + w_).strip()
    if d0.textlength(t, font=fq) > 900: lines.append(cur); cur = w_
    else: cur = t
lines.append(cur)
wpos = []   # (word, x, y, idx)
idx = 0
for li, l_ in enumerate(lines):
    lw = d0.textlength(l_, font=fq); x = (W - lw) / 2
    for w_ in l_.split():
        wpos.append((w_, x, 480 + li * 70, idx)); x += d0.textlength(w_ + ' ', font=fq); idx += 1
def star(d, cx, cy, r, fill):
    pts = []
    for k in range(10):
        a = -math.pi / 2 + k * math.pi / 5; rr = r if k % 2 == 0 else r * 0.45; pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d.polygon(pts, fill=fill)
enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', OUTF], stdin=subprocess.PIPE)
for fi in range(int(DUR * FPS)):
    t = fi / FPS / SC_; im = Image.new('RGB', (W, H), (255, 255, 255)); d = ImageDraw.Draw(im, 'RGBA')
    a0 = ease(t / 0.3); d.text((W / 2, 215 + (1 - a0) * 20), 'REAL CUSTOMER REVIEW', font=ImageFont.truetype(FM, 40), fill=MAG + (int(255 * a0),), anchor='mm')
    for k in range(5):
        p = (t - 0.35 - k * 0.12) / 0.25
        if p > 0: star(d, 330 + k * 105, 295, 44 * back(p), GOLD + (255,))
    a1 = ease((t - 0.95) / 0.3); d.text((W / 2, 390 + (1 - a1) * 30), 'Impressed!', font=ImageFont.truetype(FB, 118), fill=INK + (int(255 * a1),), anchor='mm')
    for (w_, x, y, i_) in wpos:
        p = (t - 1.4 - i_ * 0.085) / 0.2
        if p > 0: d.text((x, y + (1 - ease(p)) * 16), w_, font=fq, fill=INK + (int(255 * ease(p)),))
    for k, imc in enumerate(imgs):
        p = ease((t - 2.2 - k * 0.3) / 0.5)
        if p > 0:
            w_, h_ = imc.size; band = imc.crop((0, int(h_ * 0.22), w_, int(h_ * 0.22) + w_ // 2)).resize((1000, 500), Image.LANCZOS); yy = 720 + k * 520 + int((1 - p) * 50)
            lay = Image.new('RGBA', (1000, 500), (0, 0, 0, 0)); lay.paste(band, (0, 0)); lay.putalpha(Image.new('L', (1000, 500), int(255 * p)))
            im.paste(lay, (40, yy), lay)
            for lab_, lx_ in (('BEFORE', 70), ('AFTER', 570)):
                d.text((lx_, yy + 445), lab_, font=ImageFont.truetype(FB, 42), fill=(255, 255, 255, int(255 * p)), stroke_width=4, stroke_fill=(0, 0, 0, int(200 * p)))
    enc.stdin.write(im.tobytes())
enc.stdin.close(); enc.wait(); print('ok')
