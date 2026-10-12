"""Batch 29 — ShapeShift UGC flow, shortened (~28 s) in 4 hook variants, with motion-design upgrades:
closed-form springs for type/checks/cards, whip-pan transitions with motion blur between people, punch-ins on cutaways,
synthesized SFX (whoosh / pop / thump), speech sped up 10 %. Same clips and word timings as render28.
usage: python render29.py [v1 v2 v3 v4] -> out/u29_v*.mp4 + out/u29_v*_contact.jpg"""
import sys, math
from render28 import *   # W, H, FPS, SR, frames, words, WORDS, fonts, top_shade, wrap, caption, label, stars, endcard, ...

SPEED = 1.10
GAIN_SFX = 0.0 if os.environ.get('MUSIC') else 0.22   # with MUSIC=1 the SFX come from mgaudio (music29.py)

# ---------- motion primitives (pure functions of time)
def spring(t, k=170, d=22):
    if t <= 0: return 0.0
    w0 = math.sqrt(k); z = d / (2 * w0)
    if z < 1:
        wd = w0 * math.sqrt(1 - z * z)
        return 1 - math.exp(-z * w0 * t) * (math.cos(wd * t) + (z * w0 / wd) * math.sin(wd * t))
    return 1 - math.exp(-w0 * t) * (1 + w0 * t)

def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))

# ---------- kinetic overlays
def k_headline(img, text, t, y=300, size=78, t0=0.0):
    """words rise in one after another on a spring"""
    base = Image.new('RGBA', img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(base); f = font(FB, size)
    lines = wrap(d, text, f, 950); i = 0
    for li, ln in enumerate(lines):
        x = 65
        for wd in ln.split():
            s = spring(t - t0 - i * 0.05, 260, 24); a = clamp((t - t0 - i * 0.05) * 8)
            yy = y + li * int(size * 1.02) + (1 - s) * 46
            d.text((x, yy), wd, font=f, fill=(255, 255, 255, int(255 * a)), stroke_width=2, stroke_fill=(0, 0, 0, int(255 * a)))
            x += d.textlength(wd + ' ', font=f); i += 1
    img.paste(base, (0, 0), base)
    return y + len(lines) * int(size * 1.02)

def k_checklist(img, items, t, y0):
    base = Image.new('RGBA', img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(base); f = font(FB, 44)
    for i, (ts, txt) in enumerate(items):
        if t < ts: continue
        s = spring(t - ts, 300, 20); a = clamp((t - ts) * 10)
        y = y0 + 22 + i * 74; x = 65 - (1 - s) * 80
        d.rectangle((x, y + 4, x + 44, y + 48), outline=(255, 255, 255, int(255 * a)), width=5)
        c = clamp((t - ts - 0.08) / 0.12)
        if c > 0:
            p1, p2, p3 = (x + 9, y + 26), (x + 19, y + 37), (x + 37, y + 13)
            if c < 0.5: q = (p1[0] + (p2[0] - p1[0]) * c * 2, p1[1] + (p2[1] - p1[1]) * c * 2); d.line([p1, q], fill='white', width=6)
            else: q = (p2[0] + (p3[0] - p2[0]) * (c - .5) * 2, p2[1] + (p3[1] - p2[1]) * (c - .5) * 2); d.line([p1, p2, q], fill='white', width=6, joint='curve')
        d.text((x + 64, y), txt, font=f, fill=(255, 255, 255, int(255 * a)), stroke_width=2, stroke_fill=(0, 0, 0, int(255 * a)))
    img.paste(base, (0, 0), base)

def k_review(img, name, text, y, t, ts):
    s = spring(t - ts, 220, 22)
    if t < ts: return
    card = Image.new('RGBA', img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(card); w = 600
    lines = wrap(d, text, font(FM, 34), w - 48); h = 120 + len(lines) * 40; x = 65 + (1 - s) * -120
    d.rounded_rectangle((x, y, x + w, y + h), 18, fill=(255, 255, 255, 245))
    d.text((x + 24, y + 18), name, font=font(FB, 34), fill=(20, 20, 20))
    stars(d, x + 24, y + 60, 28, (169, 33, 192))
    for i, ln in enumerate(lines): d.text((x + 24, y + 98 + i * 40), ln, font=font(FM, 34), fill=(30, 30, 30))
    a = clamp((t - ts) * 8); card.putalpha(card.getchannel('A').point(lambda v: int(v * a)))
    img.paste(card, (0, 0), card)

def k_rating(img, t, ts):
    d = ImageDraw.Draw(img); f = font(FB, 78)
    d.text((65, 300), '4.7', font=f, fill='white', stroke_width=2, stroke_fill=(0, 0, 0))
    x0 = 65 + d.textlength('4.7 ', font=f)
    for k in range(5):          # stars pop in one by one
        s = spring(t - ts - k * 0.06, 320, 18)
        if s > 0.02: stars(d, x0 + k * 67 + 31 * (1 - s), 306 + 31 * (1 - s), 62 * s, (255, 255, 255), n=1)
    d.text((65, 380), 'FROM 576 REVIEWS', font=f, fill='white', stroke_width=2, stroke_fill=(0, 0, 0))

# ---------- beats (each returns segments in SOURCE time; t passed to overlays is source time)
SFX = []   # (output_time, type) collected while rendering

def B(clip, a0, a1, shots, draw, who, cues=()):
    return dict(ac=clip, a0=a0, a1=a1, shots=shots, draw=draw, who=who, cues=list(cues))

def beat_hook_obsessed():
    w = WORDS['c11_A_hook']; a0 = max(0, w[0][1] - 0.3); a1 = w[-1][2] + 0.25
    def f(im, t, ws): im = top_shade(im); k_headline(im, "WHY EVERYONE'S OBSESSED WITH THIS", t); caption(im, ws, t); return im
    return [B('c11_A_hook', a0, a1, [(0, 'c11_A_hook', a0, 1.0)], f, 'A')]

def beat_ingredients(short=False):
    n = 'c15b_C_ingredients'; w = WORDS[n]; a0 = max(0, w[0][1] - 0.1); a1 = w[-1][2] + 0.25
    ws = words(n, a0, a1); tw = wstart(ws, 'with', 2.6)
    if short:
        a1s = a0 + tw - 0.05
        def fs(im, t, w_): im = top_shade(im); k_headline(im, 'SHAPESHIFT HELPS VISIBLY TIGHTEN & FIRM THE NECK', t); caption(im, w_, t); return im
        return [B(n, a0, a1s, [(0, 'c20_macro', 0.3, 1.0)], fs, 'M')]
    tn, tc, ti = wstart(ws, 'nx', tw), wstart(ws, 'caffeine', tw + 1), wstart(ws, 'niacinamide', tw + 2)
    def f(im, t, w_):
        im = top_shade(im)
        if t < tw: k_headline(im, 'SHAPESHIFT HELPS VISIBLY TIGHTEN & FIRM THE NECK', t)
        else:
            y = k_headline(im, 'WITH', t, t0=tw)
            k_checklist(im, [(tn, 'NX35™ SCULPT TECHNOLOGY'), (tc, 'CAFFEINE'), (ti, 'NIACINAMIDE (VITAMIN B3)')], t, y)
        caption(im, w_, t); return im
    return [B(n, a0, a1, [(0, 'c20_macro', 0.3, 1.0), (tw, n, a0 + tw, 1.0)], f, 'C', [(tn, 'pop'), (tc, 'pop'), (ti, 'pop'), (tw, 'punch')])]

def beat_problem(hook=False):
    w = WORDS['c16_D_problem']; a0 = max(0, w[0][1] - 0.1); a1 = w[-1][2] + 0.25
    ws = words('c16_D_problem', a0, a1)
    to, td, tl, ts = wstart(ws, 'only', 0.3), wstart(ws, 'deliver', 2.2), wstart(ws, 'leave', 4.2), wstart(ws, 'still', 4.0)
    def f(im, t, w_):
        im = top_shade(im); y = k_headline(im, 'MOST NECK CREAMS…', t)
        k_checklist(im, [(to, 'ONLY WORK ON THE SURFACE'), (td, 'DELIVER TEMPORARY RESULTS'), (tl, 'LEAVE YOU DEPENDENT ON PROCEDURES')], t, y)
        caption(im, w_, t); return im
    return [B('c16_D_problem', a0, a1, [(0, 'c16_D_problem', a0, 1.0), (td, 'c19_A_pinch', 0.2, 1.0), (ts, 'c14_profilecheck', 0.5, 1.0)], f, 'D',
              [(to, 'pop'), (td, 'pop'), (tl, 'pop'), (td, 'punch'), (ts, 'punch')])]

def beat_testimony(hook=False, s1only=False):
    """two sentences of the real Venus B. review, jump-cut (skips the mispronounced product name)"""
    n = 'c13b_B_testimony'; w = WORDS[n]
    s1_end = [x for x in w if x[0].lower().startswith('sagging')][0][2] + 0.2
    im_ = [x for x in w if x[0].lower() == "i'm"][0][1] - 0.05
    a0 = max(0, w[0][1] - 0.1); a1 = w[-1][2] + 0.25
    def f(im, t, ws):
        if hook: im = top_shade(im); k_headline(im, "WHY EVERYONE'S OBSESSED WITH THIS", t)
        label(im, 'Venus B., verified review'); caption(im, ws, t); return im
    def g(im, t, ws): label(im, 'Venus B., verified review'); caption(im, ws, t); return im
    first = [B(n, a0, s1_end, [(0, n, a0, 1.0)], f, 'B')]
    return first if s1only else first + [B(n, im_, a1, [(0, n, im_, 1.0)], g, 'B', [(0, 'punch')])]

def beat_offer(short=False):
    w = WORDS['c17_A_offer']; a0 = max(0, w[0][1] - 0.1); a1 = w[-1][2] + 0.25
    ws = words('c17_A_offer', a0, a1)
    t15 = wstart(ws, '15', 1.5); tj = next((st for w_, st, e_ in ws if w_.lower().strip('.,') == 'and' and st > t15), 2.0)   # the 'and' AFTER '15%'
    if short:
        a1s = a0 + tj - 0.02
        def fs(im, t, w_):
            im = top_shade(im); y = k_headline(im, 'SUBSCRIBE & SAVE 15%', t)
            ts = 0.45; s_ = spring(t - ts, 260, 24)
            if t > ts:
                d = ImageDraw.Draw(im); f = font(FB, 56); yy = y + 14 + (1 - s_) * 30
                d.text((65, yy), '4.7', font=f, fill='white', stroke_width=2, stroke_fill=(0, 0, 0))
                x0 = 65 + d.textlength('4.7 ', font=f); stars(d, x0, yy + 6, 44, (255, 255, 255))
                d.text((x0 + 5 * 48 + 14, yy), '· 576 REVIEWS', font=f, fill='white', stroke_width=2, stroke_fill=(0, 0, 0))
            caption(im, w_, t); return im
        return [B('c17_A_offer', a0, a1s, [(0, 'c17_A_offer', a0, 1.0)], fs, 'A', [(0.45, 'pop')])]
    def f(im, t, w_):
        im = top_shade(im)
        if t < tj: k_headline(im, 'SUBSCRIBE & SAVE 15%', t)
        else:
            k_rating(im, t, tj)
            k_review(im, 'Carol F.', 'I can see a difference in my jawline in two weeks. Impressed with this product.', 520, t, tj + 0.15)
            k_review(im, 'Katie W.', 'I was considering cosmetic surgery for my neck. This product changed my mind!', 780, t, tj + 0.6)
        caption(im, w_, t); return im
    return [B('c17_A_offer', a0, a1, [(0, 'c17_A_offer', a0, 1.0), (tj, 'c11_A_hook', 1.2, 1.0)], f, 'A',
              [(tj, 'punch'), (tj + 0.15, 'pop'), (tj + 0.6, 'pop')])]

def beat_result(full=False):
    w = WORDS['c18_C_howto']; ws_all = words('c18_C_howto', 0, 99)
    tc = wstart(ws_all, 'chisel', 3.5)
    a0 = max(0, (w[0][1] - 0.5) if full else tc - 0.25); a1 = w[-1][2] + 0.25
    def f(im, t, ws):
        im = top_shade(im)
        if full and t < tc - a0: k_headline(im, '1–2 PUMPS · TWICE DAILY', t)
        else: k_headline(im, 'CHISEL YOUR JAWLINE IN 2 WEEKS', t, t0=(tc - a0) if full else 0)
        caption(im, ws, t); return im
    return [B('c18_C_howto', a0, a1, [(0, 'c18_C_howto', a0, 1.42)], f, 'C')]

VARIANTS = {   # max 20 s each (user 2026-10-09)
    'v1': lambda: beat_hook_obsessed() + beat_ingredients() + beat_problem() + beat_offer(short=True),
    'v2': lambda: beat_problem(hook=True) + beat_ingredients(short=True) + beat_testimony(s1only=True) + beat_result() + beat_offer(short=True),
    'v3': lambda: beat_testimony(hook=True) + beat_problem() + beat_ingredients(short=True) + beat_offer(short=True),
    'v4': lambda: beat_result(full=True) + beat_problem() + beat_ingredients(short=True) + beat_offer(short=True),
}

# ---------- audio
def audio_fast(name, a0, a1):
    raw = subprocess.run([FF, '-v', 'error', '-ss', str(a0), '-t', str(a1 - a0), '-i', os.path.join(CL, name + '.mp4'),
                          '-af', f'atempo={SPEED}', '-ac', '2', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).reshape(-1, 2).astype(np.float32)
    n = round((a1 - a0) / SPEED * SR); a = np.pad(a, ((0, max(0, n - len(a))), (0, 0)))[:n]
    f = min(len(a), int(0.015 * SR)); r = np.linspace(0, 1, f)[:, None]; a[:f] *= r; a[-f:] *= r[::-1]
    return a

def synth(kind):
    rng = np.random.default_rng(7)
    if kind == 'whoosh':
        n = int(0.32 * SR); t = np.arange(n) / SR; x = rng.standard_normal(n)
        env = np.sin(np.pi * np.clip(t / 0.32, 0, 1)) ** 2
        # sweep a one-pole low-pass from dark to bright
        y = np.zeros(n); c = np.linspace(0.02, 0.35, n); acc = 0.0
        for i in range(n): acc += c[i] * (x[i] - acc); y[i] = acc
        return (y * env * 0.9)
    if kind == 'pop':
        n = int(0.09 * SR); t = np.arange(n) / SR
        return np.sin(2 * np.pi * (700 + 1400 * t) * t) * np.exp(-t * 45) * 0.55
    if kind == 'thump':
        n = int(0.45 * SR); t = np.arange(n) / SR
        return np.sin(2 * np.pi * (95 - 55 * t) * t) * np.exp(-t * 9) * 1.0
    return np.zeros(1)

# ---------- transitions
def whip(img, amount, direction):
    """horizontal shift + motion blur; amount 0..1"""
    if amount <= 0.01: return img
    a = np.asarray(img).astype(np.float32); shift = int(direction * amount * 260)
    taps = 7; acc = np.zeros_like(a)
    pad = 420; ap = np.pad(a, ((0, 0), (pad, pad), (0, 0)), mode='edge')   # edge-extend instead of wrapping
    for k in range(taps):
        sh = max(-pad, min(pad, shift + int((k - taps // 2) * amount * 26)))
        acc += ap[:, pad - sh:pad - sh + a.shape[1]]
    return Image.fromarray((acc / taps).astype(np.uint8))

def punch(img, t):
    s = 1 + 0.07 * (1 - spring(t, 220, 24))
    if s <= 1.001: return img
    im = img.resize((round(W * s), round(H * s)), Image.BILINEAR)
    return im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H))

class Reader:
    """sequential frame reader for one clip (+zoom); reopens with -ss only when asked to go backwards or far ahead"""
    def __init__(self, name, zoom):
        self.name, self.zoom, self.p, self.pos = name, zoom, None, -1
    def _open(self, idx):
        self.close()
        vf = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}'
        if self.zoom != 1.0:
            zw, zh = round(W * self.zoom), round(H * self.zoom); vf += f',scale={zw}:{zh},crop={W}:{H}:{(zw - W) // 2}:0'
        self.p = subprocess.Popen([FF, '-v', 'error', '-ss', f'{idx / FPS:.4f}', '-i', os.path.join(CL, self.name + '.mp4'),
                                   '-vf', vf, '-r', str(FPS), '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
        self.pos = idx - 1; self.last = None
    def get(self, idx):
        if self.p is None or idx <= self.pos - 0 and idx != self.pos or idx > self.pos + 48: self._open(idx)
        while self.pos < idx:
            buf = self.p.stdout.read(W * H * 3)
            if len(buf) < W * H * 3: break                    # clip ended: hold the last frame
            self.last = buf; self.pos += 1
        return Image.frombuffer('RGB', (W, H), self.last, 'raw', 'RGB', 0, 1).copy()
    def close(self):
        if self.p: self.p.stdout.close(); self.p.kill(); self.p.wait(); self.p = None

def render(vname, tmpdir=None):
    import collections, tempfile, shutil
    tmpdir = tmpdir or tempfile.mkdtemp(prefix=f'u29_{vname}_')
    segs = VARIANTS[vname](); auds, sfx = [], []
    tout = 0.0; prev_who = None; plan = []
    # pass 1: audio + timeline (cheap)
    for si, s in enumerate(segs):
        n = round((s['a1'] - s['a0']) / SPEED * FPS)
        auds.append(audio_fast(s['ac'], s['a0'], s['a1'])[:round(n / FPS * SR)])
        kind = None
        if si > 0:
            kind = 'whip' if s['who'] != prev_who else 'punch'
            sfx.append((tout, 'whoosh' if kind == 'whip' else 'pop'))
        for c in s['cues']:
            if c[1] != 'punch': sfx.append((tout + c[0] / SPEED, c[1]))
        plan.append((s, n, kind)); tout += n / FPS; prev_who = s['who']
    END = 1.5; nend = round(END * FPS); sfx.append((tout, 'thump'))
    total = sum(n for _, n, _ in plan) + nend
    auds.append(np.zeros((round(END * SR), 2), np.float32)); a = np.concatenate(auds)
    for ts, kind in sfx:
        x = synth(kind) * 32767 * GAIN_SFX; i0 = int(ts * SR); i1 = min(len(a), i0 + len(x))
        if i0 < len(a): a[i0:i1] += x[:i1 - i0, None]
    json.dump({'duration': total / FPS, 'end': tout, 'sfx': [[round(t, 3), k] for t, k in sfx]},
              open(os.path.join(OUT, f'u29_{vname}_cues.json'), 'w'))
    raw = os.path.join(tmpdir, 'a.raw'); np.clip(a, -32768, 32767).astype(np.int16).tofile(raw)
    tmp_out = os.path.join(tmpdir, 'out.mp4')
    enc = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', raw, '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18',
                            '-c:a', 'aac', '-b:a', '192k', '-shortest', tmp_out], stdin=subprocess.PIPE)
    # pass 2: stream frames; keep 3 unwritten frames so a whip can reach back across the cut
    q = collections.deque(); readers = {}
    def emit(im):
        q.append(im)
        if len(q) > 3: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    for s, n, kind in plan:
        ws = words(s['ac'], s['a0'], s['a1'])
        punches = [c[0] for c in s['cues'] if c[1] == 'punch'] + ([0.0] if kind == 'punch' else [])
        if kind == 'whip':
            for j, amt in enumerate((0.25, 0.6, 1.0)[-len(q):]): q[j] = whip(q[j], amt, -1)
        for k in range(n):
            t = k / FPS * SPEED
            shot = [x for x in s['shots'] if x[0] <= t][-1]
            key = (shot[1], shot[3])
            if key not in readers:
                if len(readers) >= 3: readers.pop(next(iter(readers))).close()
                readers[key] = Reader(*key)
            im = readers[key].get(round((shot[2] + (t - shot[0])) * FPS))
            pts = sorted(p for p in punches if p <= t)
            if pts: im = punch(im, (t - pts[-1]) / SPEED)
            im = s['draw'](im, t, ws)
            if kind == 'whip' and k < 3: im = whip(im, (1.0, 0.6, 0.25)[k], 1)
            emit(im)
    for r in readers.values(): r.close()
    ec = endcard()
    for k in range(nend):
        t = k / FPS; sc = 1.06 - 0.06 * spring(t, 200, 22)
        im = ec.resize((round(W * sc), round(H * sc)), Image.LANCZOS)
        emit(im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H)))
    while q: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    enc.stdin.close(); enc.wait()
    out = os.path.join(OUT, f'u29_{vname}_voice.mp4' if os.environ.get('MUSIC') else f'u29_{vname}.mp4')
    shutil.copy(tmp_out, out); shutil.rmtree(tmpdir, ignore_errors=True)
    subprocess.run([FF, '-v', 'error', '-y', '-i', out, '-vf', 'fps=2,scale=180:-1,tile=8x8', '-frames:v', '1',
                    os.path.join(OUT, f'u29_{vname}_contact.jpg')])
    print(vname, 'ok', round(total / FPS, 1), 's')

if __name__ == '__main__':
    for v in (sys.argv[1:] or list(VARIANTS)): render(v)
