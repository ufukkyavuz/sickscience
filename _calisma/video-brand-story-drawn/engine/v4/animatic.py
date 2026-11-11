# v4 animatic: the storyboard5 spread written beat by beat in sync with the narrator VO.
# usage: python animatic.py [--frames t1,t2] [--out file.mp4]
import json, math, os, re, subprocess, sys, difflib, random
import numpy as np
from PIL import Image, ImageDraw, ImageChops, ImageFilter
import storyboard5 as sb

R = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
BG = (236, 237, 238)

# ---------- beat times from whisper words ----------
WJ = json.load(open(os.path.join(R, 'vo_words.json')))
norm = lambda w: re.sub(r'[^a-z0-9]', '', w.lower())
sw = [norm(w['w']) for w in WJ['words']]
beat_words, beat_first = [], []
for _, _, _, nar in sb.BEATS:
    ws = [norm(x) for x in nar.replace('NX35', 'N X thirty five').replace('SickScience', 'Sick Science').replace('Harvard–MIT', 'Harvard MIT').split()]
    ws = [x for x in ws if x]
    beat_first.append(len(beat_words)); beat_words += ws
sm = difflib.SequenceMatcher(a=beat_words, b=sw, autojunk=False)
amap = {}
for a0, b0, n in sm.get_matching_blocks():
    for k in range(n): amap[a0 + k] = b0 + k
def t_of(ai):
    for k in range(ai, len(beat_words)):          # nearest matched word at or after
        if k in amap: return WJ['words'][amap[k]]['s']
    return WJ['dur']
LEAD = 1.6                                         # finished-spread cover before VO starts
BT = [LEAD + t_of(i) for i in beat_first]
BT[0] = LEAD
VO_END = LEAD + WJ['dur']
END_PULL = BT[-1]                                  # "Science, but never boring." -> pull back
EC_T = END_PULL + 1.4                              # end card
TOTAL = VO_END + 2.6

# ---------- page states ----------
random.seed(11)
final = sb.base(); fd = ImageDraw.Draw(final)
for _, _, fns, _ in sb.BEATS:
    for fn in fns: fn(fd)
random.seed(11)
cur = sb.base(); cd = ImageDraw.Draw(cur)
STATES = [cur.copy()]
for _, _, fns, _ in sb.BEATS:
    for fn in fns: fn(cd)
    STATES.append(cur.copy())
# per beat: every new mark is drawn along its own stroke path (skeleton), word by word, with the pen at the tip
from scipy import ndimage
from skimage.morphology import skeletonize
SPEED = 1700.0          # spread px of stroke path per second

N8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
def stroke_order(pm):
    """time map (path length at which each ink pixel gets drawn) + ordered tip points.
    Glyph by glyph strictly left to right; each glyph finished before the next starts."""
    sk = skeletonize(pm)
    if not sk.any():
        return None
    glab, gn = ndimage.label(ndimage.binary_dilation(pm, iterations=3))
    groups = []
    for g in range(1, gn + 1):
        ys, xs = np.where(sk & (glab == g))
        if len(ys): groups.append((xs.min(), set(zip(ys, xs))))
    groups.sort(key=lambda g: g[0])
    tval = {}; path = []; L = 0.0
    for _, pts in groups:
        def nbrs(p): return [(p[0] + dy, p[1] + dx) for dy, dx in N8 if (p[0] + dy, p[1] + dx) in pts]
        cur = None; d0 = (0.0, 1.0)
        while pts:
            nb = nbrs(cur) if cur is not None else []
            if nb:   # keep following the stroke, preferring the same direction, then the left-most
                nxt = max(nb, key=lambda q: ((q[0] - cur[0]) * d0[0] + (q[1] - cur[1]) * d0[1]) - 0.15 * (q[1] - cur[1]))
                L += math.hypot(nxt[0] - cur[0], nxt[1] - cur[1])
                d0 = (nxt[0] - cur[0], nxt[1] - cur[1])
            else:    # pen lift: next stroke starts at the left-most ink not drawn yet
                left = min(p[1] for p in pts)
                cand = [p for p in pts if p[1] <= left + 4]
                ends = [p for p in cand if len(nbrs(p)) <= 1] or cand
                nxt = min(ends, key=lambda p: (p[1], p[0]))
                L += 3.0 if cur is not None else 0.0
                d0 = (0.0, 1.0)
            pts.discard(nxt); tval[nxt] = L; path.append((nxt, L)); cur = nxt
        L += 6.0                                              # pen moves to the next glyph
    key = np.full(pm.shape, np.inf, np.float32)
    for (y, x), v in tval.items(): key[y, x] = v
    skm = np.isfinite(key)
    _, (iy, ix) = ndimage.distance_transform_edt(~skm, return_indices=True)
    tm = key[iy, ix]; tm[~pm] = np.inf
    return tm, path, L


REVEAL = []; BBOX = []
for i in range(len(sb.BEATS)):
    a_, b_ = STATES[i], STATES[i + 1]
    diff = np.asarray(ImageChops.difference(a_, b_).convert('L')) > 6
    if not diff.any():
        REVEAL.append(None); BBOX.append(None); continue
    ys_, xs_ = np.where(diff); BBOX.append((xs_.min(), ys_.min(), xs_.max(), ys_.max()))
    B = np.asarray(b_).astype(np.int16)
    yellow = (B[..., 0] > 200) & (B[..., 1] > 170) & (B[..., 2] < 175) & diff
    ink = diff & ~yellow
    lab, n = ndimage.label(ndimage.binary_dilation(ink, structure=np.ones((7, 13))))
    pieces = []
    for sl_i, sl in enumerate(ndimage.find_objects(lab), 1):
        if sl is None: continue
        pm = (lab[sl] == sl_i) & ink[sl]
        if pm.sum() < 8: continue
        so = stroke_order(pm)
        if so is None: continue
        pieces.append([sl[0].start, sl[1].start, pm, so])
    pieces.sort(key=lambda p: (int((p[0] + p[2].shape[0] / 2) // 70), p[1]))
    t = 0.0
    for p in pieces:
        d = max(0.1, p[3][2] / SPEED); p += [t, d]; t += d + 0.03
    hl = None
    if yellow.any():
        ys, xs = np.where(yellow); hb = (ys.min(), xs.min(), ys.max() + 1, xs.max() + 1)
        hl = (hb, yellow[hb[0]:hb[2], hb[1]:hb[3]], t, 0.3); t += 0.32
    REVEAL.append((pieces, hl, t, b_))
print('strokes ready', flush=True)


def state_at(t):
    """page at time t plus the pen tip (spread coords) while writing"""
    i = 0
    while i + 1 < len(BT) and BT[i + 1] <= t: i += 1
    img = STATES[i].copy(); tip = None
    rv = REVEAL[i]
    if rv and t >= BT[i]:
        pieces, hl, total, src = rv
        nxt = BT[i + 1] if i + 1 < len(BT) else TOTAL
        k = max(1.0, total / max(0.4, (nxt - BT[i]) * 0.92))
        lt = (t - BT[i]) * k
        S = np.asarray(src)
        for y0, x0, pm, (tm, path, L), t0, d in pieces:
            if lt <= t0: break
            p = min(1.0, (lt - t0) / d)
            hh, ww = pm.shape
            vis = tm <= p * L
            if vis.any():
                img.paste(Image.fromarray(S[y0:y0 + hh, x0:x0 + ww]), (x0, y0), Image.fromarray(vis.astype(np.uint8) * 255))
            if p < 1:
                cur = p * L
                lo, hi = 0, len(path) - 1
                while lo < hi:
                    mid = (lo + hi) // 2
                    if path[mid][1] < cur: lo = mid + 1
                    else: hi = mid
                seg = path[max(0, lo - 18):lo + 19]
                py = sum(q[0][0] for q in seg) / len(seg); px = sum(q[0][1] for q in seg) / len(seg)
                tip = (x0 + px, y0 + py)
        if hl and lt > hl[2]:
            (hy0, hx0, hy1, hx1), hm, t0, d = hl
            p = min(1.0, (lt - t0) / d)
            vis = hm.copy(); vis[:, int(hm.shape[1] * p):] = False
            img.paste(Image.fromarray(S[hy0:hy1, hx0:hx1]), (hx0, hy0), Image.fromarray(vis.astype(np.uint8) * 255))
            if p < 1: tip = (hx0 + hm.shape[1] * p, (hy0 + hy1) / 2)
    return img, i, tip


_TIP = {}
def draw_pen(im, tip, view):
    if 'p' in _TIP and math.dist(_TIP['p'], tip) < 160:
        tip = (_TIP['p'][0] * 0.45 + tip[0] * 0.55, _TIP['p'][1] * 0.45 + tip[1] * 0.55)
    _TIP['p'] = tip
    """pen in screen space: barrel up-right from the tip, soft shadow"""
    (vx0, vy0, sc) = view
    x, y = (tip[0] - vx0) * sc, (tip[1] - vy0) * sc
    d = ImageDraw.Draw(im, 'RGBA')
    L, ang = 330, math.radians(-58)
    ex, ey = x + L * math.cos(ang), y + L * math.sin(ang)
    d.line((x + 18, y + 22, ex + 40, ey + 40), fill=(0, 0, 0, 40), width=26)          # shadow
    d.line((x, y, x + 26 * math.cos(ang), y + 26 * math.sin(ang)), fill=(70, 70, 76, 255), width=8)
    d.line((x + 26 * math.cos(ang), y + 26 * math.sin(ang), ex, ey), fill=(30, 32, 44, 255), width=22)
    d.line((x + 60 * math.cos(ang), y + 60 * math.sin(ang), x + 110 * math.cos(ang), y + 110 * math.sin(ang)), fill=(200, 200, 205, 255), width=22)   # grip
    return im


# ---------- camera ----------
CW = 900; CH = int(CW * H / W)
def focus(i):
    side = sb.BEATS[i][1]
    bb = BBOX[i]
    if side == 'W' or bb is None:
        return None
    cx, cy = (bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2
    x0, x1 = (sb.PL if side == 'L' else sb.PR)
    lo, hi = bb[2] + 60 - CW / 2, bb[0] - 60 + CW / 2          # range of centres that keep the element inside
    pc = (x0 + x1) / 2
    cx = (lo + hi) / 2 if lo > hi else min(max(pc, lo), hi)
    cy = min(max(cy + 120, CH / 2), sb.SH - CH / 2)
    return cx, cy

FOC = []
last = (sum(sb.PL) / 2, sb.SH / 2)
for i in range(len(sb.BEATS)):
    f = focus(i)
    if f: last = f
    FOC.append(last)


def ss(a):
    a = min(1.0, max(0.0, a)); return a * a * (3 - 2 * a)


def cam(t):
    i = 0
    while i + 1 < len(BT) and BT[i + 1] <= t: i += 1
    tgt = FOC[i]; prev = FOC[i - 1] if i else tgt
    k = ss((t - BT[i]) / 0.9)
    return prev[0] + (tgt[0] - prev[0]) * k, prev[1] + (tgt[1] - prev[1]) * k


LASTVIEW = [0, 0, 1]
def close_view(img, c, w=CW):
    h = w * H / W
    cx, cy = c
    box = (int(cx - w / 2), int(cy - h / 2), int(cx + w / 2), int(cy + h / 2))
    can = Image.new('RGB', (box[2] - box[0], box[3] - box[1]), BG)
    can.paste(img, (-box[0], -box[1]))
    LASTVIEW[:] = [box[0], box[1], W / (box[2] - box[0])]
    return can.resize((W, H), Image.BICUBIC)


def wide_view(img, title=None, sub=None, sub_col=(28, 34, 70)):
    P = Image.new('RGB', (W, H), BG)
    s = img.resize((W, int(W * sb.SH / sb.SW)), Image.LANCZOS)
    P.paste(s, (0, (H - s.height) // 2 + 80))
    if title:
        d = ImageDraw.Draw(P)
        f = sb.GROT(66); tw = d.textlength(title, font=f); d.text(((W - tw) / 2, 470), title, font=f, fill=(20, 20, 24))
        f2 = sb.BIRO(64); tw = d.textlength(sub, font=f2); d.text(((W - tw) / 2, 560), sub, font=f2, fill=sub_col)
    return P


ENDCARD = Image.open(os.path.join(R, '..', 'assets', 'endcard.png')).convert('RGB').resize((W, H))


def lerp(a, b, k): return a + (b - a) * k


def frame(t):
    if t < BT[1]:                                  # cover: finished spread, ending first
        im = wide_view(final, 'FOR THE FIRST TIME', 'the SickScience story')
        if t > BT[1] - 0.45:                       # push into page 01
            k = ss((t - (BT[1] - 0.45)) / 0.45)
            im = Image.blend(im, close_view(STATES[0], FOC[1]), k)
        return im
    st, i, tip = state_at(t)
    if t < END_PULL:
        im = close_view(st, cam(t))
        if tip: im = draw_pen(im, tip, LASTVIEW)
        return im
    # pull back to the full spread, then the real products
    k = ss((t - END_PULL) / 1.2)
    c0 = FOC[-2]
    w = lerp(CW, sb.SW * 1.0, k)
    c = (lerp(c0[0], sb.SW / 2, k), lerp(c0[1], sb.SH / 2 - 40 * k, k))
    im = close_view(final, c, w)
    if t >= EC_T:
        a = ss((t - EC_T) / 0.7)
        im = Image.blend(im, ENDCARD, a)
        if t > EC_T + 0.4:
            d = ImageDraw.Draw(im); f = sb.BIRO(84)
            for li, (line, ly) in enumerate((('Science,', 226), ('but never', 314), ('boring.', 402))):
                p = min(1.0, max(0.0, (t - EC_T - 0.4 - li * 0.45) / 0.7))
                if p <= 0: continue
                tw = d.textlength(line, font=f)
                lay = Image.new('L', (int(tw) + 30, 130), 0); ImageDraw.Draw(lay).text((10, 0), line, font=f, fill=255)
                m = Image.new('L', lay.size, 0); m.paste(lay.crop((0, 0, max(1, int(lay.width * p)), lay.height)), (0, 0))
                im.paste((28, 34, 70), (78, ly), m)
    return im


def grain(im, t):
    a = np.asarray(im).astype(np.int16)
    n = np.random.default_rng(int(t * 1000)).normal(0, 2.6, (H // 2, W // 2, 1)).repeat(2, 0).repeat(2, 1)
    return np.clip(a + n, 0, 255).astype(np.uint8)


if __name__ == '__main__':
    args = sys.argv[1:]
    json.dump({'BT': BT, 'TOTAL': TOTAL, 'LEAD': LEAD, 'EC_T': EC_T, 'sides': [b[1] for b in sb.BEATS]}, open(os.path.join(R, 'anim_timeline.json'), 'w'), indent=1)
    if '--info' in args:
        print([round(x, 2) for x in BT], round(TOTAL, 2)); sys.exit()
    if '--frames' in args:
        for tt in args[args.index('--frames') + 1].split(','):
            Image.fromarray(grain(frame(float(tt)), float(tt))).save(os.path.join(R, f'af_{float(tt):06.2f}.jpg'), quality=88)
        sys.exit()
    out = args[args.index('--out') + 1] if '--out' in args else os.path.join(R, 'animatic_noaudio.mp4')
    n = int(TOTAL * FPS)
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    for f in range(n):
        t = f / FPS
        p.stdin.write(grain(frame(t), t).tobytes())
        if f % 300 == 0: print(f, '/', n, flush=True)
    p.stdin.close(); p.wait(); print('done', out)
