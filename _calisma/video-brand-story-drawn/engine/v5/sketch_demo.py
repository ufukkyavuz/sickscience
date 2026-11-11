# Sketchbook demo: each scene = one real-looking sketch page (Higgsfield), its ink revealed stroke by stroke under the real
# writing hand, then the finished sheet is pulled off the pad and the next page starts. Silent rough cut to show the idea.
import os, sys, math, json, subprocess
import numpy as np, cv2
from PIL import Image, ImageFilter
from scipy import ndimage
sys.path.insert(0, os.path.expanduser('~/sickscience-work/brandfilm/v4'))
from skimage.morphology import skeletonize

D = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma/video-brand-story-drawn/sketch_scenes/master")
OUT = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma/video-brand-story-drawn/sketch_demo.mp4")
W, H, FPS = 1080, 1920, 30
SCENES = sys.argv[1].split(',') if len(sys.argv) > 1 else ['m01_two_minds', 'm02_met_2009', 'm03_research', 'm12_thats_sick']
DRAW, HOLD, PULL = 3.6, 0.9, 0.7


MASTER = cv2.resize(cv2.cvtColor(cv2.imread(os.path.join(os.path.dirname(D), 'master_blank.png')), cv2.COLOR_BGR2RGB), (W, H), interpolation=cv2.INTER_AREA).astype(np.float32)


def prep(name):
    im = cv2.cvtColor(cv2.imread(os.path.join(D, name + '.png')), cv2.COLOR_BGR2RGB)
    im = cv2.resize(im, (W, H), interpolation=cv2.INTER_AREA)
    lab = cv2.cvtColor(im, cv2.COLOR_RGB2HSV)
    L = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY).astype(np.float32)
    bg = cv2.medianBlur(L.astype(np.uint8), 41).astype(np.float32)
    ink = ((bg - L) > 22) | ((lab[..., 1] > 70) & (lab[..., 2] > 60))
    ink = ndimage.binary_opening(ink, iterations=1)
    lab_, n = ndimage.label(ink); sizes = ndimage.sum(ink, lab_, range(1, n + 1))
    ink = np.isin(lab_, np.where(sizes >= 12)[0] + 1)
    inkd = ndimage.binary_dilation(ink, iterations=3)
    inp = cv2.inpaint(im, ndimage.binary_dilation(inkd, iterations=6).astype(np.uint8) * 255, 9, cv2.INPAINT_TELEA).astype(np.float32)
    # clean paper: the real blank master page, relit with this scene's very-low-frequency light (no ghost of the drawing)
    low = cv2.GaussianBlur(inp, (0, 0), 90); mlow = cv2.GaussianBlur(MASTER, (0, 0), 90)
    blank = np.clip(MASTER * (low / np.maximum(mlow, 1)), 0, 255).astype(np.uint8)
    # stroke order: skeleton, glyph groups left to right inside rows, greedy path following
    sk = skeletonize(inkd)
    glab, gn = ndimage.label(ndimage.binary_dilation(inkd, iterations=6))
    objs = ndimage.find_objects(glab)
    groups = sorted(range(1, gn + 1), key=lambda g: (objs[g - 1][0].start // 160, objs[g - 1][1].start))
    key = np.full(ink.shape, np.inf, np.float32); path = []; Lc = 0.0
    N8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for g in groups:
        sl = objs[g - 1]
        ys, xs = np.where(sk[sl] & (glab[sl] == g))
        pts = set(zip(ys + sl[0].start, xs + sl[1].start))
        cur = None
        while pts:
            nb = [(cur[0] + dy, cur[1] + dx) for dy, dx in N8 if (cur[0] + dy, cur[1] + dx) in pts] if cur else []
            if nb:
                nxt = nb[0]; Lc += math.hypot(nxt[0] - cur[0], nxt[1] - cur[1])
            else:
                left = min(p[1] for p in pts); cand = [p for p in pts if p[1] <= left + 6]
                nxt = min(cand, key=lambda p: (p[1], p[0])); Lc += 4.0 if cur else 0.0
            pts.discard(nxt); key[nxt] = Lc; path.append((nxt[1], nxt[0], Lc)); cur = nxt
        Lc += 25.0
    fin = np.isfinite(key)
    _, (iy, ix) = ndimage.distance_transform_edt(~fin, return_indices=True)
    tm = key[iy, ix]; tm[~inkd] = np.inf
    return dict(im=im, blank=blank, ink=inkd, tm=tm, path=path, L=Lc)


SC = [prep(s) for s in SCENES]
print('prepared', flush=True)

# hand sprite (same real hand as the notebook film)
HD = os.path.expanduser('~/sickscience-work/brandfilm/v4/hand')
HJ = json.load(open(os.path.join(HD, 'hand.json')))
spr = Image.open(os.path.join(HD, HJ['file'])).convert('RGBA')
K = 52.0 / HJ['px_per_cm']                                    # ~52 px per cm at this framing (sheet ~21 cm wide)
SPR = spr.resize((int(spr.width * K), int(spr.height * K)), Image.LANCZOS)
SHA = Image.new('RGBA', SPR.size, (0, 0, 0, 0)); SHA.putalpha(SPR.getchannel('A').filter(ImageFilter.GaussianBlur(14)))
TX, TY = HJ['tip'][0] * K, HJ['tip'][1] * K
REST = (1250.0, 2100.0)
HS = {'p': None}


def ss(a): a = min(1, max(0, a)); return a * a * a * (a * (a * 6 - 15) + 10)


def tip_at(sc, u):
    if not sc['path']: return None
    target = u * sc['L']; arr = sc['_Ls'] if '_Ls' in sc else sc.setdefault('_Ls', np.array([p[2] for p in sc['path']]))
    i = min(len(arr) - 1, int(np.searchsorted(arr, target)))
    seg = sc['path'][max(0, i - 6):i + 7]
    return (sum(p[0] for p in seg) / len(seg), sum(p[1] for p in seg) / len(seg))


def hand(frame, tip, lift):
    p = HS['p'] = tip if HS['p'] is None else (HS['p'][0] + (tip[0] - HS['p'][0]) * 0.35, HS['p'][1] + (tip[1] - HS['p'][1]) * 0.35)
    base = Image.fromarray(frame).convert('RGBA')
    ox, oy = int(p[0] - TX), int(p[1] - TY)
    sh = SHA.getchannel('A').point(lambda v: int(v * (0.26 - 0.06 * lift)))
    base.paste((30, 28, 26, 255), (ox + 22 + int(20 * lift), oy + 30 + int(26 * lift)), sh)
    base.alpha_composite(SPR, (ox, oy))
    return np.asarray(base.convert('RGB'))


def page(sc, t):
    """sheet at local time t of its drawing"""
    u = min(1.0, max(0.0, t / DRAW))
    img = sc['blank'].copy()
    vis = sc['tm'] <= u * sc['L']
    img[vis] = sc['im'][vis]
    return img, u


SEG = DRAW + HOLD + PULL
TOTAL = len(SC) * SEG
p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                      '-c:v', 'libx264', '-crf', '20', '-pix_fmt', 'yuv420p', OUT], stdin=subprocess.PIPE)
for f in range(int(TOTAL * FPS)):
    t = f / FPS; k = min(len(SC) - 1, int(t // SEG)); lt = t - k * SEG; sc = SC[k]
    img, u = page(sc, lt)
    if lt < DRAW + 0.05:
        tp = tip_at(sc, u) if 0 < u < 1 else None
        if lt < 0.45: tp, lift = (REST[0] + (tip_at(sc, 0.0)[0] - REST[0]) * ss(lt / 0.45), REST[1] + (tip_at(sc, 0.0)[1] - REST[1]) * ss(lt / 0.45)), 1.0
        else: lift = 0.0
        img = hand(img, tp or tip_at(sc, 0.999), lift)
    elif lt < DRAW + 0.5:
        a = ss((lt - DRAW) / 0.5); e = tip_at(sc, 0.999)
        img = hand(img, (e[0] + (REST[0] - e[0]) * a, e[1] + (REST[1] - e[1]) * a), 1.0)
    if lt > DRAW + HOLD and k + 1 < len(SC):                    # pull the sheet off the pad: next blank page underneath
        a = ss((lt - DRAW - HOLD) / PULL)
        under = SC[k + 1]['blank'].copy()
        M = cv2.getRotationMatrix2D((W * 0.1, H * 0.95), -14 * a, 1.0); M[0, 2] -= a * W * 1.15; M[1, 2] -= a * 120
        top = cv2.warpAffine(img, M, (W, H), borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0))
        mask = cv2.warpAffine(np.full((H, W), 255, np.uint8), M, (W, H))
        shadow = cv2.GaussianBlur(cv2.warpAffine(mask, np.float32([[1, 0, 28], [0, 1, 18]]), (W, H)), (0, 0), 25) / 255.0 * 0.35
        under = (under * (1 - shadow[..., None])).astype(np.uint8)
        img = np.where(mask[..., None] > 127, top, under).astype(np.uint8)
    p.stdin.write(np.ascontiguousarray(img).tobytes())
p.stdin.close(); p.wait(); print('done', OUT, round(TOTAL, 1))
