# Founders film v3 (2026-11-06). User: "inodaki gibi ... gerçekçi ... önce tam sayfa ... yazılar genel görücez, sonra başa alıp sıfırdan
# anlatmaya başlıcaz ... kamera da hareket edecek".
# Structure: overview of the FINISHED page (camera drifts down the whole page) -> whip back to the top, page blank ->
# written from scratch, camera close and following the pen -> pull back to the full finished page -> end card.
# All writing lives on ONE page, drawn in flat page space and perspective-warped onto the real notebook plate,
# ink multiplied into the paper so the grid and fibre show through.
# Usage: ~/motion-tools/.venv/bin/python render3.py [--info] [--frames a,b] [--out file]
import json, math, os, random, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

ROOT = os.path.dirname(os.path.abspath(__file__))
A = lambda p: os.path.join(ROOT, 'assets', p)
FPS = 30
W, H = 1080, 1920
FONT_HAND = os.path.expanduser('~/Library/Fonts/Caveat-Bold.ttf')
FONT_PEN = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fonts', 'NothingYouCouldDo.ttf')
FONT_GROT = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Medium.otf')
INK = (28, 32, 48)
VIOLET = (150, 30, 175)
YELLOW = (255, 222, 60)
random.seed(7)

# ---------------- plate + page geometry ----------------
PLATE = Image.open(A('page.png')).convert('RGB')            # 1536 x 2752
PWp, PHp = PLATE.size
# grid corners on the plate (measured): TL, TR, BR, BL
QUAD = [(314, 597), (1268, 696), (1126, 2079), (155, 2001)]
FW, FH = 960, 1420                                          # flat grid size
OX, OY = 60, 150                                            # canvas margin so header/bottom fit
CW, CH = FW + 2 * OX, FH + OY + 120


def homography(src, dst):
    A_ = []
    for (x, y), (u, v) in zip(src, dst):
        A_.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); A_.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    b = np.array([c for p in dst for c in p], float)
    h = np.linalg.solve(np.array(A_, float), b)
    return np.append(h, 1).reshape(3, 3)


FLAT_PTS = [(OX, OY), (OX + FW, OY), (OX + FW, OY + FH), (OX, OY + FH)]
H_f2p = homography(FLAT_PTS, QUAD)          # canvas px -> plate px
H_p2f = np.linalg.inv(H_f2p)
COEF = tuple((H_p2f / H_p2f[2, 2]).flatten()[:8])


def f2p(x, y):                               # flat layout coords -> plate px
    v = H_f2p @ np.array([x + OX, y + OY, 1.0])
    return v[0] / v[2], v[1] / v[2]


def warp(layer):                             # RGBA canvas -> RGBA plate-sized
    return layer.transform((PWp, PHp), Image.PERSPECTIVE, COEF, resample=Image.BICUBIC)


# ---------------- VO timeline ----------------
WORDS = json.load(open(os.path.join(ROOT, 'words.json')))
DUR = {k: max(w['e'] for w in v['words']) + 0.25 for k, v in WORDS.items()}
ORDER = ['01_P', '02_M', '03_P', '04_M', '05_P', '06_M', '07_P', '08_M', '09_P', '10_M', '11_P']
GAP = {'04_M': 0.55, '05_P': 0.4, '06_M': 0.7, '11_P': 0.7}
OVER_END = 3.3            # overview of the finished page
WHIP_END = 3.95           # whip back to the top, page blank
HEADER_T = 4.0
t = 4.75
LINE_T = {}
for k in ORDER:
    if k + '.mp3' not in WORDS:
        continue
    t += GAP.get(k, 0.2)
    LINE_T[k] = t
    t += DUR[k + '.mp3']
END_VO = t
TOTAL = END_VO + 1.9


def wt(line, word, nth=0, edge='s'):
    f = line + '.mp3'
    hits = [w for w in WORDS[f]['words'] if word.lower() in w['w'].lower()]
    if not hits:
        return LINE_T[line]
    return LINE_T[line] + hits[min(nth, len(hits) - 1)][edge]


# ---------------- elements (flat page coords) ----------------
def font(size, f=FONT_HAND):
    return ImageFont.truetype(f, size)


_rng = random.Random(11)


def hand_mask(text, size):
    # real-handwriting look: pen font, every letter with its own baseline, slant, size and spacing; pressure varies
    size = int(size * 1.06)
    pad = int(size * 0.6)
    tw = int(size * 0.62 * len(text)) + 2 * pad
    th = int(size * 1.7)
    img = Image.new('L', (tw, th), 0)
    x = pad // 2
    base = int(size * 0.25)
    drift = 0.0
    for ch in text:
        if ch == ' ':
            x += int(size * _rng.uniform(0.26, 0.36)); continue
        sc = _rng.uniform(0.93, 1.07)
        fnt = ImageFont.truetype(FONT_PEN, max(8, int(size * sc)))
        bb = fnt.getbbox(ch)
        gw, gh = bb[2] - bb[0] + 8, bb[3] + 8
        g = Image.new('L', (gw + 10, gh + 10), 0)
        ImageDraw.Draw(g).text((5 - bb[0], 5), ch, font=fnt, fill=255)
        g = g.filter(ImageFilter.MaxFilter(3))                       # fine-liner weight
        g = g.rotate(_rng.uniform(-4, 4), resample=Image.BICUBIC, expand=True)
        drift += _rng.uniform(-0.6, 0.6)
        drift = max(-size * 0.05, min(size * 0.05, drift))
        img.paste(255, (x, int(base + drift + _rng.uniform(-size * 0.025, size * 0.025))), g)
        x += int((bb[2] - bb[0]) * _rng.uniform(0.97, 1.02) + size * 0.035)
    img = img.crop((0, 0, min(tw, x + pad // 2), th))
    nz = Image.effect_noise(img.size, 30).filter(ImageFilter.GaussianBlur(1.2))
    img = ImageChops.multiply(img, nz.point(lambda v: 175 + v * 80 // 255))   # pressure / ink density
    return img.filter(ImageFilter.GaussianBlur(0.5))


class Note:
    kind = 'ink'

    def __init__(self, x, y, text, size, t0, cps=13.0, color=INK, rot=None, hl=None, strike=None):
        self.x, self.y, self.text, self.size, self.color, self.t0 = x, y, text, size, color, t0
        self.dur = max(0.35, len(text) / cps)
        self.rot = random.uniform(-1.4, 1.0) if rot is None else rot
        self.mask0 = hand_mask(text, size)
        img = self.mask0
        m = img.rotate(self.rot, resample=Image.BICUBIC, expand=True)
        bb = m.point(lambda v: 255 if v > 40 else 0).getbbox() or (0, 0, m.width, m.height)
        self.mask = m.crop((max(0, bb[0] - 3), max(0, bb[1] - 3), bb[2] + 3, bb[3] + 3))
        self.w, self.h = self.mask.size
        self.hl = hl
        self.hl_t = self.t0 + self.dur + 0.05
        self.strike = strike
        self.sfx = ('pen', self.t0, self.dur)
        if hl:
            w, h = self.w + 26, int(self.h * 0.58)
            m = Image.new('L', (w, h), 0)
            d = ImageDraw.Draw(m)
            top = [(x, 4 + random.uniform(-3, 3)) for x in range(0, w + 1, 12)]
            bot = [(x, h - 4 + random.uniform(-3, 3)) for x in range(w, -1, -12)]
            d.polygon(top + bot, fill=150)
            d.ellipse((-8, 0, 18, h), fill=190); d.ellipse((w - 18, 0, w + 8, h), fill=190)
            self.hlmask = m.filter(ImageFilter.GaussianBlur(1.2)).rotate(self.rot, resample=Image.BICUBIC, expand=True)

    def end(self):
        e = self.t0 + self.dur
        if self.hl: e = max(e, self.hl_t + 0.4)
        if self.strike is not None: e = max(e, self.strike + 0.6)
        return e

    def focus(self):
        return self.x + self.w / 2, self.y + self.h / 2

    def draw(self, ink, t):           # ink: RGBA canvas (premultiplied-ish via alpha)
        if t < self.t0:
            return
        X, Y = int(self.x + OX), int(self.y + OY)
        if self.hl and t >= self.hl_t:
            p = min(1.0, (t - self.hl_t) / 0.35)
            hm = self.hlmask
            cut = hm.crop((0, 0, max(1, int(hm.width * p)), hm.height))
            lay = Image.new('RGBA', cut.size, self.hl + (0,)); lay.putalpha(cut)
            ink.alpha_composite(lay, (X - 13, Y + int(self.h * 0.42)))
        p = min(1.0, (t - self.t0) / self.dur)
        cw = int(self.w * p)
        if cw < 1:
            return
        m = self.mask.copy()
        if p < 1:
            edge = Image.new('L', (self.w, self.h), 0)
            ImageDraw.Draw(edge).rectangle((0, 0, cw, self.h), fill=255)
            g = Image.linear_gradient('L').rotate(90).resize((14, self.h))
            edge.paste(ImageChops.invert(g), (max(0, cw - 14), 0))
            m = ImageChops.multiply(m, edge)
        lay = Image.new('RGBA', m.size, self.color + (0,)); lay.putalpha(m)
        ink.alpha_composite(lay, (X, Y))
        if self.strike is not None and t >= self.strike:
            d = ImageDraw.Draw(ink)
            y0 = Y + int(self.h * 0.58)
            p2 = min(1.0, (t - self.strike) / 0.28)
            pts = [(xx, y0 + math.sin(xx * 0.05) * 2.5 - (xx - X) * 0.02) for xx in range(X, max(X + 2, X + int((self.w - 6) * p2)), 6)]
            if len(pts) > 1: d.line(pts, fill=INK + (225,), width=max(2, self.size // 20), joint='curve')
            if False:
                p3 = min(1.0, (t - self.strike - 0.32) / 0.22)
                pts = [(xx, y0 - 9 + math.sin(xx * 0.07 + 1) * 2.5) for xx in range(X, max(X + 2, X + int((self.w - 6) * p3)), 6)]
                if len(pts) > 1: d.line(pts, fill=INK + (225,), width=max(3, self.size // 13), joint='curve')


class Lines:
    kind = 'ink'

    def __init__(self, strokes, t0, dur, width=4):
        self.strokes, self.t0, self.dur, self.width = strokes, t0, dur, width
        self.total = sum(sum(math.dist(s[i], s[i + 1]) for i in range(len(s) - 1)) for s in strokes)
        self.sfx = ('pen', t0, dur)

    def end(self):
        return self.t0 + self.dur

    def focus(self):
        xs = [p[0] for s in self.strokes for p in s]; ys = [p[1] for s in self.strokes for p in s]
        return sum(xs) / len(xs), sum(ys) / len(ys)

    def draw(self, ink, t):
        if t < self.t0:
            return
        L = self.total * min(1.0, (t - self.t0) / self.dur)
        d = ImageDraw.Draw(ink)
        for s in self.strokes:
            if L <= 0: break
            pts = [(s[0][0] + OX, s[0][1] + OY)]
            for i in range(len(s) - 1):
                seg = math.dist(s[i], s[i + 1])
                if L >= seg:
                    pts.append((s[i + 1][0] + OX, s[i + 1][1] + OY)); L -= seg
                else:
                    f = L / seg
                    pts.append((s[i][0] + (s[i + 1][0] - s[i][0]) * f + OX, s[i][1] + (s[i + 1][1] - s[i][1]) * f + OY)); L = 0
                    break
            if len(pts) > 1:
                d.line(pts, fill=INK + (235,), width=self.width, joint='curve')


class Print:
    kind = 'print'

    def __init__(self, path, x, y, w, t0, rot=3.0):
        self.x, self.y, self.t0, self.dur = x, y, t0, 0.3
        im = Image.open(path).convert('RGB')
        hh = int(im.height * w / im.width)
        im = im.resize((w, hh), Image.LANCZOS)
        b = 11
        card = Image.new('RGB', (w + 2 * b, hh + 2 * b), (246, 245, 239)); card.paste(im, (b, b))
        gl = Image.linear_gradient('L').rotate(35, expand=True).resize(card.size).point(lambda v: max(0, v - 200) // 4)
        card = Image.composite(Image.new('RGB', card.size, (255, 255, 255)), card, gl)
        cw, ch = card.size
        tape = Image.new('RGBA', (100, 32), (232, 222, 196, 165))
        full = Image.new('RGBA', (cw + 60, ch + 60), (0, 0, 0, 0))
        full.paste(card, (30, 30))
        full.alpha_composite(tape.rotate(-28, expand=True), (0, 6))
        full.alpha_composite(tape.rotate(30, expand=True), (cw - 36, 4))
        self.img = full.rotate(rot, resample=Image.BICUBIC, expand=True)
        a = self.img.split()[3]
        self.shadow = a.filter(ImageFilter.GaussianBlur(9)).point(lambda v: v * 60 // 255)
        self.sfx = ('tape', t0, 0.3)

    def end(self):
        return self.t0 + self.dur

    def focus(self):
        return self.x + self.img.width / 2, self.y + self.img.height / 2

    def draw(self, layer, t):
        if t < self.t0:
            return
        p = min(1.0, (t - self.t0) / 0.3)
        e = 1 - (1 - p) ** 3
        X, Y = self.x + OX, self.y + OY
        sh = Image.new('RGBA', self.shadow.size, (55, 50, 45, 0)); sh.putalpha(Image.eval(self.shadow, lambda v: int(v * e)))
        layer.alpha_composite(sh, (X + 6, Y + 10))
        im = self.img.copy(); im.putalpha(Image.eval(self.img.split()[3], lambda v: int(v * e)))
        layer.alpha_composite(im, (X, Y))


# ---------------- layout: ONE page ----------------
els = []
def N(x, y, *a, **k):
    n = Note(x, y, *a, **k); els.append(n); return n


def right_of(n, gap=34):
    return n.x + n.w + gap


def below(n, gap=10):
    return n.y + n.h + gap


N(0, -112, 'PROJECT  SickScience', 30, HEADER_T, cps=26, rot=0)
N(760, -112, 'PAGE 01', 30, HEADER_T + 0.45, cps=26, rot=0)
a1 = N(10, 0, "That's sick!", 92, wt('01_P', "That's"), cps=9)
a2 = N(18, below(a1, 6), '— a beauty exec, about our data', 30, wt('01_P', 'beauty') - 0.1, cps=18)
els.append(Print(A('founders.jpg'), 668, -96, 186, wt('02_M', 'geneticists'), rot=4))
b1 = N(10, below(a2, 22), 'two geneticists', 44, wt('02_M', 'geneticists') - 0.2, cps=16)
b2 = N(14, below(b1, 10), '2009', 70, wt('02_M', '2009') - 0.1, cps=6, hl=YELLOW)
TLY = below(b2, 34)
tl_t = wt('02_M', 'chemistry')
els.append(Lines([[(10, TLY), (900, TLY - 8)]], tl_t, 0.7, width=4))
for i, yr in enumerate(['2009', '2013', '2018', '2020', '2024', '2025']):
    x = 14 + i * 172
    els.append(Lines([[(x + 24, TLY - 14 - i * 1.4), (x + 25, TLY + 10 - i * 1.4)]], tl_t + 0.5 + i * 0.12, 0.1, width=4))
    N(x, TLY + 16 - i * 1.4, yr, 28, tl_t + 0.55 + i * 0.12, cps=20, rot=0)
c1 = N(10, TLY + 80, '14 YEARS', 64, wt('02_M', 'years') - 0.35, cps=8, hl=YELLOW)
c2 = N(520, TLY + 72, 'patents + papers', 34, wt('03_P', 'Patents'), cps=14)
c3 = N(528, below(c2, 8), '20-30', 56, wt('03_P', 'papers') + 0.1, cps=6, hl=YELLOW)
c4 = N(532, below(c3, 6), 'peer-reviewed', 28, wt('03_P', 'PhDs'), cps=16)
d1 = N(12, below(c1, 22), 'for mom', 32, wt('04_M', 'mom'), cps=9)
d2 = N(12, below(d1, 6), 'still preclinical', 32, wt('04_M', 'preclinical') - 0.3, cps=11)
EY = max(below(d2, 44), below(c4, 44))
e1 = N(10, EY, 'in the lab', 54, wt('05_P', 'science') - 0.6, cps=11, strike=wt('05_P', 'lab') + 0.1)
e2 = N(right_of(e1, 90), EY - 30, 'at home', 56, wt('05_P', 'homes') - 0.35, cps=8, hl=YELLOW)
ax = right_of(e1, 14)
els.append(Lines([[(ax, EY + 34), (ax + 56, EY + 12), (ax + 40, EY - 6)]], wt('05_P', 'homes') - 0.45, 0.25, width=4))
f1 = N(10, below(e1, 44), 'exosomes =', 42, wt('06_M', 'Exosomes'), cps=14)
f2 = N(10, below(f1, 6), 'tiny messengers', 54, wt('06_M', 'tiny'), cps=12)
dx, dy = 760, f1.y + 20
drone = [[(dx - 60, dy), (dx + 60, dy)], [(dx - 70, dy - 18), (dx - 50, dy - 18)], [(dx + 50, dy - 18), (dx + 70, dy - 18)],
         [(dx - 60, dy), (dx - 60, dy - 18)], [(dx + 60, dy), (dx + 60, dy - 18)],
         [(dx - 25, dy), (dx - 25, dy + 22), (dx + 25, dy + 22), (dx + 25, dy), (dx - 25, dy)], [(dx, dy + 22), (dx, dy + 44)],
         [(dx - 30, dy + 44), (dx + 30, dy + 44), (dx + 30, dy + 84), (dx - 30, dy + 84), (dx - 30, dy + 44)],
         [(dx - 30, dy + 44), (dx, dy + 66), (dx + 30, dy + 44)]]
els.append(Lines(drone, wt('06_M', 'delivery') - 0.3, 1.1, width=4))
f0 = wt('07_P', 'plants')
GY = below(f2, 40)
caps = []
for i, (k, kw) in enumerate([('pineapple', 'Pineapple'), ('garlic', 'garlic'), ('wheat', 'wheat'), ('radish', 'radish')]):
    x = 0 + i * 236
    tt = wt('07_P', kw) - 0.15
    pr = Print(A(f'fig_{k}.jpg'), x, GY, 156, min(tt, f0 + 0.3 + i * 0.35), rot=random.uniform(-3, 3))
    els.append(pr)
    cy_ = GY + pr.img.height - 18
    g1 = N(x + 34, cy_, f'FIG. 0{i + 1}', 24, tt + 0.05, cps=18, rot=0)
    caps.append(N(x + 34, below(g1, 2), k, 24, tt + 0.3, cps=18, rot=0))
HY = max(below(c, 26) for c in caps)
h1 = N(10, HY, 'THOUSANDS', 60, wt('07_P', 'Thousands') - 0.1, cps=9, hl=YELLOW)
h2 = N(right_of(h1, 22), HY + 16, 'plant library', 30, wt('07_P', 'library') - 0.3, cps=14)
i1 = N(10, below(h1, 14), 'NX35', 70, wt('08_M', 'NX35'), cps=6, hl=YELLOW)
i2 = N(right_of(i1, 26), i1.y + 20, 'no cold chain', 34, wt('08_M', 'cold') - 0.2, cps=13)
j1 = N(10, below(i1, 18), 'scientist?', 48, wt('09_P', 'scientist') - 0.3, cps=10, strike=wt('09_P', 'marketers') - 0.25)
j2 = N(right_of(j1, 40), j1.y, 'marketer.', 48, wt('09_P', 'marketers'), cps=10)
KX = max(right_of(h2, 30), right_of(i2, 30), 600)
k1 = N(KX, HY + 4, "No, that's", 38, wt('10_M', 'No'), cps=12)
k1b = N(KX, below(k1, 4), 'science.', 38, wt('10_M', 'science') - 0.2, cps=12)
l1 = N(KX - 6, below(k1b, 14), 'Sick', 70, wt('11_P', 'Sick') - 0.05, cps=9, rot=-1)
l2 = N(KX - 6, below(l1, 4), 'Science', 70, wt('11_P', 'science') - 0.05, cps=11, color=VIOLET, rot=-1)
LAST_WRITE = max(e.end() for e in els)
PULL0 = LAST_WRITE + 0.1
PULL1 = PULL0 + 1.0
END_T = PULL1 + 0.2                   # end card starts

# ---------------- page state with caching ----------------
class State:
    def __init__(self):
        self.ink = Image.new('RGBA', (CW, CH), (0, 0, 0, 0))
        self.prt = Image.new('RGBA', (CW, CH), (0, 0, 0, 0))
        self.baked = set()


ST = State()


def layers_at(t, final=False):
    if final:
        ink = Image.new('RGBA', (CW, CH), (0, 0, 0, 0)); prt = Image.new('RGBA', (CW, CH), (0, 0, 0, 0))
        for e in els:
            e.draw(prt if e.kind == 'print' else ink, 1e9)
        return ink, prt
    for i, e in enumerate(els):
        if i not in ST.baked and t >= e.end() + 0.02:
            e.draw(ST.prt if e.kind == 'print' else ST.ink, 1e9); ST.baked.add(i)
    ink, prt = ST.ink.copy(), ST.prt.copy()
    for i, e in enumerate(els):
        if i not in ST.baked and t >= e.t0:
            e.draw(prt if e.kind == 'print' else ink, t)
    return ink, prt


PLATE_A = np.asarray(PLATE).astype(np.float32)


def compose(ink, prt):
    wi = np.asarray(warp(ink)).astype(np.float32)
    wp = np.asarray(warp(prt)).astype(np.float32)
    a = wi[..., 3:4] / 255.0
    out = PLATE_A * (1 - a + a * wi[..., :3] / 255.0)          # ink multiplies into the paper
    pa = wp[..., 3:4] / 255.0
    out = out * (1 - pa) + wp[..., :3] * pa                      # prints sit on top
    return out


FINAL = None
_cache = {'key': None, 'img': None}


def page_img(t, final=False):
    global FINAL
    if final:
        if FINAL is None:
            FINAL = compose(*layers_at(0, final=True))
        return FINAL
    active = tuple(i for i, e in enumerate(els) if e.t0 <= t < e.end() + 0.02)
    nb = len(ST.baked)
    key = (active, nb) if not active else None
    if key is not None and _cache['key'] == key:
        return _cache['img']
    img = compose(*layers_at(t))
    _cache['key'], _cache['img'] = key, img
    return img


# ---------------- camera ----------------
def focus_at(t):
    f = None
    for e in els:
        if e.t0 <= t:
            f = e.focus()
    if f is None:
        f = (300, -60)
    return f2p(*f)


_cam = {'x': None, 'y': None}


def smooth_focus(t):
    fx, fy = focus_at(t)
    if _cam['x'] is None:
        _cam['x'], _cam['y'] = fx, fy
    _cam['x'] += (fx - _cam['x']) * 0.05
    _cam['y'] += (fy - _cam['y']) * 0.06
    return _cam['x'], _cam['y']


Z_CLOSE = 1.36


def crop(img_arr, cx, cy, z, t, blur=0):
    vw, vh = PWp / z, PHp / z
    cx = min(max(cx, vw / 2), PWp - vw / 2); cy = min(max(cy, vh / 2), PHp - vh / 2)
    cx += math.sin(t * 0.37) * 5 + math.sin(t * 0.91) * 2
    cy += math.cos(t * 0.29) * 5
    x0, y0 = cx - vw / 2, cy - vh / 2
    im = Image.fromarray(np.clip(img_arr, 0, 255).astype(np.uint8))
    im = im.transform((W, H), Image.EXTENT, (x0, y0, x0 + vw, y0 + vh), resample=Image.BICUBIC)
    if blur:
        im = im.filter(ImageFilter.GaussianBlur(blur))
    return im


def ease(a):
    a = min(1.0, max(0.0, a)); return a * a * (3 - 2 * a)


GROT = ImageFont.truetype(FONT_GROT, 56)
endcard = Image.open(A('endcard.png')).convert('RGB').resize((W, H), Image.LANCZOS)
START_CAM = f2p(300, 10)
PAGE_CX = f2p(470, 700)[0] - 30


def frame(t):
    if t < OVER_END:                                   # 1) overview of the finished page
        a = t / OVER_END
        z = 1.0 + 0.10 * ease(a)
        cy = PHp / 2 - 120 + 300 * ease(a)
        im = crop(page_img(t, final=True), PWp / 2, cy, z, t)
        d = ImageDraw.Draw(im)
        op = min(1.0, t / 0.25) * (1 - max(0.0, (t - (OVER_END - 0.35)) / 0.35))
        col = tuple(int(255 - (255 - c) * op) for c in (22, 22, 26))
        lay = Image.new('L', (W, H), 0); dl = ImageDraw.Draw(lay)
        for i, line in enumerate(["THAT'S SICK.", "HERE'S HOW IT STARTED."]):
            tw = dl.textlength(line, font=GROT)
            dl.text(((W - tw) / 2, 112 + i * 68), line, font=GROT, fill=255)
        im.paste((22, 22, 26), (0, 0), Image.eval(lay, lambda v: int(v * op)))
        return im
    if t < WHIP_END:                                   # 2) whip back to the top, ink gone
        a = ease((t - OVER_END) / (WHIP_END - OVER_END))
        z = 1.10 + (Z_CLOSE - 1.10) * a
        cy = (PHp / 2 + 180) + (START_CAM[1] + 260 - (PHp / 2 + 180)) * a
        cx = PWp / 2 + (PAGE_CX - PWp / 2) * a
        src = page_img(t, final=True) if a < 0.5 else PLATE_A
        blur = 14 * math.sin(math.pi * a)
        _cam['x'], _cam['y'] = START_CAM[0], START_CAM[1]
        return crop(src, cx, cy, z, t, blur=blur)
    if t < PULL0:                                      # 3) writing from scratch, camera follows
        fx, fy = smooth_focus(t)
        return crop(page_img(t), PAGE_CX, fy + 260, Z_CLOSE, t)
    if t < END_T:                                      # 4) pull back to the whole finished page
        a = ease((t - PULL0) / (PULL1 - PULL0))
        fx, fy = smooth_focus(t)
        z = Z_CLOSE + (1.0 - Z_CLOSE) * a
        cx = PAGE_CX + (PWp / 2 - PAGE_CX) * a
        cy = (fy + 260) + (PHp / 2 - (fy + 260)) * a
        return crop(page_img(t), cx, cy, z, t)
    a = min(1.0, (t - END_T) / 0.7)                    # 5) end card
    pg = crop(page_img(t), PWp / 2, PHp / 2, 1.0, t)
    s = 1.0 + 0.04 * (t - END_T) / max(0.1, TOTAL - END_T)
    ec = endcard.resize((int(W * s), int(H * s)), Image.BICUBIC)
    ecf = ec.crop(((ec.width - W) // 2, (ec.height - H) // 2, (ec.width - W) // 2 + W, (ec.height - H) // 2 + H))
    im = Image.blend(pg, ecf, a)
    if t > END_T + 0.4:
        hf = ImageFont.truetype(FONT_HAND, 80)
        d = ImageDraw.Draw(im)
        for li, (line, ly) in enumerate((('Science,', 226), ('but never', 304), ('boring.', 382))):
            tw = d.textlength(line, font=hf)
            p = min(1.0, max(0.0, (t - END_T - 0.4 - li * 0.6) / 0.9))
            if p <= 0: continue
            lay = Image.new('L', (int(tw) + 20, 130), 0)
            ImageDraw.Draw(lay).text((10, 0), line, font=hf, fill=255)
            m = Image.new('L', lay.size, 0); m.paste(lay.crop((0, 0, max(1, int((tw + 20) * p)), lay.height)), (0, 0))
            im.paste((24, 28, 40), (78, ly), m)
    return im


def finish(im, t):
    a = np.asarray(im).astype(np.int16)
    rng = np.random.default_rng(int(t * 1000))
    a = np.clip(a + rng.normal(0, 3.0, (H // 2, W // 2, 1)).repeat(2, 0).repeat(2, 1), 0, 255)
    yy, xx = np.mgrid[0:H, 0:W]
    r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    a = a * (1 - 0.10 * np.clip(r - 0.55, 0, 1) ** 1.5)[..., None]
    return a.astype(np.uint8)


def sfx_events():
    ev = [e.sfx for e in els]
    ev.append(('whoosh', OVER_END, 0.5))
    return ev


if __name__ == '__main__':
    args = sys.argv[1:]
    info = {'LINE_T': LINE_T, 'TOTAL': TOTAL, 'END_T': END_T, 'OVER_END': OVER_END, 'PULL0': PULL0, 'sfx': sfx_events()}
    if '--info' in args:
        json.dump(info, open(os.path.join(ROOT, 'timeline3.json'), 'w'), indent=1)
        print({k: v for k, v in info.items() if k != 'sfx'})
        sys.exit()
    if '--frames' in args:
        ts = sorted(float(x) for x in args[args.index('--frames') + 1].split(','))
        # walk the timeline so caches/camera are right
        k = 0
        tt = 0.0
        while k < len(ts):
            im = frame(tt)
            if tt >= ts[k] - 1e-6:
                Image.fromarray(finish(im, tt)).save(os.path.join(ROOT, f'g_{ts[k]:05.2f}.jpg'), quality=88); k += 1
            tt += 1 / FPS
        sys.exit()
    out = args[args.index('--out') + 1] if '--out' in args else os.path.join(ROOT, 'video3_noaudio.mp4')
    nfr = int(TOTAL * FPS)
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    for i in range(nfr):
        tt = i / FPS
        p.stdin.write(finish(frame(tt), tt).tobytes())
        if i % 150 == 0:
            print(f'{i}/{nfr}', flush=True)
    p.stdin.close(); p.wait()
    print('done', out)
