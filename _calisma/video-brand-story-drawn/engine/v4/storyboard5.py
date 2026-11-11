# v4d outline: ChatGPT v4b script (chatgpt-v4b-answer.txt), 2 pages, Biro Script Plus, wobbly ballpoint-pen sketches.
import math, os, random
from PIL import Image, ImageDraw, ImageFont

R = os.path.dirname(os.path.abspath(__file__))
F = os.path.expanduser('~/Library/Fonts/')
random.seed(11)
KW = None                                     # narration word the next strokes illustrate (drawing finishes as it is said)


def kw(w):
    global KW
    KW = w


BIRO = lambda s: ImageFont.truetype(F + 'BiroScriptUSPlus-Regular.ttf', s)
GOCHI = lambda s: ImageFont.truetype(os.path.join(R, '..', 'fonts', 'GochiHand.ttf'), s)
MARK = lambda s: ImageFont.truetype(os.path.join(R, '..', 'fonts', 'PermanentMarker.ttf'), s)
GROT = lambda s: ImageFont.truetype(F + 'FoundersGrotesk-Medium.otf', s)
INK, GRID, YEL, VIO = (28, 34, 70), (206, 215, 228), (238, 158, 232), (169, 33, 192)   # highlighter = SickScience pink (client, 2026-11-08)
RED, GRN, COB, GREY = (205, 40, 50), (40, 150, 70), (40, 60, 170), (120, 125, 140)
SW, SH = 2040, 1480
PL, PR = (60, 1000), (1040, 1980)
PT, PB = 150, 1420


from PIL import ImageChops, ImageFilter


def _img(d):
    return d._image


def multiply_mask(d, mask, col, opacity=1.0):
    im = _img(d)
    layer = Image.new('RGB', im.size, col)
    mul = ImageChops.multiply(im, layer)
    m = mask.point(lambda v: int(v * opacity))
    im.paste(Image.composite(mul, im, m))


def highlighter(d, bb, col=YEL):
    # chisel highlighter: 2 overlapping passes, streaky, darker where they overlap, ragged ends
    im = _img(d); m = Image.new('L', im.size, 0); md = ImageDraw.Draw(m)
    x0, x1 = bb[0] - 12, bb[2] + 12
    h = (bb[3] - bb[1]) * 0.62
    for p in range(2):
        yc = bb[1] + (bb[3] - bb[1]) * (0.6 + p * 0.08) + random.uniform(-3, 3)
        for k in range(int(h)):
            yy = yc - h / 2 + k
            a = 235 + int(20 * math.sin(k * 0.9 + p))
            md.line((x0 + random.uniform(-6, 10) + p * 8, yy, x1 + random.uniform(-10, 6) - p * 6, yy + random.uniform(-2, 2)), fill=a)
    m = m.filter(ImageFilter.GaussianBlur(0.8))
    multiply_mask(d, m, col, 1.0)


def marker_text(d, x, y, s, size, col=(22, 22, 26), font=None):
    # felt marker glyphs, slight ink density variation
    im = _img(d); f = (font or MARK)(size)
    m = Image.new('L', im.size, 0); ImageDraw.Draw(m).text((x, y), s, font=f, fill=255)
    tb = m.getbbox()
    if tb: m = m.rotate(random.uniform(-1.6, 1.6), resample=Image.BICUBIC, center=((tb[0] + tb[2]) / 2, (tb[1] + tb[3]) / 2))
    nz = Image.effect_noise(im.size, 30).point(lambda v: 205 + v * 50 // 255)
    m = ImageChops.multiply(m, nz)
    multiply_mask(d, m, col, 1.0)
    return d.textbbox((x, y), s, font=f)


def marker_fill(d, poly_mask_fn, col, angle=35, gap=7):
    # coloured felt-tip hatching inside a shape (mask drawn by poly_mask_fn on an L image)
    im = _img(d); shape = Image.new('L', im.size, 0); poly_mask_fn(ImageDraw.Draw(shape))
    strokes = Image.new('L', im.size, 0); sd = ImageDraw.Draw(strokes)
    bx = shape.getbbox()
    if not bx: return
    L = (bx[2] - bx[0]) + (bx[3] - bx[1])
    for k in range(-L, L, gap):
        x0 = bx[0] + k; sd.line((x0, bx[3] + 10, x0 + L * math.tan(math.radians(angle)), bx[1] - L), fill=random.randint(170, 235), width=gap + 3)
    m = ImageChops.multiply(shape, strokes.filter(ImageFilter.GaussianBlur(0.6)))
    multiply_mask(d, m, col, 1.0)


# ---------- ballpoint helpers: smooth hand wobble, 4x supersampled anti-aliased ink, pressure taper, ink grain ----------
import numpy as _np, cv2 as _cv2


def _dense(pts, step=1.5):
    out = [pts[0]]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        n = max(1, int(math.dist((x0, y0), (x1, y1)) / step))
        for k in range(1, n + 1): out.append((x0 + (x1 - x0) * k / n, y0 + (y1 - y0) * k / n))
    return out


def wob(pts, amp=1.0, step=1.5):
    """smooth but irregular hand wobble: slow drift + medium tremor, no per-point jitter"""
    P = _dense(pts, step)
    ph = [random.uniform(0, 6.28) for _ in range(6)]
    out, s = [], 0.0
    for i, (x, y) in enumerate(P):
        if i: s += math.dist(P[i - 1], P[i])
        out.append((x + amp * (0.55 * math.sin(s / 31 + ph[0]) + 0.3 * math.sin(s / 11 + ph[1]) + 0.15 * math.sin(s / 4.7 + ph[2])),
                    y + amp * (0.55 * math.sin(s / 29 + ph[3]) + 0.3 * math.sin(s / 12 + ph[4]) + 0.15 * math.sin(s / 5.1 + ph[5]))))
    return out


def ink_stroke(im, P, width, col, alpha=0.95, S=4):
    xs = [p[0] for p in P]; ys = [p[1] for p in P]; m = width + 4
    x0, y0 = int(max(0, min(xs) - m)), int(max(0, min(ys) - m)); x1, y1 = int(min(im.width, max(xs) + m + 1)), int(min(im.height, max(ys) + m + 1))
    if x1 <= x0 or y1 <= y0: return
    msk = _np.zeros(((y1 - y0) * S, (x1 - x0) * S), _np.uint8)
    n = len(P); L = 0.0; acc = [0.0]
    for i in range(1, n): L += math.dist(P[i - 1], P[i]); acc.append(L)
    ch = 4; ph = random.uniform(0, 6.28)
    for i in range(0, n - 1, ch):
        seg = P[i:i + ch + 1]
        u = acc[min(i + ch // 2, n - 1)] / max(L, 1e-6)
        taper = min(1.0, 0.55 + u * 5, 0.55 + (1 - u) * 5) * (1 + 0.16 * math.sin(acc[min(i, n - 1)] / 17 + ph))   # pressure: lighter ends, uneven hand
        th = max(1, int(round(width * taper * S)))
        q = _np.array([[(x - x0) * S, (y - y0) * S] for x, y in seg], _np.int32).reshape(-1, 1, 2)
        _cv2.polylines(msk, [q], False, 255, th, _cv2.LINE_AA)
    a = _cv2.resize(msk, (x1 - x0, y1 - y0), interpolation=_cv2.INTER_AREA).astype(_np.float32) / 255
    g = _np.array([random.random() for _ in range(64)], _np.float32)        # ballpoint grain, seeded by `random`
    gy, gx = _np.mgrid[y0:y1, x0:x1]
    grain = 0.86 + 0.14 * g[(gx * 7 + gy * 13) % 64] * g[(gx * 3 + gy * 5 + 17) % 64]
    a = a * alpha * grain
    roi = _np.asarray(im.crop((x0, y0, x1, y1))).astype(_np.float32)
    c = _np.array(col, _np.float32) / 255
    roi = roi * (1 - a[..., None] * (1 - c))
    im.paste(Image.fromarray(_np.clip(roi, 0, 255).astype(_np.uint8)), (x0, y0))


def _pen_raw(im, pts, w=3, col=INK, passes=2):
    pts = list(pts)
    if len(pts) >= 2 and math.dist(pts[0], pts[-1]) > 3:                    # open stroke: tiny overshoot at both ends
        for a, b, at in ((pts[1], pts[0], 0), (pts[-2], pts[-1], None)):
            L = math.dist(a, b) or 1; o = random.uniform(1.0, 3.5)
            q = (b[0] + (b[0] - a[0]) / L * o, b[1] + (b[1] - a[1]) / L * o)
            if at == 0: pts.insert(0, q)
            else: pts.append(q)
    for p in range(passes):
        P = wob(pts, amp=1.15 if p == 0 else 1.45)
        if p: dx, dy = random.uniform(-1.1, 1.1), random.uniform(-1.1, 1.1); P = [(x + dx, y + dy) for x, y in P]
        ink_stroke(im, P, w * 0.8 if p == 0 else max(1, w - 1) * 0.62, col, 0.93 if p == 0 else 0.6)


def pen(d, pts, w=3, col=INK, passes=2):
    _pen_raw(_img(d), pts, w, col, passes)


def pline(d, a, b, **k): pen(d, [a, b], **k)


def pcirc(d, x, y, r, **k):
    n = max(48, int(r * 1.2))
    a0 = random.uniform(0, 6.28); sq = random.uniform(0.96, 1.04)
    pen(d, [(x + r * math.cos(a0 + 6.45 * i / n), y + r * sq * math.sin(a0 + 6.45 * i / n)) for i in range(n + 1)], **k)


def prect(d, x0, y0, x1, y1, **k):
    j = lambda: random.uniform(-2.6, 2.6)
    c = [(x0 + j(), y0 + j()), (x1 + j(), y0 + j()), (x1 + j(), y1 + j()), (x0 + j(), y1 + j())]
    pen(d, c + [(c[0][0] + random.uniform(2, 6), c[0][1] + j())], **k)


def arrow(d, a, b, dotted=False):
    if dotted:
        n = int(math.dist(a, b) // 16)
        for i in range(0, n, 2):
            pline(d, (a[0] + (b[0] - a[0]) * i / n, a[1] + (b[1] - a[1]) * i / n), (a[0] + (b[0] - a[0]) * (i + 1) / n, a[1] + (b[1] - a[1]) * (i + 1) / n), passes=1)
    else:
        pline(d, a, b)
    ang = math.atan2(b[1] - a[1], b[0] - a[0])
    for s in (0.45, -0.45):
        pline(d, b, (b[0] - 22 * math.cos(ang + s), b[1] - 22 * math.sin(ang + s)), passes=1)


def check(d, x, y, s=1):
    pen(d, [(x, y), (x + 12 * s, y + 16 * s), (x + 36 * s, y - 18 * s)], w=4)


def txt(d, x, y, s, size, col=INK, hl=None, strike=None, bold=False):
    f = MARK(int(size * 0.82)) if bold else BIRO(size)
    bb = d.textbbox((x, y), s, font=f)
    if bold:
        bb = marker_text(d, x, y, s, int(size * 0.82), col if col != INK else (22, 22, 26))
    else:                                                   # handwriting is never on a ruler: the line drifts, each word sits a little off
        x += random.uniform(-3, 3); y += random.uniform(-2.5, 2.5)
        slope = random.uniform(-0.022, 0.022); xc = x; bbs = []
        for k, wd in enumerate(s.split(' ')):
            if wd:
                yy = y + (xc - x) * slope + random.uniform(-1.4, 1.4)
                d.text((xc, yy), wd, font=f, fill=col); bbs.append(d.textbbox((xc, yy), wd, font=f))
            xc += d.textlength(wd + ' ', font=f) * random.uniform(0.97, 1.05)
        if bbs: bb = (min(q[0] for q in bbs), min(q[1] for q in bbs), max(q[2] for q in bbs), max(q[3] for q in bbs))
    if hl:
        highlighter(d, bb, hl)
    if strike is not None:
        if strike == 'all':
            sx0, sx1 = bb[0], bb[2]
        else:
            pre = s[:s.index(strike)]
            sx0 = x + d.textlength(pre, font=f); sx1 = sx0 + d.textlength(strike, font=f)
        ym = (bb[1] + bb[3]) / 2 + 6
        pen(d, [(sx0 - 6, ym + 3), (sx1 + 6, ym - 5)], w=4)
        pen(d, [(sx0 - 4, ym - 4), (sx1 + 4, ym - 9)], w=3, passes=1)
    return bb


def scientist(d, x, y, hair_up=True):
    """lab-coat woman, ballpoint sketch, ~240 px tall"""
    pcirc(d, x, y + 30, 26)
    if hair_up:
        pcirc(d, x + 4, y - 2, 13)                                     # bun
    else:
        pen(d, [(x - 26, y + 26), (x - 32, y + 70)], passes=1); pen(d, [(x + 26, y + 26), (x + 32, y + 70)], passes=1)   # long hair
    pen(d, [(x - 8, y + 56), (x - 8, y + 70)], passes=1); pen(d, [(x + 8, y + 56), (x + 8, y + 70)], passes=1)  # neck
    pen(d, [(x - 40, y + 76), (x + 40, y + 76), (x + 52, y + 200), (x - 52, y + 200), (x - 40, y + 76)])        # coat
    pen(d, [(x, y + 76), (x - 6, y + 200)], passes=1)                                                            # coat opening
    pen(d, [(x - 22, y + 76), (x, y + 104), (x + 22, y + 76)], passes=1)                                         # lapels
    prect(d, x + 14, y + 120, x + 34, y + 134, passes=1)                                                         # pocket
    pen(d, [(x - 40, y + 82), (x - 62, y + 160), (x - 50, y + 166)])                                             # arms
    pen(d, [(x + 40, y + 82), (x + 64, y + 150), (x + 52, y + 156)])
    pen(d, [(x - 22, y + 200), (x - 24, y + 250)]); pen(d, [(x + 22, y + 200), (x + 24, y + 250)])               # legs


def cell(d, x, y, r):
    pcirc(d, x, y, r); pcirc(d, x + r * 0.15, y - r * 0.1, r * 0.32)
    for k in range(7):
        a = random.uniform(0, 6.28); rr = random.uniform(r * 0.45, r * 0.8)
        pcirc(d, x + rr * math.cos(a), y + rr * math.sin(a), 4, passes=1)


PLANTS = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma/video-brand-story-drawn/sketch_scenes/09_plants.png")
_PL = {}


def _trace(sk):
    """skeleton pixels -> ordered polylines"""
    N8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    pts = set(zip(*_np.where(sk)))
    deg = lambda p: sum((p[0] + a, p[1] + b) in pts for a, b in N8)
    paths = []
    while pts:
        ends = [p for p in pts if deg(p) <= 1]
        cur = min(ends) if ends else min(pts)
        path = [cur]; pts.discard(cur); d0 = (0, 0)
        while True:
            nb = [(cur[0] + a, cur[1] + b) for a, b in N8 if (cur[0] + a, cur[1] + b) in pts]
            if not nb: break
            nxt = max(nb, key=lambda q: (q[0] - cur[0]) * d0[0] + (q[1] - cur[1]) * d0[1] - 0.3 * abs(q[0] - cur[0]) * abs(q[1] - cur[1]))
            d0 = (nxt[0] - cur[0], nxt[1] - cur[1]); pts.discard(nxt); path.append(nxt); cur = nxt
        if len(path) >= 7: paths.append(path)
    return paths


def plant_sketch(d, cx, cy, h, i):
    """dish i (0 pineapple, 1 garlic, 2 wheat, 3 radish): the pen sketch's line work traced, then drawn with this notebook's ballpoint"""
    from skimage.morphology import skeletonize
    if 'flat' not in _PL:
        im = _cv2.cvtColor(_cv2.imread(PLANTS), _cv2.COLOR_BGR2RGB)
        sm = _cv2.resize(im, (im.shape[1] // 4, im.shape[0] // 4), interpolation=_cv2.INTER_AREA)
        bg = _cv2.resize(_cv2.medianBlur(sm, 31), (im.shape[1], im.shape[0]), interpolation=_cv2.INTER_CUBIC).astype(_np.float32)
        _PL['flat'] = _np.clip(im.astype(_np.float32) / _np.maximum(bg, 1) * 255, 0, 255).mean(2)
    x0, y0, x1, y1 = [(26, 1193, 392, 1613), (406, 1199, 776, 1601), (765, 1128, 1160, 1604), (1144, 1159, 1503, 1610)][i]
    lum = _PL['flat'][y0:y1, x0:x1]
    from scipy import ndimage as _nd
    ink = (255 - lum) > (52 if i == 0 else 70)
    ink = _nd.binary_opening(ink, iterations=1)
    lab, n = _nd.label(_nd.binary_dilation(ink, iterations=3)); sz = _nd.sum(ink, lab, range(1, n + 1))
    edge = set(_np.unique(_np.r_[lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    keep = [k + 1 for k in range(n) if sz[k] >= 40 and (k + 1 not in edge or sz[k] == sz.max())]
    ink &= _np.isin(lab, keep)                                              # this dish and what is in it, not the neighbours
    s = h / ink.shape[0]
    im = _img(d); bx, by = cx - ink.shape[1] * s / 2, cy - h / 2
    if i == 0:                                                              # pineapple flesh: light yellow felt-tip, like the other coloured bits
        marker_fill(d, lambda md: md.ellipse((cx + 7 - h * 0.25, cy - 6 - h * 0.25, cx + 7 + h * 0.25, cy - 6 + h * 0.25), fill=255) or md.ellipse((cx + 7 - h * 0.07, cy - 6 - h * 0.07, cx + 7 + h * 0.07, cy - 6 + h * 0.07), fill=0), (252, 230, 150), gap=9)
    for path in _trace(skeletonize(ink)):
        q = [(bx + p[1] * s, by + p[0] * s) for p in path[::2]] + [(bx + path[-1][1] * s, by + path[-1][0] * s)]
        _pen_raw(im, q, w=2, passes=1)


def pineapple(d, x, y, r):      # cross-section slice: rind ring, eyes, core, radial fibres
    pcirc(d, x, y, r * 0.92, w=3); pcirc(d, x, y, r * 0.78, passes=1)
    for k in range(14):
        a = k * 6.283 / 14; pcirc(d, x + r * 0.85 * math.cos(a), y + r * 0.85 * math.sin(a), 3, passes=1)
    pcirc(d, x, y, r * 0.2, passes=1)
    for k in range(12):
        a = k * 6.283 / 12; pline(d, (x + r * 0.22 * math.cos(a), y + r * 0.22 * math.sin(a)), (x + r * 0.74 * math.cos(a), y + r * 0.74 * math.sin(a)), passes=1)
def garlic(d, x, y, r):         # bulb with cloves, papery tip and roots
    pen(d, [(x, y - r * 0.85), (x - r * 0.15, y - r * 0.55), (x - r * 0.7, y - r * 0.1), (x - r * 0.62, y + r * 0.5), (x, y + r * 0.62), (x + r * 0.62, y + r * 0.5), (x + r * 0.7, y - r * 0.1), (x + r * 0.15, y - r * 0.55), (x, y - r * 0.85)])
    for dx in (-0.38, 0, 0.38):
        pen(d, [(x + dx * r * 0.4, y - r * 0.5), (x + dx * r, y), (x + dx * r * 0.6, y + r * 0.58)], passes=1)
    for k in range(-3, 4): pline(d, (x + k * 6, y + r * 0.62), (x + k * 9, y + r * 0.85), passes=1, w=2)
def wheat(d, x, y, r):          # ear of wheat: stem, alternating grains, awns
    pen(d, [(x, y + r * 0.9), (x + 2, y - r * 0.75)])
    for k in range(6):
        yy = y + r * 0.35 - k * r * 0.2
        for sgn in (-1, 1):
            gx = x + sgn * 11
            pen(d, [(x, yy + 6), (gx, yy - 4), (gx - sgn * 3, yy - 16), (x, yy - 8)], passes=1)
            pline(d, (gx - sgn * 3, yy - 16), (gx + sgn * 6, yy - 40), passes=1, w=1)
def radish(d, x, y, r):         # round root, tail root, three leaves with veins
    pcirc(d, x, y + r * 0.2, r * 0.42); pen(d, [(x + 2, y + r * 0.62), (x + 6, y + r * 0.95)], passes=1)
    for ang in (-35, 0, 35):
        a = math.radians(ang - 90); tx, ty = x + r * 0.8 * math.cos(a), y - r * 0.2 + r * 0.8 * math.sin(a)
        pen(d, [(x, y - r * 0.2), ((x + tx) / 2 - 8, (y - r * 0.2 + ty) / 2), (tx, ty), ((x + tx) / 2 + 8, (y - r * 0.2 + ty) / 2), (x, y - r * 0.2)], passes=1)
        pline(d, (x, y - r * 0.2), (tx, ty), passes=1, w=1)
    marker_fill(d, lambda md: md.ellipse((x - r * 0.42, y - r * 0.22, x + r * 0.42, y + r * 0.62), fill=255), (230, 110, 150), gap=6)


def drone(d, x, y, s=1.0):
    pline(d, (x - 60 * s, y), (x + 60 * s, y))
    for dx in (-60 * s, 60 * s):
        pline(d, (x + dx, y), (x + dx, y - 16 * s), passes=1); pline(d, (x + dx - 20 * s, y - 16 * s), (x + dx + 20 * s, y - 16 * s), passes=1)
    prect(d, x - 28 * s, y + 24 * s, x + 28 * s, y + 64 * s, passes=1); pen(d, [(x - 28 * s, y + 24 * s), (x, y + 46 * s), (x + 28 * s, y + 24 * s)], passes=1)


def snow(d, x, y, r):
    for a in range(0, 180, 60):
        q = math.radians(a); pline(d, (x - r * math.cos(q), y - r * math.sin(q)), (x + r * math.cos(q), y + r * math.sin(q)), passes=1)


SILVER = (178, 184, 196)


def capsule(d, x, y, col, h, wd):
    """pill: coloured chrome cap = exact upper half, mirror-silver lower half, both ends round"""
    r = wd / 2
    marker_fill(d, lambda md: md.rounded_rectangle((x + 2, y + 2, x + wd - 2, y + h // 2 + r), int(r), fill=255) or md.rectangle((x, y + h // 2, x + wd, y + h), fill=0), col, gap=6)
    marker_fill(d, lambda md: md.rounded_rectangle((x + 2, y + h // 2 - r, x + wd - 2, y + h - 2), int(r), fill=255) or md.rectangle((x, y, x + wd, y + h // 2), fill=0), SILVER, angle=-35, gap=9)
    out = [(x + r + r * math.cos(math.pi + math.pi * k / 24), y + r + r * math.sin(math.pi + math.pi * k / 24)) for k in range(25)] + \
          [(x + r + r * math.cos(math.pi * k / 24), y + h - r + r * math.sin(math.pi * k / 24)) for k in range(25)] + [(x, y + r)]
    pen(d, out, w=3)
    pline(d, (x + 1, y + h // 2), (x + wd - 1, y + h // 2), passes=1)
    pline(d, (x + wd * 0.26, y + h * 0.12), (x + wd * 0.26, y + h * 0.4), passes=1, w=2, col=(255, 255, 255))     # chrome glint
    pline(d, (x + wd * 0.26, y + h * 0.6), (x + wd * 0.26, y + h * 0.88), passes=1, w=2, col=(255, 255, 255))


def tube(d, x, y, col, h, wd):
    """DropOff: matte squeeze tube standing on its cap, crimped flat seal on top, no stripe"""
    ct = h * 0.1; cw = wd * 0.6; top = wd * 1.2
    cx = x + wd / 2
    body = [(cx - top / 2, y + 12), (cx + top / 2, y + 12), (cx + wd * 0.47, y + h * 0.3), (cx + wd * 0.36, y + h * 0.72), (cx + cw / 2 + 1, y + h - ct), (cx - cw / 2 - 1, y + h - ct), (cx - wd * 0.36, y + h * 0.72), (cx - wd * 0.47, y + h * 0.3)]
    marker_fill(d, lambda md: md.polygon(body, fill=255), col, gap=6)
    marker_fill(d, lambda md: md.rounded_rectangle((cx - cw / 2, y + h - ct, cx + cw / 2, y + h), 6, fill=255), col, gap=5)
    pen(d, body + [body[0]])
    prect(d, cx - top / 2, y, cx + top / 2, y + 12, passes=1)                                 # crimp
    for k in range(4): pline(d, (cx - top / 2 + 6 + k * (top - 12) / 3, y + 2), (cx - top / 2 + 6 + k * (top - 12) / 3, y + 10), passes=1, w=1)
    prect(d, cx - cw / 2, y + h - ct, cx + cw / 2, y + h, passes=1)                           # cap


def star(d, x, y, r):
    pts = [(x + r * math.cos(math.radians(-90 + k * 36)) * (1 if k % 2 == 0 else 0.45), y + r * math.sin(math.radians(-90 + k * 36)) * (1 if k % 2 == 0 else 0.45)) for k in range(11)]
    pen(d, pts)


def dish_layer():
    """the four plant dishes, pre-drawn on page 2 (white ink layer)"""
    st = random.getstate(); random.seed(77)
    im = Image.new('RGB', (SW, SH), (255, 255, 255)); d = ImageDraw.Draw(im)
    for i in range(4): plant_sketch(d, 1160 + i * 220, 272, 190, i)
    txt(d, 1080, 148, '02 / APPLICATION', 40)
    random.setstate(st)
    return im


def base():
    im = Image.new('RGB', (SW, SH), (238, 239, 240))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((30, 40, SW - 30, SH - 20), 18, fill=(250, 250, 250), outline=(225, 225, 228), width=3)
    for j, (x0, x1) in enumerate((PL, PR)):
        d.rectangle((x0, 60, x1, SH - 40), fill=(253, 252, 248))
        for x in range(x0 + 20, x1 - 10, 28): d.line((x, PT - 20, x, PB), fill=GRID)
        for y in range(PT - 20, PB, 28): d.line((x0 + 20, y, x1 - 20, y), fill=GRID)
        d.text((x0 + 24, 80), 'LAB NOTEBOOK', font=GROT(28), fill=GREY)
        d.text((x1 - 300, 80), 'PROJECT: SICKSCIENCE', font=GROT(24), fill=GREY)
    d.line((1020, 50, 1020, SH - 30), fill=(215, 215, 218), width=6)
    return im


# ---------------- left page: the researchers (00-64 s) ----------------
def L01(d): txt(d, 110, 148, '01 / ORIGIN', 40)
def L02(d): kw('minds'); scientist(d, 175, 225, True); scientist(d, 345, 225, False)
def L03(d):
    txt(d, 118, 485, 'Polen', 40); txt(d, 296, 485, 'Merve', 40)
    txt(d, 585, 200, '2009', 96, hl=YEL, bold=True)
def L04(d):
    arrow(d, (520, 425), (930, 425)); txt(d, 520, 435, '2009', 30); txt(d, 870, 435, '2023', 30)
    txt(d, 520, 325, '14 YEARS', 72, hl=YEL, bold=True)
def L05(d):
    kw('phds')
    for k, x in enumerate((112, 196)):
        prect(d, x, 560, x + 70, 610); pcirc(d, x + 50, 600, 10, passes=1)        # diplomas
    marker_text(d, 290, 566, 'PhD ×2', 46, INK, lambda z: ImageFont.truetype(os.path.join(R, '..', 'fonts', 'Kalam-Regular.ttf'), z))
def L05b(d):
    txt(d, 560, 515, 'Merve: plant exosomes · cancer', 36)


def L06(d):
    cell(d, 175, 705, 58)
    pcirc(d, 400, 705, 40); arrow(d, (448, 680), (470, 720)); arrow(d, (360, 735), (338, 690))
    for k in range(6): pcirc(d, 630 + (k % 3) * 30, 680 + (k // 3) * 32, 9, passes=1)
    txt(d, 110, 780, 'stem cells', 34); txt(d, 320, 780, 'regenerative med.', 34); txt(d, 600, 780, 'exosomes · cancer', 34)
def L07(d):
    kw('dozens')
    for k in range(3): d.rectangle((210 + k * 14, 849 + k * 10, 278 + k * 14, 933 + k * 10), fill=(253, 252, 248)); prect(d, 210 + k * 14, 849 + k * 10, 278 + k * 14, 933 + k * 10, passes=1)
    txt(d, 340, 862, 'DOZENS OF STUDIES', 56, hl=YEL, bold=True)
def L08(d):
    kw('mother'); bb = txt(d, 110, 975, 'for mom', 40); hx, hy = bb[2] + 22, (bb[1] + bb[3]) / 2 + 4
    pen(d, [(hx, hy + 9), (hx - 10, hy), (hx - 11, hy - 6), (hx - 7, hy - 10), (hx - 2, hy - 9), (hx, hy - 5), (hx + 2, hy - 9), (hx + 7, hy - 10), (hx + 11, hy - 6), (hx + 10, hy), (hx, hy + 9)], w=2)
    kw(None); txt(d, 322, 979, 'preclinical', 36); pline(d, (322, 1027), (542, 1027), passes=1)
def L09(d):
    kw('published'); prect(d, 640, 962, 706, 1046)
    for k in range(4): pline(d, (652, 982 + k * 16), (694, 982 + k * 16), passes=1)
    txt(d, 726, 972, 'published', 40); check(d, 896, 1002)
def L10(d): txt(d, 110, 1082, 'in the lab', 60, strike='lab')
def L11(d): marker_text(d, 410, 1060, 'at home', 84, font=GOCHI); highlighter(d, (410, 1077, 640, 1132))
def L12(d): cell(d, 195, 1295, 78); txt(d, 330, 1182, 'exosomes', 44)
def L13(d):
    d.ellipse((376, 1291, 384, 1299), fill=INK); arrow(d, (462, 1258), (392, 1289))
    txt(d, 500, 1218, '1/1000', 76, hl=YEL, bold=True)
    kw('between'); cell(d, 845, 1350, 34); kw(None); txt(d, 470, 1376, 'coded messages', 28)          # said in this line: "coded messages between cells"
def L14(d): kw('drones'); drone(d, 580, 1318, 0.62); kw('carrying'); arrow(d, (660, 1350), (790, 1350), dotted=True)


# ---------------- right page: platform + brand (64-114 s) ----------------
FIGS = [('PINEAPPLE', pineapple), ('GARLIC', garlic), ('WHEAT', wheat), ('RADISH', radish)]
PETRI_PRINTS = False


def R01(d):
    # the page title is already on page 2 with the dishes (dish_layer); drawn here on a scratch sheet only so the
    # random hand-jitter sequence of every later mark stays exactly as before
    txt(ImageDraw.Draw(Image.new('RGB', (SW, SH), (255, 255, 255))), 1080, 148, '02 / APPLICATION', 40)
    for i, (nm, fn) in enumerate(FIGS):
        x = 1160 + i * 220
        bw = d.textlength(nm, font=BIRO(34)); txt(d, x - bw / 2, 386, nm, 34)      # dishes are already on the page (dish_layer); only the names are written
def R02(d):
    for i in range(4): pline(d, (1160 + i * 220, 440), (1290, 474), passes=1)
    txt(d, 1430, 540, '100% plant-based · vegan', 38)
def R03(d): txt(d, 1080, 500, 'NX35', 112, hl=YEL, bold=True)
def R04(d):
    for i, s in enumerate(['SEPARATION', 'STABILIZATION', 'LIBRARY']):
        x = 1080 + i * 292
        prect(d, x, 646, x + 252, 712)
        tb = d.textbbox((0, 0), s, font=BIRO(36)); txt(d, x + 126 - (tb[0] + tb[2]) / 2, 679 - (tb[1] + tb[3]) / 2, s, 36)
        if i < 2: arrow(d, (x + 256, 679), (x + 288, 679))
    txt(d, 1080, 724, 'biomimetic', 34)
def R05(d):
    kw('cold'); snow(d, 1330, 772, 24); pline(d, (1298, 802), (1362, 742), w=4)
    txt(d, 1390, 750, 'ROOM TEMPERATURE', 40)
def R06(d):
    kw('laboratory'); x, y = 1100, 850
    pen(d, [(x - 6, y), (x + 66, y), (x + 62, y + 6), (x + 62, y + 80), (x - 2, y + 80), (x - 2, y + 6), (x - 6, y)])   # beaker with lip
    for k in range(4): pline(d, (x + 4, y + 20 + k * 14), (x + 18, y + 20 + k * 14), passes=1, w=1)
    marker_fill(d, lambda md: md.rectangle((x, y + 44, x + 60, y + 78), fill=255), (200, 215, 235), gap=6)
    kw('home'); arrow(d, (1200, 890), (1290, 890))
    pen(d, [(1312, 875), (1352, 875), (1352, 935), (1312, 935), (1312, 875)]); pen(d, [(1326, 875), (1326, 857), (1338, 857), (1338, 875)], passes=1); pen(d, [(1332, 857), (1332, 847), (1352, 847)], passes=1)
    txt(d, 1390, 857, 'LAB', 58, hl=YEL, bold=True); arrow(d, (1510, 890), (1590, 890)); txt(d, 1610, 857, 'HOME', 58, hl=YEL, bold=True)
def R07(d): txt(d, 1080, 972, 'scientist?', 58, strike='all'); arrow(d, (1350, 1007), (1440, 1007)); txt(d, 1460, 972, 'marketer.', 58)
def R08(d):
    kw('data')
    for k, h in enumerate([20, 38, 30, 56]): prect(d, 1090 + k * 26, 1132 - h, 1110 + k * 26, 1132, passes=1)
    kw(None)                                       # v31 (user): the quote is written as "That's sick" is spoken, not with the data bars
    txt(d, 1220, 1052, '"THAT\'S SICK!"', 80, bold=True)
def R09(d): txt(d, 1080, 1168, "No, that's science.", 52); marker_text(d, 1500, 1142, 'SickScience', 96, VIO, GOCHI)
def R10(d):
    # no product line-up (the range will grow): a dropper lets one drop fall, research -> home
    kw('research'); k = 0.55; x, y = 1130, 1282
    P = lambda pts: [(x + a * k, y + b * k) for a, b in pts]
    pen(d, P([(-14, 0), (14, 0), (14, 26), (-14, 26), (-14, 0)]))
    pen(d, P([(-12, 0), (-16, -22), (-8, -40), (8, -40), (16, -22), (12, 0)]))
    pen(d, P([(-7, 26), (-5, 110), (0, 122), (5, 110), (7, 26)]))
    pen(d, P([(0, 140), (-9, 156), (-7, 168), (0, 172), (7, 168), (9, 156), (0, 140)]))
    pcirc(d, x, y + 205 * k, 18, passes=1)
    arrow(d, (x + 40, y + 70), (x + 120, y + 70))
    kw('home'); hx, hy = x + 190, y + 20
    pen(d, [(hx - 40, hy + 24), (hx, hy - 12), (hx + 40, hy + 24)]); prect(d, hx - 32, hy + 20, hx + 32, hy + 80)
    pen(d, [(hx - 8, hy + 80), (hx - 8, hy + 54), (hx + 8, hy + 54), (hx + 8, hy + 80)], passes=1)
    txt(d, x + 250, y + 30, 'bring it home', 40)


def R11(d): kw('fourteen'); star(d, 1662, 1322, 24); kw(None); txt(d, 1700, 1300, '14 AWARDS', 52, hl=YEL, bold=True); txt(d, 1700, 1362, 'TODAY · NewBeauty · Beacon', 26)


BEATS = [  # (time, page side, fns, narration) — v5 storytelling script (chatgpt-v5-answer.md + user edit 2026-11-07)
    ('0:00', 'W', [], "This story didn't begin with skincare."),
    ('0:03', 'L', [L01, L02], 'It began with two curious minds.'),
    ('0:06', 'L', [L03], 'In 2009, Polen and Merve met in a chemistry and biology class. And they kept working together!'),
    ('0:14', 'L', [L05, L07], 'Both earned PhDs, and led dozens of studies'),
    ('0:17', 'L', [L06], 'on stem cells, regenerative medicine, and plant-derived exosomes in cancer research.'),
    ('0:24', 'L', [], "Then the science became personal. Merve's mother was living with mesothelioma."),
    ('0:29', 'L', [L08], 'No treatment was available to her. Their research was still preclinical. Merve lost her mother.'),
    ('0:36', 'L', [L09], 'They finished the research, and published it.'),
    ('0:39', 'L', [L10, L11], "But one thought stayed: science shouldn't end behind laboratory doors."),
    ('0:44', 'L', [L12], 'Their next chapter centered on exosomes.'),
    ('0:47', 'L', [L14, L13], 'Tiny delivery drones, a thousand times smaller than cells, carrying coded messages between them.'),
    ('0:54', 'R', [R01], 'Their sources? They tested thousands of plants, such as pineapple, garlic, wheat, and radish.'),
    ('0:58', 'R', [R02], 'An entirely plant-based, vegan approach.'),
    ('1:01', 'R', [R03], 'Then came NX35.'),
    ('1:03', 'R', [R04], 'Their biomimetic platform to isolate exosomes, stabilize them at room temperature, and use their own plant libraries.'),
    ('1:10', 'R', [R05], 'No cold chain needed.'),
    ('1:12', 'R', [R06], 'The distance from laboratory to home was getting smaller.'),
    ('1:16', 'R', [R07], 'They chose skincare. In an industry crowded with science claims, they wanted real research behind the formulas.'),
    ('1:24', 'R', [R08], "A beauty executive saw their data. That's sick!"),
    ('1:28', 'R', [R09], "Their answer? No, that's science. And SickScience was born."),
    ('1:33', 'R', [R10], 'Their formulas bring that research home.'),
    ('1:40', 'R', [R11], 'Fourteen awards and counting, including the TODAY Show, NewBeauty, and the Beacon Awards.'),
    ('1:48', 'W', [], 'Two geneticists. One decision: bring science into everyday life. SickScience. Science, but never boring.'),
]


def page_view(sp, side):
    pc = (PL[0] + PL[1]) / 2 - 8 if side == 'L' else (PR[0] + PR[1]) / 2 - 8
    return sp.crop((int(pc - 416), 0, int(pc + 416), SH)).resize((540, 960))


def wide(sp, head, sub, note, col=INK):
    P = Image.new('RGB', (540, 960), (245, 245, 246)); d = ImageDraw.Draw(P)
    P.paste(sp.resize((540, int(540 * SH / SW))), (0, 300))
    f = GROT(38); tw = d.textlength(head, font=f); d.text(((540 - tw) / 2, 150), head, font=f, fill=INK)
    f2 = BIRO(40); tw = d.textlength(sub, font=f2); d.text(((540 - tw) / 2, 205), sub, font=f2, fill=col)
    for i, ln in enumerate(note): d.text((40, 740 + i * 32), ln, font=GROT(24), fill=GREY)
    return P


def main():
    final = base(); fd = ImageDraw.Draw(final)
    random.seed(11)
    for _, _, fns, _ in BEATS:
        for fn in fns: fn(fd)
    final.save(os.path.join(R, 'spread_v4f.png'))
    random.seed(11)
    sp = base(); d = ImageDraw.Draw(sp); panels = []
    for t, side, fns, nar in BEATS:
        for fn in fns: fn(d)
        if side == 'W':
            P = wide(final, 'FOR THE FIRST TIME', 'the SickScience story', ['finished spread first,', 'then cut to the empty page']) if t == '0:00' else \
                wide(final, 'SICK SCIENCE', 'Science, but never boring.', ['pull back to the wide spread,', 'the real 4 products on the bench'], VIO)
        else:
            P = page_view(sp, side)
        panels.append((t, nar, P))
    cols = 9; cw, ch, cap = 220, 391, 180
    rows = math.ceil(len(panels) / cols)
    sheet = Image.new('RGB', (cols * (cw + 10) + 10, rows * (ch + cap + 10) + 10), 'white'); sd = ImageDraw.Draw(sheet)
    for i, (t, nar, p) in enumerate(panels):
        x = 10 + (i % cols) * (cw + 10); y = 10 + (i // cols) * (ch + cap + 10)
        sheet.paste(p.resize((cw, ch)), (x, y)); sd.rectangle((x, y, x + cw - 1, y + ch - 1), outline=(200, 200, 205))
        sd.text((x, y + ch + 6), t, font=GROT(22), fill=VIO)
        f = GROT(16); words, line, ly = nar.split(), '', y + ch + 34
        for wd in words:
            tt = (line + ' ' + wd).strip()
            if sd.textlength(tt, font=f) > cw - 6: sd.text((x, ly), line, font=f, fill=INK); ly += 20; line = wd
            else: line = tt
        sd.text((x, ly), line, font=f, fill=INK)
    sheet.save(os.path.join(R, 'storyboard_v4f.jpg'), quality=90)
    print('ok', len(panels))


if __name__ == '__main__':
    main()
