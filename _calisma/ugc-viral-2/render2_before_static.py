"""All UGC viral re-edits (2026-11-06), per Buzzfy playbook: open on the peak (no greeting), one claim line on top for ~2 s,
burned word captions on raw talking (2–3 words, bold, one colour), tight cuts on word gaps, ≤20 s, no logo end card.
Sources read straight from the client Drive folder (srcmap.py); nothing copied. Creator fat/lipid lines are never used."""
import os, sys, math, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageChops
from srcmap import SRC
from edits import E, BIG, FUN, METAL, STYLE, CHIPS, INSERTS, MUSIC, SYNTH
import shutil, tempfile
from PIL import ImageFilter
from resolve import resolve
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
ACC = {'ss': (196, 120, 255), 'nw': (255, 96, 108), 'pc': (96, 222, 132), 'do': (96, 154, 255)}
ROOT = os.path.dirname(os.path.abspath(__file__)); OUT = f'{ROOT}/out'; os.makedirs(OUT, exist_ok=True)
FB = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Bold.otf')
W, H, FPS, SR = 1080, 1920, 30, 48000
PURPLE = (169, 33, 192)
FIX = {'sixscience': 'SickScience', 'sixsciences': "SickScience's", 'sixsigns': 'SickScience',
       'shapeshift': 'ShapeShift', 'network': 'NetWork', 'powercycle': 'PowerCycle', 'dropoff': 'DropOff', 'drop-off': 'DropOff', 'nx35': 'NX35'}
_fc = {}
def font(s):
    if s not in _fc: _fc[s] = ImageFont.truetype(FB, s)
    return _fc[s]
def sh(c): subprocess.run(c, shell=True, check=True, capture_output=True)

def hook_img(lines):
    f = font(104); lh = 118; d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    bb = [d0.textbbox((0, 0), l, font=f) for l in lines]; top0 = bb[0][1]; bot = (len(lines) - 1) * lh + bb[-1][3]
    wmax = int(max(d0.textlength(l, font=f) for l in lines) + 84); hh = int(bot - top0 + 64)
    card = Image.new('RGBA', (wmax, hh), (0, 0, 0, 0)); cd = ImageDraw.Draw(card)
    cd.rounded_rectangle([0, 0, wmax - 1, hh - 1], radius=34, fill=(255, 255, 255, 250))
    for i, l in enumerate(lines):
        tw = cd.textlength(l, font=f); cd.text(((wmax - tw) / 2, 32 - top0 + i * lh), l, font=f, fill=(20, 20, 24) if i < len(lines) - 1 else PURPLE)
    card = card.rotate(-3, expand=True, resample=Image.BICUBIC)
    if card.width > 960: card = card.resize((960, int(card.height * 960 / card.width)), Image.LANCZOS)
    return card

def fixw(w):
    k = w.lower().replace('-', '').replace(' ', '').rstrip(',.?!')
    for a, b in FIX.items():
        if k == a.replace('-', ''): return b + w[len(w.rstrip(',.?!')):]
    return w.replace(' -', '-').replace('- ', '-')

_cc = {}
def cap_img(txt):
    if txt in _cc: return _cc[txt]
    f = font(76); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1))); tw = d0.textlength(txt, font=f)
    im = Image.new('RGBA', (int(tw) + 80, 150), (0, 0, 0, 0))
    shd = Image.new('RGBA', im.size, (0, 0, 0, 0)); ImageDraw.Draw(shd).text((40, 38), txt, font=f, fill=(0, 0, 0, 200), stroke_width=3, stroke_fill=(0, 0, 0, 200))
    im = Image.alpha_composite(im, shd.filter(ImageFilter.GaussianBlur(7)))
    d = ImageDraw.Draw(im); d.text((40, 34), txt, font=f, fill=(255, 255, 255), stroke_width=1, stroke_fill=(30, 30, 30))
    if im.width > 1000: im = im.resize((1000, int(im.height * 1000 / im.width)), Image.LANCZOS)
    _cc[txt] = im; return im

WFIX = {'11': {"cargo's": 'cargo'}, '01': {'shapelift': 'ShapeShift', 'v': 'V-Line'}, '02': {'liposurum': 'lipo-serum'}}
def clean(words, k):
    out = []
    for a, b, w in words:
        w = w.strip()
        if not w: continue
        lw = w.lower().rstrip(',.?!')
        if out and (w.startswith('-') or w.startswith("'")):
            out[-1] = (out[-1][0], b, out[-1][2] + w); continue
        if out and lw in ('science', 'sciences', 'signs', 'science.') and out[-1][2].lower() in ('six', 'sick', 'sake', 'stick'):
            out[-1] = (out[-1][0], b, 'SickScience' + ("'s" if lw.endswith('s') and lw != 'signs' else '') + w[len(w.rstrip(',.?!')):]); continue
        if out and w.startswith('.') and out[-1][2] == '6': out[-1] = (out[-1][0], b, '6:30AM'); continue
        pl = out[-1][2].lower() if out else ''
        if (pl, lw) in (('power', 'cycle'), ('drop', 'off'), ('shape', 'shifts'), ('shape', 'shift')):
            out[-1] = (out[-1][0], b, {'power': 'PowerCycle', 'drop': 'DropOff', 'shape': 'ShapeShift'}[pl] + w[len(w.rstrip(',.?!')):]); continue
        w = WFIX.get(k, {}).get(lw, None) or w
        out.append((a, b, fixw(w)))
    return out

def groups(words):
    gs, cur = [], []
    for j, w in enumerate(words):
        cur.append(w); nxt = words[j + 1] if j + 1 < len(words) else None
        brk = nxt is None or w[2][-1:] in ',.?!' or nxt[0] - w[1] > 0.3 or len(cur) == 4 or (len(cur) == 3 and len(' '.join(x[2] for x in cur)) > 16)
        if brk:
            if nxt is not None and len(words) > j + 1 and nxt[2][-1:] in '.?!' and len(nxt[2]) <= 3 and len(cur) < 4: continue
            gs.append(cur); cur = []
    if cur: gs.append(cur)
    return gs



def ease(p): p = max(0.0, min(1.0, p)); return 1 - (1 - p) ** 3
def back(p):
    p = max(0.0, min(1.0, p)); c1 = 1.9; c3 = c1 + 1
    return 1 + c3 * (p - 1) ** 3 + c1 * (p - 1) ** 2

def fx(im, style, age, dur=0.3):
    """returns (image, dx, dy) with the entry effect applied at `age` seconds after the word/line appears"""
    p = age / dur
    if p >= 1: return im, 0, 0
    if p < 0: return None, 0, 0
    if style == 'pop':
        s = 0.55 + 0.45 * back(p); al = min(1, p * 4); dx = dy = 0
    elif style == 'blur':
        s = 1.12 - 0.12 * ease(p); al = ease(p); dx = dy = 0
        r = (1 - ease(p)) * 24
        if r > 0.5: im = im.filter(ImageFilter.GaussianBlur(r))
    elif style == 'slide':
        s = 1.0; al = min(1, p * 3); dx = 0; dy = int((1 - ease(p)) * 120)
    elif style == 'spin':
        s = 0.5 + 0.5 * back(p); al = min(1, p * 4); dx = dy = 0
        im = im.rotate((1 - ease(p)) * -34, expand=True, resample=Image.BICUBIC)
    elif style == 'drop':
        s = 1.0; al = min(1, p * 4); dx = 0; dy = int(-(1 - back(p)) * 150)
    else:
        return im, 0, 0
    if abs(s - 1) > 0.01: im = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.BILINEAR)
    if al < 1: im = im.copy(); im.putalpha(im.split()[3].point(lambda v: int(v * al)))
    return im, dx, dy

_wc = {}
def word_img(txt, col):
    k_ = (txt, col)
    if k_ in _wc: return _wc[k_]
    f = font(80); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1))); tw = d0.textlength(txt, font=f)
    im = Image.new('RGBA', (int(tw) + 70, 160), (0, 0, 0, 0))
    shd = Image.new('RGBA', im.size, (0, 0, 0, 0)); ImageDraw.Draw(shd).text((35, 38), txt, font=f, fill=(0, 0, 0, 215), stroke_width=4, stroke_fill=(0, 0, 0, 215))
    im = Image.alpha_composite(im, shd.filter(ImageFilter.GaussianBlur(7)))
    ImageDraw.Draw(im).text((35, 34), txt, font=f, fill=col, stroke_width=1, stroke_fill=(25, 25, 25))
    _wc[k_] = (im, tw); return _wc[k_]

PNGDIR = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/Products/png")
PNGF = {'ss': 'ERH_7470B.png', 'nw': 'ERH_7477C.png', 'pc': 'ERH_7460B.png', 'do': 'ERH_7488.png'}
_pc = {}
def prod_png(pk, h=200):
    if pk not in _pc:
        im = Image.open(f'{PNGDIR}/{PNGF[pk]}').convert('RGBA'); im = im.crop(im.getbbox()); sc = h / im.height
        _pc[pk] = im.resize((max(1, int(im.width * sc)), h), Image.LANCZOS)
    return _pc[pk]

def chip_img(l1, l2, col, pk=None):
    """plain text label (no box/bar/badge) with the real product PNG to its left when the label is a product name"""
    f1 = font(64); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1))); tw = int(d0.textlength(l1, font=f1))
    named = pk and any(n in l1 for n in ('DropOff', 'ShapeShift', 'NetWork', 'PowerCycle'))
    dot = pk and l1 in ('PROTEINS', 'LIPIDS', 'MOLECULES')
    pim = prod_png(pk) if named else None; pw = (pim.width + 22) if pim else (60 if dot else 0)
    H_ = 240 if pim else 130; im = Image.new('RGBA', (tw + pw + 90, H_), (0, 0, 0, 0))
    ty = (H_ - 64) // 2 - 6
    shd = Image.new('RGBA', im.size, (0, 0, 0, 0)); ImageDraw.Draw(shd).text((45 + pw, ty + 4), l1, font=f1, fill=(0, 0, 0, 220), stroke_width=4, stroke_fill=(0, 0, 0, 220))
    if pim:
        a_ = pim.split()[3].point(lambda v: int(v * 0.55)); blk = Image.new('RGBA', pim.size, (0, 0, 0, 255)); blk.putalpha(a_); shd.alpha_composite(blk, (45, (H_ - pim.height) // 2 + 6))
    im = Image.alpha_composite(im, shd.filter(ImageFilter.GaussianBlur(7)))
    if pim: im.alpha_composite(pim, (45, (H_ - pim.height) // 2))
    if dot: ImageDraw.Draw(im).ellipse([45, H_ // 2 - 26, 97, H_ // 2 + 26], fill=PCOL[pk] + (255,), outline=(255, 255, 255, 255), width=4)
    ImageDraw.Draw(im).text((45 + pw, ty), l1, font=f1, fill=(255, 255, 255), stroke_width=1, stroke_fill=(25, 25, 25))
    return im

def stat_img(num, label, col):
    fN = font(210); fL = ImageFont.truetype(FM, 44); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    tw = max(d0.textlength(num, font=fN), d0.textlength(label, font=fL)) + 120
    im = Image.new('RGBA', (int(tw), 360), (0, 0, 0, 0))
    sh_ = Image.new('RGBA', im.size, (0, 0, 0, 0)); ImageDraw.Draw(sh_).rounded_rectangle([10, 16, im.width - 10, 350], radius=44, fill=(0, 0, 0, 80))
    im = Image.alpha_composite(im, sh_.filter(ImageFilter.GaussianBlur(12)))
    d = ImageDraw.Draw(im); d.rounded_rectangle([10, 10, im.width - 10, 340], radius=44, fill=(255, 255, 255, 248))
    d.text(((im.width - d0.textlength(num, font=fN)) / 2, 8), num, font=fN, fill=col)
    d.text(((im.width - d0.textlength(label, font=fL)) / 2, 262), label, font=fL, fill=(30, 30, 34))
    return im

def _tx(d, xy, txt, f, fill, anchor='mm', sh=True):
    if sh: d.text((xy[0], xy[1] + 4), txt, font=f, fill=(0, 0, 0, 40), anchor=anchor)
    d.text(xy, txt, font=f, fill=fill, anchor=anchor)

def make_insert(kind, p):
    """full-bleed white science explainer beat (brand colours only): exosome = delivery truck carrying NX35 cargo between two cells"""
    SSP = (115, 0, 199); INK = (20, 20, 24)
    im = Image.new('RGB', (W, H), (255, 255, 255)); px = im.load()
    top = np.linspace(0, 1, H)[:, None, None]; bg = (np.array([255, 255, 255]) * (1 - top * 0.045) + np.array([240, 232, 250]) * top * 0.045)
    im = Image.fromarray(bg.repeat(W, 1).astype(np.uint8)); d = ImageDraw.Draw(im, 'RGBA')
    pt = ease(p / 0.14)
    _tx(d, (W / 2, 400 - (1 - pt) * 40), 'EXOSOME', font(150), INK + (int(255 * pt),), sh=False)
    _tx(d, (W / 2, 560 - (1 - pt) * 40), '= DELIVERY TRUCK', font(92), SSP + (int(255 * pt),), sh=False)
    cy = 880; lx, rx = 230, 850; r = 150
    arrive = ease((p - 0.68) / 0.12)
    for cx, resp in ((lx, 0.0), (rx, arrive)):
        pulse = 1 + 0.08 * math.sin(max(0, (p - 0.68)) * 20) * resp * (1 - max(0, (p - 0.68)) / 0.3 if cx == rx else 0)
        rr = int(r * (pulse if cx == rx else 1))
        col = (238, 226, 250) if cx == lx else (int(238 - 40 * resp), int(226 - 60 * resp), int(250 - 10 * resp))
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=col + (255,), outline=(90, 90, 100, 255) if cx == lx else (115, 0, 199, 255), width=6)
        d.ellipse([cx - 50, cy - 50, cx + 50, cy + 50], fill=(210, 190, 240, 255) if cx == lx else (int(210 - 95 * resp), int(190 - 190 * resp), int(240 - 41 * resp), 255))
        _tx(d, (cx, cy + r + 54), 'CELL', ImageFont.truetype(FM, 44), INK, sh=False)
    s = ease((p - 0.22) / 0.46)
    ex = lx + 110 + (rx - lx - 220) * s; ey = cy - 190 * math.sin(math.pi * s)
    if 0.2 < p < 0.8:
        for j in range(1, 7):
            sj = max(0, s - j * 0.045); tx_ = lx + 110 + (rx - lx - 220) * sj; ty_ = cy - 190 * math.sin(math.pi * sj)
            d.ellipse([tx_ - 7, ty_ - 7, tx_ + 7, ty_ + 7], fill=SSP + (int(120 - j * 17),))
    if p > 0.18 and not (p > 0.8):
        sc = min(1.0, (p - 0.18) / 0.06) * (1 - ease((p - 0.74) / 0.06) * 0.0)
        R = int(64 * sc)
        d.ellipse([ex - R, ey - R, ex + R, ey + R], fill=SSP + (255,), outline=(255, 255, 255, 255), width=5)
        for (ox, oy, c) in ((-22, -16, (255, 255, 255)), (20, -20, (200, 30, 40)), (-18, 20, (30, 130, 60)), (22, 18, (25, 60, 190))):
            d.ellipse([ex + ox * sc - 11, ey + oy * sc - 11, ex + ox * sc + 11, ey + oy * sc + 11], fill=c + (255,))
        _tx(d, (ex, ey + 92 * sc), 'exosome', ImageFont.truetype(FM, 40), SSP, sh=False)
    if p > 0.76:
        a_ = ease((p - 0.76) / 0.1); f_ = font(84); yy = 1190 - (1 - a_) * 40
        _tx(d, (W / 2, yy), 'MESSAGE DELIVERED', f_, SSP + (int(255 * a_),), sh=False)
    return im


# ---------- Vox-style explainer helpers (spotlight on an object + hand-drawn arrow + label) ----------
HSVR = {'truck': lambda H, S, V: ((H >= 7) & (H <= 24) & (S > 160) & (V > 150)) | ((H >= 150) & (H <= 175) & (S > 70) & (V > 110)),
        'blue': lambda H, S, V: (H >= 135) & (H <= 150) & (S > 90) & (V > 150),
        'pink': lambda H, S, V: (H >= 232) & (H <= 250) & (S > 50) & (V > 170),
        'yellow': lambda H, S, V: (H >= 26) & (H <= 40) & (S > 190) & (V > 190)}
from scipy import ndimage as ndi
def obj_mask(fr, name):
    sm = fr.resize((270, 480), Image.BILINEAR).convert('HSV'); a = np.asarray(sm); m = HSVR[name](a[..., 0].astype(int), a[..., 1].astype(int), a[..., 2].astype(int))
    if name != 'truck': m[int(480 * 0.62):] = False
    lab, n = ndi.label(m)
    if n == 0: return m
    sizes = ndi.sum(m, lab, range(1, n + 1)); keep = 1 + int(np.argmax(sizes))
    out = lab == keep
    if name == 'truck':   # keep other big orange parts of the truck too (windows split it)
        for j in range(1, n + 1):
            if sizes[j - 1] > 0.25 * sizes[keep - 1]: out |= lab == j
    return out

def spot(fr):
    m = obj_mask(fr, 'truck')
    if m.mean() < 0.02: return fr
    mL = Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(13)).filter(ImageFilter.MinFilter(9)).filter(ImageFilter.GaussianBlur(2))
    ring = ImageChops.subtract(mL.filter(ImageFilter.MaxFilter(5)), mL).point(lambda v: min(255, v * 3))
    mF = np.asarray(mL.resize((W, H), Image.BILINEAR)).astype(np.float32)[..., None] / 255
    arr = np.asarray(fr).astype(np.float32) * (0.72 + 0.28 * mF)
    rg = np.asarray(ring.resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(1.2))).astype(np.float32)[..., None] / 255
    arr = arr * (1 - 0.9 * rg) + 255 * 0.9 * rg
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))

def bez(p0, p1, p2, u): return ((1 - u) ** 2 * p0[0] + 2 * (1 - u) * u * p1[0] + u * u * p2[0], (1 - u) ** 2 * p0[1] + 2 * (1 - u) * u * p1[1] + u * u * p2[1])

PINK_KF = [(18.0, 448, 770), (19.0, 448, 790), (19.6, 600, 1280), (20.0, 640, 1300)]
HAND = os.path.expanduser('~/Library/Fonts/Caveat-Bold.ttf')
PINK_BR = (169, 33, 192)   # brand magenta (SickScience 'Science' #A921C0)
def pointer(fr, name, label, age, st, ts=0.0, maskfr=None, style='thin'):
    """highlighter-pen ring around the (tracked) object, a hand-drawn arrow out of it into the empty upper area, handwritten label there"""
    if name == 'pink':
        xk = np.interp(ts, [k_[0] for k_ in PINK_KF], [k_[1] for k_ in PINK_KF]); yk = np.interp(ts, [k_[0] for k_ in PINK_KF], [k_[2] for k_ in PINK_KF])
        st['bb'] = (xk - 70, yk - 70, xk + 70, yk + 70); xs = []
    else:
        m = obj_mask(maskfr if maskfr is not None else fr, name); ys, xs = np.nonzero(m)
    if len(xs) > 25:
        bb = (np.percentile(xs, 3) * 4, np.percentile(ys, 3) * 4, np.percentile(xs, 97) * 4, np.percentile(ys, 97) * 4)
        st['bb'] = bb if 'bb' not in st else tuple(0.55 * o + 0.45 * n for o, n in zip(st['bb'], bb)); st['miss'] = 0
    elif name != 'pink': st['miss'] = st.get('miss', 0) + 1
    if 'bb' not in st or st.get('miss', 0) > 6: return fr
    x0, y0, x1, y1 = st['bb']; cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    big = style == 'big'
    rx = max(70, (x1 - x0) / 2 * (1.12 if big else 1.55) + (30 if big else 38)); ry = max(70, (y1 - y0) / 2 * (1.18 if big else 1.55) + (30 if big else 38))
    # --- highlighter ring (loop with overshoot), multiply-blended so the picture shows through
    prog = ease(age / 0.5); rng = np.random.default_rng(7)
    ph = rng.uniform(0, 6.28, 3); a0 = -2.2
    nn = 90; pts = []
    for j in range(int(nn * prog) + 1):
        u = j / nn; ang = a0 + u * 2 * math.pi * 1.12; wob = 1 + (0.07 if big else 0.045) * math.sin(2 * ang + ph[0]) + 0.03 * math.sin(3 * ang + ph[1]) + 0.015 * math.sin(7 * ang + ph[2]) - 0.06 * u
        pts.append((cx + rx * wob * math.cos(ang), cy + ry * wob * math.sin(ang)))
    ring = Image.new('L', (W, H), 0); dr = ImageDraw.Draw(ring)
    for j_, p_ in enumerate(pts):
        rr_ = (19 + 7 * math.sin(j_ * 0.21 + ph[0])) if big else (7 + 2.5 * math.sin(j_ * 0.3 + ph[1]))
        dr.ellipse([p_[0] - rr_, p_[1] - rr_, p_[0] + rr_, p_[1] + rr_], fill=255)
    ring = ring.filter(ImageFilter.GaussianBlur(1.6))
    a_ = np.asarray(ring).astype(np.float32)[..., None] / 255
    arr = np.asarray(fr.convert('RGB')).astype(np.float32); hl = np.array(PINK_BR, np.float32); al_ = 0.74 if big else 0.95
    arr = arr * (1 - al_ * a_) + hl * (al_ * a_); fr2 = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)).convert('RGBA')
    # --- label placed in the empty upper blocks (left/right of the head), never over the face
    lines = label.split('|'); fs = 150
    f = ImageFont.truetype(HAND, fs); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    while max(d0.textlength(l_, font=f) for l_ in lines) > 300 and fs > 60: fs -= 6; f = ImageFont.truetype(HAND, fs)
    left = cx < 600; bx = 195 if left else 885; by = min(max(cy - 330, 380), 700)
    tw = max(d0.textlength(l_, font=f) for l_ in lines); th = len(lines) * fs * 0.95
    # --- arrow from the ring edge towards the label (drawn after the ring)
    if age > 0.3:
        ap = ease((age - 0.3) / 0.35); ang = math.atan2(by + th / 2 + 26 - cy, bx - cx)
        S = (cx + rx * math.cos(ang), cy + ry * math.sin(ang)); E = (bx + (-1 if not left else 1) * 0, by + th / 2 + 34)
        C = ((S[0] + E[0]) / 2 + (30 if left else -30), (S[1] + E[1]) / 2 + 5)
        lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); n = max(2, int(30 * ap))
        pp = [bez(S, C, E, j / 29 * ap) for j in range(n + 1)]
        for off, col, wd in (((3, 5), (0, 0, 0, 140), 15), ((0, 0), (255, 255, 255, 255), 10)):
            for j in range(len(pp) - 1): d.line([(pp[j][0] + off[0], pp[j][1] + off[1]), (pp[j + 1][0] + off[0], pp[j + 1][1] + off[1])], fill=col, width=wd)
            if ap > 0.95:
                an = math.atan2(E[1] - pp[-4][1], E[0] - pp[-4][0])
                for da in (0.55, -0.55): d.line([(E[0] + off[0], E[1] + off[1]), (E[0] - 44 * math.cos(an + da) + off[0], E[1] - 44 * math.sin(an + da) + off[1])], fill=col, width=wd)
        fr2.alpha_composite(lay)
    # --- handwritten label, revealed left to right like writing
    if age > 0.6:
        wp = ease((age - 0.6) / 0.45); iw, ih = int(tw) + 60, int(th) + 60
        ti = Image.new('RGBA', (iw, ih), (0, 0, 0, 0)); shd = Image.new('RGBA', ti.size, (0, 0, 0, 0))
        for i_, l_ in enumerate(lines):
            ImageDraw.Draw(shd).text((iw / 2, 30 + i_ * fs * 0.95), l_, font=f, fill=(0, 0, 0, 235), anchor='mt', stroke_width=6, stroke_fill=(0, 0, 0, 235))
        ti = Image.alpha_composite(ti, shd.filter(ImageFilter.GaussianBlur(6)))
        for i_, l_ in enumerate(lines): ImageDraw.Draw(ti).text((iw / 2, 30 + i_ * fs * 0.95), l_, font=f, fill=(255, 255, 255), anchor='mt', stroke_width=1, stroke_fill=(20, 20, 20))
        ti = ti.rotate(3 if left else -3, expand=True, resample=Image.BICUBIC)
        msk = Image.new('L', ti.size, 0); ImageDraw.Draw(msk).rectangle([0, 0, int(ti.width * wp), ti.height], fill=255)
        ti.putalpha(ImageChops.multiply(ti.split()[3], msk))
        fr2.alpha_composite(ti, (int(bx - ti.width / 2), int(by + th / 2 - ti.height / 2)))
    return fr2

def mini_cells(fr, age):
    """small looping cell-to-cell animation in the empty upper block (no box): exosome carries NX35 dots from one cell to the other"""
    cx, cy = 900, 340; T = 2.6; u = (age % T) / T; lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    appear = ease(age / 0.35)
    ax, bx_ = cx - 110, cx + 110; yy = cy + 50; R = 70
    act = ease((u - 0.58) / 0.12) * (1 - ease((u - 0.9) / 0.1))
    for x_, ac in ((ax, 0.0), (bx_, act)):
        r_ = int(R * (1 + 0.07 * ac))
        d.ellipse([x_ - r_, yy - r_, x_ + r_, yy + r_], fill=(244, 232, 250, int(235 * appear)), outline=PINK_BR + (int(255 * appear),), width=5)
        nc = (int(205 - 36 * ac), int(160 - 127 * ac), int(228 - 36 * ac))
        d.ellipse([x_ - 25, yy - 25, x_ + 25, yy + 25], fill=nc + (int(255 * appear),))
    s = ease((u - 0.12) / 0.46)
    if 0.1 < u < 0.62:
        ex = ax + 30 + (bx_ - ax - 60) * s; ey = yy - 90 * math.sin(math.pi * s) - 6
        for j in range(1, 6):
            sj = max(0, s - j * 0.05); tx_ = ax + 30 + (bx_ - ax - 60) * sj; ty_ = yy - 90 * math.sin(math.pi * sj) - 6
            d.ellipse([tx_ - 4, ty_ - 4, tx_ + 4, ty_ + 4], fill=PINK_BR + (int(150 - j * 24),))
        d.ellipse([ex - 27, ey - 27, ex + 27, ey + 27], fill=PINK_BR + (255,), outline=(255, 255, 255, 255), width=3)
        for (ox, oy, c) in ((-10, -9, (255, 255, 255)), (10, -10, (200, 30, 40)), (-9, 10, (30, 130, 60)), (10, 9, (25, 60, 190))):
            d.ellipse([ex + ox - 5.5, ey + oy - 5.5, ex + ox + 5.5, ey + oy + 5.5], fill=c + (255,))
    f = ImageFont.truetype(HAND, 92); wp = ease((age - 0.2) / 0.5)
    lab = Image.new('RGBA', (360, 110), (0, 0, 0, 0)); shd = Image.new('RGBA', lab.size, (0, 0, 0, 0))
    ImageDraw.Draw(shd).text((180, 14), 'cells talk', font=f, fill=(0, 0, 0, 230), anchor='mt', stroke_width=5, stroke_fill=(0, 0, 0, 230))
    lab = Image.alpha_composite(lab, shd.filter(ImageFilter.GaussianBlur(5))); ImageDraw.Draw(lab).text((180, 14), 'cells talk', font=f, fill=(255, 255, 255), anchor='mt')
    mk = Image.new('L', lab.size, 0); ImageDraw.Draw(mk).rectangle([0, 0, int(360 * wp), 110], fill=255); lab.putalpha(ImageChops.multiply(lab.split()[3], mk))
    lay.alpha_composite(lab, (cx - 180, yy + R + 8))
    out = fr.convert('RGBA'); out.alpha_composite(lay); return out

SEGVID = os.path.expanduser('~/sickscience-work/tools/segvid')
FM = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Medium.otf')
PK = {k_: v_.get('pk', 'ss') for k_, v_ in E.items()}
BIGY = {'05': 420}
FORCE_FRONT = {'02'}
BIGDUR = {('05', 'BEFORE'): 1.3, ('05', 'AFTER'): 2.0}
VHOLD = {('09', 2): 15.4}
BIGSTART = {('08', 'BEFORE'): 0.0}
PCOL = {'ss': (115, 0, 199), 'nw': (200, 30, 40), 'pc': (30, 130, 60), 'do': (25, 60, 190)}

def envelope(src):
    a = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout
    x = np.frombuffer(a, np.int16).astype(np.float32) / 32768
    n = len(x) // 160; return np.sqrt((x[:n * 160].reshape(n, 160) ** 2).mean(1))   # 10 ms RMS

def snap(env, t):
    """move a word start to where the audio actually gets loud (faster-whisper starts words ~0.1 s early)"""
    i0, i1 = max(0, int((t - 0.06) * 100)), min(len(env) - 1, int((t + 0.22) * 100))
    if i1 <= i0: return t
    seg = env[i0:i1 + 1]; pk = seg.max()
    if pk < 0.01: return t
    j = int(np.argmax(seg > max(0.3 * pk, 0.008)))
    return max(t - 0.06, min(t + 0.22, (i0 + j) / 100))

def big_img(text, color):
    size = 400; f = ImageFont.truetype(FB, size); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    while d0.textlength(text, font=f) > W * 0.85 and size > 60: size -= 6; f = ImageFont.truetype(FB, size)
    l, t, rr, b = d0.textbbox((0, 0), text, font=f); w, h = rr - l, b - t
    pad = 40; im = Image.new('RGBA', (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    sh_ = Image.new('RGBA', im.size, (0, 0, 0, 0)); ImageDraw.Draw(sh_).text((pad - l, pad - t + 6), text, font=f, fill=(0, 0, 0, 90))
    im = Image.alpha_composite(im, sh_.filter(ImageFilter.GaussianBlur(14)))
    ImageDraw.Draw(im).text((pad - l, pad - t), text, font=f, fill=color + (255,))
    return im, h, pad

EMOJI = '/System/Library/Fonts/Apple Color Emoji.ttc'
_em = {}
def emoji_big(e):
    if e not in _em:
        f = ImageFont.truetype(EMOJI, 160); im = Image.new('RGBA', (240, 240), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((20, 20), e, font=f, embedded_color=True); im = im.crop(im.getbbox())
        _em[e] = im.resize((380, int(im.height * 380 / im.width)), Image.LANCZOS)
    return _em[e]

def metal_clang(path):
    sr = 48000; L = 2.2; t = np.arange(int(sr * L)) / sr; out = np.zeros_like(t)
    parts = [(523, 1.0, 1.1), (1347, 0.7, 0.8), (2311, 0.5, 0.6), (3420, 0.35, 0.45), (4870, 0.25, 0.3), (812, 0.5, 0.9)]
    for hit_t, g in [(0.0, 1.0), (0.17, 0.55), (0.29, 0.35), (0.37, 0.2)]:
        tt = t - hit_t; m = tt >= 0
        for f, a_, d_ in parts:
            out[m] += g * a_ * np.sin(2 * np.pi * f * (1 + 0.004 * g) * tt[m]) * np.exp(-tt[m] / (d_ * (0.5 + 0.5 * g)))
        n = np.random.default_rng(1).standard_normal(m.sum()) * np.exp(-tt[m] / 0.01) * 0.6 * g
        out[m] += n
    out = out / np.abs(out).max() * 0.9
    import wave
    st = np.stack([out, out], 1); pcm = (st * 32767).astype(np.int16)
    with wave.open(path, 'wb') as wv: wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(sr); wv.writeframes(pcm.tobytes())

def norm_w(s): return ''.join(c for c in s.lower() if c.isalnum())

def render(k):
    e = E[k]; ws, segs = resolve(k); src = SRC[k]; d = f'{OUT}/{k}'; os.makedirs(d, exist_ok=True)
    segs = [(s, en) for s, en, *_ in segs]
    starts = np.cumsum([0] + [b - a for a, b in segs]); total = float(starts[-1])
    env = envelope(src)
    ws = [(snap(env, w[0]), w[1], w[2]) for w in ws]
    nfrs = [int(round(starts[i + 1] * FPS)) - int(round(starts[i] * FPS)) for i in range(len(segs))]
    f0s = np.cumsum([0] + nfrs)
    def to_out(ts):
        for si_, (a_, b_) in enumerate(segs):
            if a_ <= ts < b_: return float(starts[si_] + ts - a_)
        return float(starts[min(range(len(segs)), key=lambda i: abs(segs[i][0] - ts))])
    PTRS = [(to_out(p_[0]), to_out(p_[1]), p_[2], p_[3], p_[0], (p_[4] if len(p_) > 4 else 'thin')) for p_ in e.get('ptr', [])]
    MINI = [(to_out(a_), to_out(b_)) for (a_, b_) in e.get('mini', [])]
    SPOT = [(to_out(a_), to_out(b_)) for (a_, b_) in e.get('spot', [])]
    if 'srcins' in e: INSERTS[k] = [(to_out(a_), to_out(b_), kd_) for (a_, b_, kd_) in e['srcins']]
    pst = {}

    def seg_frames(si):
        a, b = segs[si]; av = e.get('vstart', {}).get(si, a); z0, z1 = (1.0, 1.0) if not e['zoom'] else ((1.0, 1.05) if si % 2 == 0 else (1.08, 1.08))
        lc = e.get('lcrop', {}).get(si)
        if lc:
            sw, shh = e['srcdim']; vf = f'scale={sw}:{shh}:in_color_matrix=auto,fps={FPS}'; fsz = sw * shh * 3
        else:
            vf = (f"crop={e['crop'][2]}:{e['crop'][3]}:{e['crop'][0]}:{e['crop'][1]}," if e.get('crop') else '') + f'scale={W}:{H}:in_color_matrix=auto:flags=lanczos,fps={FPS}'; fsz = W * H * 3
        dec = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-ss', f'{av}', '-i', src, '-t', f'{b - a + 0.3}', '-vf', vf, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
        last = None
        for kf in range(nfrs[si]):
            hold = VHOLD.get((k, si))
            if last is None or hold is None or av + kf / FPS <= hold:
                buf = dec.stdout.read(fsz)
                if len(buf) == fsz: last = buf
            if lc:
                big_fr = Image.frombuffer('RGB', (sw, shh), last); c0, c1 = lc; cx = (c0 + (c1 - c0) * ease(kf / max(1, nfrs[si] - 1))) * sw; ww = shh * 9 / 16
                x0 = min(max(0, cx - ww / 2), sw - ww); fr = big_fr.resize((W, H), Image.LANCZOS, box=(x0, 0, x0 + ww, shh))
            else:
                fr = Image.frombuffer('RGB', (W, H), last)
            z = z0 + (z1 - z0) * kf / max(1, nfrs[si] - 1)
            if abs(z - 1) > 1e-3:
                cw, ch = W / z, H / z; fr = fr.resize((W, H), Image.BILINEAR, box=((W - cw) / 2, H * 0.42 - ch * 0.42, (W + cw) / 2, H * 0.42 + ch * 0.58))
            yield kf, fr
        dec.stdout.close(); dec.wait()

    # ---- big word behind the head ----
    bigs = []
    for bw in BIG.get(k, []):
        big = None; masks = {}
        text, match, bsi, pk = bw; a, b = segs[bsi]
        cand = [w for w in clean([w for w in ws if a - 0.05 <= w[0] < b], k) if norm_w(w[2]) == norm_w(match)]
        if cand:
            tw = starts[bsi] + cand[0][0] - a
            if (k, text) in BIGSTART: tw = starts[bsi] + BIGSTART[(k, text)]
            fw0 = int(round(tw * FPS)); segend = int(next(f0s[i + 1] for i in range(len(segs)) if f0s[i] <= fw0 < f0s[i + 1])); fw1 = min(segend, fw0 + int(BIGDUR.get((k, text), BIGDUR.get(k, 2.4)) * FPS))
            tmp = tempfile.mkdtemp(prefix=f'big{k}_', dir='/private/tmp/claude-501'); os.makedirs(f'{tmp}/f'); keep = {}
            for si in range(len(segs)):
                if f0s[si + 1] <= fw0 or f0s[si] >= fw1: continue
                for kf, fr in seg_frames(si):
                    g = int(f0s[si]) + kf
                    if fw0 <= g < fw1: fr.save(f'{tmp}/f/{g:05d}.png'); keep[g] = True
            subprocess.run([SEGVID, f'{tmp}/f', f'{tmp}/m'], check=True, capture_output=True)
            for g in keep: masks[g] = Image.open(f'{tmp}/m/{g:05d}.png').convert('L')
            m0 = np.asarray(masks[fw0]); cols = m0[:, int(W * 0.3):int(W * 0.7)]
            rows = np.where(cols.max(1) > 128)[0]
            head = int(rows[0]) if len(rows) else -1
            if True:
                fr0 = Image.open(f'{tmp}/f/{fw0:05d}.png').convert('RGB')
                probe, hT, pad = big_img(text, (255, 255, 255))
                behind = head >= 300 and k not in FORCE_FRONT
                y0 = int(head - 0.4 * hT) if behind else int(BIGY.get(k, 1000) - hT / 2)
                if not behind: masks = {}
                reg = np.asarray(fr0.convert('L'))[y0:y0 + hT, 60:W - 60].astype(float); mreg = (np.asarray(Image.open(f'{tmp}/m/{fw0:05d}.png').convert('L'))[y0:y0 + hT, 60:W - 60] < 128) if behind else np.ones_like(reg, bool)
                lum = reg[mreg].mean() if mreg.any() else 0
                col = PCOL[pk] if lum > 150 else (255, 255, 255)
                im, hT, pad = big_img(text, col)
                big = dict(im=im, y=y0 - pad, fw0=fw0, fw1=fw1, text=text, tw=tw, behind=behind, masks=masks); bigs.append(big)
                print(k, 'big', text, 'behind' if behind else 'front', 'head', head, 'y0', y0, 'lum', round(lum), 'col', col, flush=True)
            shutil.rmtree(tmp, ignore_errors=True)

    wout = []
    for si2, (a2, b2) in enumerate(segs):
        for w in clean([w for w in ws if a2 - 0.05 <= w[0] < b2], k): wout.append((float(starts[si2] + w[0] - a2), w[2]))
    fun = FUN.get(k, {}); punches = [t for t, w in wout if w in fun.get('punch', [])]; shakes = [t for t, w in wout if w in fun.get('shake', [])]
    emos = []
    for t_, w in wout:
        if w in fun.get('emoji', {}): emos.append((t_, fun['emoji'][w], 1 if len(emos) % 2 == 0 else -1))
    metals = [t for t, w in wout if w in METAL.get(k, [])][:1]
    enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-vf', 'scale=out_color_matrix=bt709', '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p',
                            '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', f'{d}/video.mp4'], stdin=subprocess.PIPE)
    fi = 0
    for si, (a, b) in enumerate(segs):
        segw = clean([w for w in ws if a - 0.05 <= w[0] < b], k); gs = groups(segw) if e['caps'] else []
        for kf, fr in seg_frames(si):
            t = fi / FPS; ts = a + kf / FPS
            zp = 1.0; dx = dy = 0
            for tp in punches:
                if 0 <= t - tp < 0.6: zp = max(zp, 1 + 0.13 * math.exp(-(t - tp) / 0.13))
            for tk in shakes:
                if 0 <= t - tk < 0.35: amp = 22 * (1 - (t - tk) / 0.35); dx = int(amp * math.sin(t * 90)); dy = int(amp * math.cos(t * 70))
            if zp > 1.001 or dx or dy:
                cw, ch = W / zp, H / zp; cx0 = (W - cw) / 2 + dx; cy0 = H * 0.42 - ch * 0.42 + dy
                cx0 = min(max(0, cx0), W - cw); cy0 = min(max(0, cy0), H - ch)
                fr = fr.resize((W, H), Image.BILINEAR, box=(cx0, cy0, cx0 + cw, cy0 + ch))
            _in = next((w_ for w_ in INSERTS.get(k, []) if w_[0] <= t < w_[1]), None)
            if _in: fr = make_insert(_in[2], (t - _in[0]) / (_in[1] - _in[0]))
            fr0 = fr
            if not _in and any(a_ <= t < b_ for a_, b_ in SPOT): fr = spot(fr)
            base = fr; fr = fr.convert('RGBA')
            for big in bigs:
                if not (big['fw0'] <= fi < big['fw1']): continue
                age = (fi - big['fw0']) / FPS
                st_ = STYLE.get(k, {}).get('big', 'pop')
                im, ddx, ddy = fx(big['im'], st_, age, 0.34)
                al = min(1.0, (big['fw1'] - fi) / 4)
                if im.width > W: im = im.resize((W, int(im.height * W / im.width)), Image.BILINEAR)
                if al < 1: im = im.copy(); im.putalpha(im.split()[3].point(lambda v: int(v * al)))
                cy = big['y'] + big['im'].height / 2 + ddy
                fr.alpha_composite(im, (int((W - im.width) / 2 + ddx), int(cy - im.height / 2)))
                if big['behind'] and fi in big['masks']: person = base.convert('RGBA'); person.putalpha(big['masks'][fi]); fr.alpha_composite(person)
            for (te, emo, side) in emos:
                age = t - te
                if 0 <= age < 0.9:
                    p = min(1.0, age / 0.14); s = 0.3 + 0.7 * p + 0.25 * math.sin(p * math.pi)
                    al = min(1.0, (1.0 - age) / 0.15)
                    im = emoji_big(emo).rotate(-12 * side + 6 * math.sin(age * 9), expand=True, resample=Image.BICUBIC)
                    im = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.BILINEAR)
                    if al < 1: im = im.copy(); im.putalpha(im.split()[3].point(lambda v: int(v * al)))
                    fly = 1 - min(1.0, age / 0.18) ** 0.5; cx = W / 2 + side * (330 + 480 * fly); cy = 860 - 70 * min(1, age / 0.6) + 120 * fly
                    fr.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))
            if not _in:
                for pi_, (pa_, pb_, pn_, pl_, ps_, pst_) in enumerate(PTRS):
                    if pa_ <= t < pb_:
                        fr = pointer(fr.convert('RGB'), pn_, pl_, t - pa_, pst.setdefault(pi_, {}), ps_ + (t - pa_), fr0, pst_).convert('RGBA')
            for ma_, mb_ in MINI:
                if ma_ <= t < mb_: fr = mini_cells(fr.convert('RGB'), t - ma_)
            inbig = next((bg for bg in bigs if bg['fw0'] <= fi < bg['fw1']), None)
            for g in (gs if not _in else []):
                if g[0][0] - 0.05 <= ts <= g[-1][1] + 0.1:
                    if inbig and any(norm_w(w[2]) == norm_w(inbig['text']) for w in g): break
                    cs = STYLE.get(k, {}).get('cap', 'pop'); col = ACC[PK.get(k, 'ss')]
                    texts = [w[2].upper().rstrip(',.') for w in g]
                    ims = [word_img(t_, (255, 255, 255)) for t_ in texts]; ws_ = [m[1] for m in ims]
                    gap = 26; tot = sum(ws_) + gap * (len(ws_) - 1); sc = min(1.0, 980 / tot) if tot > 0 else 1.0
                    x = (W - tot * sc) / 2
                    lastv = max([j for j, w in enumerate(g) if ts >= w[0] - 0.02] or [-1])
                    for j, w in enumerate(g):
                        wx = x; x += (ws_[j] + gap) * sc
                        if ts < w[0] - 0.02: continue
                        age = ts - w[0] + 0.02
                        wim = word_img(texts[j], col if (j == lastv and cs in ('pop', 'spin', 'drop')) else (255, 255, 255))[0]
                        if cs == 'line':   # whole group appears together
                            age = ts - g[0][0] + 0.02
                        wim2, ddx, ddy = fx(wim, 'pop' if cs == 'line' else cs, age, 0.26)
                        if wim2 is None: continue
                        if sc < 1: wim2 = wim2.resize((int(wim2.width * sc), int(wim2.height * sc)), Image.BILINEAR)
                        cxw = wx + 35 * sc + ws_[j] * sc / 2
                        fr.alpha_composite(wim2, (int(cxw - wim2.width / 2 + ddx), int(1180 - wim2.height / 2 + ddy)))
                    break
            for (c0, c1, kind, a1, a2, pk_) in CHIPS.get(k, []):
                if not (c0 <= t < c1): continue
                age = t - c0; colr = PCOL[pk_]
                if kind == 'chip': im = chip_img(a1, a2, colr, pk_)
                else:
                    tgt = int(a1.rstrip('%')); cur = int(round(tgt * ease(age / 0.9))); im = stat_img(f'{cur}%' if a1.endswith('%') else str(cur), a2, colr)
                outp = min(1.0, (c1 - t) / 0.25)
                px = int(-im.width + (60 + im.width) * back(age / 0.4)) if kind == 'chip' else int((W - im.width) / 2)
                py = 300 if kind == 'chip' else 330
                if kind == 'stat':
                    im, ddx, ddy = fx(im, 'pop', age, 0.35); px += ddx; py += ddy
                if outp < 1: im = im.copy(); im.putalpha(im.split()[3].point(lambda v: int(v * outp)))
                fr.alpha_composite(im, (px, py))
            enc.stdin.write(fr.convert('RGB').tobytes()); fi += 1
    enc.stdin.close(); enc.wait()
    parts = [f'[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,afade=t=in:d=0.01,afade=t=out:st={b - a - 0.012}:d=0.012[s{i}]' for i, (a, b) in enumerate(segs)]
    cc = ''.join(f'[s{i}]' for i in range(len(segs)))
    sh(f'ffmpeg -loglevel error -y -i "{src}" -filter_complex "{";".join(parts)};{cc}concat=n={len(segs)}:v=0:a=1,aresample={SR},aformat=channel_layouts=stereo[v]" '
       f'-map "[v]" -t {total} "{d}/voice.wav"')
    from mgaudio import recipes
    from mgaudio import sfx
    if k in SYNTH:   # restored original bed for the 10 approved edits (the user did not ask for new music there)
        from mgaudio import recipes
        m = recipes.pop(duration=total + 0.5, bpm=STYLE.get(k, {}).get('bpm', 112), key=STYLE.get(k, {}).get('key', 'A'), drop=0.0)
    else:
        from mgaudio.mix import Mix
        m = Mix(duration=total + 0.5)   # SFX only; music is a real Pixabay track (MUSIC in edits.py)
    for bg in bigs: m.sfx(sfx.swish(0.22), at=max(0, bg['tw'] - 0.12), gain=-8)
    for tp in punches: m.sfx(sfx.whoosh(0.3), at=max(0, tp - 0.15), gain=-8)
    for (c0, c1, kind, a1, a2, pk_) in CHIPS.get(k, []): m.sfx(sfx.swish(0.22), at=max(0, c0 - 0.05), gain=-9)
    if STYLE.get(k, {}).get('tick'):
        for t_, w_ in wout[::2]: m.sfx(sfx.pop(), at=t_, gain=-17)
    for te, _, _ in emos: m.sfx(sfx.pop(), at=te, gain=-6)
    if k in SYNTH:
        m.export(f'{d}/bed.wav', lufs=-30.0 if fun else -34.0, analyze=False)
    else:
        m.export(f'{d}/sfx.wav', lufs=-26.0, analyze=False)
        mp, ms = MUSIC[k]
        sh(f'ffmpeg -loglevel error -y -ss {ms} -t {total + 0.5} -i "{mp}" -af "loudnorm=I=-27:TP=-3,afade=t=in:d=0.6,afade=t=out:st={max(0, total - 0.9)}:d=0.9,aresample={SR}" -ac 2 "{d}/music.wav"')
        sh(f'ffmpeg -loglevel error -y -i "{d}/music.wav" -i "{d}/sfx.wav" -filter_complex "[0:a]aresample={SR},aformat=channel_layouts=stereo[a];[1:a]aresample={SR},aformat=channel_layouts=stereo,volume=-3dB[b];[a][b]amix=inputs=2:normalize=0:duration=longest" -t {total + 0.5} "{d}/bed.wav"')
    ins = f'-i "{d}/voice.wav" -i "{d}/bed.wav"'; extra = ''; mixn = 2
    if metals:
        metal_clang(f'{d}/metal.wav'); ms = int(max(0, metals[0] + 0.05) * 1000)
        ins += f' -i "{d}/metal.wav"'; extra = f';[2:a]aresample={SR},volume=-9dB,adelay={ms}|{ms},apad[mt]'; mixn = 3
    tail = '[bd][vB][mt]' if metals else '[bd][vB]'
    sh(f'ffmpeg -loglevel error -y {ins} -filter_complex '
       f'"[0:a]loudnorm=I=-16:TP=-2,aresample={SR},asplit[vA][vB];[1:a]aresample={SR},aformat=channel_layouts=stereo,atrim=0:{total}[bb];'
       f'[bb][vA]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=300[bd]{extra};{tail}amix=inputs={mixn}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[mx]" '
       f'-map "[mx]" -t {total} -ar {SR} "{d}/mix.wav"')
    sh(f'ffmpeg -loglevel error -y -i "{d}/video.mp4" -i "{d}/mix.wav" -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart "{OUT}/{k} {e["name"]}.mp4"')
    print(k, round(total, 2), flush=True)

if __name__ == '__main__':
    for k in (sys.argv[1:] or E): render(k)
