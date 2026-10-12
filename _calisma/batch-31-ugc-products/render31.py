"""Batch 31 — short product UGCs (≤15 s, 9:16) from Buzzfy formats: PowerCycle night routine, DropOff 'same mirror',
NetWork October/BCRF. Talking clips: Kling 3.0 with own voices (product names never spoken). Products are generated
inside every photo (never pasted). Brand end card on a generated packshot. Streams frames (memory feedback-render-memory).
usage: python render31.py p1|d1|n1   -> out/u31_<v>_voice.mp4 + cues  (music: music31.py)"""
import os, sys, json, subprocess, tempfile, shutil, collections
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__)); SS = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(SS, '_calisma', 'batch-28-video'))
os.chdir(os.path.join(SS, '_calisma', 'batch-28-video'))
import render29 as R
CL, ST, OUT = os.path.join(HERE, 'clips'), os.path.join(HERE, 'stills'), os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)
W, H, FPS, SR = 1080, 1920, 24, 48000
FF = shutil.which('ffmpeg'); FD = os.path.expanduser('~/Library/Fonts/')
FB, FM, FR = FD + 'FoundersGrotesk-Bold.otf', FD + 'FoundersGrotesk-Medium.otf', FD + 'FoundersGrotesk-Regular.otf'
INK, PINK = (24, 18, 22), (169, 33, 192)
WORDS = json.load(open(os.path.join(CL, 'words.json')))
def font(p, s): return ImageFont.truetype(p, s)

def words(name, a0, a1):
    return [(w.strip('.,!?'), s - a0, e - a0) for w, s, e in WORDS[name] if a0 - 0.05 <= s < a1]

class ClipReader(R.Reader):
    def _open(self, idx):
        self.close(); vf = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}'
        self.p = subprocess.Popen([FF, '-v', 'error', '-ss', f'{idx / FPS:.4f}', '-i', os.path.join(CL, self.name + '.mp4'),
                                   '-vf', vf, '-r', str(FPS), '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
        self.pos = idx - 1; self.last = None

def endcard(photo, name, sub, extra=None):
    """Brand end card on a generated packshot: logo, product name, sub line, optional extra lines (all ≥40 px)."""
    p = photo if os.path.isabs(photo) else os.path.join(ST, photo + '.png')
    im = Image.open(p).convert('RGB'); sc = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    im = im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H)).convert('RGBA')
    d = ImageDraw.Draw(im)
    lg = Image.open(os.path.join(SS, 'output/video-01-bcrf/assets/logo.png')).convert('RGBA'); lg = lg.resize((380, round(380 * lg.height / lg.width)), Image.LANCZOS)
    im.paste(lg, ((W - lg.width) // 2, 275), lg)                 # compact block: must end above the product cap (~y 620)
    f = font(FB, 84); tw = d.textlength(name, font=f); d.text(((W - tw) / 2, 340), name, font=f, fill=INK); y = 432
    if sub: f = font(FR, 40); tw = d.textlength(sub, font=f); d.text(((W - tw) / 2, y), sub, font=f, fill=INK); y += 58
    if extra:
        f = font(FM, 40)
        for ln in extra:
            tw = d.textlength(ln, font=f); d.text(((W - tw) / 2, y), ln, font=f, fill=PINK); y += 46
    return im.convert('RGB')

def clip_seg(name, draw, who='?'):
    w = WORDS[name]; return dict(name=name, a0=max(0, w[0][1] - 0.15), a1=w[-1][2] + 0.3, draw=draw, who=who)

def sclip(name, draw, a0=0.2, dur=2.6):
    return dict(name=name, a0=a0, a1=a0 + dur, draw=draw, who='M', silent=True)

def talk(headline):
    def f(im, t, ws): im = R.top_shade(im); R.k_headline(im, headline, t); R.caption(im, ws, t); return im
    return f

def talk2(h1, h2, key):
    def f(im, t, ws):
        name = f.name; ts = next((st - f.a0 for w, st, e in WORDS[name] if w.lower().strip('.,!?').startswith(key)), 9) - 0.15
        im = R.top_shade(im); R.k_headline(im, h1 if t < ts else h2, t, t0=0 if t < ts else ts, size=78 if t < ts else 70)
        R.caption(im, ws, t); return im
    return f

def stat(title, line=None):
    def f(im, t, ws):
        im = R.top_shade(im); yb = R.k_headline(im, title, t, size=70)
        if line and t > 0.35:
            d = ImageDraw.Draw(im, 'RGBA'); fo = font(FM, 42); a = min(1, (t - 0.35) * 5)
            d.text((65, yb + 14), line, font=fo, fill=(255, 255, 255, int(255 * a)), stroke_width=2, stroke_fill=(0, 0, 0, int(200 * a)))
        return im
    return f

def p1():
    return [clip_seg('u31_pc_night', talk('THE STEP I NEVER SKIP')),
            sclip('u31_pc_morning', stat('89% EXPERIENCED IMPROVEMENT OF HAIR DENSITY', 'PowerCycle Scalp Treatment Serum'), dur=3.0)], \
           endcard(os.path.join(SS, 'output/batch-30-ulta-ugc/stills/ec_pc.png'), 'PowerCycle', 'Scalp Treatment Serum', ['SickScienceLabs.com']), 2.2

def d1():
    dr = talk2('SAME MIRROR. SAME JEANS.', 'VISIBLY SMOOTHS THE LOOK OF CELLULITE & STRETCH MARKS', 'this')
    seg = clip_seg('u31_do_mirror', dr); dr.name, dr.a0 = seg['name'], seg['a0']
    return [seg], endcard('ec_do', 'DropOff', 'Body Sculpting Serum'), 2.2

def n1():
    return [clip_seg('u31_nw_selfie', talk('ONE SERUM THIS OCTOBER'))], \
           endcard('ec_nw', 'NetWork', None,
                   ['This October, 20% of NetWork sales', 'on SickScienceLabs.com go to', 'The Breast Cancer Research Foundation.']), 3.2

VIDEOS = {'p1': p1, 'd1': d1, 'n1': n1}

def render(v):
    segs, ec, END = VIDEOS[v](); tmp = tempfile.mkdtemp(prefix=f'u31_{v}_')
    auds, sfx, tout, plan = [], [], 0.0, []
    for i, s in enumerate(segs):
        dur = s['a1'] - s['a0']; n = round(dur * FPS)
        if not s.get('silent'):
            raw = subprocess.run([FF, '-v', 'error', '-ss', str(s['a0']), '-t', str(dur), '-i', os.path.join(CL, s['name'] + '.mp4'),
                                  '-ac', '2', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True).stdout
            a = np.frombuffer(raw, np.int16).reshape(-1, 2).astype(np.float32)
        else: a = np.zeros((0, 2), np.float32)
        m = round(n / FPS * SR); a = np.pad(a, ((0, max(0, m - len(a))), (0, 0)))[:m]
        f_ = min(len(a), int(.015 * SR)); rr = np.linspace(0, 1, f_)[:, None]; a[:f_] *= rr; a[-f_:] *= rr[::-1]; auds.append(a)
        if i > 0: sfx.append((round(tout, 3), 'whoosh'))
        plan.append((s, n)); tout += n / FPS
    nend = round(END * FPS); sfx.append((round(tout, 3), 'thump')); total = sum(n for _, n in plan) + nend
    auds.append(np.zeros((round(END * SR), 2), np.float32)); a = np.concatenate(auds)
    json.dump({'duration': total / FPS, 'end': tout, 'sfx': sfx}, open(os.path.join(OUT, f'u31_{v}_cues.json'), 'w'))
    rawp = os.path.join(tmp, 'a.raw'); np.clip(a, -32768, 32767).astype(np.int16).tofile(rawp); tmp_out = os.path.join(tmp, 'o.mp4')
    enc = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', rawp, '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18',
                            '-c:a', 'aac', '-b:a', '192k', '-shortest', tmp_out], stdin=subprocess.PIPE)
    q = collections.deque()
    def emit(im):
        q.append(im)
        if len(q) > 3: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    def whip_in(i):
        if i > 0:
            for j, amt in enumerate((0.25, 0.6, 1.0)[-len(q):]): q[j] = R.whip(q[j], amt, -1)
    for i, (s, n) in enumerate(plan):
        whip_in(i); rd = ClipReader(s['name'], 1.0)
        ws = words(s['name'], s['a0'], s['a1']) if not s.get('silent') else []
        for k in range(n):
            t = k / FPS; im = s['draw'](rd.get(round((s['a0'] + t) * FPS)), t, ws)
            if i > 0 and k < 3: im = R.whip(im, (1.0, 0.6, 0.25)[k], 1)
            emit(im)
        rd.close()
    whip_in(1)
    for k in range(nend):
        t = k / FPS; sc = 1.06 - 0.06 * R.spring(t, 200, 22); im = ec.resize((round(W * sc), round(H * sc)), Image.LANCZOS)
        im = im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H))
        if k < 3: im = R.whip(im, (1.0, 0.6, 0.25)[k], 1)
        emit(im)
    while q: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    enc.stdin.close(); enc.wait()
    shutil.copy(tmp_out, os.path.join(OUT, f'u31_{v}_voice.mp4')); shutil.rmtree(tmp, ignore_errors=True)
    subprocess.run([FF, '-v', 'error', '-y', '-i', os.path.join(OUT, f'u31_{v}_voice.mp4'), '-vf', 'fps=2,scale=180:-1,tile=8x4',
                    '-frames:v', '1', os.path.join(OUT, f'u31_{v}_contact.jpg')])
    print(v, 'ok', round(total / FPS, 1), 's')

if __name__ == '__main__':
    for v in sys.argv[1:] or list(VIDEOS): render(v)
