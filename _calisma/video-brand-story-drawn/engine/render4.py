# Founders film v4 (2026-11-06): the notebook.
# User: a notebook with the SickScience logo on the cover opens, pages flip, then we stay on a wide two-page spread;
# a real hand writes with a marker from the top left, synced to the VO, photos taped in.
# Pipeline: Veo flip clip (first frame = cover with real logo, last frame = blank spread plate) -> spread plate,
# per-page homography, ink warped straight to output resolution and multiplied into the paper, prints on top,
# a cut-out hand whose pen tip follows the writing front (lift, shadow, travel between notes) -> pull back -> end card.
# Usage: ~/motion-tools/.venv/bin/python render4.py [--info] [--frames a,b] [--out file]
import json, math, os, random, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

ROOT = os.path.dirname(os.path.abspath(__file__))
A = lambda p: os.path.join(ROOT, 'assets', p)
V = lambda p: os.path.join(ROOT, 'v4', p)
FPS = 30
W, H = 1080, 1920
FONT_HAND = os.path.expanduser('~/Library/Fonts/Caveat-Bold.ttf')
FONT_PEN = os.path.join(ROOT, 'fonts', 'NothingYouCouldDo.ttf')
INK = (24, 28, 44)
VIOLET = (150, 30, 175)
YELLOW = (255, 222, 60)
random.seed(7)

GEOM = json.load(open(V('geom.json')))
PLATE = Image.open(V('spread.png')).convert('RGB')
PWp, PHp = PLATE.size
PLATE_A = np.asarray(PLATE)
FW, FH = 1000, 1414                      # flat page canvas (A5 ratio)
CM = GEOM.get('page_w_px', 700) / 14.8   # plate px per cm


def homography(src, dst):
    A_ = []
    for (x, y), (u, v) in zip(src, dst):
        A_.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); A_.append([0, 0, 0, x, y, 1, -v * x, -v * y])
    h = np.linalg.solve(np.array(A_, float), np.array([c for p in dst for c in p], float))
    return np.append(h, 1).reshape(3, 3)


FLAT = [(0, 0), (FW, 0), (FW, FH), (0, FH)]
HP = [homography(FLAT, GEOM['quads'][p]) for p in (0, 1)]   # flat page -> plate


def f2p(p, x, y):
    v = HP[p] @ np.array([x, y, 1.0]); return v[0] / v[2], v[1] / v[2]


# ---------------- VO timeline ----------------
WORDS = json.load(open(os.path.join(ROOT, 'words.json')))
DUR = {k: max(w['e'] for w in v['words']) + 0.25 for k, v in WORDS.items()}
ORDER = ['01_P', '02_M', '03_P', '04_M', '05_P', '06_M', '07_P', '08_M', '09_P', '10_M', '11_P']
GAP = {'04_M': 0.55, '05_P': 0.4, '06_M': 1.3, '11_P': 0.7}     # 06: camera crosses to the right page
FLIP_DUR = GEOM.get('flip_dur', 7.0)      # Veo opening (cover -> flips -> blank spread)
WIDE_END = FLIP_DUR + 0.7                 # hold on the empty spread
PUSH_END = WIDE_END + 0.9                 # push in to the top left, hand enters
t = PUSH_END + 0.15
LINE_T = {}
for k in ORDER:
    t += GAP.get(k, 0.2)
    LINE_T[k] = t
    t += DUR[k + '.mp3']
END_VO = t
TOTAL = END_VO + 1.9


def wt(line, word, nth=0, edge='s'):
    hits = [w for w in WORDS[line + '.mp3']['words'] if word.lower() in w['w'].lower()]
    if not hits:
        return LINE_T[line]
    return LINE_T[line] + hits[min(nth, len(hits) - 1)][edge]


# ---------------- handwriting ----------------
_rng = random.Random(11)


def hand_mask(text, size):
    size = int(size * 1.06)
    pad = int(size * 0.6)
    tw = int(size * 0.95 * len(text)) + 2 * pad
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
        asc = fnt.getmetrics()[0]
        g = Image.new('L', (int(size * 1.6), int(size * 1.8)), 0)
        ImageDraw.Draw(g).text((int(size * 0.3), int(size * 0.2)), ch, font=fnt, fill=255)
        g = g.filter(ImageFilter.MaxFilter(3))
        g = g.rotate(_rng.uniform(-4, 4), resample=Image.BICUBIC, center=(int(size * 0.3), int(size * 0.2) + asc))
        bb = g.getbbox()
        if not bb:
            x += int(size * 0.3); continue
        drift += _rng.uniform(-0.6, 0.6)
        drift = max(-size * 0.05, min(size * 0.05, drift))
        gy = int(base + drift + _rng.uniform(-size * 0.025, size * 0.025)) - int(size * 0.2)
        arr = np.asarray(g)[bb[1] + (bb[3] - bb[1]) * 3 // 10: bb[1] + (bb[3] - bb[1]) * 7 // 10, bb[0]:bb[2]]
        cols = np.where(arr.max(0) > 60)[0]
        lft = bb[0] + (int(cols[0]) if len(cols) else 0)
        gx = x - lft
        img.paste(255, (max(0, gx), gy), g)
        x += int((bb[2] - lft) * _rng.uniform(0.98, 1.02) + size * (0.07 if ch.isupper() else 0.045))
    img = img.crop((0, 0, min(tw, x + pad // 2), th))
    nz = Image.effect_noise(img.size, 30).filter(ImageFilter.GaussianBlur(1.2))
    img = ImageChops.multiply(img, nz.point(lambda v: 175 + v * 80 // 255))
    return img.filter(ImageFilter.GaussianBlur(0.5))


class Note:
    kind = 'ink'

    def __init__(self, p, x, y, text, size, t0, cps=13.0, color=INK, rot=None, hl=None, strike=None):
        self.p, self.x, self.y, self.text, self.size, self.color, self.t0 = p, x, y, text, size, color, t0
        self.dur = max(0.35, len(text) / cps)
        self.rot = random.uniform(-1.4, 1.0) if rot is None else rot
        m = hand_mask(text, size).rotate(self.rot, resample=Image.BICUBIC, expand=True)
        bb = m.point(lambda v: 255 if v > 40 else 0).getbbox() or (0, 0, m.width, m.height)
        self.mask = m.crop((max(0, bb[0] - 3), max(0, bb[1] - 3), bb[2] + 3, bb[3] + 3))
        self.w, self.h = self.mask.size
        self.hl, self.hl_t, self.strike = hl, self.t0 + self.dur + 0.05, strike
        self.sfx = ('pen', self.t0, self.dur)
        if hl:
            w, h = self.w + 26, int(self.h * 0.58)
            mm = Image.new('L', (w, h), 0)
            d = ImageDraw.Draw(mm)
            top = [(x, 4 + random.uniform(-3, 3)) for x in range(0, w + 1, 12)]
            bot = [(x, h - 4 + random.uniform(-3, 3)) for x in range(w, -1, -12)]
            d.polygon(top + bot, fill=150)
            d.ellipse((-8, 0, 18, h), fill=190); d.ellipse((w - 18, 0, w + 8, h), fill=190)
            self.hlmask = mm.filter(ImageFilter.GaussianBlur(1.2)).rotate(self.rot, resample=Image.BICUBIC, expand=True)

    def end(self):
        e = self.t0 + self.dur
        if self.hl: e = max(e, self.hl_t + 0.4)
        if self.strike is not None: e = max(e, self.strike + 0.35)
        return e

    def pen_intervals(self):        # (t0, t1, pos(t) -> flat xy)
        out = []
        X, Y, w, h = self.x, self.y, self.w, self.h
        def write(t, t0=self.t0, d=self.dur):
            p = min(1.0, max(0.0, (t - t0) / d))
            return (X + w * p + math.sin(t * 19) * 3, Y + h * 0.58 + math.sin(t * 37) * h * 0.16)
        out.append((self.t0, self.t0 + self.dur, write))
        if self.hl:
            out.append((self.hl_t, self.hl_t + 0.35, lambda t: (X - 13 + (w + 26) * min(1, (t - self.hl_t) / 0.35), Y + h * 0.7)))
        if self.strike is not None:
            s = self.strike
            out.append((s, s + 0.28, lambda t: (X + (w - 6) * min(1, (t - s) / 0.28), Y + h * 0.58)))
        return out

    def draw(self, ink, t):
        if t < self.t0:
            return
        X, Y = int(self.x), int(self.y)
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


class Lines:
    kind = 'ink'

    def __init__(self, p, strokes, t0, dur, width=4):
        self.p, self.strokes, self.t0, self.dur, self.width = p, strokes, t0, dur, width
        self.total = sum(sum(math.dist(s[i], s[i + 1]) for i in range(len(s) - 1)) for s in strokes)
        self.sfx = ('pen', t0, dur)

    def end(self):
        return self.t0 + self.dur

    def _walk(self, L):
        pts_all, last = [], self.strokes[0][0]
        for s in self.strokes:
            if L <= 0: break
            pts = [s[0]]
            for i in range(len(s) - 1):
                seg = math.dist(s[i], s[i + 1])
                if L >= seg:
                    pts.append(s[i + 1]); L -= seg
                else:
                    f = L / seg
                    pts.append((s[i][0] + (s[i + 1][0] - s[i][0]) * f, s[i][1] + (s[i + 1][1] - s[i][1]) * f)); L = 0
                    break
            pts_all.append(pts); last = pts[-1]
        return pts_all, last

    def pen_intervals(self):
        return [(self.t0, self.t0 + self.dur, lambda t: self._walk(self.total * min(1.0, max(0.0, (t - self.t0) / self.dur)))[1])]

    def draw(self, ink, t):
        if t < self.t0:
            return
        d = ImageDraw.Draw(ink)
        for pts in self._walk(self.total * min(1.0, (t - self.t0) / self.dur))[0]:
            if len(pts) > 1:
                d.line(pts, fill=INK + (235,), width=self.width, joint='curve')


class Print:
    kind = 'print'

    def __init__(self, p, path, x, y, w, t0, rot=3.0):
        self.p, self.x, self.y, self.t0, self.dur = p, x, y, t0, 0.3
        im = Image.open(path).convert('RGB')
        hh = int(im.height * w / im.width)
        im = im.resize((w, hh), Image.LANCZOS)
        b = 12
        card = Image.new('RGB', (w + 2 * b, hh + 2 * b), (246, 245, 239)); card.paste(im, (b, b))
        gl = Image.linear_gradient('L').rotate(35, expand=True).resize(card.size).point(lambda v: max(0, v - 200) // 4)
        card = Image.composite(Image.new('RGB', card.size, (255, 255, 255)), card, gl)
        cw, ch = card.size
        tape = Image.new('RGBA', (110, 34), (232, 222, 196, 165))
        full = Image.new('RGBA', (cw + 60, ch + 60), (0, 0, 0, 0))
        full.paste(card, (30, 30))
        full.alpha_composite(tape.rotate(-28, expand=True), (0, 6))
        full.alpha_composite(tape.rotate(30, expand=True), (cw - 36, 4))
        self.img = full.rotate(rot, resample=Image.BICUBIC, expand=True)
        self.shadow = self.img.split()[3].filter(ImageFilter.GaussianBlur(9)).point(lambda v: v * 60 // 255)
        self.sfx = ('tape', t0, 0.3)

    def end(self):
        return self.t0 + self.dur

    def pen_intervals(self):      # the hand presses the tape on the right corner
        tx, ty = self.x + self.img.width - 50, self.y + 40
        return [(self.t0 - 0.05, self.t0 + 0.3, lambda t: (tx, ty))]

    def draw(self, layer, t):
        if t < self.t0:
            return
        e = 1 - (1 - min(1.0, (t - self.t0) / 0.3)) ** 3
        X, Y = int(self.x), int(self.y)
        sh = Image.new('RGBA', self.shadow.size, (55, 50, 45, 0)); sh.putalpha(Image.eval(self.shadow, lambda v: int(v * e)))
        layer.alpha_composite(sh, (X + 6, Y + 10))
        im = self.img.copy(); im.putalpha(Image.eval(self.img.split()[3], lambda v: int(v * e)))
        layer.alpha_composite(im, (X, Y))


# ---------------- layout: two pages ----------------
els = []


def N(p, x, y, *a, **k):
    n = Note(p, x, y, *a, **k); els.append(n); return n


def right_of(n, gap=34):
    return n.x + n.w + gap


def below(n, gap=10):
    return n.y + n.h + gap


L, R = 0, 1
M = 70                                      # page margin
N(L, M, 50, 'PROJECT  SickScience', 34, PUSH_END - 0.35, cps=26, rot=0)
a1 = N(L, M, 110, "That's sick!", 116, wt('01_P', "That's"), cps=9)
a2 = N(L, M + 8, below(a1, 2), '— a beauty exec, about our data', 36, wt('01_P', 'beauty') - 0.1, cps=18)
els.append(Print(L, A('founders.jpg'), 640, 262, 210, wt('02_M', 'geneticists'), rot=4))
b1 = N(L, M, 360, 'two geneticists', 56, wt('02_M', 'geneticists') - 0.2, cps=16)
b2 = N(L, M + 4, below(b1, 14), '2009', 90, wt('02_M', '2009') - 0.1, cps=6, hl=YELLOW)
TLY = 760
tl_t = wt('02_M', 'chemistry')
els.append(Lines(L, [[(M, TLY), (FW - M, TLY - 8)]], tl_t, 0.7, width=5))
for i, yr in enumerate(['2009', '2013', '2018', '2020', '2024', '2025']):
    x = M + 6 + i * 150
    els.append(Lines(L, [[(x + 26, TLY - 16 - i * 1.4), (x + 27, TLY + 12 - i * 1.4)]], tl_t + 0.5 + i * 0.12, 0.1, width=5))
    N(L, x, TLY + 18 - i * 1.4, yr, 32, tl_t + 0.55 + i * 0.12, cps=20, rot=0)
c1 = N(L, M, 870, '14 YEARS', 80, wt('02_M', 'years') - 0.35, cps=8, hl=YELLOW)
c2 = N(L, 560, 860, 'patents + papers', 40, wt('03_P', 'Patents'), cps=14)
c3 = N(L, 568, below(c2, 8), '20-30', 70, wt('03_P', 'papers') + 0.1, cps=6, hl=YELLOW)
c4 = N(L, 572, below(c3, 6), 'peer-reviewed', 34, wt('03_P', 'PhDs'), cps=16)
d1 = N(L, M + 2, below(c1, 34), 'for mom', 42, wt('04_M', 'mom'), cps=9)
d2 = N(L, M + 2, below(d1, 10), 'still preclinical', 42, wt('04_M', 'preclinical') - 0.3, cps=11)
EY = max(below(d2, 70), below(c4, 80))
e1 = N(L, M, EY, 'in the lab', 66, wt('05_P', 'science') - 0.6, cps=11, strike=wt('05_P', 'lab') + 0.1)
e2 = N(L, right_of(e1, 110), EY - 40, 'at home', 74, wt('05_P', 'homes') - 0.35, cps=8, hl=YELLOW)
ax = right_of(e1, 18)
els.append(Lines(L, [[(ax, EY + 42), (ax + 70, EY + 14), (ax + 50, EY - 8)]], wt('05_P', 'homes') - 0.45, 0.25, width=5))

N(R, FW - M - 170, 50, 'PAGE 02', 34, LINE_T['06_M'] - 0.5, cps=26, rot=0)
f1 = N(R, M, 120, 'exosomes =', 58, wt('06_M', 'Exosomes'), cps=14)
f2 = N(R, M, below(f1, 8), 'tiny messengers', 74, wt('06_M', 'tiny'), cps=12)
dx, dy = 820, 190
k_ = 1.25
drone = [[(dx - 70 * k_, dy), (dx + 70 * k_, dy)], [(dx - 82 * k_, dy - 20 * k_), (dx - 58 * k_, dy - 20 * k_)], [(dx + 58 * k_, dy - 20 * k_), (dx + 82 * k_, dy - 20 * k_)],
         [(dx - 70 * k_, dy), (dx - 70 * k_, dy - 20 * k_)], [(dx + 70 * k_, dy), (dx + 70 * k_, dy - 20 * k_)],
         [(dx - 28 * k_, dy), (dx - 28 * k_, dy + 24 * k_), (dx + 28 * k_, dy + 24 * k_), (dx + 28 * k_, dy), (dx - 28 * k_, dy)], [(dx, dy + 24 * k_), (dx, dy + 50 * k_)],
         [(dx - 34 * k_, dy + 50 * k_), (dx + 34 * k_, dy + 50 * k_), (dx + 34 * k_, dy + 96 * k_), (dx - 34 * k_, dy + 96 * k_), (dx - 34 * k_, dy + 50 * k_)],
         [(dx - 34 * k_, dy + 50 * k_), (dx, dy + 74 * k_), (dx + 34 * k_, dy + 50 * k_)]]
els.append(Lines(R, drone, wt('06_M', 'delivery') - 0.3, 1.1, width=5))
f0 = wt('07_P', 'plants')
GY = 400
caps = []
for i, (k, kw) in enumerate([('pineapple', 'Pineapple'), ('garlic', 'garlic'), ('wheat', 'wheat'), ('radish', 'radish')]):
    x = 10 + i * 226
    tt = wt('07_P', kw) - 0.15
    pr = Print(R, A(f'fig_{k}.jpg'), x, GY, 176, min(tt, f0 + 0.3 + i * 0.35), rot=random.uniform(-3, 3))
    els.append(pr)
    cy_ = GY + pr.img.height - 14
    g1 = N(R, x + 40, cy_, f'FIG. 0{i + 1}', 30, tt + 0.05, cps=18, rot=0)
    caps.append(N(R, x + 40, below(g1, 2), k, 30, tt + 0.3, cps=18, rot=0))
HY = max(below(c, 50) for c in caps)
h1 = N(R, M, HY, 'THOUSANDS', 78, wt('07_P', 'Thousands') - 0.1, cps=9, hl=YELLOW)
h2 = N(R, right_of(h1, 26), HY + 26, 'plant library', 38, wt('07_P', 'library') - 0.3, cps=14)
i1 = N(R, M, below(h1, 22), 'NX35', 90, wt('08_M', 'NX35'), cps=6, hl=YELLOW)
i2 = N(R, right_of(i1, 30), i1.y + 30, 'no cold chain', 42, wt('08_M', 'cold') - 0.2, cps=13)
j1 = N(R, M, below(i1, 36), 'scientist?', 60, wt('09_P', 'scientist') - 0.3, cps=10, strike=wt('09_P', 'marketers') - 0.25)
j2 = N(R, right_of(j1, 50), j1.y, 'marketer.', 60, wt('09_P', 'marketers'), cps=10)
k1 = N(R, M, below(j1, 44), "No, that's science.", 52, wt('10_M', 'No'), cps=12)
l1 = N(R, M + 150, below(k1, 26), 'Sick', 100, wt('11_P', 'Sick') - 0.05, cps=9, rot=-2)
l2 = N(R, right_of(l1, 30), l1.y + 4, 'Science', 100, wt('11_P', 'science') - 0.05, cps=11, color=VIOLET, rot=-2)
LAST_WRITE = max(e.end() for e in els)
HAND_OUT = LAST_WRITE + 0.15
PULL0 = LAST_WRITE + 0.35
PULL1 = PULL0 + 1.3
END_T = PULL1 + 0.9
for e in els:
    assert e.p in (0, 1)


# ---------------- page state ----------------
class State:
    def __init__(self):
        self.ink = [Image.new('RGBA', (FW, FH), (0, 0, 0, 0)) for _ in (0, 1)]
        self.prt = [Image.new('RGBA', (FW, FH), (0, 0, 0, 0)) for _ in (0, 1)]
        self.baked = set()


ST = State()


def layers_at(t):
    for i, e in enumerate(els):
        if i not in ST.baked and t >= e.end() + 0.02:
            e.draw(ST.prt[e.p] if e.kind == 'print' else ST.ink[e.p], 1e9); ST.baked.add(i)
    ink = [ST.ink[0], ST.ink[1]]; prt = [ST.prt[0], ST.prt[1]]
    copied = set()
    for i, e in enumerate(els):
        if i not in ST.baked and t >= e.t0:
            tgt = prt if e.kind == 'print' else ink
            key = (e.kind, e.p)
            if key not in copied:
                tgt[e.p] = tgt[e.p].copy(); copied.add(key)
            e.draw(tgt[e.p], t)
    return ink, prt


# ---------------- pen / hand path ----------------
IV = []
for e in els:
    for (a, b, f) in e.pen_intervals():
        IV.append((a, b, e.p, f))
IV.sort(key=lambda r: r[0])


def ivpos(iv, t):
    a, b, p, f = iv
    x, y = f(min(max(t, a), b))
    return f2p(p, x, y)


OFF = (PWp * 0.98, PHp * 0.86)       # off-frame bottom right (plate px)
HAND_IN = IV[0][0] - 0.75


def ease(a):
    a = min(1.0, max(0.0, a)); return a * a * (3 - 2 * a)


def pen_at(t):
    """-> (plate x, plate y, lift 0..1) or None when the hand is out of frame."""
    if t < HAND_IN or t > HAND_OUT + 0.8:
        return None
    if t < IV[0][0]:
        a = ease((t - HAND_IN) / 0.75); q = ivpos(IV[0], IV[0][0])
        return OFF[0] + (q[0] - OFF[0]) * a, OFF[1] + (q[1] - OFF[1]) * a, 1 - a * 0.7
    if t > HAND_OUT:
        a = ease((t - HAND_OUT) / 0.8); q = ivpos(IV[-1], IV[-1][1])
        return q[0] + (OFF[0] - q[0]) * a, q[1] + (OFF[1] - q[1]) * a, 0.3 + 0.7 * a
    act = [iv for iv in IV if iv[0] <= t <= iv[1]]
    if act:
        x, y = ivpos(act[-1], t); return x, y, 0.0
    prev = max((iv for iv in IV if iv[1] < t), key=lambda r: r[1])
    nx = [iv for iv in IV if iv[0] > t]
    if not nx:
        q = ivpos(prev, prev[1]); return q[0], q[1], 0.2
    nxt = min(nx, key=lambda r: r[0])
    A_, B_ = ivpos(prev, prev[1]), ivpos(nxt, nxt[0])
    gap = nxt[0] - prev[1]
    travel = min(gap, 0.25 + math.dist(A_, B_) / 900)
    ts = nxt[0] - travel
    if t < ts:                                   # resting: lift a little and drift out of the way
        r = ease(min(1.0, (t - prev[1]) / 0.4)) * min(1.0, gap / 1.2)
        k = r * (1 - ease((t - (ts - 0.25)) / 0.25)) if t > ts - 0.25 else r
        return A_[0] + 26 * k, A_[1] + 34 * k, 0.15 + 0.5 * k
    a = ease((t - ts) / travel)
    lift = math.sin(math.pi * a)
    return A_[0] + (B_[0] - A_[0]) * a, A_[1] + (B_[1] - A_[1]) * a - 10 * lift, 0.2 + 0.8 * lift


# hand cut-out: RGBA, pen tip at GEOM['hand_tip'], marker length GEOM['hand_marker_px'] (14 cm)
HAND = Image.open(V('hand_cut.png')).convert('RGBA')
HTIP = GEOM['hand_tip']
HPX_CM = GEOM['hand_marker_px'] / 14.0


# ---------------- camera ----------------
Z_W = 2.05
_cam = {'x': None, 'y': None}


PAGE_C = [f2p(p, FW / 2, FH / 2) for p in (0, 1)]


def cam_follow(t):
    pp = pen_at(t)
    if pp is None:
        pp = ivpos(IV[0], IV[0][0]) if t < IV[0][0] else ivpos(IV[-1], IV[-1][1])
    pg = 0 if pp[0] < (PAGE_C[0][0] + PAGE_C[1][0]) / 2 else 1
    cx0, cy0 = PAGE_C[pg]
    tx = cx0 + (pp[0] - cx0) * 0.22
    ty = cy0 + (pp[1] - cy0) * 0.25 + 110
    if _cam['x'] is None:
        _cam['x'], _cam['y'] = tx, ty
    _cam['x'] += (tx - _cam['x']) * 0.035
    _cam['y'] += (ty - _cam['y']) * 0.035
    return _cam['x'], _cam['y']


def view(cx, cy, z, t):
    vw, vh = PWp / z, PHp / z
    cx = min(max(cx, vw / 2), PWp - vw / 2); cy = min(max(cy, vh / 2), PHp - vh / 2)
    cx += math.sin(t * 0.37) * 4 + math.sin(t * 0.91) * 1.5
    cy += math.cos(t * 0.29) * 4
    return cx - vw / 2, cy - vh / 2, W / vw          # x0, y0, scale plate->screen


def persp_coefs(Mtx):
    inv = np.linalg.inv(Mtx); inv = inv / inv[2, 2]
    return tuple(inv.flatten()[:8])


def render_page_view(t, x0, y0, s, ink, prt, hand=None):
    base = PLATE.transform((W, H), Image.EXTENT, (x0, y0, x0 + W / s, y0 + H / s), resample=Image.BICUBIC)
    out = np.asarray(base).astype(np.float32)
    S = np.array([[s, 0, -x0 * s], [0, s, -y0 * s], [0, 0, 1.0]])
    for p in (0, 1):
        Mt = S @ HP[p]
        c = persp_coefs(Mt)
        if ink[p].getbbox():
            wi = np.asarray(ink[p].transform((W, H), Image.PERSPECTIVE, c, resample=Image.BICUBIC)).astype(np.float32)
            a = wi[..., 3:4] / 255.0
            out *= (1 - a + a * wi[..., :3] / 255.0)
        if prt[p].getbbox():
            wp = np.asarray(prt[p].transform((W, H), Image.PERSPECTIVE, c, resample=Image.BICUBIC)).astype(np.float32)
            pa = wp[..., 3:4] / 255.0
            out = out * (1 - pa) + wp[..., :3] * pa
    if hand is not None:
        out = draw_hand(out, hand, x0, y0, s)
    return out


_hcache = {}


def draw_hand(out, hand, x0, y0, s):
    px, py, lift = hand
    sx, sy = (px - x0) * s, (py - y0) * s
    sc = CM * s / HPX_CM * (1 + 0.05 * lift)
    ang = -(sx - W * 0.45) / W * 7
    key = (round(sc, 3), round(ang, 1))
    if key not in _hcache:
        if len(_hcache) > 64: _hcache.clear()
        hw, hh = int(HAND.width * sc), int(HAND.height * sc)
        hi = HAND.resize((hw, hh), Image.BICUBIC)
        tip = (HTIP[0] * sc, HTIP[1] * sc)
        pad = max(hw, hh)
        canvas = Image.new('RGBA', (hw + 2 * pad, hh + 2 * pad), (0, 0, 0, 0))
        canvas.alpha_composite(hi, (pad, pad))
        cx, cy = tip[0] + pad, tip[1] + pad
        canvas = canvas.rotate(ang, resample=Image.BICUBIC, center=(cx, cy))
        bb = canvas.getbbox()
        canvas = canvas.crop(bb)
        _hcache[key] = (canvas, (cx - bb[0], cy - bb[1]))
    img, (tx, ty) = _hcache[key]
    X, Y = int(round(sx - tx)), int(round(sy - ty))
    # shadow: soft, offset to the bottom right (light from top left), grows with lift
    al = img.split()[3]
    off = (int(8 + 30 * lift), int(12 + 40 * lift))
    blur = 6 + 14 * lift
    sh = al.resize((max(1, al.width // 4), max(1, al.height // 4))).filter(ImageFilter.GaussianBlur(blur / 4)).resize(al.size)
    out = composite_mul(out, sh, X + off[0], Y + off[1], 0.32 - 0.1 * lift)
    return composite_over(out, img, X, Y)


def composite_mul(out, mask, X, Y, k):
    x0, y0 = max(0, X), max(0, Y); x1, y1 = min(W, X + mask.width), min(H, Y + mask.height)
    if x1 <= x0 or y1 <= y0: return out
    m = np.asarray(mask).astype(np.float32)[y0 - Y:y1 - Y, x0 - X:x1 - X, None] / 255.0
    out[y0:y1, x0:x1] *= (1 - k * m)
    return out


def composite_over(out, img, X, Y):
    x0, y0 = max(0, X), max(0, Y); x1, y1 = min(W, X + img.width), min(H, Y + img.height)
    if x1 <= x0 or y1 <= y0: return out
    a = np.asarray(img).astype(np.float32)[y0 - Y:y1 - Y, x0 - X:x1 - X]
    al = a[..., 3:4] / 255.0
    out[y0:y1, x0:x1] = out[y0:y1, x0:x1] * (1 - al) + a[..., :3] * al
    return out


# ---------------- opening clip ----------------
FLIP = None


def flip_frame(t):
    global FLIP
    if FLIP is None:
        FLIP = sorted(f for f in os.listdir(V('flip')) if f.endswith('.jpg'))
    i = min(len(FLIP) - 1, int(t * GEOM.get('flip_fps', 24) * GEOM.get('flip_speed', 1.0)))
    return Image.open(os.path.join(V('flip'), FLIP[i])).convert('RGB').resize((W, H), Image.LANCZOS)


endcard = Image.open(A('endcard.png')).convert('RGB').resize((W, H), Image.LANCZOS)
Z0 = 1.0


def frame(t):
    if t < FLIP_DUR:
        im = flip_frame(t)
        xf = GEOM.get('xfade', 0.35)
        if t > FLIP_DUR - xf:                         # settle onto the plate
            pl = Image.fromarray(np.clip(render_page_view(t, *view(PWp / 2, PHp / 2, Z0, 0), *layers_at(t)), 0, 255).astype(np.uint8))
            im = Image.blend(im, pl, ease((t - (FLIP_DUR - xf)) / xf))
        return np.asarray(im).astype(np.float32)
    ink, prt = layers_at(t)
    hand = pen_at(t)
    if t < WIDE_END:
        return render_page_view(t, *view(PWp / 2, PHp / 2, Z0, t * 0), ink, prt, hand)
    if t < PUSH_END:
        a = ease((t - WIDE_END) / (PUSH_END - WIDE_END))
        fx, fy = cam_follow(t)
        z = Z0 + (Z_W - Z0) * a
        cx = PWp / 2 + (fx - PWp / 2) * a; cy = PHp / 2 + (fy - PHp / 2) * a
        return render_page_view(t, *view(cx, cy, z, t), ink, prt, hand)
    if t < PULL0:
        fx, fy = cam_follow(t)
        return render_page_view(t, *view(fx, fy, Z_W, t), ink, prt, hand)
    if t < END_T:
        a = ease((t - PULL0) / (PULL1 - PULL0))
        fx, fy = cam_follow(t)
        z = Z_W + (Z0 - Z_W) * a
        cx = fx + (PWp / 2 - fx) * a; cy = fy + (PHp / 2 - fy) * a
        return render_page_view(t, *view(cx, cy, z, t), ink, prt, hand)
    a = min(1.0, (t - END_T) / 0.7)
    pg = Image.fromarray(np.clip(render_page_view(t, *view(PWp / 2, PHp / 2, Z0, t), ink, prt), 0, 255).astype(np.uint8))
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
    return np.asarray(im).astype(np.float32)


_yy, _xx = np.mgrid[0:H, 0:W]
_VIG = (1 - 0.10 * np.clip(np.sqrt(((_xx - W / 2) / (W / 2)) ** 2 + ((_yy - H / 2) / (H / 2)) ** 2) - 0.55, 0, 1) ** 1.5)[..., None]


def finish(a, t):
    rng = np.random.default_rng(int(t * 1000))
    a = a + rng.normal(0, 3.0, (H // 2, W // 2, 1)).repeat(2, 0).repeat(2, 1)
    return np.clip(a * _VIG, 0, 255).astype(np.uint8)


def sfx_events():
    ev = [e.sfx for e in els]
    ev += [('paper', x, 0.6) for x in GEOM.get('flip_sfx', [])]
    ev.append(('whoosh', LINE_T['06_M'] - 1.0, 0.5))
    return ev


if __name__ == '__main__':
    args = sys.argv[1:]
    info = {'LINE_T': LINE_T, 'TOTAL': TOTAL, 'END_T': END_T, 'FLIP_DUR': FLIP_DUR, 'PULL0': PULL0, 'sfx': sfx_events()}
    if '--info' in args:
        json.dump(info, open(os.path.join(ROOT, 'timeline4.json'), 'w'), indent=1)
        print({k: v for k, v in info.items() if k != 'sfx'})
        sys.exit()
    if '--frames' in args:
        ts = sorted(float(x) for x in args[args.index('--frames') + 1].split(','))
        for tt in ts:                        # camera smoothing: warm up 3 s before each frame
            _cam['x'] = None
            for k in range(int(3 * FPS), 0, -1):
                if tt - k / FPS > FLIP_DUR: cam_follow(tt - k / FPS)
            Image.fromarray(finish(frame(tt), tt)).save(os.path.join(ROOT, 'v4', f'g_{tt:05.2f}.jpg'), quality=88)
        sys.exit()
    out = args[args.index('--out') + 1] if '--out' in args else os.path.join(ROOT, 'video4_noaudio.mp4')
    nfr = int(TOTAL * FPS)
    f0 = int(float(args[args.index('--from') + 1]) * FPS) if '--from' in args else 0
    if '--to' in args: nfr = int(float(args[args.index('--to') + 1]) * FPS)
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    for i in range(f0, nfr):
        tt = i / FPS
        if f0 and i == f0:
            for k in range(max(0, f0 - 90), f0):
                if k / FPS > FLIP_DUR: cam_follow(k / FPS)
        p.stdin.write(finish(frame(tt), tt).tobytes())
        if i % 150 == 0:
            print(f'{i}/{nfr}', flush=True)
    p.stdin.close(); p.wait()
    print('done', out)
