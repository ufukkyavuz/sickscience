"""Batch 40 — 'play with the UI' hook videos (2026-10-11), reference: katrina_pahomova reel DeR13pfRvtx.
The model (Kling 3.0) only acts; every UI card, the burn, the grab and the crumple are drawn here so the text is exact.
No comment CTA (user): stat slam on the product colour -> campaign still + logo + SickScienceLabs.com, like batch 32/33.
  v1 ShapeShift  question sticker 'Is jawline serum a scam?' burned by the lighter flame   -> 92% (PDP)
  v2 NetWork     'Your NetWork order has shipped' notification caught and pulled down       -> BCRF October line
  v3 PowerCycle  comment card crumpled and thrown                                           -> +29% thickness (PDP)
usage: python render40.py v1|v2|v3  -> out/u40_<v>_voice.mp4 + cues  (music: music40.py)"""
import os, sys, json, math, subprocess, tempfile, shutil, collections
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__)); SS = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(SS, '_calisma', 'batch-32-gloss-angeles'))
import render32 as G
B, R = G.B, G.R
W, H, FPS, SR, FF = G.W, G.H, G.FPS, G.SR, G.FF
CL, ST, OUT = (os.path.join(HERE, d) for d in ('clips', 'stills', 'out')); os.makedirs(OUT, exist_ok=True)
INK = (24, 18, 22)

def clip(path, dur):
    p = subprocess.Popen([FF, '-v', 'error', '-i', path, '-t', f'{dur + 0.2:.3f}',
                          '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}', '-r', str(FPS), '-an',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    last = None
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        last = Image.frombytes('RGB', (W, H), b); yield last
    p.wait()
    while True: yield last

def lerp_track(keys, t):
    """keys: [(t, x, y), ...] -> linear interpolation"""
    if t <= keys[0][0]: return keys[0][1:]
    for (t0, x0, y0), (t1, x1, y1) in zip(keys, keys[1:]):
        if t <= t1:
            u = (t - t0) / (t1 - t0); u = u * u * (3 - 2 * u); return x0 + (x1 - x0) * u, y0 + (y1 - y0) * u
    return keys[-1][1:]

def shadowed(card, blur=22, off=10, alpha=70):
    pad = blur * 2; sh = Image.new('RGBA', (card.width + pad * 2, card.height + pad * 2), (0, 0, 0, 0))
    a = card.getchannel('A').point(lambda v: int(v * alpha / 255)); blk = Image.new('RGBA', card.size, (0, 0, 0, 255)); blk.putalpha(a)
    sh.paste(blk, (pad, pad + off), blk); sh = sh.filter(ImageFilter.GaussianBlur(blur)); sh.alpha_composite(card, (pad, pad)); return sh, pad

def paste_center(im, lay, cx, cy, sc=1.0, rot=0.0, alpha=1.0):
    if sc != 1.0: lay = lay.resize((max(1, round(lay.width * sc)), max(1, round(lay.height * sc))), Image.BILINEAR)
    if rot: lay = lay.rotate(rot, expand=True, resample=Image.BICUBIC)
    if alpha < 1: lay.putalpha(lay.getchannel('A').point(lambda v: int(v * alpha)))
    im.paste(lay, (round(cx - lay.width / 2), round(cy - lay.height / 2)), lay)

# ---------------- UI cards (Instagram-like, drawn in Founders Grotesk) ----------------
def question_sticker(q):
    w, h = 720, 250; c = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(c)
    d.rounded_rectangle((0, 0, w, h), 34, fill=(255, 255, 255, 255))
    ftop, fq = B.font(B.FM, 36), B.font(B.FB, 52)
    d.text(((w - d.textlength('Ask me a question', font=ftop)) / 2, 30), 'Ask me a question', font=ftop, fill=(140, 140, 140))
    d.rounded_rectangle((34, 96, w - 34, h - 34), 22, fill=(239, 239, 241, 255))
    d.text(((w - d.textlength(q, font=fq)) / 2, 118), q, font=fq, fill=INK)
    av = Image.new('RGBA', (84, 84), (0, 0, 0, 0)); ImageDraw.Draw(av).ellipse((0, 0, 83, 83), fill=(169, 33, 192, 255))
    ImageDraw.Draw(av).ellipse((6, 6, 77, 77), outline=(255, 255, 255, 255), width=5)
    out = Image.new('RGBA', (w, h + 42), (0, 0, 0, 0)); out.alpha_composite(c, (0, 42)); out.alpha_composite(av, ((w - 84) // 2, 0)); return out

def notification(title, body):
    w, h = 960, 170; c = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(c)
    d.rounded_rectangle((0, 0, w, h), 40, fill=(250, 250, 250, 245))
    d.rounded_rectangle((32, 37, 128, 133), 24, fill=(115, 0, 199, 255))
    fs = B.font(B.FB, 54); d.text((80 - d.textlength('S', font=fs) / 2, 52), 'S', font=fs, fill=(255, 255, 255))
    d.text((156, 34), title, font=B.font(B.FB, 38), fill=INK); d.text((156, 88), body, font=B.font(B.FM, 34), fill=(70, 70, 75))
    d.text((w - 40 - d.textlength('now', font=B.font(B.FM, 30)), 38), 'now', font=B.font(B.FM, 30), fill=(150, 150, 150)); return c

def comment(user, text):
    w = 820; f = B.font(B.FM, 40); fu = B.font(B.FB, 34)
    d0 = ImageDraw.Draw(Image.new('L', (1, 1))); lines = R.wrap(d0, text, f, w - 210)
    h = 92 + 50 * len(lines) + 34; c = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(c)
    d.rounded_rectangle((0, 0, w, h), 36, fill=(255, 255, 255, 250))
    d.ellipse((30, 30, 110, 110), fill=(214, 196, 178, 255)); d.text((134, 30), user, font=fu, fill=INK)
    d.text((134 + d.textlength(user, font=fu) + 16, 34), '2h', font=B.font(B.FM, 30), fill=(150, 150, 150))
    for i, ln in enumerate(lines): d.text((134, 78 + 50 * i), ln, font=f, fill=(40, 36, 40))
    hx, hy = w - 60, 64; d.text((hx - 14, hy - 22), '♡', font=B.font(B.FM, 44), fill=(150, 150, 150)); return c

# ---------------- effects ----------------
_noise = None
def burn(card, origin, prog, seed=3):
    """burn a card away from origin (card coords); prog 0..1. Charred band + glowing edge, hole grows."""
    global _noise
    w, h = card.size
    if _noise is None or _noise.shape != (h, w):
        rng = np.random.default_rng(seed); n = rng.random((h // 60 + 3, w // 60 + 3)).astype(np.float32)
        n = np.array(Image.fromarray((n * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)).astype(np.float32) / 255
        _noise = n
    yy, xx = np.mgrid[0:h, 0:w]; dist = np.hypot(xx - origin[0], yy - origin[1]) / math.hypot(w, h) + 0.10 * _noise
    front = prog * 1.25
    a = np.array(card).astype(np.float32)
    gone = dist < front - 0.02
    char = (dist >= front - 0.02) & (dist < front + 0.035)
    glow = (dist >= front - 0.05) & (dist < front - 0.005)
    k = np.clip((dist - (front - 0.02)) / 0.055, 0, 1)[..., None]
    a[..., :3] = np.where(char[..., None], a[..., :3] * k + np.array([40, 22, 12]) * (1 - k), a[..., :3])
    a[..., :3] = np.where(glow[..., None], np.array([255, 150, 40]), a[..., :3])
    a[..., 3] = np.where(gone, 0, a[..., 3]); a[..., 3] = np.where(glow, np.minimum(a[..., 3], 255), a[..., 3])
    return Image.fromarray(a.clip(0, 255).astype(np.uint8), 'RGBA')

def embers(im, cx, cy, t, n=14, seed=5):
    rng = np.random.default_rng(seed); d = ImageDraw.Draw(im, 'RGBA')
    for i in range(n):
        t0 = rng.random() * 1.2; life = 0.6 + rng.random() * 0.6; u = (t - t0) / life
        if 0 <= u <= 1:
            x = cx + (rng.random() - 0.5) * 380 + math.sin(u * 6 + i) * 20; y = cy - u * (160 + rng.random() * 220)
            r = 3 + rng.random() * 4; a = int(255 * (1 - u))
            d.ellipse((x - r, y - r, x + r, y + r), fill=(255, 170 + int(60 * rng.random()), 60, a))

def crumple(card, u):
    """u 0..1: card squeezes into a paper ball"""
    w, h = card.size; s = 1 - 0.85 * u
    c = card.resize((max(1, int(w * s)), max(1, int(h * s * (1 - 0.3 * u)))), Image.BILINEAR)
    if u > 0.2:
        rng = np.random.default_rng(int(u * 40)); a = np.array(c).astype(np.float32)
        sh = (rng.random(a.shape[:2]) * 70 * u).astype(np.float32); a[..., :3] -= sh[..., None]
        c = Image.fromarray(a.clip(0, 255).astype(np.uint8), 'RGBA')
        m = Image.new('L', c.size, 0); ImageDraw.Draw(m).ellipse((0, 0, c.width - 1, c.height - 1), fill=255)
        r = min(1, (u - 0.2) / 0.5); c.putalpha(Image.composite(m, c.getchannel('A'), Image.new('L', c.size, int(255 * r))).point(lambda v: v) if False else
                                             Image.blend(c.getchannel('A').convert('L'), m, r))
    return c

# ---------------- ends (same grammar as batch 32: slam -> still + logo + URL) ----------------
LOGO_K = G.LOGO_K
def slam(bg, ink, big, count, small, small_above, dur, logo_t=1.3, CY=980):
    fb, bs = G.fit_font(big, 960, 420); fsm = B.font(B.FM, 52)
    lg = Image.open(G.LOGO_W if sum(bg) < 600 else G.LOGO_K).convert('RGBA'); lg = lg.resize((420, round(420 * lg.height / lg.width)), Image.LANCZOS); furl = B.font(B.FM, 44)
    for k in range(round(dur * FPS) + 8):
        t = k / FPS; im = Image.new('RGB', (W, H), bg); d = ImageDraw.Draw(im, 'RGBA'); txt = big
        if count: txt = (big[0] if big[0] == '+' else '') + f"{round(count * min(1, t / 0.55) ** 0.6)}" + ('%' if '%' in big else '')
        sc = 1.35 - 0.35 * R.spring(t, 300, 16)
        lay = Image.new('RGBA', (W, bs + 80), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay); tw = dl.textlength(big, font=fb)
        dl.text(((W - tw) / 2, 10), txt, font=fb, fill=ink + (255,))
        lay = lay.resize((round(W * sc), round(lay.height * sc)), Image.BILINEAR); im.paste(lay, ((W - lay.width) // 2, CY - lay.height // 2), lay)
        a = int(255 * min(1, max(0, (t - 0.22) * 6))); off = (1 - R.spring(t - 0.22, 260, 20)) * 40
        lines = R.wrap(d, small, fsm, 900)
        for li, ln in enumerate(lines):
            lw = d.textlength(ln, font=fsm)
            y = (CY - bs // 2 - 100 - 64 * (len(lines) - 1 - li)) if small_above else (CY + bs // 2 + 40 + li * 64)
            d.text(((W - lw) / 2, y + off), ln, font=fsm, fill=ink + (a,))
        la = min(1, max(0, (t - logo_t) * 5))
        if la > 0:                                   # brand sign-off on the same field: logo + URL above the stat
            l2 = lg.copy(); l2.putalpha(l2.getchannel('A').point(lambda x: int(x * la))); ly = 330 + int((1 - R.spring(t - logo_t, 260, 20)) * 30)
            im.paste(l2, ((W - lg.width) // 2, ly), l2); uw = d.textlength('SickScienceLabs.com', font=furl)
            d.text(((W - uw) / 2, ly + lg.height + 16), 'SickScienceLabs.com', font=furl, fill=(ink if sum(bg) < 600 else INK) + (int(255 * la),))
        yield im

def endstill(path, dur, logo_y=230):
    st = G.cover(path); lg = Image.open(LOGO_K).convert('RGBA'); lg = lg.resize((420, round(420 * lg.height / lg.width)), Image.LANCZOS)
    f = B.font(B.FM, 44)
    for k in range(round(dur * FPS) + 8):
        t = k / FPS; z = 1.0 + 0.05 * t / dur; im = st.resize((round(W * z), round(H * z)), Image.BILINEAR)
        im = im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H)).convert('RGBA')
        a = min(1, t * 5); l2 = lg.copy(); l2.putalpha(l2.getchannel('A').point(lambda x: int(x * a)))
        im.paste(l2, ((W - lg.width) // 2, logo_y), l2); d = ImageDraw.Draw(im, 'RGBA')
        tw = d.textlength('SickScienceLabs.com', font=f); d.text(((W - tw) / 2, logo_y + lg.height + 18), 'SickScienceLabs.com', font=f, fill=INK + (int(255 * a),))
        yield im.convert('RGB')

# ---------------- videos: list of (generator_factory, duration, overlay(im, t) or None) ----------------
def v1():
    card = question_sticker('Is jawline serum a scam?'); sh, pad = shadowed(card)
    flame = json.load(open(os.path.join(CL, 'v1_flame.json')))
    CX, CY = 590, 470                      # card centre; the raised flame (≈950,577) touches its lower-right corner
    origin = (card.width - 70, card.height - 10)
    def o(im, t):
        if t > 3.3: return im
        im = im.convert('RGBA'); pop = R.spring(t, 380, 16)
        prog = 0 if t < 1.7 else min(1, (t - 1.7) / 1.4)
        c = burn(card, origin, prog) if prog > 0 else card
        s2, p2 = shadowed(c, alpha=int(70 * (1 - prog)))
        paste_center(im, s2, CX, CY, sc=0.6 + 0.4 * pop)
        if 1.6 < t < 3.3: embers(im, CX + 300 - prog * 260, CY + 120 - prog * 120, t - 1.6)
        return im.convert('RGB')
    return [(lambda: clip(os.path.join(CL, 'v1.mp4'), 3.6), 3.6, o),
            (lambda: slam((115, 0, 199), (255, 255, 255), '92%', 92, 'saw a more sculpted jawline', False, 2.8), 2.8, None)]

def v2():
    card = notification('SickScience', 'Your NetWork order has shipped'); sh, pad = shadowed(card)
    hand = [(0.0, 841, 428), (0.75, 841, 410), (1.0, 841, 492), (1.5, 820, 535), (2.0, 798, 813), (2.5, 733, 1091)]
    def o(im, t):
        if t > 1.9: return im
        im = im.convert('RGBA')
        if t < 0.72:                                   # drops in from the top, sways, then she reaches for it
            y = -120 + (300 + 120) * R.spring(t, 260, 14); paste_center(im, sh, W / 2, y, rot=math.sin(t * 9) * 2 * (1 - t))
        else:                                          # caught: snaps to the hand, shrinks into the fist, follows it down
            u = min(1, (t - 0.72) / 0.6); hx, hy = lerp_track(hand, t)
            cx = W / 2 + (hx - W / 2) * min(1, u * 1.6); cy = 300 + (hy - 300) * min(1, u * 1.6)
            paste_center(im, sh, cx, cy, sc=1 - 0.88 * u, rot=-12 * u, alpha=1 - max(0, (u - 0.75) / 0.25))
        return im.convert('RGB')
    return [(lambda: clip(os.path.join(CL, 'v2.mp4'), 3.6), 3.6, o),
            (lambda: slam((250, 248, 247), (200, 16, 46), '20%', 20,
                          'This October, 20% of NetWork sales on SickScienceLabs.com go to The Breast Cancer Research Foundation', False, 3.4, logo_t=1.9, CY=900), 3.4, None)]

def v3():
    card = comment('jess.m', 'my ponytail used to be twice this thick'); sh, pad = shadowed(card)
    hand = [(0.0, 820, 834), (1.0, 820, 834), (1.25, 906, 727), (1.5, 927, 770), (1.75, 927, 727), (2.0, 949, 663), (2.25, 1180, 600)]
    def o(im, t):
        if t > 2.3: return im
        im = im.convert('RGBA'); hx, hy = lerp_track(hand, t)
        if t < 1.15:                                    # pops up out of the card she is reading
            pop = R.spring(t - 0.1, 330, 15); paste_center(im, sh, 540 + (hx - 540) * (1 - pop), 470 + (hy - 470) * (1 - pop), sc=0.15 + 0.85 * pop)
        else:                                           # sucked back into her hand and crumpled, then thrown with it
            u = min(1, (t - 1.15) / 0.55); c = crumple(card, u); s2, _ = shadowed(c, blur=10, off=4)
            cx = 540 + (hx - 540) * min(1, u * 1.5); cy = 470 + (hy - 470) * min(1, u * 1.5)
            paste_center(im, s2, cx, cy, rot=u * 160 + max(0, t - 1.9) * 600)
        return im.convert('RGB')
    return [(lambda: clip(os.path.join(CL, 'v3.mp4'), 4.8), 4.8, o),
            (lambda: slam((62, 155, 28), (255, 255, 255), '+29%', 29, 'average increase in hair thickness (hair diameter)', False, 2.8), 2.8, None)]

VIDEOS = dict(v1=v1, v2=v2, v3=v3)

def render(v):
    shots = VIDEOS[v](); tmp = tempfile.mkdtemp(prefix=f'u40_{v}_'); sfx, tout = [(0.0, 'thump')], 0.0
    for i, (g, dur, o) in enumerate(shots):
        if i > 0: sfx.append((round(tout, 3), 'whoosh'))
        tout += round(dur * FPS) / FPS
    if v == 'v1': sfx.append((1.7, 'fire'))
    if v == 'v2': sfx += [(0.15, 'pop'), (0.75, 'pop')]
    if v == 'v3': sfx += [(0.1, 'pop'), (1.2, 'crumple'), (2.0, 'whoosh')]
    end = tout - round(shots[-1][1] * FPS) / FPS
    json.dump({'duration': tout, 'end': end, 'sfx': sfx}, open(os.path.join(OUT, f'u40_{v}_cues.json'), 'w'))
    out = os.path.join(tmp, 'o.mp4')
    enc = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-f', 'lavfi', '-t', f'{tout:.3f}', '-i', f'anullsrc=r={SR}:cl=stereo',
                            '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-c:a', 'aac', '-shortest', out], stdin=subprocess.PIPE)
    q = collections.deque()
    def emit(im):
        q.append(im)
        if len(q) > 3: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    for i, (g, dur, o) in enumerate(shots):
        n = round(dur * FPS); gen = g()
        if i > 0:
            for j, amt in enumerate((0.25, 0.6, 1.0)[-len(q):]): q[j] = R.whip(q[j], amt, -1)
        for k in range(n):
            t = k / FPS; im = next(gen).copy()
            if o: im = o(im, t)
            if i > 0 and k < 3: im = R.whip(im, (1.0, 0.6, 0.25)[k], 1)
            emit(im)
    while q: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    enc.stdin.close(); enc.wait()
    shutil.copy(out, os.path.join(OUT, f'u40_{v}_voice.mp4')); shutil.rmtree(tmp, ignore_errors=True)
    subprocess.run([FF, '-v', 'error', '-y', '-i', os.path.join(OUT, f'u40_{v}_voice.mp4'), '-vf', 'fps=4,scale=150:-1,tile=10x4',
                    '-frames:v', '1', os.path.join(OUT, f'u40_{v}_contact.jpg')])
    print(v, 'ok', round(tout, 1), 's')

if __name__ == '__main__':
    for v in sys.argv[1:] or list(VIDEOS): render(v)
