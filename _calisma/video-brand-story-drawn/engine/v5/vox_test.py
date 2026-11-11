# Vox-style paper collage test over narration part 1 (~24 s).
# Real cut-outs (sketch pieces, founder prints, product PNGs) with paper edges and contact shadows,
# animated on twos (15 fps holds) with a light boil, label strips, stamps, marker strokes, torn-paper wipes.
# usage: python vox_test.py OUT_noaudio.mp4 [events.json]
import os, sys, math, json, subprocess
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy import ndimage

W, H, FPS, HOLD = 1080, 1920, 30, 2          # HOLD=2 -> animate on twos
LEAD = 0.35                                    # narration starts at video t = LEAD
END = 23.72 + LEAD + 0.9
DRIVE = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience")
SK = DRIVE + '/_calisma/video-brand-story-drawn/sketch_scenes'
PNG = DRIVE + '/Products/png'
PR = os.path.expanduser('~/sickscience-work/brandfilm/v4/prints')
FB = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Bold.otf')
FS = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Semibold.otf')
MAG = (169, 33, 192); INK = (24, 22, 24); YEL = (255, 222, 60); PAPER = (250, 247, 240)
RNG = np.random.default_rng(7)
OUT = sys.argv[1]
EVJ = sys.argv[2] if len(sys.argv) > 2 else None


def T(n): return n + LEAD                       # narration time -> video time


# ---------------------------------------------------------------- textures
def paper_tex(w, h, seed):
    r = np.random.default_rng(seed)
    n = r.standard_normal((h // 4 + 1, w // 4 + 1)).astype(np.float32)
    n = cv2.resize(cv2.GaussianBlur(n, (0, 0), 1.2), (w, h))
    f = r.standard_normal((h, w)).astype(np.float32)
    f = cv2.GaussianBlur(f, (0, 0), 0.7)
    return 1.0 + 0.018 * n + 0.012 * f


def rough_alpha(mask, amp=5, seed=0):
    """binary mask -> alpha with a hand-cut, slightly irregular edge"""
    m = mask.astype(np.float32)
    r = np.random.default_rng(seed)
    nz = cv2.resize(r.standard_normal((mask.shape[0] // 18 + 2, mask.shape[1] // 18 + 2)).astype(np.float32),
                    (mask.shape[1], mask.shape[0]), interpolation=cv2.INTER_CUBIC)
    d = cv2.GaussianBlur(m, (0, 0), amp)
    a = (d + 0.10 * nz) > 0.5
    a = cv2.GaussianBlur(a.astype(np.float32), (0, 0), 0.8)
    return np.clip(a * 255, 0, 255).astype(np.uint8)


def to_piece(rgb, alpha, seed):
    """rgb float/uint8 + alpha -> RGBA PIL with a faint cut-edge rim"""
    rgb = rgb.astype(np.float32)
    a = alpha.astype(np.float32) / 255
    er = cv2.erode((a > 0.5).astype(np.uint8), np.ones((3, 3), np.uint8), iterations=2)
    rim = ((a > 0.5) & (er == 0)).astype(np.float32)
    rgb = rgb * (1 - 0.10 * rim[..., None])
    rgb = rgb * paper_tex(rgb.shape[1], rgb.shape[0], seed)[..., None] ** 0.6
    out = np.dstack([np.clip(rgb, 0, 255), alpha]).astype(np.uint8)
    return Image.fromarray(out, 'RGBA')


_flat = {}


def flat_sketch(path):
    if path in _flat: return _flat[path]
    im = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
    small = cv2.resize(im, (im.shape[1] // 4, im.shape[0] // 4), interpolation=cv2.INTER_AREA)
    bg = cv2.resize(cv2.medianBlur(small, 31), (im.shape[1], im.shape[0]), interpolation=cv2.INTER_CUBIC).astype(np.float32)
    fl = np.clip(im.astype(np.float32) / np.maximum(bg, 1) * np.array(PAPER, np.float32), 0, 255)
    L = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY).astype(np.float32)
    Lb = cv2.cvtColor(bg.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32)
    hsv = cv2.cvtColor(im, cv2.COLOR_RGB2HSV)
    ink = ((Lb - L) > 24) | ((hsv[..., 1] > 80) & (hsv[..., 2] > 60) & ((Lb - L) > 8))
    ink = ndimage.binary_opening(ink, iterations=1)
    lab, n = ndimage.label(ink); sz = ndimage.sum(ink, lab, range(1, n + 1))
    ink = np.isin(lab, np.where(sz >= 25)[0] + 1)
    _flat[path] = (fl, ink)
    return _flat[path]


def cut_sketch(name, box, height=None, width=None, border=22, seed=0):
    fl, ink = flat_sketch(f'{SK}/{name}.png')
    x0, y0, x1, y1 = box; m = border * 3
    x0, y0 = max(0, x0 - m), max(0, y0 - m); x1, y1 = min(fl.shape[1], x1 + m), min(fl.shape[0], y1 + m)
    rgb, k = fl[y0:y1, x0:x1], ink[y0:y1, x0:x1]
    sil = ndimage.binary_dilation(k, iterations=border)
    sil = ndimage.binary_closing(sil, iterations=border)
    sil = ndimage.binary_fill_holes(sil)
    lab, n = ndimage.label(sil)
    if n > 1:                                                     # keep the main paper piece(s)
        sz = ndimage.sum(sil, lab, range(1, n + 1)); sil = np.isin(lab, np.where(sz >= sz.max() * 0.08)[0] + 1)
    ys, xs = np.where(sil); rgb, sil = rgb[ys.min():ys.max() + 1, xs.min():xs.max() + 1], sil[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    a = rough_alpha(sil, 3, seed)
    rgb = rgb.copy(); rgb[a < 128] = PAPER
    s = (height / rgb.shape[0]) if height else (width / rgb.shape[1])
    sz = (max(2, int(rgb.shape[1] * s)), max(2, int(rgb.shape[0] * s)))
    return to_piece(cv2.resize(rgb, sz, interpolation=cv2.INTER_AREA), cv2.resize(a, sz, interpolation=cv2.INTER_AREA), seed)


def cut_product(code, cm, ppcm=34, seed=0):
    import glob
    im = Image.open(glob.glob(f'{PNG}/{code}*.png')[0]).convert('RGBA')
    im = im.crop(im.getchannel('A').getbbox())
    h = int(cm * ppcm); im = im.resize((int(im.width * h / im.height), h), Image.LANCZOS)
    pad = 26; A = np.zeros((im.height + 2 * pad, im.width + 2 * pad), np.uint8)
    A[pad:-pad, pad:-pad] = np.asarray(im.getchannel('A'))
    sil = ndimage.binary_dilation(A > 100, iterations=13)
    a = rough_alpha(sil, 2.5, seed)
    base = np.zeros((A.shape[0], A.shape[1], 3), np.float32) + np.array(PAPER, np.float32)
    base = base * paper_tex(A.shape[1], A.shape[0], seed)[..., None] ** 0.6
    p = Image.fromarray(np.dstack([np.clip(base, 0, 255), a]).astype(np.uint8), 'RGBA')
    p.alpha_composite(im, (pad, pad))
    return p


def photo(path, width, seed=0):
    im = Image.open(path).convert('RGB'); s = width / im.width
    im = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    b = 18; bb = 18
    card = np.zeros((im.height + b + bb, im.width + 2 * b, 3), np.float32) + np.array((248, 246, 241), np.float32)
    card *= paper_tex(card.shape[1], card.shape[0], seed)[..., None] ** 0.5
    card[b:b + im.height, b:b + im.width] = np.asarray(im, np.float32)
    a = np.full(card.shape[:2], 255, np.uint8)
    return Image.fromarray(np.dstack([np.clip(card, 0, 255), a]).astype(np.uint8), 'RGBA')


def torn_strip(w, h, color, seed, jag=9):
    r = np.random.default_rng(seed)
    pts = []
    for y in np.linspace(0, h, 9): pts.append((r.uniform(0, jag), y))
    for y in np.linspace(h, 0, 9): pts.append((w - r.uniform(0, jag), y))
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).polygon(pts, fill=255)
    rgb = np.zeros((h, w, 3), np.float32) + np.array(color, np.float32)
    rgb *= paper_tex(w, h, seed)[..., None]
    return Image.fromarray(np.dstack([np.clip(rgb, 0, 255), np.asarray(m.filter(ImageFilter.GaussianBlur(0.6)))]).astype(np.uint8), 'RGBA')


def label(text, size=64, bg=INK, fg=(255, 255, 255), font=FB, seed=0, padx=30, pady=22):
    f = ImageFont.truetype(font, size)
    lines = text.split('\n')
    bxs = [f.getbbox(l) for l in lines]
    tw = max(b[2] - b[0] for b in bxs); lh = int(size * 0.98)
    w, h = tw + 2 * padx, lh * len(lines) + 2 * pady
    p = torn_strip(w, h, bg, seed)
    d = ImageDraw.Draw(p)
    for i, (l, b) in enumerate(zip(lines, bxs)):
        d.text(((w - (b[2] - b[0])) / 2 - b[0], pady + i * lh - int(size * 0.12)), l, font=f, fill=fg)
    return p


def glyph_card(ch, size=250, seed=0):
    f = ImageFont.truetype(FB, size); b = f.getbbox(ch)
    w, h = b[2] - b[0] + 56, int(size * 0.86) + 56
    p = torn_strip(w, h, (252, 250, 244) if seed % 2 else YEL, seed, jag=6)
    ImageDraw.Draw(p).text((28 - b[0], 28 - int(size * 0.2)), ch, font=f, fill=INK)
    return p


def stamp(text, r=118, color=(214, 30, 110), seed=0):
    S = 2 * r + 20; im = Image.new('RGBA', (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.ellipse((10, 10, S - 10, S - 10), outline=color + (255,), width=12)
    d.ellipse((30, 30, S - 30, S - 30), outline=color + (255,), width=4)
    f = ImageFont.truetype(FB, int(r * 0.78)); b = f.getbbox(text)
    d.text(((S - (b[2] - b[0])) / 2 - b[0], (S - (b[3] - b[1])) / 2 - b[1]), text, font=f, fill=color + (255,))
    a = np.asarray(im.getchannel('A')).astype(np.float32)
    nz = np.random.default_rng(seed).random(a.shape)
    nz = cv2.GaussianBlur(nz.astype(np.float32), (0, 0), 1.6)
    a = a * np.clip((nz - 0.36) * 6, 0.35, 1.0)
    im.putalpha(Image.fromarray(a.astype(np.uint8)))
    return im


def tape(w=170, h=52, seed=0):
    p = torn_strip(w, h, (236, 228, 205), seed, jag=7)
    a = np.asarray(p.getchannel('A')).astype(np.float32) * 0.78
    p.putalpha(Image.fromarray(a.astype(np.uint8)))
    return p


# ---------------------------------------------------------------- easing
def clamp(u): return max(0.0, min(1.0, u))
def eio(u): u = clamp(u); return u * u * (3 - 2 * u)
def eout(u): u = clamp(u); return 1 - (1 - u) ** 3
def back(u, s=1.9): u = clamp(u) - 1; return 1 + (s + 1) * u ** 3 + s * u ** 2


# ---------------------------------------------------------------- scene graph
class E:
    def __init__(s, img, x, y, t, entry='slide', rot=0.0, sc=1.0, z=0, frm=(0, 1), dur=0.38, out=None, outdir=(0, -1),
                 parent=None, lift=0.0, shadow=True, sfx=None):
        s.img, s.x, s.y, s.t, s.entry, s.rot, s.sc, s.z, s.frm, s.dur = img, x, y, t, entry, rot, sc, z, frm, dur
        s.out, s.outdir, s.parent, s.moves, s.lift0, s.shadow = out, outdir, parent, [], lift, shadow
        s.sfx = sfx; s.id = len(ALL); ALL.append(s)
        if shadow:
            a = img.getchannel('A').filter(ImageFilter.GaussianBlur(7))
            s.sh = Image.new('RGBA', img.size, (25, 18, 12, 0)); s.sh.putalpha(a.point(lambda v: int(v * 0.42)))

    def move(s, t, dur=0.4, **kw):
        s.moves.append((t, dur, kw)); return s

    def pose(s, t):
        x, y, rot, sc, op, lift = s.x, s.y, s.rot, s.sc, 1.0, s.lift0
        for (mt, md, kw) in s.moves:
            u = eio((t - mt) / md)
            if t <= mt: break
            x += (kw.get('x', x) - x) * u; y += (kw.get('y', y) - y) * u
            rot += (kw.get('rot', rot) - rot) * u; sc += (kw.get('sc', sc) - sc) * u
            if 0 < u < 1: lift = max(lift, 0.5 * math.sin(math.pi * u))
        u = (t - s.t) / s.dur
        if u < 0: return None
        if u < 1:
            if s.entry == 'slide':
                k = 1 - back(u, 1.4); x += s.frm[0] * 1300 * k; y += s.frm[1] * 1500 * k
                rot += 14 * k * (1 if s.frm[0] >= 0 else -1); lift = max(lift, 0.6 * (1 - u))
            elif s.entry == 'pop':
                sc *= max(0.01, back(u, 2.6)); rot += 10 * (1 - eout(u))
            elif s.entry == 'drop':
                k = 1 - eout(u); sc *= 1 + 0.45 * k; y -= 60 * k; lift = max(lift, 1.0 * k); op = clamp(u * 3)
            elif s.entry == 'stamp':
                k = 1 - clamp(u * 2.4); sc *= 1 + 0.9 * k; lift = max(lift, 1.2 * k); op = clamp(u * 4)
            elif s.entry == 'cut':
                pass
        if s.out is not None and t > s.out:
            v = (t - s.out) / 0.42
            if v >= 1: return None
            k = v * v; x += s.outdir[0] * 1500 * k; y += s.outdir[1] * 2000 * k
            rot += 35 * k * (1 if s.outdir[0] >= 0 else -1); lift = max(lift, 0.8 * min(1, v * 3))
        if s.parent is not None:
            pp = s.parent.pose(t)
            if pp is None: return None
            px, py, prot, psc, pop_, _ = pp
            c, sn = math.cos(math.radians(-prot)), math.sin(math.radians(-prot))
            dx, dy = (x * c - y * sn) * psc, (x * sn + y * c) * psc
            x, y, rot, sc, op = px + dx, py + dy, rot + prot, sc * psc, op * pop_
        return x, y, rot, sc, op, lift


ALL = []
STROKES = []       # (pts, width, color, t0, dur, out)
BURSTS = []        # (x, y, t0)
WIPES = []         # (t_cover, color)
SHAKES = []        # t
SCENES = []        # (t_start, bg_color)
EVENTS = []        # sound events (kind, t)


def ev(kind, t, **k): EVENTS.append(dict(kind=kind, t=round(t, 3), **k))


# ---------------------------------------------------------------- the story (narration part 1)
SCENES.append((-10.0, (244, 238, 228)))

# S1  "This story didn't begin with skincare."
prods = [('ERH_7470B', 12, 215), ('ERH_7477C', 12, 425), ('ERH_7460B', 14, 650), ('ERH_7487', 19, 880)]
P = []
for i, (c, cm, x) in enumerate(prods):
    im = cut_product(c, cm, 34, seed=10 + i)
    P.append(E(im, x, 1180 - im.height / 2, T(-0.6) + i * 0.13, 'slide', rot=(-4, 3, -2, 5)[i], frm=(0, 1), out=T(2.42) + i * 0.05,
               outdir=((-1, -0.2), (-0.4, -1), (0.4, -1), (1, -0.2))[i]))
    ev('slide', P[-1].t + 0.12)
sk = E(label('SKINCARE', 92, seed=3), 540, 520, T(0.05), 'stamp', rot=-3, out=T(2.5), outdir=(0, -1)); ev('stamp', sk.t + 0.06)
STROKES.append(([(120, 640), (360, 800), (640, 980), (960, 1260)], 30, MAG, T(0.74), 0.24, T(2.4)))
STROKES.append(([(960, 640), (700, 830), (420, 1040), (130, 1260)], 30, MAG, T(1.02), 0.24, T(2.4)))
ev('marker', T(0.74), dur=0.24); ev('marker', T(1.02), dur=0.24)
for e in P + [sk]: ev('swish', e.out + 0.05)

# S2  "It began with two curious minds."
hl = E(cut_sketch('master/m01_two_minds', (171, 1174, 640, 1870), height=560, seed=21), 285, 930, T(2.88), 'slide', rot=-3, frm=(-1, 0), out=T(5.55), outdir=(-1, 0))
hr = E(cut_sketch('master/m01_two_minds', (880, 1174, 1365, 1870), height=560, seed=22), 795, 930, T(3.38), 'slide', rot=3, frm=(1, 0), out=T(5.55), outdir=(1, 0))
q = E(cut_sketch('master/m01_two_minds', (650, 1270, 800, 1600), height=260, seed=23), 540, 820, T(4.06), 'pop', rot=8, out=T(5.55))
q.move(T(4.42), 0.18, sc=1.3, rot=-10).move(T(4.62), 0.2, sc=1.0, rot=6)
ev('slide', hl.t + 0.1); ev('slide', hr.t + 0.1); ev('pop', q.t + 0.05); ev('boing', T(4.42))
tcm = E(label('TWO CURIOUS\nMINDS', 96, bg=MAG, seed=24), 540, 1370, T(5.14) - 0.05, 'stamp', rot=-2, out=T(5.6)); ev('stamp', tcm.t + 0.06); SHAKES.append(tcm.t + 0.06)
WIPES.append((T(5.86), MAG)); SCENES.append((T(5.86), (232, 224, 240))); ev('wipe', T(5.86))

# S3  "In 2009, Polen ... and Merve ... met in a chemistry and biology class."
dig = []
for i, ch in enumerate('2009'):
    g = E(glyph_card(ch, 240, seed=31 + i), 255 + i * 190, 390, T(6.42) + i * 0.15, 'stamp', rot=(-6, 4, -3, 7)[i], out=T(10.9) + i * 0.04, outdir=(0, -1))
    dig.append(g); ev('stamp_small', g.t + 0.05)
SHAKES.append(T(6.42) + 0.45 + 0.05)
ph = E(photo(f'{PR}/pair_t.png', 560, seed=35), 540, 930, T(7.35), 'slide', rot=-3, frm=(0, 1)); ev('slide', ph.t + 0.12)
t1 = E(tape(seed=36), -230, -360, T(7.72), 'pop', rot=-28, parent=ph, shadow=False); t2 = E(tape(seed=37), 230, -360, T(7.84), 'pop', rot=24, parent=ph, shadow=False)
ev('tape', t1.t); ev('tape', t2.t)
n1 = E(label('Polen Koçak Denizci', 58, font=FS, seed=38), 540, 1385, T(7.7), 'slide', rot=-1.5, frm=(-1, 0), out=T(10.95), outdir=(-1, 0)); ev('slide', n1.t + 0.1)
n2 = E(label('Merve Yıldırım Canpolat', 58, bg=MAG, font=FS, seed=39), 540, 1490, T(9.34), 'slide', rot=1.5, frm=(1, 0), out=T(11.0), outdir=(1, 0)); ev('slide', n2.t + 0.1)
for e in dig + [n1, n2]: ev('swish', e.out + 0.05)
ph.move(T(10.92), 0.45, y=640, sc=0.78, rot=2)
desk = E(cut_sketch('master/m02_met_2009', (144, 1261, 1427, 2110), width=760, seed=40), 540, 1420, T(11.05), 'slide', rot=-1, frm=(0, 1)); ev('slide', desk.t + 0.12)
c1 = E(label('CHEMISTRY', 56, bg=YEL, fg=INK, seed=41), 330, 1160, T(11.44), 'pop', rot=-5, z=2); ev('pop', c1.t + 0.05)
c2 = E(label('BIOLOGY', 56, bg=YEL, fg=INK, seed=42), 770, 1160, T(12.04), 'pop', rot=4, z=2); ev('pop', c2.t + 0.05)

# S4  "They kept working together."
sc_ = E(photo(f'{PR}/scope_t.png', 430, seed=43), 760, 900, T(13.24), 'slide', rot=6, frm=(1, 0), z=1); ev('slide', sc_.t + 0.12)
t3 = E(tape(150, 48, seed=44), 0, -300, T(13.6), 'pop', rot=-6, parent=sc_, shadow=False); ev('tape', t3.t)
ph.move(T(13.24), 0.4, x=340, y=700, sc=0.74, rot=-4)
WIPES.append((T(14.86), INK)); SCENES.append((T(14.86), (226, 236, 229))); ev('wipe', T(14.86))

# S5  "Both earned PhDs, and led dozens of studies on stem cells, regenerative medicine, plant-derived exosomes and cancer research."
fl_ = E(cut_sketch('01_two_geneticists', (125, 936, 600, 2128), height=720, seed=51), 300, 860, T(15.08), 'slide', rot=-2, frm=(0, 1))
fr_ = E(cut_sketch('01_two_geneticists', (930, 936, 1380, 2128), height=720, seed=52), 785, 860, T(15.28), 'slide', rot=2, frm=(0, 1))
ev('slide', fl_.t + 0.1); ev('slide', fr_.t + 0.1)
s1 = E(stamp('PhD', seed=53), 30, 260, T(15.78), 'stamp', rot=-10, parent=fl_); s2 = E(stamp('PhD', seed=54), -30, 260, T(16.0), 'stamp', rot=8, parent=fr_)
ev('stamp', s1.t + 0.05); ev('stamp', s2.t + 0.05); SHAKES += [s1.t + 0.05, s2.t + 0.05]
fl_.move(T(16.9), 0.4, x=250, y=520, sc=0.62, rot=-6); fr_.move(T(16.9), 0.4, x=830, y=520, sc=0.62, rot=6)
fl_.out = fr_.out = T(18.05); fl_.outdir, fr_.outdir = (-1, -0.3), (1, -0.3); ev('swish', T(18.08))
stack = E(cut_sketch('05_papers', (60, 880, 880, 1800), width=560, seed=55), 540, 1220, T(17.1), 'drop', rot=-3, out=T(18.12), outdir=(0, 1)); ev('drop', T(17.1) + 0.3)
dz = E(label('DOZENS OF STUDIES', 70, bg=YEL, fg=INK, seed=56), 540, 1640, T(17.8) - 0.04, 'stamp', rot=2, out=T(18.15), outdir=(0, 1)); ev('stamp', dz.t + 0.06)
ev('swish', T(18.15))
cards = [
    (cut_sketch('master/m03_research', (930, 960, 1409, 1300), width=380, seed=61), 290, 600, T(18.42), 'STEM CELLS', -4),
    (cut_sketch('master/m03_research', (188, 839, 830, 2032), height=470, seed=62), 790, 640, T(19.46), 'REGENERATIVE\nMEDICINE', 3),
    (cut_sketch('09_plants', (10, 1102, 740, 1708), width=440, seed=63), 290, 1240, T(20.86), 'PLANT-DERIVED\nEXOSOMES', 3),
    (cut_sketch('01_two_geneticists', (640, 936, 900, 2128), height=470, seed=64), 790, 1250, T(22.46), 'CANCER\nRESEARCH', -3),
]
for i, (im, x, y, t, txt, r) in enumerate(cards):
    e = E(im, x, y, t, ('pop', 'drop', 'slide', 'drop')[i], rot=r, frm=(-1, 0)); ev(('pop', 'drop', 'slide', 'drop')[i], t + (0.05 if i == 0 else 0.25))
    l = E(label(txt, 52, bg=(INK, MAG, INK, MAG)[i], seed=70 + i), x, y + im.height / 2 - 10, t + 0.2, 'stamp', rot=-r * 0.6)
    ev('stamp_small', l.t + 0.05)
BURSTS.append((290, 1180, T(21.62))); ev('sparkle', T(21.62))

# ---------------------------------------------------------------- rendering
BLANK = cv2.cvtColor(cv2.imread(SK + '/master_blank.png'), cv2.COLOR_BGR2RGB)
BLANK = cv2.resize(BLANK, (W, H), interpolation=cv2.INTER_AREA).astype(np.float32)
TEX = (paper_tex(W, H, 1) ** 2.2)[..., None]
YY, XX = np.mgrid[0:H, 0:W]
VIG = (1 - 0.10 * (((XX - W / 2) / (W / 2)) ** 2 + ((YY - H / 2) / (H / 2)) ** 2))[..., None].astype(np.float32)
BG = {}


def bg_for(col):
    if col not in BG:
        BG[col] = Image.fromarray(np.clip(TEX * np.array(col, np.float32) * VIG, 0, 255).astype(np.uint8)).convert('RGBA')
    return BG[col]


def scene_at(t):
    cur = SCENES[0]
    for s in SCENES:
        if t >= s[0]: cur = s
    return cur


def jitter(e, k):
    r = np.random.default_rng(e.id * 1000 + k)
    return r.uniform(-1.6, 1.6), r.uniform(-1.6, 1.6), r.uniform(-0.45, 0.45)


TORN = {}


def wipe_sheet(color):
    if color in TORN: return TORN[color]
    w = int(W * 1.7); r = np.random.default_rng(len(TORN) + 99)
    pts = [(r.uniform(0, 34), y) for y in np.linspace(0, H, 40)] + [(w - r.uniform(0, 34), y) for y in np.linspace(H, 0, 40)]
    m = Image.new('L', (w, H), 0); ImageDraw.Draw(m).polygon(pts, fill=255)
    fringe = Image.new('L', (w, H), 0); ImageDraw.Draw(fringe).polygon([(x - 10 if i < 40 else x + 10, y) for i, (x, y) in enumerate(pts)], fill=255)
    rgb = np.zeros((H, w, 3), np.float32) + np.array(color, np.float32); rgb *= paper_tex(w, H, 5)[..., None] ** 1.5
    a = np.asarray(m, np.float32); fr = (np.asarray(fringe, np.float32) - a).clip(0)
    rgb = rgb * (a[..., None] / 255) + np.array((250, 248, 242), np.float32) * (fr[..., None] / 255)
    al = np.clip(a + fr, 0, 255)
    TORN[color] = Image.fromarray(np.dstack([rgb, al]).astype(np.uint8), 'RGBA')
    return TORN[color]


def draw_strokes(fr, t):
    for pts, wd, col, t0, dur, out in STROKES:
        if t < t0 or any(t0 < s0 <= t for s0, _ in SCENES): continue
        dy = 0
        if out is not None and t > out:
            v = (t - out) / 0.4
            if v >= 1: continue
            dy = -2000 * v * v
        u = clamp((t - t0) / dur)
        P = np.array(pts, np.float32)
        seg = np.r_[0, np.cumsum(np.hypot(*np.diff(P, axis=0).T))]
        L = seg[-1] * eout(u)
        q = [tuple(P[0])]
        for i in range(1, len(P)):
            if seg[i] <= L: q.append(tuple(P[i]))
            else:
                f = (L - seg[i - 1]) / max(1e-6, seg[i] - seg[i - 1]); q.append(tuple(P[i - 1] + (P[i] - P[i - 1]) * f)); break
        lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        q = [(x, y + dy) for x, y in q]
        d.line(q, fill=col + (235,), width=wd, joint='curve')
        for x, y in (q[0], q[-1]): d.ellipse((x - wd / 2, y - wd / 2, x + wd / 2, y + wd / 2), fill=col + (235,))
        fr.alpha_composite(lay)


def draw_bursts(fr, t):
    d = ImageDraw.Draw(fr)
    for x0, y0, t0 in BURSTS:
        u = (t - t0) / 0.7
        if not 0 <= u < 1: continue
        r = np.random.default_rng(int(x0))
        for i in range(22):
            a = r.uniform(0, 2 * math.pi); v = r.uniform(180, 420); s = r.uniform(9, 20) * (1 - u)
            x = x0 + math.cos(a) * v * eout(u); y = y0 + math.sin(a) * v * eout(u) + 140 * u * u
            col = MAG if i % 3 else (255, 196, 40)
            d.ellipse((x - s, y - s, x + s, y + s), fill=col + (255,))


def render(t):
    sc = scene_at(t)
    fr = bg_for(sc[1]).copy()
    items = []
    for e in ALL:
        if e.t > t + 0.01: continue
        # elements from an earlier scene disappear at the wipe that ends it
        nxt = [s[0] for s in SCENES if s[0] > e.t]
        if nxt and t >= nxt[0]: continue
        p = e.pose(t)
        if p is None: continue
        items.append((e.z, e.id, e, p))
    items.sort(key=lambda a: (a[0], a[1]))
    k = int(t * FPS) // HOLD
    for _, _, e, (x, y, rot, s, op, lift) in items:
        jx, jy, jr = jitter(e, k)
        im = e.img
        if abs(s - 1) > 0.005: im = im.resize((max(2, int(im.width * s)), max(2, int(im.height * s))), Image.BICUBIC)
        im = im.rotate(rot + jr, resample=Image.BICUBIC, expand=True)
        if op < 1: im.putalpha(im.getchannel('A').point(lambda v: int(v * op)))
        cx, cy = x + jx - im.width / 2, y + jy - im.height / 2
        if e.shadow:
            sh = e.sh
            if abs(s - 1) > 0.005: sh = sh.resize((max(2, int(sh.width * s)), max(2, int(sh.height * s))), Image.BILINEAR)
            sh = sh.rotate(rot + jr, resample=Image.BILINEAR, expand=True)
            if lift > 0.05: sh = sh.filter(ImageFilter.GaussianBlur(6 * lift))
            if op < 1 or lift > 0: sh.putalpha(sh.getchannel('A').point(lambda v: int(v * op * (1 - 0.35 * min(1, lift)))))
            fr.alpha_composite(sh, (int(cx + 7 + 26 * lift), int(cy + 11 + 34 * lift)))
        fr.alpha_composite(im, (int(cx), int(cy)))
    draw_strokes(fr, t); draw_bursts(fr, t)
    for tc, col in WIPES:
        u = (t - (tc - 0.3)) / 0.6
        if 0 <= u < 1:
            sheet = wipe_sheet(col); xl = W - (W + sheet.width) * eio(u)
            sh = Image.new('RGBA', sheet.size, (0, 0, 0, 0)); sh.putalpha(sheet.getchannel('A').filter(ImageFilter.GaussianBlur(14)).point(lambda v: int(v * 0.35)))
            fr.alpha_composite(sh, (int(xl) + 14, 0)) if xl + 14 < W else None
            fr.alpha_composite(sheet, (int(xl), 0)) if xl < W else None
    img = np.asarray(fr.convert('RGB'))
    # camera: slow push inside each scene + stamp shake
    z = 1 + 0.035 * clamp((t - sc[0]) / 6.0)
    sx = sy = 0.0
    for ts in SHAKES:
        v = (t - ts) / 0.18
        if 0 <= v < 1:
            r = np.random.default_rng(int(t * 100)); sx += r.uniform(-9, 9) * (1 - v); sy += r.uniform(-9, 9) * (1 - v)
    M = np.float32([[z, 0, W / 2 * (1 - z) + sx], [0, z, H / 2 * (1 - z) + sy]])
    return cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)


if EVJ:
    json.dump(dict(lead=LEAD, end=END, events=EVENTS), open(EVJ, 'w'), indent=1)
N = int(END * FPS)
only = os.environ.get('FRAMES')
if only:
    for f in map(int, only.split(',')):
        cv2.imwrite(OUT.replace('.mp4', f'_{f:04d}.jpg'), cv2.cvtColor(render(f / FPS), cv2.COLOR_RGB2BGR))
    sys.exit()
p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                      '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', OUT], stdin=subprocess.PIPE)
last = None
for f in range(N):
    if f % HOLD == 0: last = render((f // HOLD) * HOLD / FPS)
    p.stdin.write(np.ascontiguousarray(last).tobytes())
    if f % 90 == 0: print(f, flush=True)
p.stdin.close(); p.wait(); print('done', OUT, round(END, 2))
