# Human writing pass on top of animatic_real:
#  - every drawn element is recorded in the order the storyboard draws it (pen polylines keep their real direction)
#  - each text element starts when the narrator says its word (script word -> whisper time)
#  - speed slows in curves; the pen lifts between elements and travels through the air
#  - the real hand: the wrist stays put while the fingers write, ratchets along, rotates a little, rests in long gaps
# usage: python animatic_human.py [--range a,b] [--frames t1,t2] [--out file.mp4]
import json, math, os, re, subprocess, sys, random
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage
import animatic_real as ar
import storyboard5 as sb

R = ar.R; W, H, FPS = ar.W, ar.H, ar.FPS

# ---------------- record elements ----------------
ELEMS = []
_cur = {'beat': 0, 'depth': 0, 'img': None, 'd': None}


def leaf(kind, fn, method=False):
    def w(*a, **k):
        d = a[0]
        if _cur['depth'] > 0 or _cur['d'] is None or d is not _cur['d']:
            return fn(*a, **k)
        before = np.asarray(_cur['img']).copy()
        _cur['depth'] += 1
        try:
            r = fn(*a, **k)
        finally:
            _cur['depth'] -= 1
        after = np.asarray(_cur['img'])
        diff = np.abs(after.astype(np.int16) - before).max(2) > 6
        if diff.any():
            ys, xs = np.where(diff)
            y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
            e = dict(kind=kind, beat=_cur['beat'], box=(x0, y0, x1, y1), mask=diff[y0:y1, x0:x1], src=after[y0:y1, x0:x1].copy())
            if kind == 'line':
                e['pts'] = [tuple(p) for p in a[1]]
            elif kind == 'dline':
                xy = a[1]; e['pts'] = [tuple(p) for p in xy] if isinstance(xy[0], (tuple, list)) else list(zip(xy[0::2], xy[1::2]))
            elif kind in ('text', 'mtext'):
                e['s'] = a[2] if kind == 'text' else a[3]
            ELEMS.append(e)
        return r
    return w


import PIL.ImageDraw as PID
_orig_text, _orig_line = PID.ImageDraw.text, PID.ImageDraw.line
sb.pen = leaf('line', sb.pen)
sb.marker_text = leaf('mtext', sb.marker_text)
sb.marker_fill = leaf('fill', sb.marker_fill)
sb.highlighter = leaf('hl', sb.highlighter)
PID.ImageDraw.text = leaf('text', _orig_text)
PID.ImageDraw.line = leaf('dline', _orig_line)

random.seed(11)
cur = sb.base(); cd = ImageDraw.Draw(cur)
_cur['img'], _cur['d'] = cur, cd
for bi, (_, _, fns, _) in enumerate(sb.BEATS):
    _cur['beat'] = bi
    for fn in fns: fn(cd)
_cur['d'] = None
PID.ImageDraw.text, PID.ImageDraw.line = _orig_text, _orig_line
_dd = np.abs(np.asarray(cur).astype(int) - np.asarray(ar.final).astype(int)).max(2) > 40
print('spread match: differing px share', round(float(_dd.mean()), 4), flush=True)   # marker noise is not seeded, small share expected
print('elements', len(ELEMS), flush=True)


# ---------------- paths and time-lengths ----------------
def dense(pts, step=3.0):
    out = [pts[0]]
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        n = max(1, int(math.dist((x0, y0), (x1, y1)) / step))
        for k in range(1, n + 1): out.append((x0 + (x1 - x0) * k / n, y0 + (y1 - y0) * k / n))
    return out


def tau_of(path):
    """time-length: arc length weighted up where the stroke turns (people slow down in curves)"""
    n = len(path); tau = [0.0]
    for i in range(1, n):
        ds = math.dist(path[i - 1], path[i])
        a = path[max(0, i - 6)]; b = path[i]; c = path[min(n - 1, i + 6)]
        v1 = (b[0] - a[0], b[1] - a[1]); v2 = (c[0] - b[0], c[1] - b[1])
        n1, n2 = math.hypot(*v1), math.hypot(*v2)
        turn = 0.0 if n1 < 1e-6 or n2 < 1e-6 else math.acos(max(-1, min(1, (v1[0] * v2[0] + v1[1] * v2[1]) / (n1 * n2))))
        f = 1.0 - 0.5 * min(1.0, turn / 1.6)
        jump = ds > 8                                            # pen lift inside a glyph group
        tau.append(tau[-1] + (ds / f if not jump else 18.0))
    return tau


def build(e):
    x0, y0, x1, y1 = e['box']; m = e['mask']
    if e['kind'] in ('line', 'dline') and len(e.get('pts', [])) >= 2:
        path = [(x - x0, y - y0) for x, y in dense(e['pts'])]
        tau = tau_of(path)
        key = np.full(m.shape, np.inf, np.float32)
        for (px, py), tv in zip(path, tau):
            ix, iy = int(round(px)), int(round(py))
            if 0 <= iy < m.shape[0] and 0 <= ix < m.shape[1] and tv < key[iy, ix]: key[iy, ix] = tv
        fin = np.isfinite(key)
        if not fin.any(): return None
        _, (iy, ix) = ndimage.distance_transform_edt(~fin, return_indices=True)
        tm = key[iy, ix]; tm[~m] = np.inf
        return tm, path, tau
    if e['kind'] == 'hl' or e['kind'] == 'fill':
        hh, ww = m.shape
        if e['kind'] == 'hl':
            tm = np.tile(np.arange(ww, dtype=np.float32), (hh, 1)); path = [(x, hh / 2) for x in range(0, ww, 3)]
        else:                                                    # felt-tip hatching sweeps along the diagonal, zig-zag tip
            yy, xx = np.mgrid[0:hh, 0:ww]; tm = (xx + yy * 0.6).astype(np.float32)
            L = ww + hh * 0.6; path = []
            for k in range(0, int(L), 6):
                path.append((min(ww - 1, k), hh * (0.15 if (k // 6) % 2 else 0.85)))
        tm[~m] = np.inf
        tau = [p[0] if e['kind'] == 'hl' else p[0] for p in path]
        return tm, path, tau
    so = ar.stroke_order(m)                                      # text and anything else: skeleton, glyph by glyph, left to right
    if so is None: return None
    tmL, pth, L = so
    path = [(p[0][1], p[0][0]) for p in pth]
    tau = tau_of(path)
    Ls = [p[1] for p in pth]
    tm = np.interp(np.where(np.isfinite(tmL), tmL, 0), Ls, tau).astype(np.float32); tm[~np.isfinite(tmL)] = np.inf
    return tm, path, tau


for e in ELEMS:
    b = build(e)
    e['ok'] = b is not None
    if b: e['tm'], e['path'], e['tau'] = b; e['T'] = b[2][-1] if b[2] else 1.0
ELEMS = [e for e in ELEMS if e['ok']]
print('paths ready', flush=True)

# ---------------- schedule to the narration ----------------
NUM = {'14': 'fourteen', '2009': '2009', '20': 'twenty', '30': 'thirty', '100': 'one'}
norm = ar.norm
script = []                                                      # (beat, word, time)
for bi, (_, _, _, nar) in enumerate(sb.BEATS):
    ws = [norm(x) for x in nar.replace('NX35', 'N X thirty five').replace('SickScience', 'Sick Science').replace('Harvard–MIT', 'Harvard MIT').split()]
    k0 = ar.beat_first[bi]
    for j, wv in enumerate([x for x in ws if x]):
        script.append((bi, wv, ar.LEAD + ar.t_of(k0 + j)))
used = set()


def anchor(e):
    if e['kind'] not in ('text', 'mtext'): return None
    toks = [norm(t) for t in re.split(r'[\s·/+×–\-]+', e['s']) if norm(t)]
    toks = [NUM.get(t, t) for t in toks]
    best = None
    for idx, (bi, wv, tt) in enumerate(script):
        if bi != e['beat'] or idx in used: continue
        for t in toks:
            if len(t) >= 2 and (wv == t or (len(t) >= 4 and wv.startswith(t[:4]))):
                if best is None or tt < best[1]: best = (idx, tt)
    if best: used.add(best[0]); return best[1]
    return None


SPEED = {'line': 900.0, 'dline': 900.0, 'text': 820.0, 'mtext': 800.0, 'hl': 1600.0, 'fill': 600.0}
AIR = 2000.0                                                     # spread px per second through the air
BT = ar.BT
by_beat = {}
for e in ELEMS: by_beat.setdefault(e['beat'], []).append(e)


def tip0(e):
    p = e['path'][0]; return (e['box'][0] + p[0], e['box'][1] + p[1])


def tip1(e):
    p = e['path'][-1]; return (e['box'][0] + p[0], e['box'][1] + p[1])


cursor, last = BT[1], None
for bi in range(len(sb.BEATS)):
    es = by_beat.get(bi, [])
    if not es: continue
    for e in es: e['anc'] = anchor(e)
    nxt = BT[bi + 1] if bi + 1 < len(BT) else ar.END_PULL
    for boost in (1.0, 1.2, 1.4, 1.6, 1.8):
        c, lp = max(cursor, BT[bi]), last
        for e in es:
            travel = 0.0 if lp is None else max(0.07, math.dist(lp, tip0(e)) / AIR)
            st = c + travel
            if e['anc'] is not None: st = max(st, e['anc'] - 0.06)
            small = 2.0 if e['T'] < 60 else 1.0                       # tiny details (dots, grains) go quicker
            e['start'] = st; e['dur'] = max(0.04, e['T'] / (SPEED[e['kind']] * boost * small))
            c = st + e['dur']; lp = tip1(e)
        if c <= nxt - 0.1: break
    cursor, last = c, lp
EL = sorted(ELEMS, key=lambda e: e['start'])
STARTS = [e['start'] for e in EL]
print('schedule', round(EL[0]['start'], 2), '->', round(EL[-1]['start'] + EL[-1]['dur'], 2), 'END_PULL', round(ar.END_PULL, 2), flush=True)


# ---------------- page state + pen tip ----------------
_cache = {'t': -1.0, 'img': None, 'n': 0}


def paste_el(img, e, p=1.0):
    x0, y0, _, _ = e['box']
    vis = e['tm'] <= p * e['T'] if p < 1 else e['mask']
    if vis.any():
        img.paste(Image.fromarray(e['src']), (x0, y0), Image.fromarray((vis & e['mask']).astype(np.uint8) * 255))


def path_at(e, p):
    tt = p * e['T']; tau = e['tau']
    i = int(np.searchsorted(tau, tt)); i = min(max(i, 0), len(tau) - 1)
    seg = e['path'][max(0, i - 4):i + 5]
    return (e['box'][0] + sum(q[0] for q in seg) / len(seg), e['box'][1] + sum(q[1] for q in seg) / len(seg))


def state_at(t):
    """page with every element finished by t, the one in progress partly drawn; tip info for the hand"""
    if _cache['img'] is None or t < _cache['t']:
        _cache['img'], _cache['n'] = sb.base(), 0
    img = _cache['img']
    while _cache['n'] < len(EL) and EL[_cache['n']]['start'] + EL[_cache['n']]['dur'] <= t:
        paste_el(img, EL[_cache['n']]); _cache['n'] += 1
    _cache['t'] = t
    out = img.copy(); info = None
    n = _cache['n']
    if n < len(EL) and EL[n]['start'] <= t:
        e = EL[n]; p = (t - e['start']) / e['dur']
        paste_el(out, e, p)
        info = ('down', path_at(e, p))
    else:
        prv = EL[n - 1] if n > 0 else None; nx = EL[n] if n < len(EL) else None
        a = tip1(prv) if prv else None; b = tip0(nx) if nx else None
        t0 = prv['start'] + prv['dur'] if prv else -9; t1 = nx['start'] if nx else 1e9
        info = ('air', a, b, t0, t1)
    i = 0
    while i + 1 < len(BT) and BT[i + 1] <= t: i += 1
    return out, i, info


# ---------------- the hand ----------------
HJ = json.load(open(os.path.join(R, 'hand', 'hand.json')))
_SPR = Image.open(os.path.join(R, 'hand', HJ['file'])).convert('RGBA')
WRIST = HJ.get('wrist', [616, 1059])
SC_VIEW = W / ar.CW
K = 44.8 / HJ['px_per_cm'] * SC_VIEW                             # sprite px -> screen px at the close view
SPR = _SPR.resize((int(_SPR.width * K), int(_SPR.height * K)), Image.LANCZOS)
SHA = Image.new('RGBA', SPR.size, (0, 0, 0, 0)); SHA.putalpha(SPR.getchannel('A').filter(ImageFilter.GaussianBlur(16)))
TS = complex(HJ['tip'][0] * K, HJ['tip'][1] * K); WS = complex(WRIST[0] * K, WRIST[1] * K)
V0 = (WS - TS) / SC_VIEW                                          # tip -> wrist in spread units
RATCHET = 80.0                                                    # spread px the fingers can reach before the wrist slides
HS = {'w': None, 'tp': None, 'last_t': None, 'moving': False}


def ss(a):
    a = min(1.0, max(0.0, a)); return a * a * (3 - 2 * a)


def sst(a):
    a = min(1.0, max(0.0, a)); return a * a * a * (a * (a * 6 - 15) + 10)


REST_GAP, REST_MOVE = 2.5, 0.85


def tip_and_lift(info, t, view):
    """spread-space tip and lift 0..1 (0 = pen on the paper)"""
    vx0, vy0, sc = view
    rest = complex(vx0 + 1240 / sc, vy0 + 1900 / sc)                 # fully out of frame, lower right
    if info[0] == 'down':
        return complex(*info[1]), 0.0
    _, a, b, t0, t1 = info
    a = complex(*a) if a else rest; b = complex(*b) if b else rest
    gap = t1 - t0; u = min(1.0, max(0.0, (t - t0) / max(0.05, gap)))
    if gap < REST_GAP:                                              # glide to the next stroke, pen just off the paper
        return a + (b - a) * sst(u), math.sin(math.pi * u) * min(1.0, gap / 0.5)
    if t - t0 < REST_MOVE:                                          # slowly to rest
        return a + (rest - a) * sst((t - t0) / REST_MOVE), 1.0
    if t1 - t < REST_MOVE:                                          # slowly back
        return rest + (b - rest) * sst(1 - (t1 - t) / REST_MOVE), 1.0
    return rest, 1.0


def lp(key, val, dt, tau):
    """low-pass filter kept in HS"""
    if HS.get(key) is None: HS[key] = val
    else: HS[key] += (val - HS[key]) * (1 - math.exp(-dt / tau))
    return HS[key]


def draw_hand(im, info, view, t):
    if info is None: return im
    vx0, vy0, sc = view
    if abs(sc - SC_VIEW) > 0.02: return im                          # only in the close views
    tip, lift = tip_and_lift(info, t, view)
    dt = 1 / FPS if HS['last_t'] is None or t < HS['last_t'] else min(0.2, t - HS['last_t']); HS['last_t'] = t
    lift = lp('lift', lift, dt, 0.10)
    tip = lp('tip', tip, dt, 0.06)                                   # tiny lag: removes the hops, the pen stays on the line
    wr = lp('w', tip + V0, dt, 0.45)                                  # the forearm drifts slowly, it never jumps
    P = complex((tip.real - vx0) * sc, (tip.imag - vy0) * sc); Wr = complex((wr.real - vx0) * sc, (wr.imag - vy0) * sc)
    a = (P - Wr) / (TS - WS)
    r, th = abs(a), math.atan2(a.imag, a.real)
    r, th = 1.0, 0.0                                                  # rigid hand: it only glides, never rocks
    a = r * (1 + 0.012 * lift) * complex(math.cos(th), math.sin(th))
    bb = P - a * TS                                                   # pen tip exactly on the (smoothed) tip
    c = 1 / a; off = -c * bb
    data = (c.real, -c.imag, off.real, c.imag, c.real, off.imag)
    hand = SPR.transform((W, H), Image.AFFINE, data, Image.BICUBIC)
    sdx, sdy = 22 + 14 * lift, 30 + 18 * lift
    off2 = -c * (bb + complex(sdx, sdy))
    sh = SHA.transform((W, H), Image.AFFINE, (c.real, -c.imag, off2.real, c.imag, c.real, off2.imag), Image.BILINEAR)
    sha = sh.getchannel('A').point(lambda v: int(v * (0.27 - 0.04 * lift)))
    base = im.convert('RGBA')
    base.paste((28, 26, 24, 255), (0, 0), sha)
    base.alpha_composite(hand)
    return base.convert('RGB')


ar.state_at = state_at
ar.draw_hand = draw_hand

if __name__ == '__main__':
    args = sys.argv[1:]
    if '--frames' in args:
        ts = [float(x) for x in args[args.index('--frames') + 1].split(',')]
        t = 0.0; want = sorted(ts)
        start = max(0.0, want[0] - 3.0)
        f = int(start * FPS)
        while want:
            t = f / FPS
            im = ar.frame(t)
            if t >= want[0] - 1e-6:
                Image.fromarray(ar.grain(im, t)).save(os.path.join(R, f'hf_{want[0]:06.2f}.jpg'), quality=88); want.pop(0)
            f += 1
        sys.exit()
    a, b = 0.0, ar.TOTAL
    if '--range' in args: a, b = [float(x) for x in args[args.index('--range') + 1].split(',')]
    out = args[args.index('--out') + 1] if '--out' in args else os.path.join(R, 'human_noaudio.mp4')
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
    for f in range(int(a * FPS), int(b * FPS)):
        t = f / FPS
        p.stdin.write(ar.grain(ar.frame(t), t).tobytes())
        if f % 300 == 0: print(f, flush=True)
    p.stdin.close(); p.wait(); print('done', out)
