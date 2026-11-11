# Founders brand-story film: "That's sick. No, that's science." (realistic lab notebook, style-guide-v2-notebook.md)
# Usage: ~/motion-tools/.venv/bin/python render.py [--preview] [--frames a,b,c] [--out out.mp4]
import json, math, os, random, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

ROOT = os.path.dirname(os.path.abspath(__file__))
A = lambda p: os.path.join(ROOT, 'assets', p)
FPS = 30
W, H = 1080, 1920
PW, PH = 1080, 1935                     # page plate coordinates
FONT_HAND = os.path.expanduser('~/Library/Fonts/Caveat-Bold.ttf')
FONT_HAND_M = os.path.expanduser('~/Library/Fonts/Caveat-SemiBold.ttf')
FONT_GROT = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Medium.otf')
INK = (24, 28, 40)
VIOLET = (169, 33, 192)
YELLOW = (255, 226, 70)
random.seed(7)

# ---------------- VO timeline ----------------
WORDS = json.load(open(os.path.join(ROOT, 'words.json')))
DUR = {k: max(w['e'] for w in v['words']) + 0.25 for k, v in WORDS.items()}
ORDER = ['01_P', '02_M', '03_P', '04_M', '05_P', '06_M', '07_P', '08_M', '09_P', '10_M', '11_P']
GAP = {'04_M': 0.55, '05_P': 0.4, '06_M': 0.7, '11_P': 0.7}
COVER = 1.0
t = COVER + 0.15
LINE_T = {}
for k in ORDER:
    f = k + '.mp3'
    if f not in WORDS:
        continue
    t += GAP.get(k, 0.2)
    LINE_T[k] = t
    t += DUR[f]
END_VO = t
TOTAL = END_VO + 1.9


def wt(line, word, nth=0, edge='s'):
    """global time of a word in a line (substring match, case-insensitive)."""
    f = line + '.mp3'
    if f not in WORDS:
        return None
    hits = [w for w in WORDS[f]['words'] if word.lower() in w['w'].lower()]
    if not hits:
        return LINE_T[line]
    return LINE_T[line] + hits[min(nth, len(hits) - 1)][edge]


# ---------------- page elements ----------------
class El:
    page = 1
    t0 = 0.0
    dur = 0.5
    sfx = None

    def done(self, t):
        return t >= self.t0 + self.dur

    def started(self, t):
        return t >= self.t0


def font(size, f=FONT_HAND):
    return ImageFont.truetype(f, size)


class Note(El):
    def __init__(self, page, x, y, text, size, t0, cps=13.0, color=INK, rot=None, f=FONT_HAND, hl=None, strike=None, after=None):
        self.page, self.x, self.y, self.text, self.size, self.color = page, x, y, text, size, color
        self.t0 = t0
        self.dur = max(0.35, len(text) / cps)
        self.rot = random.uniform(-1.6, 1.2) if rot is None else rot
        fnt = font(size, f)
        bb = fnt.getbbox(text)
        tw, th = bb[2] + 12, bb[3] + int(size * 0.35)
        img = Image.new('L', (tw, th), 0)
        ImageDraw.Draw(img).text((4, 0), text, font=fnt, fill=255)
        # ink texture: slight density variation
        nz = Image.effect_noise((tw, th), 22).filter(ImageFilter.GaussianBlur(1))
        img = ImageChops.multiply(img, nz.point(lambda v: 205 + v * 50 // 255))
        self.mask = img.rotate(self.rot, resample=Image.BICUBIC, expand=True)
        self.w, self.h = self.mask.size
        self.hl = hl            # highlight colour or None
        self.hl_t = self.t0 + self.dur + 0.05
        self.strike = strike    # time to strike through
        self.sfx = ('pen', self.t0, self.dur)
        if hl:
            self.hlmask = self._hl_mask()

    def _hl_mask(self):
        w, h = self.w + 24, int(self.size * 0.62)
        m = Image.new('L', (w, h), 0)
        d = ImageDraw.Draw(m)
        # ragged highlighter band, darker ends
        pts_top = [(x, 4 + random.uniform(-3, 3)) for x in range(0, w + 1, 12)]
        pts_bot = [(x, h - 4 + random.uniform(-3, 3)) for x in range(w, -1, -12)]
        d.polygon(pts_top + pts_bot, fill=150)
        d.ellipse((-8, 0, 18, h), fill=185)
        d.ellipse((w - 18, 0, w + 8, h), fill=185)
        return m.filter(ImageFilter.GaussianBlur(1.2)).rotate(self.rot, resample=Image.BICUBIC, expand=True)

    def reveal(self, t):
        return min(1.0, max(0.0, (t - self.t0) / self.dur))

    def draw(self, canvas, t):
        if t < self.t0:
            return
        # highlighter first (under ink), swept left->right
        if self.hl and t >= self.hl_t:
            p = min(1.0, (t - self.hl_t) / 0.35)
            hm = self.hlmask
            cut = hm.crop((0, 0, max(1, int(hm.width * p)), hm.height))
            layer = Image.new('RGB', cut.size, self.hl)
            x, y = self.x - 12, self.y + int(self.size * 0.42)
            region = canvas.crop((x, y, x + cut.width, y + cut.height))
            mult = ImageChops.multiply(region, layer)
            canvas.paste(Image.composite(mult, region, cut), (x, y))
        p = self.reveal(t)
        cut_w = int(self.w * p)
        if cut_w < 1:
            return
        m = self.mask.copy()
        if p < 1:
            edge = Image.new('L', (self.w, self.h), 0)
            ImageDraw.Draw(edge).rectangle((0, 0, cut_w, self.h), fill=255)
            # soft nib edge
            g = Image.linear_gradient('L').rotate(90).resize((14, self.h))
            edge.paste(ImageChops.invert(g), (max(0, cut_w - 14), 0))
            m = ImageChops.multiply(m, edge)
        canvas.paste(Image.new('RGB', m.size, self.color), (self.x, self.y), m)
        if self.strike is not None and t >= self.strike:
            p2 = min(1.0, (t - self.strike) / 0.28)
            d = ImageDraw.Draw(canvas)
            y0 = self.y + int(self.size * 0.62)
            x1 = self.x + int((self.w - 6) * p2)
            pts = [(xx, y0 + math.sin(xx * 0.05) * 2.5 - (xx - self.x) * 0.02) for xx in range(self.x, max(self.x + 2, x1), 6)]
            if len(pts) > 1:
                d.line(pts, fill=INK, width=max(3, self.size // 12), joint='curve')
            if p2 >= 1 and t >= self.strike + 0.32:
                p3 = min(1.0, (t - self.strike - 0.32) / 0.22)
                x2 = self.x + int((self.w - 6) * p3)
                pts = [(xx, y0 - 9 + math.sin(xx * 0.07 + 1) * 2.5) for xx in range(self.x, max(self.x + 2, x2), 6)]
                if len(pts) > 1:
                    d.line(pts, fill=INK, width=max(3, self.size // 13), joint='curve')

    def done(self, t):
        end = self.t0 + self.dur
        if self.hl:
            end = max(end, self.hl_t + 0.4)
        if self.strike is not None:
            end = max(end, self.strike + 0.6)
        return t >= end


class Lines(El):
    """polyline doodle drawn stroke by stroke."""
    def __init__(self, page, strokes, t0, dur, width=4, color=INK):
        self.page, self.strokes, self.t0, self.dur, self.width, self.color = page, strokes, t0, dur, width, color
        self.total = sum(self._len(s) for s in strokes)
        self.sfx = ('pen', t0, dur)

    @staticmethod
    def _len(s):
        return sum(math.dist(s[i], s[i + 1]) for i in range(len(s) - 1))

    def draw(self, canvas, t):
        if t < self.t0:
            return
        L = self.total * min(1.0, (t - self.t0) / self.dur)
        d = ImageDraw.Draw(canvas)
        for s in self.strokes:
            if L <= 0:
                break
            pts = [s[0]]
            for i in range(len(s) - 1):
                seg = math.dist(s[i], s[i + 1])
                if L >= seg:
                    pts.append(s[i + 1]); L -= seg
                else:
                    f = L / seg
                    pts.append((s[i][0] + (s[i + 1][0] - s[i][0]) * f, s[i][1] + (s[i + 1][1] - s[i][1]) * f)); L = 0
                    break
            if len(pts) > 1:
                d.line(pts, fill=self.color, width=self.width, joint='curve')


class Print(El):
    """photo print taped onto the page."""
    def __init__(self, page, path, x, y, w, t0, rot=3.0, h=None):
        self.page, self.x, self.y, self.t0, self.dur = page, x, y, t0, 0.3
        im = Image.open(path).convert('RGB')
        hh = h or int(im.height * w / im.width)
        im = im.resize((w, hh), Image.LANCZOS)
        b = 12
        card = Image.new('RGB', (w + 2 * b, hh + 2 * b), (247, 246, 241))
        card.paste(im, (b, b))
        # slight matte + glare
        gl = Image.linear_gradient('L').rotate(35, expand=True).resize(card.size).point(lambda v: max(0, v - 200) // 4)
        card = Image.composite(Image.new('RGB', card.size, (255, 255, 255)), card, gl)
        cw, ch = card.size
        tape = Image.new('RGBA', (110, 34), (232, 222, 196, 170))
        full = Image.new('RGBA', (cw + 60, ch + 60), (0, 0, 0, 0))
        full.paste(card, (30, 30))
        full.alpha_composite(tape.rotate(-28, expand=True), (0, 6))
        full.alpha_composite(tape.rotate(30, expand=True), (cw - 40, 4))
        self.img = full.rotate(rot, resample=Image.BICUBIC, expand=True)
        a = self.img.split()[3]
        self.shadow = a.filter(ImageFilter.GaussianBlur(9)).point(lambda v: v * 55 // 255)
        self.sfx = ('tape', t0, 0.3)

    def draw(self, canvas, t):
        if t < self.t0:
            return
        p = min(1.0, (t - self.t0) / 0.3)
        e = 1 - (1 - p) ** 3
        s = 1.05 - 0.05 * e
        img = self.img if s == 1 else self.img.resize((int(self.img.width * s), int(self.img.height * s)))
        sh = self.shadow if s == 1 else self.shadow.resize(img.size)
        ox = self.x - (img.width - self.img.width) // 2
        oy = self.y - (img.height - self.img.height) // 2
        canvas.paste((60, 55, 50), (ox + 6, oy + 10), Image.eval(sh, lambda v: int(v * e)))
        canvas.paste(img, (ox, oy), Image.eval(img.split()[3], lambda v: int(v * e)))


# ---------------- build the two pages ----------------
els = []
L01, L02, L03, L04, L05 = (LINE_T.get(k) for k in ['01_P', '02_M', '03_P', '04_M', '05_P'])
# PAGE 1
els.append(Note(1, 250, 438, "That's sick!", 96, wt('01_P', "That's"), cps=9))
els.append(Note(1, 258, 540, '— a beauty exec, about our data', 32, wt('01_P', 'beauty') - 0.1, cps=18))
els.append(Note(1, 252, 600, 'two geneticists', 44, wt('02_M', 'geneticists') - 0.2, cps=16))
els.append(Note(1, 252, 652, '2009', 76, wt('02_M', '2009') - 0.1, cps=6, hl=YELLOW))
# timeline line with years
tl_t = wt('02_M', 'chemistry')
els.append(Lines(1, [[(255, 768), (870, 760)]], tl_t, 0.7, width=4))
for i, (yr, x) in enumerate([('2009', 252), ('2013', 362), ('2018', 472), ('2020', 582), ('2024', 692), ('2025', 802)]):
    els.append(Lines(1, [[(x + 26, 752), (x + 27, 774)]], tl_t + 0.5 + i * 0.12, 0.1, width=4))
    els.append(Note(1, x, 782, yr, 30, tl_t + 0.55 + i * 0.12, cps=20, rot=0))
els.append(Note(1, 252, 845, '14 YEARS', 70, wt('02_M', 'years') - 0.35, cps=8, hl=YELLOW))
els.append(Print(1, A('founders.jpg'), 648, 372, 168, wt('02_M', 'geneticists'), rot=4))
els.append(Note(1, 590, 855, 'patents + papers', 38, wt('03_P', 'Patents'), cps=14))
els.append(Note(1, 600, 912, '20-30', 62, wt('03_P', 'papers') + 0.1, cps=6, hl=YELLOW))
els.append(Note(1, 604, 990, 'peer-reviewed', 32, wt('03_P', 'PhDs'), cps=16))
els.append(Note(1, 252, 1060, 'for mom', 36, wt('04_M', 'mom'), cps=9))
els.append(Note(1, 252, 1110, 'still preclinical', 36, wt('04_M', 'preclinical') - 0.3, cps=11))
lab = Note(1, 252, 1250, 'in the lab', 58, wt('05_P', 'science') - 0.6, cps=11, strike=wt('05_P', 'lab') + 0.1)
els.append(lab)
els.append(Note(1, 545, 1190, 'at home', 60, wt('05_P', 'homes') - 0.35, cps=8, hl=YELLOW))
els.append(Lines(1, [[(520, 1276), (560, 1260), (545, 1240)]], wt('05_P', 'homes') - 0.45, 0.25, width=4))
# PAGE 2
els.append(Note(2, 252, 440, 'exosomes =', 46, wt('06_M', 'Exosomes'), cps=14))
els.append(Note(2, 252, 502, 'tiny messengers', 58, wt('06_M', 'tiny'), cps=12))
dx, dy = 700, 455                       # drone doodle with envelope
drone = [[(dx - 60, dy), (dx + 60, dy)], [(dx - 70, dy - 18), (dx - 50, dy - 18)], [(dx + 50, dy - 18), (dx + 70, dy - 18)],
         [(dx - 60, dy), (dx - 60, dy - 18)], [(dx + 60, dy), (dx + 60, dy - 18)],
         [(dx - 25, dy), (dx - 25, dy + 22), (dx + 25, dy + 22), (dx + 25, dy), (dx - 25, dy)],
         [(dx, dy + 22), (dx, dy + 44)],
         [(dx - 30, dy + 44), (dx + 30, dy + 44), (dx + 30, dy + 84), (dx - 30, dy + 84), (dx - 30, dy + 44)],
         [(dx - 30, dy + 44), (dx, dy + 66), (dx + 30, dy + 44)]]
els.append(Lines(2, drone, wt('06_M', 'delivery') - 0.3, 1.1, width=4))
f0 = wt('07_P', 'plants')
for i, (k, cap) in enumerate([('pineapple', 'PINEAPPLE'), ('garlic', 'GARLIC'), ('wheat', 'WHEAT'), ('radish', 'RADISH')]):
    x = 236 + i * 158
    kw = {'pineapple': 'Pineapple', 'garlic': 'garlic', 'wheat': 'wheat', 'radish': 'radish'}[k]
    tt = wt('07_P', kw) - 0.15
    els.append(Print(2, A(f'fig_{k}.jpg'), x, 610, 132, min(tt, f0 + 0.3 + i * 0.35), rot=random.uniform(-3, 3)))
    els.append(Note(2, x + 20, 790, f'FIG. 0{i + 1}', 28, tt + 0.05, cps=18, rot=0))
    els.append(Note(2, x + 20, 822, cap.lower(), 28, tt + 0.3, cps=18, rot=0))
els.append(Note(2, 252, 890, 'THOUSANDS', 70, wt('07_P', 'Thousands') - 0.1, cps=9, hl=YELLOW))
els.append(Note(2, 640, 912, 'plant library', 38, wt('07_P', 'library') - 0.3, cps=14))
els.append(Note(2, 252, 1012, 'NX35', 80, wt('08_M', 'NX35'), cps=6, hl=YELLOW))
els.append(Note(2, 480, 1034, 'no cold chain', 40, wt('08_M', 'cold') - 0.2, cps=13))
if '09_P.mp3' in WORDS:
    els.append(Note(2, 252, 1130, 'scientist?', 58, wt('09_P', 'scientist') - 0.3, cps=10, strike=wt('09_P', 'marketers') - 0.25))
    els.append(Note(2, 560, 1130, 'marketer.', 58, wt('09_P', 'marketers'), cps=10))
els.append(Note(2, 252, 1240, "No, that's science.", 50, wt('10_M', 'No'), cps=12))
els.append(Note(2, 252, 1312, 'Sick', 104, wt('10_M', 'science', nth=1) + 0.1, cps=6, rot=-1))
els.append(Note(2, 455, 1312, 'Science', 104, wt('10_M', 'science', nth=1) + 0.55, cps=6, color=VIOLET, rot=-1))
PAGE2_T = LINE_T['06_M'] - 0.55
END_T = LINE_T['11_P'] - 0.6

# camera keyframes (page y centre) per time
def cam_y(t, page):
    focus = None
    for e in els:
        if e.page == page and e.started(t) and isinstance(e, Note):
            focus = e.y
    if focus is None:
        focus = 440
    return focus + 60


plate = Image.open(A('page.png')).convert('RGB').resize((PW, PH), Image.LANCZOS)
ec_path = A('endcard.png')
endcard = Image.open(ec_path).convert('RGB').resize((W, H), Image.LANCZOS) if os.path.exists(ec_path) else None

cache = {1: (plate.copy(), set()), 2: (plate.copy(), set())}


def page_state(page, t):
    base, baked = cache[page]
    for i, e in enumerate(els):
        if e.page == page and i not in baked and e.done(t):
            e.draw(base, t + 10)
            baked.add(i)
    img = base.copy()
    for i, e in enumerate(els):
        if e.page == page and i not in baked and e.started(t):
            e.draw(img, t)
    return img


def page_state_final(page):
    img = plate.copy()
    for e in els:
        if e.page == page:
            e.draw(img, 1e9)
    return img


# smoothed camera
_cy = {}
def smooth_cy(t, page):
    target = cam_y(t, page)
    key = page
    prev = _cy.get(key, target)
    v = prev + (target - prev) * 0.06
    _cy[key] = v
    return v


def view(img, cy, z, t):
    # crop region of page around (540, cy) at zoom z
    vw, vh = W / z, H / z
    cy = min(max(cy, 880), 1100)
    dxr = math.sin(t * 0.37) * 4 + math.sin(t * 0.91) * 2
    dyr = math.cos(t * 0.29) * 4
    x0 = 572 - vw / 2 + dxr
    y0 = cy - vh / 2 + dyr
    return img.crop((int(x0), int(y0), int(x0 + vw), int(y0 + vh))).resize((W, H), Image.BICUBIC)


GROT = ImageFont.truetype(FONT_GROT, 74)
FINAL1 = None


def frame(t):
    global FINAL1
    z = 1.55
    if t < COVER:                                   # cover: finished page 1, ending first
        if FINAL1 is None:
            FINAL1 = page_state_final(1)
        im = view(FINAL1, 760, 1.12, t)
        d = ImageDraw.Draw(im)
        for i, line in enumerate(["THAT'S SICK.", "HERE'S HOW IT STARTED."]):
            tw = d.textlength(line, font=GROT)
            d.text(((W - tw) / 2, 1460 + i * 92), line, font=GROT, fill=(20, 20, 24))
        if t > COVER - 0.25:                        # whip
            a = (t - (COVER - 0.25)) / 0.25
            im = im.filter(ImageFilter.BoxBlur(int(2 + a * 18)))
        return im
    if t < PAGE2_T:
        im = view(page_state(1, t), smooth_cy(t, 1), z, t)
    elif t < PAGE2_T + 0.5:                         # page turn: slide with blur
        a = (t - PAGE2_T) / 0.5
        e = a * a * (3 - 2 * a)
        A1 = view(page_state(1, t), smooth_cy(t, 1), z, t)
        B1 = view(page_state(2, t), 900, z, t)
        im = Image.new('RGB', (W, H))
        off = int(W * e)
        im.paste(A1, (-off, 0)); im.paste(B1, (W - off, 0))
        im = im.filter(ImageFilter.BoxBlur(int(14 * math.sin(math.pi * a))))
    elif t < END_T or endcard is None:
        im = view(page_state(2, t), smooth_cy(t, 2), z, t)
    else:                                           # end card crossfade + slow push
        a = min(1.0, (t - END_T) / 0.7)
        pg = view(page_state(2, t), smooth_cy(t, 2), z, t)
        s = 1.0 + 0.04 * (t - END_T) / (TOTAL - END_T)
        ec = endcard.resize((int(W * s), int(endcard.height * s)), Image.BICUBIC)
        oy = (ec.height - H) // 2
        ox = (ec.width - W) // 2
        ecf = ec.crop((ox, oy, ox + W, oy + H))
        im = Image.blend(pg, ecf, a)
        if t > END_T + 0.4:
            hf = ImageFont.truetype(FONT_HAND, 80)
            d = ImageDraw.Draw(im)
            for li, (line, ly) in enumerate((('Science,', 226), ('but never', 304), ('boring.', 382))):
                tw = d.textlength(line, font=hf)
                p = min(1.0, max(0.0, (t - END_T - 0.4 - li * 0.6) / 0.9))
                if p <= 0: continue
                cw = int((tw + 20) * p)
                lay = Image.new('L', (int(tw) + 20, 130), 0)
                ImageDraw.Draw(lay).text((10, 0), line, font=hf, fill=255)
                m = Image.new('L', lay.size, 0); m.paste(lay.crop((0, 0, max(1, cw), lay.height)), (0, 0))
                im.paste((24, 28, 40), (78, ly), m)
    # grain + vignette
    return im


def grain(im, t):
    a = np.asarray(im).astype(np.int16)
    rng = np.random.default_rng(int(t * 1000))
    n = rng.normal(0, 3.2, (H // 2, W // 2, 1)).repeat(2, 0).repeat(2, 1)
    a = np.clip(a + n, 0, 255).astype(np.uint8)
    return a


VIG = None
def vignette(a):
    global VIG
    if VIG is None:
        yy, xx = np.mgrid[0:H, 0:W]
        r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
        VIG = (1 - 0.10 * np.clip(r - 0.55, 0, 1) ** 1.5)[..., None]
    return (a * VIG).astype(np.uint8)


def sfx_events():
    ev = []
    for e in els:
        if e.sfx:
            ev.append(e.sfx)
    ev.append(('paper', PAGE2_T, 0.5))
    return ev


if __name__ == '__main__':
    args = sys.argv[1:]
    if '--info' in args:
        print(json.dumps({'LINE_T': LINE_T, 'TOTAL': TOTAL, 'PAGE2_T': PAGE2_T, 'END_T': END_T}, indent=1))
        json.dump({'LINE_T': LINE_T, 'TOTAL': TOTAL, 'PAGE2_T': PAGE2_T, 'END_T': END_T, 'sfx': sfx_events()}, open(os.path.join(ROOT, 'timeline.json'), 'w'), indent=1)
        sys.exit()
    if '--frames' in args:
        ts = [float(x) for x in args[args.index('--frames') + 1].split(',')]
        # need sequential cache: run through times in order
        out = []
        for tt in sorted(ts):
            n0 = 0
            im = frame(tt)
            Image.fromarray(vignette(grain(im, tt))).save(os.path.join(ROOT, f'f_{tt:05.2f}.jpg'), quality=88)
        sys.exit()
    out = args[args.index('--out') + 1] if '--out' in args else os.path.join(ROOT, 'video_noaudio.mp4')
    nfr = int(TOTAL * FPS)
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '18', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    for i in range(nfr):
        tt = i / FPS
        a = vignette(grain(frame(tt), tt))
        p.stdin.write(a.tobytes())
        if i % 150 == 0:
            print(f'{i}/{nfr}', flush=True)
    p.stdin.close(); p.wait()
    print('done', out)
