"""Batch 43 · Founder toon Ep1 — "We studied exosomes for cancer research." (≈12 s).
Kling 3.0 clips with their own voices (clips/k1..k3.mp4) + word timings (clips/words.json, mlx-whisper)
+ the batch-42 overlay helpers (textblock/slam, Founders Grotesk) + the brand film's own logo ending.
usage: ~/motion-tools/.venv/bin/python render43.py -> out/ep1_voice.mp4 + cues (music: music43.py)"""
import os, sys, json, subprocess, tempfile, shutil, collections
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__)); SS = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(SS, '_calisma', 'batch-42-nx35-reel'))
import render42 as A
W, H, FPS, SR, FF, B, R = A.W, A.H, A.FPS, A.SR, A.FF, A.B, A.R
CL = os.path.join(HERE, 'clips'); OUT = os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
WORDS = json.load(open(os.path.join(CL, 'words.json')))
FIX = {'exomonals': 'exosomes', 'eczemonals': 'exosomes'}   # caption spelling; the voice must also say it right
CUT = json.load(open(os.path.join(CL, 'cuts.json')))          # {'k1': [start, end], ...} trimmed to the spoken line

def clip(name, t0, dur):
    p = subprocess.Popen([FF, '-v', 'error', '-ss', f'{t0:.3f}', '-i', os.path.join(CL, name + '.mp4'), '-t', f'{dur + 0.2:.3f}',
                          '-vf', ('crop=iw-8:ih-4:4:2,' if 'veo' in name else '') + f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}', '-r', str(FPS), '-an',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    last = None
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        last = Image.frombytes('RGB', (W, H), b); yield last
    p.wait()
    while True: yield last

def groups(name, t0):
    ws = [((FIX[w.strip('.,').lower()] + w[len(w.rstrip('.,')):]) if w.strip('.,').lower() in FIX else w, s - t0, e - t0) for w, s, e in WORDS[name]]; out, cur = [], []
    for w in ws:
        cur.append(w)
        if len(cur) == 3 or w[0][-1:] in '.,': out.append(cur); cur = []
    if cur: out.append(cur)
    return [(' '.join(x[0].strip(',') for x in g), g[0][1], g[-1][2]) for g in out]

def caption(im, gs, t, y=1100):
    """big word-group captions (white, dark outline) inside the safe band, pop in"""
    g = next(((txt, s, e) for txt, s, e in gs if s - 0.05 <= t < e + 0.12), None)
    if not g: return
    txt, s, _ = g; f = B.font(B.FB, 78); sc = 0.85 + 0.15 * R.spring(t - s, 400, 18)
    lay = Image.new('RGBA', (W, 140), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); tw = dl.textlength(txt, font=f)
    dl.text(((W - tw) / 2, 20), txt, font=f, fill=(255, 255, 255, 255), stroke_width=6, stroke_fill=(10, 8, 12, 230))
    lay = lay.resize((round(W * sc), round(140 * sc)), Image.BILINEAR); im.paste(lay, ((W - lay.width) // 2, int(y - lay.height / 2)), lay)


def endcard(film, t0, dur=2.2):
    """the brand film's own logo ending (varies per episode); URL without a plate, ink picked from the background"""
    frames = A.foot(film, t0, dur)
    def gen():
        for f in frames: yield f
    def over(im, t):
        y = 1120; reg = im.crop((240, y - 10, 840, y + 70)).convert('L'); lum = sum(reg.getdata()) / (600 * 80)
        ink = (24, 18, 22) if lum > 150 else (255, 255, 255)
        A.textblock(im, ['SickScienceLabs.com'], y, 48, t, ink=ink, plate=False, weight=B.FM, delay=0.3)
    return (gen, dur, over, None)

def shots():
    (a0, a1), (b0, b1), (d0, d1) = CUT['k1_bk_veo'], CUT['k2b_veo'], CUT['k4b_veo']
    g1, g2, g4 = groups('k1_bk_veo', a0), groups('k2b_veo', b0), groups('k4b_veo', d0)
    return [
        (lambda: clip('k1_bk_veo', a0, a1 - a0), a1 - a0, lambda im, t: caption(im, g1, t), ('k1_bk_veo', a0)),
        (lambda: clip('k2b_veo', b0, b1 - b0), b1 - b0, lambda im, t: caption(im, g2, t), ('k2b_veo', b0)),
        # J-cut: Polen's line finishes over the product shot (her capsule gets redrawn after 2.5 s in k2)
        (lambda: clip('k3', 0.4, 2.4), 2.4,
         lambda im, t: caption(im, g2, t + (b1 - b0)), ('k2b_veo', b1)),
        # the answer: both founders, Merve says the line (Veo native voice)
        (lambda: clip('k4b_veo', d0, d1 - d0), d1 - d0,
         lambda im, t: caption(im, g4, t), ('k4b_veo', d0)),
        (lambda: A.slam(1.5), 1.5, None, None),
        endcard('product2', 15.4),
    ]

def render():
    S = shots(); tmp = tempfile.mkdtemp(prefix='ep1_'); sfx, tout, auds = [(0.0, 'thump')], 0.0, []
    for i, (_, dur, _, au) in enumerate(S):
        n = round(dur * FPS); m = round(n / FPS * SR)
        if au:
            raw = subprocess.run([FF, '-v', 'error', '-ss', str(au[1]), '-t', str(n / FPS), '-i', os.path.join(CL, au[0] + '.mp4'),
                                  '-ac', '2', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True).stdout
            a = np.frombuffer(raw, np.int16).reshape(-1, 2).astype(np.float32)
        else: a = np.zeros((0, 2), np.float32)
        a = np.pad(a, ((0, max(0, m - len(a))), (0, 0)))[:m]; f_ = int(.012 * SR); rr = np.linspace(0, 1, f_)[:, None]; a[:f_] *= rr; a[-f_:] *= rr[::-1]
        auds.append(a)
        if i > 0: sfx.append((round(tout, 3), 'whoosh' if i >= 2 else 'pop'))
        tout += n / FPS
    json.dump({'duration': tout, 'end': tout - round(S[-1][1] * FPS) / FPS, 'sfx': sfx}, open(os.path.join(OUT, 'ep1_cues.json'), 'w'))
    rawp = os.path.join(tmp, 'a.raw'); np.clip(np.concatenate(auds), -32768, 32767).astype(np.int16).tofile(rawp); out = os.path.join(tmp, 'o.mp4')
    enc = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', rawp, '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18',
                            '-c:a', 'aac', '-b:a', '192k', '-shortest', out], stdin=subprocess.PIPE)
    q = collections.deque()
    def emit(im):
        q.append(im)
        if len(q) > 3: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    for i, (g, dur, o, _) in enumerate(S):
        n = round(dur * FPS); gen = g()
        if i > 0:
            for j, amt in enumerate((0.25, 0.6, 1.0)[-len(q):]): q[j] = R.whip(q[j], amt, -1)
        for k in range(n):
            t = k / FPS; im = next(gen).copy().convert('RGB')
            if o: o(im, t)
            if i > 0 and k < 3: im = R.whip(im, (1.0, 0.6, 0.25)[k], 1)
            emit(im)
    while q: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    enc.stdin.close(); enc.wait()
    shutil.copy(out, os.path.join(OUT, 'ep1_voice.mp4')); shutil.rmtree(tmp, ignore_errors=True)
    subprocess.run([FF, '-v', 'error', '-y', '-i', os.path.join(OUT, 'ep1_voice.mp4'), '-vf', 'fps=3,scale=150:-1,tile=10x4',
                    '-frames:v', '1', os.path.join(OUT, 'ep1_contact.jpg')])
    print('ok', round(tout, 1), 's')

if __name__ == '__main__':
    render()
