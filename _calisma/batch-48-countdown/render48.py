"""Batch 48 (2026-10-15): two new countdown videos in the SS17 countdown format (12 s, timer 00:59 -> 00:48).
  ba   = DropOff cellulite before/after (AI image, 'Simulated results.'), 15% OFF first order
  glp1 = GLP-1 Facial Recovery System set, $162 -> $137 (15% off)
Formats: story 1080x1920, feed 1080x1350, square 1080x1080. Usage: python render48.py [ba|glp1] [story|feed|square]"""
import os, sys, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..', '..')
FONTS = os.path.expanduser('~/Library/Fonts')
def font(style, size): return ImageFont.truetype(os.path.join(FONTS, f'FoundersGrotesk-{style}.otf'), size)
FPS, SECS = 30, 12
PURPLE, MAGENTA, INK = (115, 0, 199), (169, 33, 192), (20, 20, 20)
SIZES = {'story': (1080, 1920), 'feed': (1080, 1350), 'square': (1080, 1080)}
# header layout per format: logo_y, logo_w, line_y, big_y, big_size, timer_y, box_h
HL = {'story': (190, 398, 268, 300, 150, 470, 150), 'feed': (52, 300, 112, 140, 150, 310, 150), 'square': (36, 280, 88, 112, 130, 255, 130)}

def logo(w):
    lg = Image.open(os.path.join(ROOT, '_calisma', 'video-01-bcrf', 'assets', 'logo.png')).convert('RGBA')
    return lg.resize((w, round(lg.height * w / lg.width)), Image.LANCZOS)

def ctext(d, cx, y, s, f, fill, ls=0):
    if not ls:
        d.text((cx, y), s, font=f, fill=fill, anchor='mt'); return
    w = sum(d.textlength(ch, font=f) + ls for ch in s) - ls; x = cx - w / 2
    base = y + round(f.size * 0.72)  # draw every glyph on the same baseline
    for ch in s: d.text((x, base), ch, font=f, fill=fill, anchor='ls'); x += d.textlength(ch, font=f) + ls

def pill(img, cx, cy, s, size=32, bg=INK, fg=(255, 255, 255)):
    d = ImageDraw.Draw(img); f = font('Medium', size)
    l, t, r, b = d.textbbox((0, 0), s, font=f, anchor='mm'); w, h = r - l + 56, b - t + 28
    d.rounded_rectangle((cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2), radius=h / 2, fill=bg)
    d.text((cx, cy), s, font=f, fill=fg, anchor='mm')

def header(img, fmt, line):
    W, H = img.size; ly, lw, liny, by, bs, _, _ = HL[fmt]
    lg = logo(lw); img.alpha_composite(lg, ((W - lg.width) // 2, ly))
    d = ImageDraw.Draw(img)
    ctext(d, W / 2, liny, line, font('Semibold', 32 if fmt == 'story' else 30 if fmt == 'feed' else 28), MAGENTA, ls=3)
    ctext(d, W / 2, by, '15% OFF', font('Bold', bs), INK)

def timer(img, fmt, sec):
    W = img.size[0]; *_, ty, bh = HL[fmt]; bw = round(bh * 1.12); gap = 46
    d = ImageDraw.Draw(img); fd = font('Bold', round(bh * 0.62)); fl = font('Medium', 32 if bh >= 150 else 28)
    for k, (val, lab) in enumerate([('00', 'MIN'), (f'{sec:02d}', 'SEC')]):
        x0 = W / 2 - gap / 2 - bw if k == 0 else W / 2 + gap / 2
        d.rounded_rectangle((x0, ty, x0 + bw, ty + bh), radius=22, fill=PURPLE)
        d.text((x0 + bw / 2, ty + bh * 0.42), val, font=fd, fill=(255, 255, 255), anchor='mm')
        d.text((x0 + bw / 2, ty + bh * 0.83), lab, font=fl, fill=(225, 205, 245), anchor='mm')
    for dy in (-0.16, 0.16):
        r = 7; cy = ty + bh * (0.42 + dy * 0.8)
        d.ellipse((W / 2 - r, cy - r, W / 2 + r, cy + r), fill=INK)

C47 = os.path.join(ROOT, '_calisma', 'batch-47-characters')
def diptych(before, after, W=1536, H=2752, line=6):
    """two same-pose photos -> one 9:16 split image (centre strip of each, white divider)"""
    out = Image.new('RGBA', (W, H), (254, 254, 254, 255)); hw = (W - line) // 2
    for k, f in enumerate((before, after)):
        im = Image.open(os.path.join(C47, f)).convert('RGBA'); sc = H / im.height; im = im.resize((round(im.width * sc), H), Image.LANCZOS)
        x0 = (im.width - hw) // 2; out.alpha_composite(im.crop((x0, 0, x0 + hw, H)), (0 if k == 0 else hw + line, 0))
    return out
# kind -> (source, crop-top fraction per format, small line)
BA = {'ba':      ('ba_do_zara.png', {'story': 0.10, 'feed': 0.22, 'square': 0.26}, 'FLASH DEAL · FIRST ORDER ONLY'),
      'ba_ss':   ('ba2_ss_leila.png', {'story': 0.06, 'feed': 0.10, 'square': 0.12}, 'SHAPESHIFT · FIRST ORDER ONLY'),
      'ba_nw':   ('ba2_nw_ama.png', {'story': 0.0, 'feed': 0.05, 'square': 0.08}, 'NETWORK · FIRST ORDER ONLY'),
      'ba_pc':   (('edit_pc_kiara.png', 'studio_kiara_src.png'), {'story': 0.0, 'feed': 0.02, 'square': 0.04}, 'POWERCYCLE · FIRST ORDER ONLY'),
      'ba_pc2':  (('edit_pc_nia.png', 'studio_nia_src.png'), {'story': 0.0, 'feed': 0.02, 'square': 0.04}, 'POWERCYCLE · FIRST ORDER ONLY')}
def base_ba(fmt, kind='ba'):
    W, H = SIZES[fmt]; img = Image.new('RGBA', (W, H), (254, 254, 254, 255))
    src, crops, line = BA[kind]
    ph = diptych(*src) if isinstance(src, tuple) else Image.open(os.path.join(C47, src)).convert('RGBA')
    ph = ph.crop((0, round(ph.height * crops[fmt]), ph.width, ph.height))
    edge = ph.crop((0, 0, ph.width, 6)).convert('RGB').resize((1, 1), Image.BOX).getpixel((0, 0))  # backdrop colour at the photo's top edge
    img = Image.new('RGBA', (W, H), edge + (255,))
    ph = ph.resize((W, round(ph.height * W / ph.width)), Image.LANCZOS)
    top = {'story': 660, 'feed': 490, 'square': 415}[fmt]
    img.alpha_composite(ph, (0, top))
    pill(img, W * 0.25, top + 60, 'BEFORE'); pill(img, W * 0.75, top + 60, 'AFTER', bg=PURPLE)
    header(img, fmt, line)
    d = ImageDraw.Draw(img); d.text((W / 2, H - 22), 'Simulated results.', font=font('Regular', 20), fill=(255, 255, 255), anchor='mb', stroke_width=1, stroke_fill=(90, 70, 60))
    return img

def base_glp1(fmt):
    W, H = SIZES[fmt]
    img = Image.new('RGBA', (W, H), (226, 214, 243, 255))
    glow = Image.new('L', (W, H), 0); ImageDraw.Draw(glow).ellipse((-W * 0.2, H * 0.25, W * 1.2, H * 1.05), fill=255)
    glow = glow.filter(ImageFilter.GaussianBlur(160))
    img = Image.composite(Image.new('RGBA', (W, H), (246, 241, 252, 255)), img, glow)
    header(img, fmt, 'GLP-1 FACIAL RECOVERY SYSTEM')
    d = ImageDraw.Draw(img); _, _, _, _, _, ty, bh = HL[fmt]
    py = ty + bh + (40 if fmt == 'story' else 30)
    fo, fn = font('Regular', 56), font('Bold', 64)
    wo, wn = d.textlength('$162', font=fo), d.textlength('$137', font=fn); x = W / 2 - (wo + 30 + wn) / 2
    d.text((x, py), '$162', font=fo, fill=(120, 110, 135), anchor='lt')
    yb = py + 32; d.line((x - 4, yb, x + wo + 4, yb), fill=(120, 110, 135), width=4)
    d.text((x + wo + 30, py - 6), '$137', font=fn, fill=INK, anchor='lt')
    st = Image.open(os.path.join(ROOT, 'Products', 'sets', 'ss-set-glp1.png')).convert('RGBA'); st = st.crop(st.split()[-1].getbbox())
    top = py + 110; bottom = {'story': 1250, 'feed': 1300, 'square': 1050}[fmt]; h = bottom - top
    w = round(st.width * h / st.height)
    if w > W - 120: w = W - 120; h = round(st.height * w / st.width)
    st = st.resize((w, h), Image.LANCZOS)
    sh = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(sh).ellipse((W / 2 - w * 0.45, top + h - 26, W / 2 + w * 0.45, top + h + 26), fill=(70, 40, 110, 70))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(18)))
    img.alpha_composite(st, ((W - w) // 2, top))
    return img

def render(kind, fmt):
    base = base_glp1(fmt) if kind == 'glp1' else base_ba(fmt, kind); W, H = base.size
    names = {'ba': 'DropOff – Countdown 15% Before-After', 'glp1': 'GLP-1 Recovery System – Countdown 15%',
             'ba_ss': 'ShapeShift – Countdown 15% Before-After', 'ba_nw': 'NetWork – Countdown 15% Before-After',
             'ba_pc': 'PowerCycle – Countdown 15% Before-After (edges)', 'ba_pc2': 'PowerCycle – Countdown 15% Before-After (part)'}
    out = os.path.join(HERE, f'{names[kind]} – {fmt}.mp4')
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    for s in range(SECS):
        fr = base.copy(); timer(fr, fmt, 59 - s); raw = fr.convert('RGB').tobytes()
        if s == 0: fr.convert('RGB').save(os.path.join(HERE, f'{kind}_{fmt}_preview.jpg'), quality=88)
        for _ in range(FPS): p.stdin.write(raw)
    p.stdin.close(); p.wait(); print('ok', out)

if __name__ == '__main__':
    kinds = [sys.argv[1]] if len(sys.argv) > 1 else ['ba', 'glp1']
    fmts = [sys.argv[2]] if len(sys.argv) > 2 else ['story', 'feed', 'square']
    for k in kinds:
        for f in fmts: render(k, f)
