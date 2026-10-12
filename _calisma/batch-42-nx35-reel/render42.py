"""Batch 42 — ShapeShift × NX35™ exosome reel, cut from the brand's own 9:16 footage (Drive 'v3', local copy
~/motion-tools/footage-v3/v3). Shape informed by Buzzfy niche reports (Skincare, Makeup & beauty, exosome skincare):
visual hook in the first frame, first cut ≈3 s, short text overlays, no comment CTA, ≤20 s.
Copy is verbatim from the ShapeShift PDP (sicksciencelabs.com/products/shapeshift, 2026-10-13).
usage: ~/motion-tools/.venv/bin/python render42.py  -> out/u42_nx35_voice.mp4 + cues (music: music42.py)"""
import os, sys, json, subprocess, tempfile, shutil, collections
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__)); SS = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(SS, '_calisma', 'batch-32-gloss-angeles'))
import render32 as G
B, R = G.B, G.R
W, H, FPS, SR, FF = G.W, G.H, G.FPS, G.SR, G.FF
FOOT = os.path.expanduser('~/motion-tools/footage-v3/v3'); OUT = os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
INK, VIO, WHITE = (24, 18, 22), (115, 0, 199), (255, 255, 255)

HOOK = os.environ.get('HOOK', 'Exosomes.\nNo needles.')

def foot(name, t0, dur):
    p = subprocess.Popen([FF, '-v', 'error', '-ss', f'{t0:.3f}', '-i', os.path.join(FOOT, name + '.mp4'), '-t', f'{dur + 0.2:.3f}',
                          '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}', '-r', str(FPS), '-an',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    last = None
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        last = Image.frombytes('RGB', (W, H), b); yield last
    p.wait()
    while True: yield last

def textblock(im, lines, y, size, t, ink=WHITE, plate=True, weight=None, delay=0.0):
    """centred lines that slide up + fade in; soft dark plate for legibility on footage"""
    f = B.font(weight or B.FB, size); d0 = ImageDraw.Draw(im, 'RGBA'); tt = t - delay
    if tt <= 0: return
    a = int(255 * min(1, tt * 6)); off = (1 - R.spring(tt, 260, 20)) * 50
    widths = [d0.textlength(l, font=f) for l in lines]; lh = int(size * 1.12)
    if plate:
        pw = max(widths) + 70; ph = lh * len(lines) + 46
        lay = Image.new('RGBA', (int(pw), int(ph)), (0, 0, 0, 0))
        ImageDraw.Draw(lay).rounded_rectangle((0, 0, pw - 1, ph - 1), 26, fill=(14, 10, 16, int(150 * a / 255)))
        im.paste(lay, (int((W - pw) / 2), int(y - 23 + off)), lay)
    for i, (l, w) in enumerate(zip(lines, widths)):
        d0.text(((W - w) / 2, y + i * lh + off), l, font=f, fill=ink + (a,))

def body(im, text, y, t, delay=0.0):
    d = ImageDraw.Draw(im, 'RGBA'); f = B.font(B.FM, 52)
    lines = R.wrap(d, text, f, 880); textblock(im, lines, y, 52, t, weight=B.FM, delay=delay)

def slam(dur):
    fb, bs = G.fit_font('92%', 900, 420); fsm = B.font(B.FM, 56)
    for k in range(round(dur * FPS) + 8):
        t = k / FPS; im = Image.new('RGB', (W, H), VIO); d = ImageDraw.Draw(im, 'RGBA')
        txt = f"{round(92 * min(1, t / 0.55) ** 0.6)}%"; sc = 1.35 - 0.35 * R.spring(t, 300, 16)
        lay = Image.new('RGBA', (W, bs + 80), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); tw = dl.textlength('92%', font=fb)
        dl.text(((W - tw) / 2, 10), txt, font=fb, fill=WHITE + (255,))
        lay = lay.resize((round(W * sc), round(lay.height * sc)), Image.BILINEAR); im.paste(lay, ((W - lay.width) // 2, 900 - lay.height // 2), lay)
        a = int(255 * min(1, max(0, (t - 0.22) * 6)))
        for i, l in enumerate(['saw a more sculpted jawline.']):
            lw = d.textlength(l, font=fsm); d.text(((W - lw) / 2, 900 + bs // 2 + 40 + i * 66), l, font=fsm, fill=WHITE + (a,))
        yield im

# shots: (generator factory, duration, overlay(im, t) or None)
def shots():
    return [
        (lambda: foot('product2', 9.0, 2.8), 2.8,                       # visual hook: hands frame the jaw
         lambda im, t: textblock(im, HOOK.split('\n'), 330, 92, t)),
        (lambda: foot('product2', 4.3, 1.6), 1.6,                       # capsule on the glass grid
         lambda im, t: textblock(im, ['What is NX35™?'], 330, 92, t)),
        (lambda: foot('product2', 2.2, 3.0), 3.0,                       # the molecule cube, then the glass dish
         lambda im, t: body(im, "NX35™ is SickScience's plant-based biomimetic exosome technology, designed to support cell-to-cell communication in the skin.", 300, t)),
        (lambda: foot('product2', 11.0, 2.8), 2.8,                      # gua sha along the jawline
         lambda im, t: (textblock(im, ['One minute, morning and night.', 'No needles, no downtime.'], 330, 64, t))),
        (lambda: foot('short9', 5.3, 1.3), 1.3,                          # capsule in hand
         lambda im, t: textblock(im, ['The 3× award-winning', 'gel-serum.'], 330, 80, t)),
        (lambda: slam(1.8), 1.8, None),
        (lambda: foot('product2', 15.4, 2.4), 2.4,                      # the brand film's own logo ending
         lambda im, t: textblock(im, ['SickScienceLabs.com'], 1120, 48, t, weight=B.FM, delay=0.3)),
    ]

def render():
    S = shots(); tmp = tempfile.mkdtemp(prefix='u42_'); sfx, tout = [(0.0, 'thump')], 0.0
    for i, (_, dur, _) in enumerate(S):
        if i > 0: sfx.append((round(tout, 3), 'whoosh' if i in (1, 5, 6) else 'pop'))
        tout += round(dur * FPS) / FPS
    json.dump({'duration': tout, 'end': tout - round(S[-1][1] * FPS) / FPS, 'sfx': sfx}, open(os.path.join(OUT, 'u42_nx35_cues.json'), 'w'))
    out = os.path.join(tmp, 'o.mp4')
    enc = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-f', 'lavfi', '-t', f'{tout:.3f}', '-i', f'anullsrc=r={SR}:cl=stereo',
                            '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-c:a', 'aac', '-shortest', out], stdin=subprocess.PIPE)
    q = collections.deque()
    def emit(im):
        q.append(im)
        if len(q) > 3: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    for i, (g, dur, o) in enumerate(S):
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
    shutil.copy(out, os.path.join(OUT, 'u42_nx35_voice.mp4')); shutil.rmtree(tmp, ignore_errors=True)
    subprocess.run([FF, '-v', 'error', '-y', '-i', os.path.join(OUT, 'u42_nx35_voice.mp4'), '-vf', 'fps=3,scale=150:-1,tile=10x5',
                    '-frames:v', '1', os.path.join(OUT, 'u42_nx35_contact.jpg')])
    print('ok', round(tout, 1), 's')

if __name__ == '__main__':
    render()
