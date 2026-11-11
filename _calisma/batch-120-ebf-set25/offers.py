# Early Black Friday offer films (9:16, 15 s each, countdown from frame 0). 4 styles.
# usage: python offers.py <price|receipt|equation|chart> [--frames t,t] [--out f.mp4]
import math, os, sys, subprocess, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

R = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, DUR = 1080, 1920, 30, 12.0
F = os.path.expanduser('~/Library/Fonts/FoundersGrotesk')
fb = lambda s: ImageFont.truetype(F + '-Bold.otf', s)
fm = lambda s: ImageFont.truetype(F + '-Medium.otf', s)
fr = lambda s: ImageFont.truetype(F + '-Regular.otf', s)
fmono = lambda s: ImageFont.truetype(F + 'Mono-Medium.otf', s)
INK, PINK, GREY = (20, 20, 24), (169, 33, 192), (120, 122, 130)
VIO, RED, GRN, COB = (120, 40, 200), (205, 35, 45), (60, 160, 60), (35, 55, 175)
BG = (250, 250, 250)


def img(n):
    return Image.open(os.path.join(R, n + '.png')).convert('RGBA')
LOGO = img('logo')


def ss(a):
    a = min(1.0, max(0.0, a)); return a * a * (3 - 2 * a)


def ease_out(a):
    a = min(1.0, max(0.0, a)); return 1 - (1 - a) ** 3


def base(tint=(240, 232, 248)):
    im = Image.new('RGB', (W, H), BG)
    g = Image.new('L', (W, H), 0); ImageDraw.Draw(g).ellipse((90, 520, 990, 1420), fill=150)
    g = g.filter(ImageFilter.GaussianBlur(160))
    im.paste(Image.new('RGB', (W, H), tint), (0, 0), g)
    return im


def ctext(d, y, s, font, fill=INK, x=None):
    tw = d.textlength(s, font=font)
    d.text(((W - tw) / 2 if x is None else x, y), s, font=font, fill=fill)
    return tw


def logo(im):
    l = LOGO.resize((398, int(398 * LOGO.height / LOGO.width)), Image.LANCZOS)
    im.paste(l, ((W - l.width) // 2, 190), l)


def cdraw(d, cx, cy, s, font, fill):
    """draw s with its real ink box centred on (cx, cy)"""
    bb = d.textbbox((0, 0), s, font=font, anchor='ls')
    d.text((cx - (bb[0] + bb[2]) / 2, cy - (bb[1] + bb[3]) / 2), s, font=font, fill=fill, anchor='ls')


def countdown(im, t):
    """big MM:SS timer from 00:59 down, visible from frame 0 (digits steady, centred in the pill)"""
    d = ImageDraw.Draw(im)
    s = max(0, 59 - int(t))
    txt = f'00:{s:02d}'
    f = fb(150)
    bb = d.textbbox((0, 0), '00:00', font=f, anchor='ls')     # fixed box so the pill never changes size
    tw = bb[2] - bb[0]
    d.rounded_rectangle((W / 2 - tw / 2 - 46, 290, W / 2 + tw / 2 + 46, 470), 40, fill=INK)
    cdraw(d, W / 2, 380, txt, f, (255, 255, 255))
    cdraw(d, W / 2, 502, 'EARLY BLACK FRIDAY', fm(32), GREY)


def pill(d, x, y, s, fill=(255, 255, 255), col=INK, outline=INK, font=None):
    font = font or fb(34)
    tw = d.textlength(s, font=font)
    d.rounded_rectangle((x, y, x + tw + 56, y + 70), 35, fill=fill, outline=outline, width=3)
    cdraw(d, x + (tw + 56) / 2, y + 35, s, font, col)
    return tw + 56


def ship_seal(im, cx, cy, a=1.0):
    if a <= 0: return
    r = int(115 * (0.8 + 0.2 * ease_out(a)))
    d = ImageDraw.Draw(im)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 255, 255), outline=PINK, width=5)
    tx, ty = cx - 40, cy - 56
    d.rectangle((tx, ty, tx + 50, ty + 30), fill=PINK); d.polygon([(tx + 50, ty + 8), (tx + 70, ty + 8), (tx + 80, ty + 20), (tx + 80, ty + 30), (tx + 50, ty + 30)], fill=PINK)
    d.ellipse((tx + 8, ty + 26, tx + 24, ty + 42), fill=PINK); d.ellipse((tx + 56, ty + 26, tx + 72, ty + 42), fill=PINK)
    cdraw(d, cx, cy + 18, 'FREE', fb(40), INK)
    cdraw(d, cx, cy + 58, 'SHIPPING', fb(30), INK)


def place(im, p, cx, base_y, h, a=1.0, rot=0):
    """paste product PNG by real-height, bottom at base_y, with a soft contact shadow"""
    if a <= 0: return
    w = int(p.width * h / p.height)
    q = p.resize((w, int(h)), Image.LANCZOS)
    if rot: q = q.rotate(rot, expand=True, resample=Image.BICUBIC)
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).ellipse((cx - w * 0.6, base_y - 14, cx + w * 0.6, base_y + 16), fill=int(110 * a))
    im.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(14)))
    if a < 1:
        al = q.split()[3].point(lambda v: int(v * a)); q.putalpha(al)
    im.paste(q, (int(cx - q.width / 2), int(base_y - q.height)), q)


def cta(d, t, t0):
    if t < t0: return
    a = ease_out((t - t0) / 0.4)
    s = 'SHOP NOW'
    f = fb(44); tw = d.textlength(s, font=f)
    x0 = (W - tw) / 2 - 60; y0 = 1530 + int(30 * (1 - a))
    d.rounded_rectangle((x0, y0, x0 + tw + 120, y0 + 100), 50, fill=PINK)
    cdraw(d, W / 2, y0 + 50, s, f, (255, 255, 255))


# ---------------- 1. PRICE DROP: Vault, digits roll $144 -> $108 ----------------
def scene_price(t):
    im = base((242, 236, 250)); d = ImageDraw.Draw(im)
    logo(im); countdown(im, t)
    place(im, img('vault'), W / 2, 1110, 440 + 16 * ss(t / 15))
    # price block
    p0, p1 = 144, 108
    k = ss((t - 3.0) / 1.6)
    if t < 3.0:
        val = p0
    else:
        val = int(round(p0 + (p1 - p0) * k))
    f = fb(190)
    s = f'${val}'
    col = INK if t < 3.0 else (PINK if k >= 1 else INK)
    ctext(d, 1125, s, f, col)
    if t >= 3.0:
        a = ease_out((t - 3.0) / 0.5)
        f2 = fm(64); s2 = '$144'; tw = d.textlength(s2, font=f2); x = W / 2 - tw / 2
        d.text((x, 560 - 30), '', font=f2)
    if k >= 1:
        a = ease_out((t - 4.7) / 0.4)
        f2 = fm(60); s2 = '$144'; tw = d.textlength(s2, font=f2)
        d.text((W / 2 - tw / 2, 1322), s2, font=f2, fill=GREY)
        d.line((W / 2 - tw / 2 - 6, 1356, W / 2 + tw / 2 + 6, 1344), fill=PINK, width=6)
    ctext(d, 560, 'THE VAULT', fb(60))
    if t > 5.4:
        f = fb(34); w1 = d.textlength('25% OFF', font=f) + 56; w2 = d.textlength('YOU SAVE $36', font=f) + 56
        x = (W - w1 - w2 - 20) / 2; x += pill(d, x, 1420, '25% OFF', fill=INK, col=(255, 255, 255)) + 20
        pill(d, x, 1420, 'YOU SAVE $36')
    if t > 6.2:
        ship_seal(im, 900, 820, ease_out((t - 6.2) / 0.4))
    cta(d, t, 7.0)
    return im


# ---------------- 2. RECEIPT: three products, set price, -25% ----------------
def scene_receipt(t):
    im = base((236, 240, 250)); d = ImageDraw.Draw(im)
    logo(im); countdown(im, t)
    lines = [('ShapeShift', '$64.00'), ('PowerCycle', '$64.00'), ('DropOff', '$52.00'),
             ('Separately', '$180.00'), ('Vault set price', '$144.00'), ('Early Black Friday', '−$36.00'), ('=', ''), ('TOTAL', '$108.00')]
    shown = min(len(lines), max(0, int((t - 1.2) / 0.55) + 1)) if t > 1.2 else 0
    # paper slides down as it prints
    px0, px1 = 170, 910
    top = 560
    rows = 0
    for i in range(shown):
        rows += 1
    ph = 120 + rows * 78 + (60 if shown == len(lines) else 0)
    d.rectangle((px0, top, px1, top + ph), fill=(255, 255, 255))
    for k in range(px0, px1, 24):                               # torn bottom edge
        d.polygon([(k, top + ph), (k + 12, top + ph + 14), (k + 24, top + ph)], fill=(255, 255, 255))
    d.text((px0 + 40, top + 34), 'SICKSCIENCE LABS · RECEIPT', font=fmono(32), fill=GREY)
    y = top + 100
    for i in range(shown):
        a, b = lines[i]
        if a in ('—', '='):
            d.line((px0 + 40, y + 34, px1 - 40, y + 34), fill=(200, 200, 205), width=3); y += 78; continue
        big = a == 'TOTAL'
        f = fmono(58) if big else fmono(40)
        col = PINK if (big or 'Friday' in a) else INK
        d.text((px0 + 40, y), a, font=f, fill=col)
        tw = d.textlength(b, font=f); d.text((px1 - 40 - tw, y), b, font=f, fill=col)
        if a == 'Separately':
            d.line((px1 - 40 - tw - 4, y + 24, px1 - 36, y + 20), fill=INK, width=3)
        y += 78
    # products beside the receipt
    if t > 0.6:
        a = ease_out((t - 0.6) / 0.5)
        sc = 0.42
        for cx, nm, h in ((150, 'ss', 12), (230, 'pc', 14), (310, 'do', 19)):
            pass
    if shown == len(lines):
        tt = t - (1.2 + 0.55 * (len(lines) - 1))
        if tt > 0.6:
            x = 170; x += pill(d, x, 1415, '25% OFF', fill=INK, col=(255, 255, 255)) + 16
            pill(d, x, 1415, 'YOU SAVE $72')
        if tt > 1.0: ship_seal(im, 880, 1505, ease_out((tt - 1.0) / 0.4))
        cta(d, t, 1.2 + 0.55 * (len(lines) - 1) + 1.4)
    return im


# ---------------- 3. EQUATION: Award Duo math ----------------
def scene_equation(t):
    im = base((240, 246, 236)); d = ImageDraw.Draw(im)
    logo(im); countdown(im, t)
    ss_, pc_ = img('ss'), img('pc')
    y_base = 1050
    a1 = ease_out((t - 0.5) / 0.5); a2 = ease_out((t - 1.6) / 0.5)
    place(im, ss_, 300, y_base, 12 * 30 * a1 if a1 > 0 else 1, a1)
    place(im, pc_, 760, y_base, 14 * 30 * a2 if a2 > 0 else 1, a2)
    if t > 0.9: ctext(d, y_base + 30, '$64', fb(84), INK, x=300 - d.textlength('$64', font=fb(84)) / 2)
    if t > 1.3: ctext(d, 820, '+', fb(140), GREY)
    if t > 2.0: ctext(d, y_base + 30, '$64', fb(84), INK, x=760 - d.textlength('$64', font=fb(84)) / 2)
    steps = [(3.2, '= $128', INK, 'separately'), (4.6, '= $81', PINK, 'Award-Winning Duo · was $108')]
    y = 1180
    for t0, s, col, sub in steps:
        if t < t0: break
        a = ease_out((t - t0) / 0.35)
        f = fb(110 if s != '= $81' else 150)
        cur = [x for x in steps if t >= x[0]][-1]
        if (t0, s) != (cur[0], cur[1]):
            continue
        tw = d.textlength(s, font=f)
        d.text(((W - tw) / 2, y + int(30 * (1 - a))), s, font=f, fill=col)
        ctext(d, y + (130 if s != '= $81' else 170), sub, fm(40), GREY)
        if s == '= $81':
            prev = '$108'; f2 = fm(56); tw2 = d.textlength(prev, font=f2)
            # struck old prices
    if t > 5.4:
        f = fb(34); w1 = d.textlength('LIMITED TIME', font=f) + 56; w2 = d.textlength('YOU SAVE $47', font=f) + 56
        x = (W - w1 - w2 - 20) / 2; x += pill(d, x, 1420, 'LIMITED TIME', fill=(255, 255, 255)) + 20
        pill(d, x, 1420, 'YOU SAVE $47', fill=INK, col=(255, 255, 255))
    if t > 6.0: ship_seal(im, 935, 1290, ease_out((t - 7.4) / 0.4))
    cta(d, t, 6.6)
    return im


# ---------------- 4. CHART: price ticker crash, Head-to-Toe Duo ----------------
def scene_chart(t):
    im = base((236, 244, 248)); d = ImageDraw.Draw(im)
    logo(im); countdown(im, t)
    gx0, gx1, gy0, gy1 = 130, 950, 640, 1100
    for k in range(5):
        y = gy0 + k * (gy1 - gy0) / 4; d.line((gx0, y, gx1, y), fill=(220, 222, 228), width=2)
    d.text((gx0, gy0 - 64), 'HEAD-TO-TOE DUO · PRICE', font=fm(36), fill=GREY)
    # price path: flat at 104, then drops to 78
    pts = []
    n = 60
    p = min(1.0, max(0.0, (t - 0.6) / 4.2))
    for i in range(int(n * p) + 1):
        x = gx0 + (gx1 - gx0) * i / n
        f = i / n
        v = 104 + math.sin(i * 0.7) * 1.2 if f < 0.62 else 104 - 26 * ease_out((f - 0.62) / 0.3)
        y = gy0 + (108 - v) / 34 * (gy1 - gy0)
        pts.append((x, y))
    if len(pts) > 1:
        d.line(pts, fill=PINK, width=9, joint='curve')
        d.ellipse((pts[-1][0] - 14, pts[-1][1] - 14, pts[-1][0] + 14, pts[-1][1] + 14), fill=PINK)
    val = 104 if p < 0.62 else int(round(104 - 26 * ease_out((p - 0.62) / 0.3)))
    ctext(d, 1130, f'${val}', fb(180), PINK if val == 78 else INK)
    if val == 78:
        a = ease_out((t - 4.8) / 0.4)
        f2 = fm(60); tw = d.textlength('$104', font=f2)
        d.text((W / 2 - tw / 2, 1330), '$104', font=f2, fill=GREY); d.line((W / 2 - tw / 2 - 6, 1364, W / 2 + tw / 2 + 6, 1352), fill=PINK, width=6)
        d.text((gx1 - 250, gy1 - 60), '−$26', font=fb(80), fill=PINK)
    h2t = img('h2t')
    if t > 5.4:
        a = ease_out((t - 5.4) / 0.5)
        place(im, h2t, 860, 1500, 300, a)
        pill(d, 130, 1420, 'LIMITED TIME', fill=INK, col=(255, 255, 255))
    if t > 6.2: ship_seal(im, 200, 905, ease_out((t - 6.2) / 0.4))
    cta(d, t, 7.0)
    return im


SCENES = {'price': scene_price, 'receipt': scene_receipt, 'equation': scene_equation, 'chart': scene_chart}


def grain(im, t):
    a = np.asarray(im).astype(np.int16)
    n = np.random.default_rng(int(t * 1000)).normal(0, 2.2, (H // 2, W // 2, 1)).repeat(2, 0).repeat(2, 1)
    return np.clip(a + n, 0, 255).astype(np.uint8)


if __name__ == '__main__':
    name = sys.argv[1]; fn = SCENES[name]; args = sys.argv[2:]
    if '--frames' in args:
        for tt in args[args.index('--frames') + 1].split(','):
            Image.fromarray(grain(fn(float(tt)), float(tt))).save(os.path.join(R, f'{name}_{float(tt):05.2f}.jpg'), quality=88)
        sys.exit()
    out = args[args.index('--out') + 1] if '--out' in args else os.path.join(R, f'{name}_noaudio.mp4')
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    for f in range(int(DUR * FPS)):
        t = f / FPS; p.stdin.write(grain(fn(t), t).tobytes())
    p.stdin.close(); p.wait(); print('done', out)
