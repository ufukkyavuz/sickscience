"""Batch 42 v2 — UGC talking-head hybrid. The Buzzfy exosome-skincare report shows talking-to-camera reels get ~5x the plays
of aesthetic montages (median 24K vs 4.8K) and the strongest hooks there are spoken warnings / hot takes.
Talking clips: existing ShapeShift UGC (batch-28, Kling, own voices). B-roll: the brand's own films (Drive 'v3').
c18_C_howto is NOT used: it shows a pink stone gua sha (ours is stainless steel) — the gua sha beat uses the brand film.
usage: ~/motion-tools/.venv/bin/python render42b.py -> out/u42b_voice.mp4 + cues (music: music42.py u42b)"""
import os, sys, json, subprocess, tempfile, shutil, collections
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__)); SS = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import render42 as A                                   # foot, textblock, body, slam, B, R, G, W, H, FPS, SR, FF
W, H, FPS, SR, FF, B, R = A.W, A.H, A.FPS, A.SR, A.FF, A.B, A.R
CL = os.path.join(SS, '_calisma', 'batch-28-video', 'clips'); OUT = A.OUT
WORDS = json.load(open(os.path.join(CL, 'words.json')))
FIX = {'NX35': 'NX35™'}

def talk(name, dur):
    p = subprocess.Popen([FF, '-v', 'error', '-i', os.path.join(CL, name + '.mp4'), '-t', f'{dur + 0.2:.3f}',
                          '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}', '-r', str(FPS), '-an',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    last = None
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        last = Image.frombytes('RGB', (W, H), b); yield last
    p.wait()
    while True: yield last

def groups(name):
    ws = [(FIX.get(w.strip('.,'), w), s, e) for w, s, e in WORDS[name]]; out, cur = [], []
    for w in ws:
        cur.append(w)
        if len(cur) == 3 or w[0][-1:] in '.,': out.append(cur); cur = []
    if cur: out.append(cur)
    return [(' '.join(x[0].strip(',') for x in g), g[0][1], g[-1][2]) for g in out]

def caption(im, gs, t, y=1060):
    """big word-group captions (white, dark outline), one group at a time, pop in"""
    g = next(((txt, s, e) for txt, s, e in gs if s - 0.05 <= t < e + 0.12), None)
    if not g: return
    txt, s, _ = g; f = B.font(B.FB, 78); d = ImageDraw.Draw(im, 'RGBA'); sc = 0.85 + 0.15 * R.spring(t - s, 400, 18)
    lay = Image.new('RGBA', (W, 140), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); tw = dl.textlength(txt, font=f)
    dl.text(((W - tw) / 2, 20), txt, font=f, fill=(255, 255, 255, 255), stroke_width=6, stroke_fill=(10, 8, 12, 230))
    lay = lay.resize((round(W * sc), round(140 * sc)), Image.BILINEAR); im.paste(lay, ((W - lay.width) // 2, int(y - lay.height / 2)), lay)

def shots():
    g16, g15 = groups('c16_D_problem'), groups('c15b_C_ingredients')
    def s1():                                              # talking head with a cutaway to the jaw on "surface… results"
        a, b = talk('c16_D_problem', 6.75), A.foot('product2', 9.0, 1.7)
        for k in range(round(6.75 * FPS) + 8):
            t = k / FPS; fa = next(a)
            yield next(b) if 2.95 <= t < 4.6 else fa
    def o1(im, t):
        caption(im, g16, t)
        if t < 2.6: A.textblock(im, ['Exosomes. No needles.'], 330, 76, t)
    def s2():                                              # second creator; cutaway to the NX35 b-roll on "NX35 Sculpt technology"
        a, b = talk('c15b_C_ingredients', 7.0), A.foot('product2', 2.4, 2.2)
        for k in range(round(7.0 * FPS) + 8):
            t = k / FPS; fa = next(a)
            yield next(b) if 3.3 <= t < 5.5 else fa
    def o2(im, t):
        caption(im, g15, t)
        if 3.3 <= t < 5.5: A.body(im, "NX35™ is SickScience's plant-based biomimetic exosome technology.", 330, t - 3.3)
    return [
        (s1, 6.75, o1, ('c16_D_problem', 0.0)),
        (s2, 7.0, o2, ('c15b_C_ingredients', 0.0)),
        (lambda: A.foot('product2', 11.0, 2.2), 2.2,
         lambda im, t: A.textblock(im, ['One minute, morning and night.', 'No needles, no downtime.'], 330, 64, t), None),
        (lambda: A.slam(1.6), 1.6, None, None),
        (lambda: A.foot('product2', 15.4, 2.2), 2.2,
         lambda im, t: A.textblock(im, ['SickScienceLabs.com'], 1120, 48, t, weight=B.FM, delay=0.3), None),
    ]

def render():
    S = shots(); tmp = tempfile.mkdtemp(prefix='u42b_'); sfx, tout, auds = [(0.0, 'thump')], 0.0, []
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
    json.dump({'duration': tout, 'end': tout - round(S[-1][1] * FPS) / FPS, 'sfx': sfx}, open(os.path.join(OUT, 'u42b_cues.json'), 'w'))
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
    shutil.copy(out, os.path.join(OUT, 'u42b_voice.mp4')); shutil.rmtree(tmp, ignore_errors=True)
    subprocess.run([FF, '-v', 'error', '-y', '-i', os.path.join(OUT, 'u42b_voice.mp4'), '-vf', 'fps=3,scale=150:-1,tile=10x6',
                    '-frames:v', '1', os.path.join(OUT, 'u42b_contact.jpg')])
    print('ok', round(tout, 1), 's')

if __name__ == '__main__':
    render()
