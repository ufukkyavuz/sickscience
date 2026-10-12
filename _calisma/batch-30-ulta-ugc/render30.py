"""Batch 30 — Ulta Beauty holiday UGC (≤20 s each, 9:16). Gifting angle from Ulta's FY26 Holiday playbook; no prices
(Ulta promos not approved yet). Talking clips: Kling 3.0 with own voices (product names never spoken). Product beats:
the real PNGs composited on generated empty holiday tabletops. End card: official Ulta logo, "Only at Ulta Beauty",
@ultabeauty #UltaBeauty. Streams frames (see memory feedback-render-memory).
usage: python render30.py u1|u2|u3   -> out/u30_<v>_voice.mp4 + out/u30_<v>_cues.json  (music: music30.py)"""
import os, sys, json, math, subprocess, tempfile, shutil, collections
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__)); SS = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(SS, '_calisma', 'batch-28-video'))
os.chdir(os.path.join(SS, '_calisma', 'batch-28-video'))            # render28/29 resolve their paths relative to here
import render29 as R                                                # spring, k_headline, caption, top_shade, whip, punch, Reader, stars
CL, ST, OUT = os.path.join(HERE, 'clips'), os.path.join(HERE, 'stills'), os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)
W, H, FPS, SR = 1080, 1920, 24, 48000
FF = shutil.which('ffmpeg'); FD = os.path.expanduser('~/Library/Fonts/')
FB, FM, FR = FD + 'FoundersGrotesk-Bold.otf', FD + 'FoundersGrotesk-Medium.otf', FD + 'FoundersGrotesk-Regular.otf'
MAGENTA, ORANGE, INK = (233, 11, 90), (227, 82, 0), (24, 18, 22)
WORDS = json.load(open(os.path.join(CL, 'words.json')))
FIX = {'ulta': 'Ulta'}
def font(p, s): return ImageFont.truetype(p, s)

def words(name, a0, a1):
    out = []
    for w, s, e in WORDS[name]:
        if a0 - 0.05 <= s < a1:
            k = w.strip('.,!?').lower(); out.append((FIX.get(k, w.strip('.,!?')), s - a0, e - a0))
    return out

class ClipReader(R.Reader):                         # same streaming reader, pointed at this batch's clips
    def _open(self, idx):
        self.close(); vf = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}'
        self.p = subprocess.Popen([FF, '-v', 'error', '-ss', f'{idx / FPS:.4f}', '-i', os.path.join(CL, self.name + '.mp4'),
                                   '-vf', vf, '-r', str(FPS), '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
        self.pos = idx - 1; self.last = None

# ---------- product stage: real PNG on an empty generated tabletop
PNG = {'ss': 'ERH_7470B', 'nw': 'ERH_7477C', 'pc': 'ERH_7460B', 'do': 'ERH_7488'}
HPX = {'ss': 700, 'nw': 700, 'pc': 784, 'do': 1060}      # real-scale relative heights (12.5 / 12.5 / 14 / 19 cm)
_png = {}
def product(k):
    if k not in _png:
        p = Image.open(os.path.join(SS, 'Products/png', PNG[k] + '.png')).convert('RGBA'); p = p.crop(p.split()[-1].getbbox())
        _png[k] = p.resize((round(p.width * HPX[k] / p.height), HPX[k]), Image.LANCZOS)
    return _png[k]
_bg = {}
def bg(name):
    if name not in _bg:
        im = Image.open(os.path.join(ST, name + '.png')).convert('RGB'); s = max(W / im.width, H / im.height)
        im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
        _bg[name] = im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H))
    return _bg[name]

def stage(t, bgname, k, base=1330, title=None, line=None, num=None):
    sc = 1.0 + 0.035 * min(1, t / 3.0)                          # slow push on the background
    b = bg(bgname); im = b.resize((round(W * sc), round(H * sc)), Image.BILINEAR)
    im = im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H)).convert('RGBA')
    p = product(k); s = R.spring(t - 0.05, 230, 20); y = base - p.height - (1 - s) * 140; x = (W - p.width) // 2
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).ellipse((W / 2 - p.width * 0.62, base - 16, W / 2 + p.width * 0.62, base + 18), fill=int(150 * s))
    im = Image.composite(Image.new('RGBA', (W, H), (60, 20, 40, 255)), im, sh.filter(ImageFilter.GaussianBlur(14)).point(lambda v: v * 0.6))
    refl = p.transpose(Image.FLIP_TOP_BOTTOM); g = np.linspace(0.22, 0, refl.height)[:, None]
    ra = (np.asarray(refl.getchannel('A')).astype(np.float32) * g * s).astype(np.uint8); refl.putalpha(Image.fromarray(ra))
    im.paste(refl, (x, base + 4), refl); im.paste(p, (x, int(y)), p)
    im = R.top_shade(im.convert('RGB'))
    if title:
        d = ImageDraw.Draw(im)
        if num: d.text((65, 290), num, font=font(FB, 64), fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))
        R.k_headline(im, title, t, y=360 if num else 300, size=70)
    if line and t > 0.35:
        d = ImageDraw.Draw(im, 'RGBA'); f = font(FM, 42); a = min(1, (t - 0.35) * 5)
        lines = R.wrap(d, line, f, 900); yy = 1400
        for i, ln in enumerate(lines):
            tw = d.textlength(ln, font=f); d.text(((W - tw) / 2, yy + i * 50), ln, font=f, fill=(255, 255, 255, int(255 * a)), stroke_width=2, stroke_fill=(0, 0, 0, int(200 * a)))
    return im

# ---------- Ulta end card (light blush so the pink 'Science' and the orange Ulta logo both read)
def endcard(photo):
    im = Image.open(os.path.join(ST, photo + '.png')).convert('RGB'); sc = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    im = im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H)).convert('RGBA')
    d = ImageDraw.Draw(im)
    lg = Image.open(os.path.join(SS, 'output/video-01-bcrf/assets/logo.png')).convert('RGBA').resize((340, 46), Image.LANCZOS)
    ul = Image.open(os.path.join(SS, 'Ulta/logo/ulta_logo_orange.png')).convert('RGBA'); ul = ul.resize((250, round(250 * ul.height / ul.width)), Image.LANCZOS)
    xx = (W - (340 + 70 + 250)) // 2; im.paste(lg, (xx, 300), lg)
    d.text((xx + 340 + 22, 292), '×', font=font(FM, 48), fill=INK); im.paste(ul, (xx + 340 + 70, 316 - ul.height // 2 + 6), ul)
    f = font(FB, 76); a_, b_ = 'ONLY AT ', 'ULTA BEAUTY'; tw = d.textlength(a_ + b_, font=f); x0 = (W - tw) / 2   # one line: ends above the tallest product
    d.text((x0, 398), a_, font=f, fill=INK); d.text((x0 + d.textlength(a_, font=f), 398), b_, font=f, fill=MAGENTA)
    f = font(FM, 36); txt = '@ultabeauty  #UltaBeauty'; tw = d.textlength(txt, font=f); d.text(((W - tw) / 2, 500), txt, font=f, fill=INK)
    return im.convert('RGB')

# ---------- videos
def clip_seg(name, a0=None, a1=None, draw=None, who='?'):
    w = WORDS[name]; a0 = max(0, w[0][1] - 0.15) if a0 is None else a0; a1 = w[-1][2] + 0.3 if a1 is None else a1
    return dict(kind='clip', name=name, a0=a0, a1=a1, draw=draw, who=who)

def wst(name, key):
    for w, s, e in WORDS[name]:
        if w.lower().strip('.,?!').startswith(key): return s
    return None

def u1():
    n = 'u30_c1_ss_talk'; t_two = wst(n, 'two')
    def f(im, t, ws):
        im = R.top_shade(im)
        R.k_headline(im, 'MY HOLIDAY GIFT TO ME' if t < (t_two or 9) - 0.15 else '1–2 PUMPS · UPWARD · AM & PM', t, t0=0 if t < (t_two or 9) - 0.15 else (t_two - 0.15))
        R.caption(im, ws, t); return im
    def macro(im, t, ws):
        im = R.top_shade(im); R.k_headline(im, 'HELPS VISIBLY TIGHTEN & FIRM THE NECK', t, size=70); return im
    return [clip_seg(n, draw=f, who='E'),
            dict(kind='clip', name='u30_c4_ss_macro', a0=0.2, a1=2.9, draw=macro, who='M', silent=True)], 'ec_ss'

def stage_draw(title, line=None, num=None):
    def f(im, t, ws):
        im = R.top_shade(im); d = ImageDraw.Draw(im)
        if num: d.text((65, 290), num, font=font(FB, 64), fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))
        yb = R.k_headline(im, title, t, y=360 if num else 300, size=70)
        if line and t > 0.35:                       # product name sits under the headline, never on the product
            d = ImageDraw.Draw(im, 'RGBA'); fo = font(FM, 42); a = min(1, (t - 0.35) * 5)
            for i, ln in enumerate(R.wrap(d, line, fo, 950)):
                d.text((65, yb + 14 + i * 50), ln, font=fo, fill=(255, 255, 255, int(255 * a)), stroke_width=2, stroke_fill=(0, 0, 0, int(200 * a)))
        return im
    return f

def sclip(name, draw, dur=2.6, who='M'):
    return dict(kind='clip', name=name, a0=0.15, a1=0.15 + dur, draw=draw, who=who, silent=True)

def u2():
    n = 'u30_c2_pc_talk'
    def f(im, t, ws): im = R.top_shade(im); R.k_headline(im, 'STOCKING STUFFER, UPGRADED.', t); R.caption(im, ws, t); return im
    return [clip_seg(n, draw=f, who='F'), sclip('u30_s_pc', stage_draw('89% EXPERIENCED IMPROVEMENT OF HAIR DENSITY', 'PowerCycle Scalp Treatment Serum'))], 'ec_pc'

def u3():
    n = 'u30_c3_gift_talk'
    def f(im, t, ws): im = R.top_shade(im); R.k_headline(im, '3 GIFTS FOR THE SKINCARE LOVER', t); R.caption(im, ws, t); return im
    return [clip_seg(n, draw=f, who='G'),
            sclip('u30_s_nw', stage_draw('REVEAL YOUR GLOW IN 2 WEEKS', 'NetWork Rich Concentrated Serum', '01'), 2.4, 'M1'),
            sclip('u30_s_ss', stage_draw('HELPS VISIBLY TIGHTEN & FIRM THE NECK', 'ShapeShift Advanced Jaw & Neck Firming Serum', '02'), 2.4, 'M2'),
            sclip('u30_s_do', stage_draw('VISIBLY SMOOTHS THE LOOK OF CELLULITE & STRETCH MARKS', 'DropOff Body Sculpting Serum', '03'), 2.4, 'M3')], 'ec_trio'

VIDEOS = {'u1': u1, 'u2': u2, 'u3': u3}
END = 2.0

def render(v):
    segs, ecphoto = VIDEOS[v](); tmp = tempfile.mkdtemp(prefix=f'u30_{v}_')
    auds, sfx, tout, plan = [], [], 0.0, []
    for i, s in enumerate(segs):
        dur = (s['a1'] - s['a0']) if s['kind'] == 'clip' else s['dur']; n = round(dur * FPS)
        if s['kind'] == 'clip' and not s.get('silent'):
            raw = subprocess.run([FF, '-v', 'error', '-ss', str(s['a0']), '-t', str(dur), '-i', os.path.join(CL, s['name'] + '.mp4'),
                                  '-ac', '2', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True).stdout
            a = np.frombuffer(raw, np.int16).reshape(-1, 2).astype(np.float32)
        else: a = np.zeros((0, 2), np.float32)
        m = round(n / FPS * SR); a = np.pad(a, ((0, max(0, m - len(a))), (0, 0)))[:m]
        f_ = min(len(a), int(.015 * SR)); rr = np.linspace(0, 1, f_)[:, None]; a[:f_] *= rr; a[-f_:] *= rr[::-1]; auds.append(a)
        if i > 0: sfx.append((round(tout, 3), 'whoosh'))
        if s['kind'] == 'still': sfx.append((round(tout + 0.1, 3), 'pop'))
        plan.append((s, n)); tout += n / FPS
    nend = round(END * FPS); sfx.append((round(tout, 3), 'thump')); total = sum(n for _, n in plan) + nend
    auds.append(np.zeros((round(END * SR), 2), np.float32)); a = np.concatenate(auds)
    json.dump({'duration': total / FPS, 'end': tout, 'sfx': sfx}, open(os.path.join(OUT, f'u30_{v}_cues.json'), 'w'))
    rawp = os.path.join(tmp, 'a.raw'); np.clip(a, -32768, 32767).astype(np.int16).tofile(rawp); tmp_out = os.path.join(tmp, 'o.mp4')
    enc = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', rawp, '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18',
                            '-c:a', 'aac', '-b:a', '192k', '-shortest', tmp_out], stdin=subprocess.PIPE)
    q = collections.deque()
    def emit(im):
        q.append(im)
        if len(q) > 3: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    for i, (s, n) in enumerate(plan):
        if i > 0:
            for j, amt in enumerate((0.25, 0.6, 1.0)[-len(q):]): q[j] = R.whip(q[j], amt, -1)
        rd = ClipReader(s['name'], 1.0) if s['kind'] == 'clip' else None
        ws = words(s['name'], s['a0'], s['a1']) if s['kind'] == 'clip' and not s.get('silent') else []
        for k in range(n):
            t = k / FPS
            im = s['draw'](rd.get(round((s['a0'] + t) * FPS)), t, ws) if rd else s['fn'](t)
            if i > 0 and k < 3: im = R.whip(im, (1.0, 0.6, 0.25)[k], 1)
            emit(im)
        if rd: rd.close()
    ec = endcard(ecphoto)
    for k in range(nend):
        t = k / FPS; sc = 1.06 - 0.06 * R.spring(t, 200, 22); im = ec.resize((round(W * sc), round(H * sc)), Image.LANCZOS)
        emit(im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H)))
    while q: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    enc.stdin.close(); enc.wait()
    shutil.copy(tmp_out, os.path.join(OUT, f'u30_{v}_voice.mp4')); shutil.rmtree(tmp, ignore_errors=True)
    subprocess.run([FF, '-v', 'error', '-y', '-i', os.path.join(OUT, f'u30_{v}_voice.mp4'), '-vf', 'fps=2,scale=180:-1,tile=8x6',
                    '-frames:v', '1', os.path.join(OUT, f'u30_{v}_contact.jpg')])
    print(v, 'ok', round(total / FPS, 1), 's')

if __name__ == '__main__':
    for v in sys.argv[1:] or list(VIDEOS): render(v)
