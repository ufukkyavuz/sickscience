# Sketchbook flip demo: no drawing hand. Each page's drawing appears piece by piece as the narrator speaks,
# then the page is flipped up like a top-bound sketch pad and the next page is underneath.
import os, sys, math, subprocess
import numpy as np, cv2
from scipy import ndimage

BASE = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma/video-brand-story-drawn")
D = os.path.join(BASE, 'sketch_scenes', 'master')
OUT = os.path.join(BASE, 'sketch_flip_demo.mp4')
VO = os.path.expanduser('~/sickscience-work/brandfilm/v5/vo')
W, H, FPS = 1080, 1920, 30
SCENES = ['m01_two_minds', 'm02_met_2009', 'm03_research', 'm12_thats_sick']
LINES = [os.path.join(VO, f'l{i + 1}.wav') for i in range(len(SCENES))]
LEAD, TAIL, FLIP = 0.35, 0.8, 1.8                     # VO starts LEAD after the page settles; hold TAIL; flip time

MASTER = cv2.resize(cv2.cvtColor(cv2.imread(os.path.join(BASE, 'sketch_scenes', 'master_blank.png')), cv2.COLOR_BGR2RGB), (W, H), interpolation=cv2.INTER_AREA).astype(np.float32)


def dur(p): return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', p]))


def prep(name):
    im = cv2.resize(cv2.cvtColor(cv2.imread(os.path.join(D, name + '.png')), cv2.COLOR_BGR2RGB), (W, H), interpolation=cv2.INTER_AREA)
    hsv = cv2.cvtColor(im, cv2.COLOR_RGB2HSV)
    L = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY).astype(np.float32)
    bg = cv2.medianBlur(L.astype(np.uint8), 41).astype(np.float32)
    ink = ((bg - L) > 18) | ((hsv[..., 1] > 60) & (hsv[..., 2] > 60))
    lab, n = ndimage.label(ink); sizes = ndimage.sum(ink, lab, range(1, n + 1))
    ink = np.isin(lab, np.where(sizes >= 10)[0] + 1)
    inkd = ndimage.binary_dilation(ink, iterations=2)
    paper = (~ndimage.binary_dilation(inkd, iterations=25)).astype(np.float32)          # light measured on bare paper only
    low = cv2.GaussianBlur(im.astype(np.float32) * paper[..., None], (0, 0), 90) / np.maximum(cv2.GaussianBlur(paper, (0, 0), 90), 1e-3)[..., None]
    mlow = cv2.GaussianBlur(MASTER, (0, 0), 90)
    blank = np.clip(MASTER * (low / np.maximum(mlow, 1)), 0, 255).astype(np.uint8)
    # pieces: ink grouped by proximity (words stay whole, separate drawings stay separate), read top-down, left-right
    glab, gn = ndimage.label(cv2.dilate(inkd.astype(np.uint8), np.ones((15, 45), np.uint8)) > 0)   # words/rows stay whole
    objs = ndimage.find_objects(glab)
    area = {g: int((inkd & (glab == g)).sum()) for g in range(1, gn + 1)}
    edge = {g for g in area if objs[g - 1][0].start == 0 or objs[g - 1][1].start == 0 or objs[g - 1][0].stop >= H or objs[g - 1][1].stop >= W}
    big = [g for g in area if area[g] >= 6000 and g not in edge]
    cen = {g: ((objs[g - 1][0].start + objs[g - 1][0].stop) / 2, (objs[g - 1][1].start + objs[g - 1][1].stop) / 2) for g in area}
    owner = {g: g for g in big}
    for g in area:                                         # small specks join the nearest real piece
        if g not in owner and big:
            owner[g] = min(big, key=lambda b: (cen[b][0] - cen[g][0]) ** 2 + (cen[b][1] - cen[g][1]) ** 2)
    big.sort(key=lambda g: (objs[g - 1][0].start // 140, objs[g - 1][1].start))
    pieces = []
    for g in big:
        m = inkd & np.isin(glab, [h for h in owner if owner[h] == g])
        ys, xs = np.where(m)
        soft = cv2.GaussianBlur(ndimage.binary_dilation(m, iterations=2).astype(np.float32), (0, 0), 1.5)
        pieces.append(dict(m=soft, box=(xs.min(), ys.min(), xs.max() + 1, ys.max() + 1)))
    return dict(im=im.astype(np.float32), blank=blank.astype(np.float32), pieces=pieces)


SC = [prep(s) for s in SCENES]
D_ = [dur(p) for p in LINES]
T0 = []; t = 0.6
for d in D_:
    T0.append(t); t += LEAD + d + TAIL + FLIP
TOTAL = t
for sc, t0, d in zip(SC, T0, D_):                         # each piece lands while its part of the line is spoken
    n = len(sc['pieces'])
    for i, pc in enumerate(sc['pieces']):
        pc['t'] = t0 + LEAD * 0.5 + d * 0.8 * (i / max(1, n))
print([len(s['pieces']) for s in SC], round(TOTAL, 1), flush=True)


def ss(a): a = min(1, max(0, a)); return a * a * a * (a * (a * 6 - 15) + 10)


def page_img(k, t):
    sc = SC[k]; img = sc['blank'].copy()
    for pc in sc['pieces']:
        a = (t - pc['t']) / 0.35
        if a <= 0: continue
        a = ss(a)
        x0, y0, x1, y1 = pc['box']
        # ink appears with a short left-to-right sweep inside the piece (like it is being revealed, not faded)
        sweep = np.clip(((np.arange(W)[None, :] - x0) / max(1, (x1 - x0)) - a * 1.3 + 0.3) * -6 + 1, 0, 1) if a < 1 else 1.0
        mm = pc['m'] * sweep
        img = img * (1 - mm[..., None]) + sc['im'] * mm[..., None]
    return img


XX, YY = np.meshgrid(np.arange(W, dtype=np.float32), np.arange(H, dtype=np.float32))
_g = cv2.GaussianBlur(cv2.cvtColor(MASTER.astype(np.uint8), cv2.COLOR_RGB2GRAY).astype(np.float32), (0, 0), 25)
LIGHT = (_g / np.percentile(_g, 97))[..., None]                   # the room light on the sheet (window band + shade)


def flip(top, under, a):
    """real page curl: the sheet rolls over a cylinder from the bottom-right corner toward the spine on the left.
    front stays flat behind the roll, the rolled part shows the paper's back (lighter, faint mirrored ink), the
    page below gets a soft contact shadow along the roll"""
    a = min(1.0, max(0.0, a))
    a = a * a * 2 if a < 0.25 else (1 - (1 - a) ** 2 * 2 if a > 0.75 else 0.125 + (a - 0.25) * 1.5)   # soft start/end, steady sweep
    R = 110.0 + 60.0 * math.sin(math.pi * a)                       # roll radius grows mid-turn
    n = np.array([0.82, 0.57], np.float32); n /= np.linalg.norm(n)  # axis normal points to the bottom-right corner
    far = np.dot(np.array([W, H], np.float32), n); near = -math.pi * R - 40
    c = far + 20 - a * (far + 20 - near)                          # axis position along n (moves from the corner past the spine)
    d = XX * n[0] + YY * n[1] - c                                  # signed distance of every pixel to the axis
    out = under.astype(np.float32).copy()
    # shadow of the lifted sheet on the page below (strongest right next to the roll)
    sh = np.clip(1 - (d - R) / (90 + 2.0 * R), 0, 1) * (d > R) * 0.45
    out *= (1 - sh[..., None])
    inside = lambda sx, sy: (sx >= 0) & (sx <= W - 1) & (sy >= 0) & (sy <= H - 1)
    # 1) flat front of the sheet, behind the roll
    front_flat = d < 0
    # 2) the roll itself: lower (front) and upper (back) halves of the cylinder
    on = (d >= 0) & (d <= R)
    asn = np.arcsin(np.clip(d / R, -1, 1))
    s_front = R * asn                                             # arc length on the front half
    s_back = R * (math.pi - asn)                                  # arc length on the back half
    sxf, syf = XX - n[0] * (d - s_front), YY - n[1] * (d - s_front)
    sxb, syb = XX - n[0] * (d - s_back), YY - n[1] * (d - s_back)
    # 3) the part already turned over lies flat on top again (back side up)
    s_flat = math.pi * R - 2.8 * d                                # d < 0 here; the turned part stands up toward the camera, so it reads foreshortened
    sxl, syl = XX - n[0] * (d - s_flat), YY - n[1] * (d - s_flat)
    back_flat = (d < 0) & inside(sxl, syl)
    back_roll = on & inside(sxb, syb)
    front_roll = on & ~back_roll & inside(sxf, syf)
    topf = top.astype(np.float32)
    # paper back: blank paper colour, light from the upper left, with the ink faintly showing through mirrored
    paper = np.array([238, 233, 224], np.float32)
    def back_px(sx, sy):
        ink = cv2.remap(topf, sx, sy, cv2.INTER_LINEAR)
        show = (0.94 * paper + 0.06 * ink) * LIGHT
        return show
    res = out
    m = front_flat & ~back_flat
    res[m] = topf[m]
    # front half of the roll: compressed, darker toward the crest
    if front_roll.any():
        f = cv2.remap(topf, sxf, syf, cv2.INTER_LINEAR)
        light = (0.78 + 0.22 * np.cos(asn))[..., None]
        res = np.where(front_roll[..., None], f * light, res)
    # back half of the roll + the flat turned-over part, lit by the window (brighter on the crest, shade at the fold)
    if back_roll.any() or back_flat.any():
        bk = back_px(sxb, syb)
        lr = (0.86 + 0.14 * np.cos(asn) + 0.06 * (d / R))[..., None]
        res = np.where(back_roll[..., None], bk * lr, res)
        bl = back_px(sxl, syl)
        fold = np.clip(-d / (1.6 * R), 0, 1)
        lf = (0.97 - 0.12 * fold)[..., None]                       # rising flap turns away from the window light
        # soft shadow the turned flap throws onto the flat front just behind the fold
        res = np.where(back_flat[..., None], bl * lf, res)
        rim = back_flat & (np.abs(d) < 6)
        res[rim] *= 0.93
    # thin dark line where the roll meets the page below
    edge = (d > R - 2) & (d < R + 3) & inside(sxb, syb)
    res[edge] *= 0.85
    return res


FLIPS = os.path.expanduser('~/sickscience-work/brandfilm/v5/flips')
_fc = {}


def flip3d(name, under, a):
    """Blender-rendered page turn (page layer with alpha) over the next blank page, with its contact shadow"""
    fs = sorted(os.listdir(os.path.join(FLIPS, name)))
    i = min(len(fs) - 1, max(0, int(round(a * (len(fs) - 1)))))
    key = (name, i)
    if key not in _fc:
        _fc.clear()
        _fc[key] = cv2.cvtColor(cv2.imread(os.path.join(FLIPS, name, fs[i]), cv2.IMREAD_UNCHANGED), cv2.COLOR_BGRA2RGBA).astype(np.float32)
    pg = _fc[key]
    al = pg[..., 3] / 255.0
    sh = cv2.GaussianBlur(np.roll(np.roll(al, 34, 0), 26, 1), (0, 0), 26) * 0.38
    out = under * (1 - sh[..., None])
    return out * (1 - al[..., None]) + pg[..., :3] * al[..., None]


def frame(t):
    k = 0
    while k + 1 < len(SC) and t >= T0[k + 1]: k += 1
    img = page_img(k, t)
    tf = T0[k + 1] - FLIP if k + 1 < len(SC) else 1e9
    if t >= tf:
        img = flip3d(SCENES[k], SC[k + 1]['blank'], (t - tf) / FLIP)
    return np.clip(img, 0, 255).astype(np.uint8)


# audio: lines at their scene starts + a soft paper flip
import wave
sr = 48000
mix = np.zeros(int((TOTAL + 1) * sr), np.float32)
for p_, t0 in zip(LINES, T0):
    with wave.open(p_) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32) / 32768
    i0 = int((t0 + LEAD) * sr); mix[i0:i0 + len(x)] += x * 0.9
rng = np.random.default_rng(3)
for k in range(1, len(SC)):                                 # paper flip: filtered noise burst
    i0 = int((T0[k] - FLIP) * sr); n = int(0.5 * sr)
    nz = rng.standard_normal(n).astype(np.float32)
    nz = np.convolve(nz, np.ones(30) / 30, 'same') * np.sin(np.linspace(0, math.pi, n)) ** 2 * 0.5
    mix[i0:i0 + n] += nz
wav = os.path.join(VO, 'flip_mix.wav')
with wave.open(wav, 'w') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes((np.clip(mix, -1, 1) * 32767).astype(np.int16).tobytes())

p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-i', wav,
                      '-c:v', 'libx264', '-crf', '21', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '160k', '-shortest', OUT], stdin=subprocess.PIPE)
for f in range(int(TOTAL * FPS)):
    p.stdin.write(np.ascontiguousarray(frame(f / FPS)).tobytes())
p.stdin.close(); p.wait(); print('done', OUT)
