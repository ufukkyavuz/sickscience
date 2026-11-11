# Photo-led offer films: client studio photo full-bleed, giant number behind the product (Vision cut-out), countdown from frame 0.
# usage: python offers2.py <vault|network|powercycle|shapeshift> [--frames t,t] [--out f.mp4]
import math, os, sys, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

R = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, DUR = 1080, 1920, 30, 12.0
F = os.path.expanduser('~/Library/Fonts/FoundersGrotesk')
fb = lambda s: ImageFont.truetype(F + '-Bold.otf', s)
fm = lambda s: ImageFont.truetype(F + '-Medium.otf', s)
fl = lambda s: ImageFont.truetype(F + '-Light.otf', s)
INK, PINK, WHITE, GOLD = (18, 18, 22), (169, 33, 192), (255, 255, 255), (222, 190, 120)
LOGO_W = Image.open(os.path.join(R, 'logo_wp.png')).convert('RGBA')
LOGO_WHITE = Image.open(os.path.join(R, 'logo_white.png')).convert('RGBA')


def ease_out(a):
    a = min(1.0, max(0.0, a)); return 1 - (1 - a) ** 3


def ss(a):
    a = min(1.0, max(0.0, a)); return a * a * (3 - 2 * a)


class Plate:
    """9:16 crop of a client photo + its Vision cut-out, with a slow push"""
    def __init__(self, n, cx=0.5, cy=0.5, dark=0.85, zoom=1.0, mask='m_'):
        im = Image.open(os.path.join(R, f'S_{n}.jpg')).convert('RGB')
        m = Image.open(os.path.join(R, f'{mask}{n}.png')).convert('L').resize(im.size)
        ch = im.height / zoom; cw = ch * 9 / 16
        x0 = min(max(cx * im.width - cw / 2, 0), im.width - cw); y0 = min(max(cy * im.height - ch / 2, 0), im.height - ch)
        box = (int(x0), int(y0), int(x0 + cw), int(y0 + ch))
        S = 1.12
        self.bg = ImageEnhance.Brightness(im.crop(box).resize((int(W * S), int(H * S)), Image.LANCZOS)).enhance(dark)
        self.fg = im.crop(box).resize((int(W * S), int(H * S)), Image.LANCZOS)
        self.m = m.crop(box).resize((int(W * S), int(H * S)), Image.LANCZOS).filter(ImageFilter.GaussianBlur(1))
        self.fg = ImageEnhance.Brightness(self.fg).enhance(dark)

    def frame(self, t):
        z = 1.0 + 0.06 * t / DUR                     # slow push, 1.00 -> 1.06 of the frame
        S = 1.12
        w, h = W * z, H * z
        sc = w / (W * S)
        ox = (W * S - W / sc) / 2; oy = (H * S - H / sc) / 2
        box = (ox, oy, ox + W / sc, oy + H / sc)
        bg = self.bg.crop(tuple(map(int, box))).resize((W, H), Image.BICUBIC)
        fg = self.fg.crop(tuple(map(int, box))).resize((W, H), Image.BICUBIC)
        m = self.m.crop(tuple(map(int, box))).resize((W, H), Image.BICUBIC)
        return bg, fg, m


def cdraw(d, cx, cy, s, font, fill):
    """draw s with its real ink box centred on (cx, cy)"""
    bb = d.textbbox((0, 0), s, font=font, anchor='ls')
    d.text((cx - (bb[0] + bb[2]) / 2, cy - (bb[1] + bb[3]) / 2), s, font=font, fill=fill, anchor='ls')


def ctext(d, y, s, font, fill=WHITE, cx=W / 2, anchor='mt'):
    d.text((cx, y), s, font=font, fill=fill, anchor=anchor)


def shadow_text(layer, xy, s, font, fill, anchor='mt', blur=18, alpha=110):
    sh = Image.new('L', layer.size, 0); ImageDraw.Draw(sh).text((xy[0], xy[1] + 8), s, font=font, fill=alpha, anchor=anchor)
    layer.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(blur)))
    ImageDraw.Draw(layer).text(xy, s, font=font, fill=fill, anchor=anchor)


TOP = 172   # logo at the Figma Story position; countdown starts at the 270 safe line


def countdown(im, t, label, dark_text=False):
    PILL, DIG, LAB = (INK, WHITE, INK) if dark_text else (WHITE, INK, WHITE)
    d = ImageDraw.Draw(im)
    s_ = max(0, 59 - int(t)); txt = f'00:{s_:02d}'
    f = fb(124)
    bb = d.textbbox((0, 0), '00:00', font=f, anchor='ls')     # fixed pill width, digits steady
    tw = bb[2] - bb[0]
    y0, y1 = 272, 272 + 150
    cx, cy = W / 2, (y0 + y1) / 2
    d.rounded_rectangle((cx - tw / 2 - 44, y0, cx + tw / 2 + 44, y1), 34, fill=PILL)
    cdraw(d, cx, cy, txt, f, DIG)
    ly = y1 + 34
    if not dark_text:
        sh = Image.new('L', im.size, 0); cdraw(ImageDraw.Draw(sh), W / 2, ly + 4, label, fm(34), 150)
        im.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(6)))
    cdraw(d, W / 2, ly, label, fm(34), LAB)


def logo(im, white=False):
    # official logo straight on the photo, soft shadow only (no box); all-white version on red photos
    src = LOGO_WHITE if white else LOGO_W
    l = src.resize((360, int(360 * src.height / src.width)), Image.LANCZOS)
    x0 = (W - l.width) // 2; y0 = TOP + 22
    sh = Image.new('L', im.size, 0); sh.paste(l.split()[3].point(lambda v: v * 150 // 255), (x0, y0 + 4))
    im.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(8)))
    im.paste(l, (x0, y0), l)


def pill(d, cx, y, s, fill=WHITE, col=INK, font=None):
    font = font or fb(36)
    tw = d.textlength(s, font=font)
    d.rounded_rectangle((cx - tw / 2 - 30, y, cx + tw / 2 + 30, y + 72), 36, fill=fill)
    cdraw(d, cx, y + 36, s, font, col)
    return tw + 60


def pills(d, y, items):
    f = fb(36)
    ws = [d.textlength(s, font=f) + 60 for s, _, _ in items]
    x = W / 2 - (sum(ws) + 18 * (len(ws) - 1)) / 2
    for (s, fill, col), w in zip(items, ws):
        pill(d, x + w / 2, y, s, fill, col); x += w + 18


def seal(im, cx, cy, a, R0=112):
    if a <= 0: return
    r = int(R0 * (0.85 + 0.15 * ease_out(a)))
    d = ImageDraw.Draw(im)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=WHITE, outline=PINK, width=5)
    tx, ty = cx - 40, cy - 54
    d.rectangle((tx, ty, tx + 50, ty + 30), fill=PINK); d.polygon([(tx + 50, ty + 8), (tx + 70, ty + 8), (tx + 80, ty + 20), (tx + 80, ty + 30), (tx + 50, ty + 30)], fill=PINK)
    d.ellipse((tx + 8, ty + 26, tx + 24, ty + 42), fill=PINK); d.ellipse((tx + 56, ty + 26, tx + 72, ty + 42), fill=PINK)
    cdraw(d, cx, cy + 20, 'FREE', fb(40), INK); cdraw(d, cx, cy + 60, 'SHIPPING', fb(30), INK)


def price_line(d, y, new, old, col=WHITE, dark=False):
    """new price big + old price struck, sharing one baseline, the pair centred"""
    f1, f2 = fb(120), fm(64)
    w1 = d.textlength(new, font=f1); w2 = d.textlength(old, font=f2)
    x = W / 2 - (w1 + 30 + w2) / 2
    yb = y + 100                                     # common baseline
    if not dark:
        sh = Image.new('L', d._image.size, 0); sd = ImageDraw.Draw(sh)
        sd.text((x, yb + 8), new, font=f1, fill=120, anchor='ls'); sd.text((x + w1 + 30, yb + 8), old, font=f2, fill=120, anchor='ls')
        d._image.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(14)))
    d.text((x, yb), new, font=f1, fill=col, anchor='ls')
    d.text((x + w1 + 30, yb), old, font=f2, fill=(110, 110, 118) if dark else (230, 230, 235), anchor='ls')
    ob = d.textbbox((x + w1 + 30, yb), old, font=f2, anchor='ls')
    ym = (ob[1] + ob[3]) / 2
    d.line((ob[0] - 6, ym + 6, ob[2] + 6, ym - 6), fill=PINK, width=7)


def cta(d, t, t0, y=1260):
    if t < t0: return
    a = ease_out((t - t0) / 0.4)
    f = fb(46); s = 'SHOP NOW'; tw = d.textlength(s, font=f)
    yy = y + int(26 * (1 - a))
    d.rounded_rectangle((W / 2 - tw / 2 - 64, yy, W / 2 + tw / 2 + 64, yy + 104), 52, fill=PINK)
    cdraw(d, W / 2, yy + 52, s, f, WHITE)


def big_front(plate, t, text, y, size, t0=0.4, col=WHITE, sub=None, x=None, anchor='mt', subsize=None, shadow=170, subcol=None):
    bg, fg, m = plate.frame(t)
    layer = bg.copy()
    a = ease_out((t - t0) / 0.6)
    if a > 0:
        f = fb(size); xx = W / 2 if x is None else x
        yy = y + int(80 * (1 - a))
        sh = Image.new('L', (W, H), 0); sd = ImageDraw.Draw(sh)
        sd.text((xx, yy + 16), text, font=f, fill=int(shadow * a), anchor=anchor)
        if sub: sd.text((xx, yy + size * 0.86 + 10), sub, font=fb(subsize or int(size * 0.24)), fill=int(shadow * a), anchor=anchor)
        layer.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(26)))
        tl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); td = ImageDraw.Draw(tl)
        td.text((xx, yy), text, font=f, fill=col + (int(255 * a),), anchor=anchor)
        if sub: td.text((xx, yy + size * 0.86), sub, font=fb(subsize or int(size * 0.24)), fill=(subcol or col) + (int(255 * a),), anchor=anchor)
        layer.paste(tl, (0, 0), tl)
    return layer


def big_behind(plate, t, text, y, size, t0=0.4, col=WHITE, sub=None):
    """giant number between photo and cut-out product"""
    bg, fg, m = plate.frame(t)
    layer = bg.copy()
    a = ease_out((t - t0) / 0.7)
    if a > 0:
        f = fb(size)
        yy = y + int(120 * (1 - a))
        tl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); td = ImageDraw.Draw(tl)
        td.text((W / 2, yy), text, font=f, fill=col + (int(255 * a),), anchor='mt')
        if sub: td.text((W / 2, yy + size * 0.80), sub, font=fb(int(size * 0.28)), fill=col + (int(255 * a),), anchor='mt')
        sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).text((W / 2, yy + 14), text, font=f, fill=int(90 * a), anchor='mt')
        layer.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(24)))
        layer.paste(tl, (0, 0), tl)
    layer.paste(fg, (0, 0), m)                       # product back on top of the number
    return layer


# ---------------- scenes ----------------
P = {}
def plate(key, *a, **k):
    if key not in P: P[key] = Plate(*a, **k)
    return P[key]


def vault(t):
    pl = plate('vault', '0342', cx=0.45, cy=0.5, dark=0.9)
    im = big_front(pl, t, '20%', 520, 330, sub='OFF THE VAULT', subsize=78)
    logo(im, white=True); countdown(im, t, 'LIMITED TIME OFFER')
    d = ImageDraw.Draw(im)
    if t > 1.8: price_line(d, 940, '$144', '$180')
    if t > 2.6: pills(d, 1100, [('BUNDLE DEAL', WHITE, INK), ('YOU SAVE $36', INK, WHITE)])
    if t > 3.2: seal(im, 182, 360, ease_out((t - 3.2) / 0.4))
    cta(d, t, 3.8)
    return im


def network(t):
    pl = plate('network', '0431', cx=0.5, cy=0.5, dark=0.92)
    im = big_front(pl, t, '15%', 520, 330, col=GOLD, sub='SUBSCRIBE & SAVE', subsize=78)
    logo(im); countdown(im, t, 'SUBSCRIBE & SAVE 15%')
    d = ImageDraw.Draw(im)
    if t > 1.8: price_line(d, 940, '$62.90', '$74')
    if t > 2.6: pills(d, 1100, [('EVERY ORDER', WHITE, INK), ('NetWork', GOLD, INK)])
    cta(d, t, 3.6)
    return im


def powercycle(t):
    pl = plate('pc', '0333', cx=0.62, cy=0.5, dark=0.88)
    bg, fg, m = pl.frame(t)
    im = bg.copy()
    # kinetic rows of "30% OFF" sliding in alternate directions behind the capsule
    f = fb(150)
    unit = 'SAVE 15%  '
    uw = ImageDraw.Draw(im).textlength(unit, font=f)
    tl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); td = ImageDraw.Draw(tl)
    for r in range(3):
        y = 520 + r * 150
        dirn = 1 if r % 2 == 0 else -1
        off = (t * 140 * dirn) % uw
        a = ease_out((t - 0.2 - r * 0.12) / 0.5)
        if a <= 0: continue
        x = -uw + off
        col = (255, 255, 255, int(235 * a)) if r != 2 else (255, 255, 255, int(255 * a))
        while x < W:
            td.text((x, y), unit, font=f, fill=col); x += uw
    im.paste(tl, (0, 0), tl)
    im.paste(fg, (0, 0), m)
    logo(im, white=True); countdown(im, t, 'SUBSCRIBE & SAVE 15%')
    d = ImageDraw.Draw(im)
    if t > 2.0: price_line(d, 940, '$54.40', '$64')
    if t > 2.8: pills(d, 1100, [('SUBSCRIBE & SAVE', WHITE, INK), ('PowerCycle', GRN_PILL, INK)])
    cta(d, t, 3.6)
    return im
GRN_PILL = (170, 230, 150)


def shapeshift(t):
    pl = plate('ss', '0469', cx=0.5, cy=0.5, dark=0.9)
    im = big_front(pl, t, '15%', 520, 330, sub='SUBSCRIBE & SAVE', subsize=78, subcol=(225, 200, 255))
    logo(im); countdown(im, t, 'SUBSCRIBE & SAVE 15%')
    d = ImageDraw.Draw(im)
    if t > 1.8: price_line(d, 940, '$54.40', '$64')
    if t > 2.6: pills(d, 1100, [('EVERY ORDER', WHITE, INK), ('ShapeShift', (215, 190, 255), INK)])
    cta(d, t, 3.6)
    return im


def rows(im, t, unit, col=(255, 255, 255), y0=520, outline=False):
    f = fb(150)
    uw = ImageDraw.Draw(im).textlength(unit, font=f)
    tl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); td = ImageDraw.Draw(tl)
    for r in range(3):
        y = y0 + r * 150
        dirn = 1 if r % 2 == 0 else -1
        off = (t * 140 * dirn) % uw
        a = ease_out((t - 0.2 - r * 0.12) / 0.5)
        if a <= 0: continue
        x = -uw + off
        while x < W:
            if outline:
                td.text((x, y), unit, font=f, fill=(0, 0, 0, 0), stroke_width=4, stroke_fill=col + (int(255 * a),))
            else:
                td.text((x, y), unit, font=f, fill=col + (int(245 * a),))
            x += uw
    im.paste(tl, (0, 0), tl)


def kinetic(pl, t, unit, col=(255, 255, 255)):
    bg, fg, m = pl.frame(t)
    im = bg.copy(); rows(im, t, unit, col); im.paste(fg, (0, 0), m)
    return im


def vault_k(t):
    pl = plate('vault_k', '0342', cx=0.45, cy=0.5, dark=0.9)
    bg, fg, m = pl.frame(t)
    im = bg.copy(); rows(im, t, '25% OFF  ', outline=True)
    logo(im); countdown(im, t, 'LIMITED TIME OFFER')
    d = ImageDraw.Draw(im)
    if t > 2.0: price_line(d, 940, '$144', '$180')
    if t > 2.8: pills(d, 1100, [('THE VAULT', WHITE, INK), ('YOU SAVE $36', INK, WHITE)])
    if t > 3.2: seal(im, 182, 360, ease_out((t - 3.2) / 0.4))
    cta(d, t, 3.8)
    return im


def network_k(t):
    pl = plate('network_k', '0431', cx=0.5, cy=0.5, dark=0.92, mask='mc_')
    im = kinetic(pl, t, '30% OFF  ', GOLD)
    logo(im); countdown(im, t, 'SUBSCRIBE & SAVE 15%')
    d = ImageDraw.Draw(im)
    if t > 2.0: price_line(d, 940, '$62.90', '$74')
    if t > 2.8: pills(d, 1100, [('EVERY ORDER', WHITE, INK), ('NetWork', GOLD, INK)])
    cta(d, t, 3.6)
    return im


def shapeshift_k(t):
    pl = plate('ss_k', '0469', cx=0.5, cy=0.5, dark=0.9, mask='mc_')
    im = kinetic(pl, t, '40% OFF  ')
    logo(im); countdown(im, t, 'SUBSCRIBE & SAVE 15%')
    d = ImageDraw.Draw(im)
    if t > 2.0: price_line(d, 940, '$54.40', '$64')
    if t > 2.8: pills(d, 1100, [('EVERY ORDER', WHITE, INK), ('ShapeShift', (215, 190, 255), INK)])
    cta(d, t, 3.6)
    return im


RED = (226, 30, 45)


def bf_scene(key, n, unit, t, label, price, old, pills_, sealed=False, rowcol=(255, 255, 255), lay=None):
    pl = plate(key, n, cx=0.5, cy=0.5, dark=1.0)
    bg, fg, m = pl.frame(t)
    im = bg.copy(); rows(im, t, unit, rowcol); im.paste(fg, (0, 0), m)
    logo(im); countdown(im, t, label)
    d = ImageDraw.Draw(im)
    py, ply, cy = lay or (940, 1100, 1260)
    if t > 2.0: price_line(d, py, price, old)
    if t > 2.8: pills(d, ply, pills_)
    if sealed and t > 3.2: seal(im, 182, 360, ease_out((t - 3.2) / 0.4))
    cta(d, t, 3.6, y=cy)
    return im


def vault_bf(t):
    return bf_scene('vbf', 'bftrio', '20% OFF  ', t, 'LIMITED TIME OFFER', '$144', '$180', [('THE VAULT', WHITE, INK), ('YOU SAVE $36', RED, WHITE)], sealed=True, lay=(946, 872, 1600))


def network_bf(t):
    return bf_scene('nbf', 'bfnetwork', 'SAVE 15%  ', t, 'SUBSCRIBE & SAVE 15%', '$62.90', '$74', [('SUBSCRIBE & SAVE', WHITE, INK), ('NetWork', RED, WHITE)])


def shapeshift_bf(t):
    return bf_scene('sbf', 'bfshapeshift', 'SAVE 15%  ', t, 'SUBSCRIBE & SAVE 15%', '$54.40', '$64', [('SUBSCRIBE & SAVE', WHITE, INK), ('ShapeShift', (215, 190, 255), INK)])


SCENES = {'vault_bf': vault_bf, 'network_bf': network_bf, 'shapeshift_bf': shapeshift_bf, 'vault_k': vault_k, 'network_k': network_k, 'shapeshift_k': shapeshift_k, 'vault': vault, 'network': network, 'powercycle': powercycle, 'shapeshift': shapeshift}


def grain(im, t):
    a = np.asarray(im).astype(np.int16)
    n = np.random.default_rng(int(t * 1000)).normal(0, 3.0, (H // 2, W // 2, 1)).repeat(2, 0).repeat(2, 1)
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
