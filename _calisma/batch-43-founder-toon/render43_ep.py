"""Batch 43 · Founder toon Ep2 / Ep3 (Google Flow, Veo 3.1 Fast native voices; stills Higgsfield Unlimited).
Reuses render43 (clip, groups, caption, Veo edge crop) + render42 helpers (textblock, foot, slam style).
usage: ~/motion-tools/.venv/bin/python render43_ep.py ep2|ep3 -> out/<ep>_voice.mp4 + cues (music: music43.py <ep>)"""
import os, sys, json, subprocess, tempfile, shutil, collections
import numpy as np
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import render43 as E
A, W, H, FPS, SR, FF, B, R = E.A, E.W, E.H, E.FPS, E.SR, E.FF, E.B, E.R
ST = os.path.join(HERE, 'stills'); OUT = E.OUT

def still(name, dur, z0=1.0, z1=1.07):
    """slow push-in on a still (no new video credits for b-roll)"""
    im = Image.open(os.path.join(ST, name)).convert('RGB'); s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    n = round(dur * FPS) + 8
    for k in range(n):
        z = z0 + (z1 - z0) * min(1, k / max(1, n - 8)); w, h = round(W * z), round(H * z)
        f = im.resize((w, h), Image.BILINEAR) if z != 1 else im
        x, y = (f.width - W) // 2, (f.height - H) // 2
        yield f.crop((x, y, x + W, y + H))

def slam(num, line, dur):
    fb, bs = A.G.fit_font(f'{num}%', 900, 420); fsm = B.font(B.FM, 56)
    for k in range(round(dur * FPS) + 8):
        t = k / FPS; im = Image.new('RGB', (W, H), A.VIO); d = ImageDraw.Draw(im, 'RGBA')
        txt = f"{round(num * min(1, t / 0.55) ** 0.6)}%"; sc = 1.35 - 0.35 * R.spring(t, 300, 16)
        lay = Image.new('RGBA', (W, bs + 80), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); tw = dl.textlength(f'{num}%', font=fb)
        dl.text(((W - tw) / 2, 10), txt, font=fb, fill=A.WHITE + (255,))
        lay = lay.resize((round(W * sc), round(lay.height * sc)), Image.BILINEAR); im.paste(lay, ((W - lay.width) // 2, 900 - lay.height // 2), lay)
        a = int(255 * min(1, max(0, (t - 0.22) * 6))); lw = d.textlength(line, font=fsm)
        d.text(((W - lw) / 2, 900 + bs // 2 + 40), line, font=fsm, fill=A.WHITE + (a,))
        yield im

def talk(name, t0, t1):
    g = E.groups(name, t0)
    return (lambda: E.clip(name, t0, t1 - t0), t1 - t0, lambda im, t: E.caption(im, g, t), (name, t0))

# copy is verbatim from the ShapeShift PDP (2026-10-13)
EPS = {
    'ep2': [talk('e2_polen_hook_veo', 0.0, 4.25),
            talk('e2_merve_bench_veofix', 0.0, 5.85),
            (lambda: still('e2_s3.png', 2.3), 2.3, lambda im, t: A.textblock(im, ['The 3× award-winning', 'gel-serum.'], 330, 80, t), None),
            (lambda: slam(94, 'saw smoother tech-neck lines.', 1.8), 1.8, None, None)],
    'ep3': [talk('e3_merve_apply_veo', 0.9, 4.1),
            talk('e3_polen_guasha2_veo', 0.0, 4.45),
            (lambda: still('e3_s3.png', 2.4), 2.4, lambda im, t: A.textblock(im, ['A visibly sharper jawline', 'in about 4 weeks.'], 330, 72, t), None),
            (lambda: slam(98, 'saw firmer, tighter neck skin.', 1.8), 1.8, None, None)],
}
ENDS = {'ep2': ('short5v4', 15.6), 'ep3': ('product3', 15.9)}

def render(ep):
    S = EPS[ep] + [E.endcard(*ENDS[ep])]; tmp = tempfile.mkdtemp(prefix=ep + '_'); sfx, tout, auds = [(0.0, 'thump')], 0.0, []
    for i, (_, dur, _, au) in enumerate(S):
        n = round(dur * FPS); m = round(n / FPS * SR)
        if au:
            raw = subprocess.run([FF, '-v', 'error', '-ss', str(au[1]), '-t', str(n / FPS), '-i', os.path.join(E.CL, au[0] + '.mp4'),
                                  '-ac', '2', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True).stdout
            a = np.frombuffer(raw, np.int16).reshape(-1, 2).astype(np.float32)
        else: a = np.zeros((0, 2), np.float32)
        a = np.pad(a, ((0, max(0, m - len(a))), (0, 0)))[:m]; f_ = int(.012 * SR); rr = np.linspace(0, 1, f_)[:, None]; a[:f_] *= rr; a[-f_:] *= rr[::-1]
        auds.append(a)
        if i > 0: sfx.append((round(tout, 3), 'whoosh' if i >= 2 else 'pop'))
        tout += n / FPS
    json.dump({'duration': tout, 'end': tout - round(S[-1][1] * FPS) / FPS, 'sfx': sfx}, open(os.path.join(OUT, f'{ep}_cues.json'), 'w'))
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
    shutil.copy(out, os.path.join(OUT, f'{ep}_voice.mp4')); shutil.rmtree(tmp, ignore_errors=True)
    subprocess.run([FF, '-v', 'error', '-y', '-i', os.path.join(OUT, f'{ep}_voice.mp4'), '-vf', 'fps=3,scale=150:-1,tile=10x5',
                    '-frames:v', '1', os.path.join(OUT, f'{ep}_contact.jpg')])
    print('ok', ep, round(tout, 1), 's')

if __name__ == '__main__':
    render(sys.argv[1])
