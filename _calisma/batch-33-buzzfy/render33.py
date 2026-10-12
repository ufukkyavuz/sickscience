"""Batch 33 — Buzzfy-format short UGCs (≤15 s, 9:16), copy verbatim from the PDPs (2026-10-10):
  b1 PowerCycle 'applying scalp serum wrong?'  (PDP How To Use)
  b2 DropOff 'the order matters'               (PDP Suggested Routine: Dry Brushing > Shower > Apply DropOff > Massage > Let Absorb)
  b3 NetWork half-face primer                  (PDP 'Doubles as a primer with a blur effect'; AI comparison -> 'Simulated results.')
  b4 ShapeShift DAY 1 -> DAY 14                (PDP before/after 'Sculpted skin in just 2 Weeks')
Talking clips: Kling 3.0 (product names never spoken); b-roll + logo endings: the brand's own footage.
Reuses the batch-32 helpers (captions, hooks, B/A card). Streams frames.
usage: python render33.py b1|b2|b3|b4  -> out/u33_<v>_voice.mp4 + cues  (music: music33.py)"""
import os, sys, json, subprocess, tempfile, shutil, collections
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__)); SS = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(SS, '_calisma', 'batch-32-gloss-angeles'))
import render32 as G                                     # B (fonts), R (render29 helpers), hooks, captions, ba_card, foot
B, R = G.B, G.R
W, H, FPS, SR, FF = G.W, G.H, G.FPS, G.SR, G.FF
CL, ST, OUT = os.path.join(HERE, 'clips'), os.path.join(HERE, 'stills'), os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
B31 = os.path.join(SS, '_calisma', 'batch-31-ugc-products')
WORDS = json.load(open(os.path.join(CL, 'words.json')))
RED, GREEN, INK = (230, 40, 60), (40, 190, 90), (24, 18, 22)

def clip(path, t0, dur):
    p = subprocess.Popen([FF, '-v', 'error', '-ss', f'{t0:.3f}', '-t', f'{dur + 0.2:.3f}', '-i', path,
                          '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}', '-r', str(FPS), '-an',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    last = None
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        last = Image.frombytes('RGB', (W, H), b); yield last
    p.wait()
    while True: yield last

def still(path, dur, z0=1.0, z1=1.06):
    im = G.cover(path); n = round(dur * FPS)
    for k in range(n + 6):
        z = z0 + (z1 - z0) * min(1, k / max(1, n)); f = im.resize((round(W * z), round(H * z)), Image.BILINEAR)
        yield f.crop(((f.width - W) // 2, (f.height - H) // 2, (f.width - W) // 2 + W, (f.height - H) // 2 + H))
    while True: yield f

def words(name, a0, a1):
    return [(w.strip('.,!?'), s - a0, e - a0, w[-1:] in '.,!?') for w, s, e in WORDS[name] if a0 - 0.05 <= s < a1]

def badge(im, txt, col, t, y=300):
    """✕ / ✓ verdict chip that pops in top-left"""
    d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1))); f = B.font(B.FB, 64); tw = d0.textlength(txt, font=f)
    lay = Image.new('RGBA', (int(tw) + 70, 110), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.rounded_rectangle((0, 0, lay.width, 110), 24, fill=col + (255,)); d.text((35, 18), txt, font=f, fill=(255, 255, 255))
    sc = 0.6 + 0.4 * R.spring(t, 380, 16); lay = lay.resize((max(1, round(lay.width * sc)), max(1, round(lay.height * sc))), Image.BILINEAR)
    im.paste(lay, (65, y), lay)

def step(im, num, label, t, y=1000):
    """numbered step: big number + label slide in, on a soft shade"""
    d = ImageDraw.Draw(im, 'RGBA')
    fn, fl = B.font(B.FB, 190), B.font(B.FB, 76); a = int(255 * min(1, t * 8)); off = (1 - R.spring(t, 320, 18)) * 80
    d.text((65 - off, y - 40), num, font=fn, fill=G.LILAC + (a,), stroke_width=4, stroke_fill=(0, 0, 0, a))
    nx = 65 + d.textlength(num, font=fn) + 30
    for i, ln in enumerate(R.wrap(d, label, fl, W - nx - 50)):
        d.text((nx + off, y + 10 + i * 82), ln, font=fl, fill=(255, 255, 255, a), stroke_width=4, stroke_fill=(0, 0, 0, a))
    return im

def tip(im, txt, t, y=1060):
    """single white-on-purple instruction line"""
    d = ImageDraw.Draw(im, 'RGBA'); f = B.font(B.FB, 70); tw = d.textlength(txt, font=f); a = int(255 * min(1, t * 8))
    off = (1 - R.spring(t, 320, 18)) * 60; x = (W - tw) / 2
    d.rounded_rectangle((x - 30, y - 14 + off, x + tw + 30, y + 92 + off), 22, fill=G.PURPLE + (a,))
    d.text((x, y + off), txt, font=f, fill=(255, 255, 255, a)); return im

def simulated(im):
    d = ImageDraw.Draw(im, 'RGBA'); f = B.font(B.FM, 32); txt = 'Simulated results.'
    d.text(((W - d.textlength(txt, font=f)) / 2, 1860), txt, font=f, fill=(255, 255, 255, 230), stroke_width=2, stroke_fill=(0, 0, 0, 160))

FOOT = G.FOOT
# shots: (generator factory, dur, overlay(im, t_local, T_global) -> im, audio (path, t0) | None)
def b1():
    talk = os.path.join(CL, 'u33_pc_wrong.mp4'); w = WORDS['u33_pc_wrong']; a0 = max(0, w[0][1] - 0.15); a1 = w[-1][2] + 0.3
    ws = words('u33_pc_wrong', a0, a1); gs = G.groups(ws); right = os.path.join(B31, 'clips', 'u31_pc_night.mp4')
    def o1(im, t, T):
        if T < 2.3 + 0.35: G.sticker_headline(im, 'ARE YOU APPLYING SCALP SERUM WRONG?', T, y=700, hook_t=2.3)
        if T > 0.4: badge(im, 'WRONG: ON YOUR HAIR', RED, T - 0.4)
        G.big_caption(im, gs, t); return im
    rt = os.path.join(CL, 'u33_pc_right.mp4'); wr = WORDS['u33_pc_right']; r0 = max(0, wr[0][1] - 0.15); r1 = wr[-1][2] + 0.5
    gr = G.groups(words('u33_pc_right', r0, r1))
    def o2(im, t, T):                                         # the right way, spoken (PDP How To Use)
        badge(im, 'RIGHT: ON YOUR SCALP', GREEN, t); G.big_caption(im, gr, t); return im
    shots = [(lambda: clip(talk, a0, a1 - a0), a1 - a0, o1, (talk, a0)),
             (lambda: clip(rt, r0, r1 - r0), r1 - r0, o2, (rt, r0)),
             (lambda: clip(os.path.join(FOOT, 'product3.mp4'), 13.0, 1.6), 1.6,
              lambda im, t, T: step(im, '', 'FOCUS: HAIRLINE & CROWN', t), None),
             (lambda: clip(os.path.join(FOOT, 'product3.mp4'), 16.0, 2.3), 2.3, lambda im, t, T: im, None)]
    return shots

def b2():
    def hook(im, t, T):
        if T < 1.6 + 0.35: G.block_headline(im, 'THE ORDER MATTERS.', T, y=620, hook_t=1.6)
        return im
    st = [('01', 'DRY BRUSH', lambda: clip(os.path.join(CL, 'u33_do_drybrush.mp4'), 0.3, 2.3), 2.3),
          ('02', 'SHOWER', lambda: still(os.path.join(ST, 'do_shower.png'), 1.6), 1.6),
          ('03', 'APPLY DROPOFF', lambda: clip(os.path.join(FOOT, 'product1.mp4'), 7.4, 1.4), 1.4),
          ('04', 'MASSAGE', lambda: clip(os.path.join(FOOT, 'product1.mp4'), 9.2, 1.5), 1.5),
          ('05', 'LET ABSORB', lambda: still(os.path.join(B31, 'stills', 'do_mirror2.png'), 1.6), 1.6)]
    shots = []
    for i, (n, lab, g, d) in enumerate(st):
        shots.append((g, d, (lambda im, t, T, n=n, lab=lab, i=i: hook(step(im, n, lab, t - (0.0 if i else 0.9)) if (i or t > 0.9) else im, t, T)), None))
    shots.append((lambda: clip(os.path.join(FOOT, 'product1.mp4'), 12.4, 2.4), 2.4, lambda im, t, T: im, None))
    return shots

NW_RED = (200, 16, 40)
def b3():
    """hook question -> answer (push into each cheek) -> how to use (PDP) -> proof (PDP stat) -> logo"""
    talk = os.path.join(CL, 'u33_nw_half.mp4'); w = WORDS['u33_nw_half']; a0 = max(0, w[0][1] - 0.15); a1 = w[-1][2] + 0.3
    gs = G.groups(words('u33_nw_half', a0, a1)); last = {}
    def o1(im, t, T):
        last['im'] = im.copy()
        if T < 2.2 + 0.35: G.stack_headline(im, 'CAN YOU TELL?', T, y=1020, hook_t=2.2)
        else: G.big_caption(im, gs, t)
        simulated(im); return im
    def answer(dur):                                          # freeze the last frame, push into her left cheek, then pan across
        n = round(dur * FPS); base = None
        for k in range(n + 6):
            if base is None: base = last['im']
            t = k / FPS; z = 1.0 + 0.55 * R.spring(t, 140, 20)
            pan = 0.0 if t < dur * 0.55 else R.spring(t - dur * 0.55, 200, 22)      # 0 = image-right cheek, 1 = image-left cheek
            cx = W * (0.62 - 0.27 * pan); cy = H * 0.40
            f = base.resize((round(W * z), round(H * z)), Image.BILINEAR)
            x0 = int(min(max(cx * z - W / 2, 0), f.width - W)); y0 = int(min(max(cy * z - H / 2, 0), f.height - H))
            yield f.crop((x0, y0, x0 + W, y0 + H))
        while True: yield f.crop((x0, y0, x0 + W, y0 + H))
    def o2(im, t, T):
        first = t < 2.6 * 0.55
        im = tip(im, 'WITH NETWORK' if first else 'WITHOUT', t if first else t - 2.6 * 0.55, y=1000)
        if first and t > 0.45: im = tip(im, 'MINIMIZES THE LOOK OF PORES', t - 0.45, y=1120)
        simulated(im); return im
    app = os.path.join(CL, 'u33_nw_apply.mp4'); wa = WORDS.get('u33_nw_apply', [])
    b0 = max(0, wa[0][1] - 0.15) if wa else 0; b1 = (wa[-1][2] + 0.3) if wa else 5.0; ga = G.groups(words('u33_nw_apply', b0, b1)) if wa else []
    def o3(im, t, T):
        if t > 0.2: badge(im, '1–2 PUMPS', G.PURPLE, t - 0.2, y=300)
        G.big_caption(im, ga, t); return im
    def proof(dur):
        n = round(dur * FPS)
        for k in range(n + 6): yield Image.new('RGB', (W, H), NW_RED)
        while True: yield Image.new('RGB', (W, H), NW_RED)
    def o4(im, t, T):
        d = ImageDraw.Draw(im, 'RGBA'); fb = B.font(B.FB, 380); txt = f"{round(94 * min(1, t / 0.5) ** 0.6)}%"
        sc = 1.3 - 0.3 * R.spring(t, 300, 16); lay = Image.new('RGBA', (W, 460), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.text(((W - dl.textlength('94%', font=fb)) / 2, 10), txt, font=fb, fill=(255, 255, 255, 255))
        lay = lay.resize((round(W * sc), round(460 * sc)), Image.BILINEAR); im.paste(lay, ((W - lay.width) // 2, 700 - lay.height // 2), lay)
        a = int(255 * min(1, max(0, (t - 0.25) * 6))); fs = B.font(B.FB, 64); fm = B.font(B.FM, 48)
        for i, ln in enumerate(['REPORTED SMOOTHER-', 'FEELING SKIN']):
            d.text(((W - d.textlength(ln, font=fs)) / 2, 960 + i * 74), ln, font=fs, fill=(255, 255, 255, a))
        b = int(255 * min(1, max(0, (t - 0.7) * 6)))
        for i, ln in enumerate(['Doubles as a primer', 'with a blur effect']):
            d.text(((W - d.textlength(ln, font=fm)) / 2, 1150 + i * 58), ln, font=fm, fill=(255, 255, 255, b))
        return im
    shots = [(lambda: clip(talk, a0, a1 - a0), a1 - a0, o1, (talk, a0)),
             (lambda: answer(2.6), 2.6, o2, None)]
    if wa: shots.append((lambda: clip(app, b0, b1 - b0), b1 - b0, o3, (app, b0)))
    shots += [(lambda: proof(2.2), 2.2, o4, None),
              (lambda: clip(os.path.join(FOOT, 'short9.mp4'), 13.9, 2.3), 2.3, lambda im, t, T: im, None)]
    return shots

def b4():
    ba = os.path.join(G.SITE_BA, 'ss_ba_2weeks.jpg'); src = Image.open(ba).convert('RGB')
    top = src.crop((0, 0, 580, 410)); cw = 1000; ch = round(410 * cw / 580); top = top.resize((cw, ch), Image.LANCZOS)
    m = Image.new('L', (cw, ch), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, cw, ch), 28, fill=255)
    BG = (238, 232, 246); Y0 = 420
    def pair(dur, reveal):
        """the site before/after; on DAY 1 the AFTER half is covered, on DAY 14 the cover slides away"""
        n = round(dur * FPS)
        for k in range(n + 6):
            t = k / FPS; f = Image.new('RGB', (W, H), BG); c = top.copy()
            if reveal: cov = round(cw / 2 * (1 - R.spring(t - 0.15, 240, 22)))
            else: cov = cw // 2
            if cov > 0: ImageDraw.Draw(c).rectangle((cw - cov, 0, cw, ch), fill=BG)
            sc = 0.92 + 0.08 * R.spring(t, 260, 18) if not reveal else 1.0
            c2 = c.resize((round(cw * sc), round(ch * sc)), Image.BILINEAR)
            f.paste(c2, ((W - c2.width) // 2, Y0 + (ch - c2.height) // 2), m.resize(c2.size)); yield f
        while True: yield f
    def label(txt, x_center):
        def o(im, t, T):
            d = ImageDraw.Draw(im, 'RGBA'); f = B.font(B.FB, 120); a = int(255 * min(1, t * 8)); off = (1 - R.spring(t, 320, 16)) * 50
            tw = d.textlength(txt, font=f); d.text((x_center - tw / 2, Y0 + ch + 50 + off), txt, font=f, fill=G.PURPLE + (a,)); return im
        return o
    def both(im, t, T):
        im = label('DAY 1', W // 2 - cw // 4)(im, 1, T); return label('DAY 14', W // 2 + cw // 4)(im, t, T)
    def hook(im, t, T):
        if T < 1.5 + 0.35: G.slam_headline(im, 'DAY 1 VS DAY 14', T, y=760, hook_t=1.5)
        return im
    return [(lambda: clip(os.path.join(FOOT, 'product2.mp4'), 9.8, 1.9), 1.9, hook, None),
            (lambda: pair(1.5, False), 1.5, label('DAY 1', W // 2 - cw // 4), None),
            (lambda: clip(os.path.join(FOOT, 'product2.mp4'), 4.0, 1.4), 1.4, lambda im, t, T: tip(im, 'TWICE DAILY, UPWARD', t), None),
            (lambda: pair(1.9, True), 1.9, both, None),
            (lambda: G.foot('product2', G.FD['product2'] - 2.4, 2.6), 2.4, lambda im, t, T: im, None)]

VIDEOS = {'b1': b1, 'b2': b2, 'b3': b3, 'b4': b4}

def render(v):
    shots = VIDEOS[v](); tmp = tempfile.mkdtemp(prefix=f'u33_{v}_'); auds, sfx, tout = [], [(0.0, 'thump')], 0.0
    for i, (g, dur, o, au) in enumerate(shots):
        n = round(dur * FPS); m = round(n / FPS * SR)
        if au:
            raw = subprocess.run([FF, '-v', 'error', '-ss', str(au[1]), '-t', str(n / FPS), '-i', au[0], '-ac', '2', '-ar', str(SR), '-f', 's16le', '-'],
                                 capture_output=True).stdout
            a = np.frombuffer(raw, np.int16).reshape(-1, 2).astype(np.float32)
        else: a = np.zeros((0, 2), np.float32)
        a = np.pad(a, ((0, max(0, m - len(a))), (0, 0)))[:m]; f_ = int(.012 * SR); rr = np.linspace(0, 1, f_)[:, None]; a[:f_] *= rr; a[-f_:] *= rr[::-1]
        auds.append(a)
        if i > 0: sfx.append((round(tout, 3), 'whoosh' if i == len(shots) - 1 else 'pop'))
        tout += n / FPS
    end = tout - round(shots[-1][1] * FPS) / FPS
    json.dump({'duration': tout, 'end': end, 'sfx': sfx}, open(os.path.join(OUT, f'u33_{v}_cues.json'), 'w'))
    aud = np.concatenate(auds); rawp = os.path.join(tmp, 'a.raw'); np.clip(aud, -32768, 32767).astype(np.int16).tofile(rawp)
    tmp_out = os.path.join(tmp, 'o.mp4')
    enc = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', rawp, '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18',
                            '-c:a', 'aac', '-b:a', '192k', '-shortest', tmp_out], stdin=subprocess.PIPE)
    q = collections.deque()
    def emit(im):
        q.append(im)
        if len(q) > 3: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    T = 0.0
    for i, (g, dur, o, au) in enumerate(shots):
        n = round(dur * FPS); gen = g()
        if i > 0:
            for j, amt in enumerate((0.25, 0.6, 1.0)[-len(q):]): q[j] = R.whip(q[j], amt, -1)
        for k in range(n):
            t = k / FPS; im = o(next(gen).copy(), t, T + t)
            if i > 0 and k < 3: im = R.whip(im, (1.0, 0.6, 0.25)[k], 1)
            if i == 0 and k < 3: im = Image.blend(im, Image.new('RGB', (W, H), (255, 255, 255)), (0.55, 0.3, 0.1)[k])
            emit(im)
        T += n / FPS
    while q: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    enc.stdin.close(); enc.wait()
    shutil.copy(tmp_out, os.path.join(OUT, f'u33_{v}_voice.mp4')); shutil.rmtree(tmp, ignore_errors=True)
    subprocess.run([FF, '-v', 'error', '-y', '-i', os.path.join(OUT, f'u33_{v}_voice.mp4'), '-vf', 'fps=2,scale=150:-1,tile=10x3',
                    '-frames:v', '1', os.path.join(OUT, f'u33_{v}_contact.jpg')])
    print(v, 'ok', round(T, 1), 's')

if __name__ == '__main__':
    for v in sys.argv[1:] or list(VIDEOS): render(v)
