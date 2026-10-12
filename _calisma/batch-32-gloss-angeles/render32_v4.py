"""Batch 32 — Gloss Angeles podcast cut-downs (ep. 2025-05-13, product segment 9:56–20:13; usage approved by the user
2026-10-10). 9:16 crop of the 16:9 two-camera podcast, jump cuts with alternating punch-in, word captions, credit line,
brand end card on a generated packshot. Not used on purpose: the 'lipid droplets / fat reserves' claim, the old $58
price, 'only on their website'. Streams frames (memory feedback-render-memory). Total ≤20 s.
usage: python render32.py g1|g2|g3|g4   -> out/u32_<v>_voice.mp4 + cues  (music: music32.py)"""
import os, sys, json, subprocess, tempfile, shutil, collections
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__)); SS = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(SS, '_calisma', 'batch-31-ugc-products'))
import render31 as B                                    # endcard, font, FM/FB; B.R = render29 helpers
R = B.R
SRC = os.path.join(HERE, 'src', 'gloss.mp4'); OUT = os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
W, H, FPS, SR = 1080, 1920, 24, 48000; FF = B.FF
WORDS = json.load(open(os.path.join(HERE, 'src', 'words_tail.json')))
FIX = {'sick': 'Sick', 'science.': 'Science.', "glam's": 'Glams'}
O = os.path.join(SS, '_calisma')
FOOT = os.path.expanduser('~/motion-tools/footage-v3/v3')      # brand's own 9:16 footage (Drive 'v3', shared by the user 2026-10-10)
FD = {k: float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', os.path.join(FOOT, k + '.mp4')],
                              capture_output=True, text=True).stdout) for k in ('product2', 'short7', 'short8')}
# per video: b-roll cutaways (segment, offset s, dur s, clip, clip start) under the podcast audio, and the end sequence
CUT = {
    'g1': dict(broll=[(1, 0.1, 1.8, 'product2', 9.8)], end=[('clip', 'product2', FD['product2'] - 2.6, 2.6)]),
    'g2': dict(broll=[(0, 1.6, 1.4, 'short7', 0.0), (1, 0.3, 1.6, 'product2', 10.0)],
               end=[('slam', 1.2), ('clip', 'short7', FD['short7'] - 2.6, 2.4)]),
    'g3': dict(broll=[(0, 0.9, 2.0, 'product2', 9.8)], end=[('slam', 1.3), ('still', 1.5)]),
    'g4': dict(broll=[(0, 4.6, 2.2, 'short10', 0.3), (1, 1.6, 1.8, 'product1', 9.2)],
               end=[('clip', 'short8', FD['short8'] - 2.7, 2.7)]),
}
HOOK = 2.6                                                     # hook headline shows, then leaves
LOGO_K = os.path.join(O, 'video-01-bcrf/assets/logo.png'); LOGO_W = os.path.join(O, 'batch-27-video/assets/logo_white.png')
# end sequence per video: stat slam on a colour field (site copy verbatim), then a different approved campaign still
ENDS = {
    'g1': dict(bg=(115, 0, 199), ink=(255, 255, 255), big='92%', count=92, small='SAW A MORE SCULPTED JAWLINE', small_above=False,
               still='batch-02-textless/02-shapeshift_9x16.png', dark=False),
    'g2': dict(bg=(169, 33, 192), ink=(255, 255, 255), big='2 WEEKS', count=None, small='CHISEL YOUR JAWLINE IN', small_above=True,
               still='batch-21-50/scenes/b22_glass.png', dark=False),
    'g3': dict(bg=(238, 232, 246), ink=(115, 0, 199), big='GEL-SERUM', count=None, small='TEXTURE', small_above=True,
               still='batch-21-50/scenes/b21_lab.png', dark=False),
    'g4': dict(bg=(14, 12, 16), ink=(255, 255, 255), big='14', count=14, small='AWARDS INCL. OPRAH, INSTYLE & ESQUIRE', small_above=False,
               still='batch-02-textless/01-vault_9x16.png', dark=True),
}

def frames(a, dur):
    """Full 16:9 frames; each frame is classified by camera (green moss wall top-right = host 2) and cropped on that
    host's face, so camera switches inside a segment keep the speaker centred."""
    p = subprocess.Popen([FF, '-v', 'error', '-ss', f'{a:.3f}', '-t', f'{dur:.3f}', '-i', SRC, '-r', str(FPS),
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    last, N = None, 1920 * 1080 * 3
    while True:
        b = p.stdout.read(N)
        if len(b) < N: break
        x = np.frombuffer(b, np.uint8).reshape(1080, 1920, 3); m = x[100:400:4, 1550:1900:4].mean((0, 1))
        x0 = 1000 if (m[1] - m[0]) > -30 else 480                # cam 2 face ~x1280, cam 1 face ~x800
        last = (Image.fromarray(x[:, x0:x0 + 608]).resize((W, H), Image.LANCZOS), x0); yield last
    p.wait()
    while True: yield last                               # pad if ffmpeg returns a frame short

def foot(name, t0, dur):
    p = subprocess.Popen([FF, '-v', 'error', '-ss', f'{t0:.3f}', '-t', f'{dur:.3f}', '-i', os.path.join(FOOT, name + '.mp4'),
                          '-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}', '-r', str(FPS), '-an',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    last = None
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        last = Image.frombytes('RGB', (W, H), b); yield last
    p.wait()
    while True: yield last

def seg_words(a, b):
    out = []
    for w, s, e in WORDS:
        if a - 0.05 <= s < b:
            k = w.strip('.,!?'); out.append((FIX.get(w.lower(), k).strip('.,!?'), s - a, e - a, w[-1:] in '.,!?'))
    return out

HY = 760                                                 # headline at chest height: podcast faces fill the top third
_g = np.interp(np.arange(H), [600, 740, 1000, 1120], [0, 0.42, 0.42, 0])[:, None, None]
def mid_shade(im):
    a = np.asarray(im).astype(np.float32); a *= (1 - _g); return Image.fromarray(a.astype(np.uint8))

def credit(im, y):
    d = ImageDraw.Draw(im, 'RGBA'); f = B.font(B.FM, 32); txt = 'via Gloss Angeles Podcast'
    d.text((65, y), txt, font=f, fill=(255, 255, 255, 235), stroke_width=2, stroke_fill=(0, 0, 0, 160))

VIDEOS = {   # headline, [(src_start, src_end)] cut only at sentence ends, end card (photo, name, sub, extra), end seconds
    'g1': ('“SO SHOOK BY THESE BEFORE & AFTERS”', [(604.2, 607.7), (616.4, 624.88), (629.2, 631.95)],
           None, 2.8),
    'g2': ('2 WEEKS IN: “AM I CRAZY?”', [(632.5, 641.6), (643.2, 648.8)],
           None, 2.8),
    'g3': ('“ISN’T STICKY AT ALL”', [(782.6, 789.8), (800.62, 803.8)],
           None, 2.8),
    'g4': ('“THEY’RE ACTUAL SCIENTISTS”', [(1112.3, 1120.5), (1141.6, 1145.5), (1152.0, 1155.62)],
           None, 2.8),
}

# ---------- hook headline: words slam in big-to-size on a spring
_wcache = {}
def word_img(wd, size):
    k = (wd, size)
    if k not in _wcache:
        f = B.font(B.FB, size); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1))); bb = d0.textbbox((0, 0), wd, font=f, stroke_width=3)
        im = Image.new('RGBA', (bb[2] - bb[0] + 8, bb[3] - bb[1] + 8), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((4 - bb[0], 4 - bb[1]), wd, font=f, fill=(255, 255, 255, 255), stroke_width=3, stroke_fill=(0, 0, 0, 255))
        _wcache[k] = im
    return _wcache[k]

def slam_headline(img, text, t, y=HY, size=88):
    if t > HOOK + 0.35: return y
    out = max(0.0, (t - HOOK) / 0.35)                    # exit: slide up + fade
    if out > 0:
        lay = Image.new('RGBA', img.size, (0, 0, 0, 0)); slam_headline(lay, text, HOOK - 0.001, y, size)
        lay.putalpha(lay.getchannel('A').point(lambda v: int(v * (1 - out)))); img.paste(lay, (0, -int(120 * out ** 2)), lay); return y
    d = ImageDraw.Draw(img); f = B.font(B.FB, size); lines = R.wrap(d, text, f, 950); i = 0; yy = y
    for ln in lines:
        x = 65
        for wd in ln.split():
            tt = t - i * 0.09; wi = word_img(wd, size); adv = d.textlength(wd + ' ', font=f)
            if tt > 0:
                sc = 1 + 0.8 * (1 - R.spring(tt, 320, 18)); a = min(1, tt * 10)
                im = wi.resize((max(1, round(wi.width * sc)), max(1, round(wi.height * sc))), Image.BILINEAR)
                if a < 1: im.putalpha(im.getchannel('A').point(lambda v: int(v * a)))
                cx, cy = x + wi.width / 2, yy + wi.height / 2
                img.paste(im, (round(cx - im.width / 2), round(cy - im.height / 2)), im)
            x += adv; i += 1
        yy += int(size * 1.04)
    return yy

# ---------- captions: 1-3 word groups, centred, pop-in, active word on a brand-purple block
PURPLE = (169, 33, 192)
def groups(ws):
    out, cur = [], []
    for w in ws:
        if cur and (len(cur) == 3 or w[1] - cur[-1][2] > 0.3): out.append(cur); cur = []
        cur.append(w)
        if w[3]: out.append(cur); cur = []
    if cur: out.append(cur)
    return out

def big_caption(img, gs, t, y=1060):
    g = next((g for g in gs if g[0][1] - 0.05 <= t < (g[-1][2] + 0.25)), None)
    if not g: return
    size = 76; f = B.font(B.FB, size); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    words = [w[0].upper() for w in g]
    while d0.textlength(' '.join(words), font=f) > 940 and size > 52: size -= 4; f = B.font(B.FB, size)
    sp = d0.textlength(' ', font=f); tw = d0.textlength(' '.join(words), font=f)
    lay = Image.new('RGBA', (W, size + 60), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); x = (W - tw) / 2
    act = max([j for j, w in enumerate(g) if w[1] - 0.03 <= t] or [0])      # exactly one active word
    for j, (w, word) in enumerate(zip(g, words)):
        wl = d.textlength(word, font=f)
        if j == act:
            d.rounded_rectangle((x - 14, 14, x + wl + 14, 14 + size + 22), radius=14, fill=PURPLE + (255,))
        d.text((x, 20), word, font=f, fill=(255, 255, 255, 255), stroke_width=4, stroke_fill=(0, 0, 0, 255))
        x += wl + sp
    sc = 0.8 + 0.2 * R.spring(t - g[0][1] + 0.05, 420, 20)
    lay = lay.resize((round(W * sc), round(lay.height * sc)), Image.BILINEAR)
    img.paste(lay, ((W - lay.width) // 2, round(y + (size + 60) * (1 - sc) / 2)), lay)

def cover(path):
    im = Image.open(path).convert('RGB'); sc = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    return im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H))

def fit_font(text, maxw, start):
    size = start
    while size > 80 and ImageDraw.Draw(Image.new('L', (1, 1))).textlength(text, font=B.font(B.FB, size)) > maxw: size -= 6
    return B.font(B.FB, size), size

SLAM = 1.3
def end_frames(v, END):
    e = ENDS[v]; parts = CUT[v]['end']
    lg = Image.open(LOGO_W if e['dark'] else LOGO_K).convert('RGBA'); lg = lg.resize((420, round(420 * lg.height / lg.width)), Image.LANCZOS)
    url_ink = (255, 255, 255) if e['dark'] else (24, 18, 22)
    fb, bs = fit_font(e['big'], 960, 420); fsm = B.font(B.FM, 56)
    for pi, part in enumerate(parts):
        n = round(part[-1] * FPS)
        if part[0] == 'clip': g = foot(part[1], part[2], part[3] + 0.2)
        if part[0] == 'still': still = cover(os.path.join(O, e['still']))
        for k in range(n):
            t = k / FPS
            if part[0] == 'slam':                                           # stat slam on the product colour
                im = Image.new('RGB', (W, H), e['bg']); d = ImageDraw.Draw(im, 'RGBA'); txt = e['big']
                if e['count']: txt = f"{round(e['count'] * min(1, (t / 0.55)) ** 0.6)}" + ('%' if '%' in e['big'] else '')
                sc = 1.35 - 0.35 * R.spring(t, 300, 16)
                lay = Image.new('RGBA', (W, bs + 80), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
                tw = dl.textlength(e['big'], font=fb); dl.text(((W - tw) / 2, 10), txt, font=fb, fill=e['ink'] + (255,))
                lay = lay.resize((round(W * sc), round(lay.height * sc)), Image.BILINEAR); im.paste(lay, ((W - lay.width) // 2, 980 - lay.height // 2), lay)
                a = int(255 * min(1, max(0, (t - 0.22) * 6))); off = (1 - R.spring(t - 0.22, 260, 20)) * 40
                lines = R.wrap(d, e['small'], fsm, 940)
                for li, ln in enumerate(lines):
                    lw = d.textlength(ln, font=fsm)
                    y = (980 - bs // 2 - 110 - 66 * (len(lines) - 1 - li)) if e['small_above'] else (980 + bs // 2 + 40 + li * 66)
                    d.text(((W - lw) / 2, y + off), ln, font=fsm, fill=e['ink'] + (a,))
            elif part[0] == 'still':                                        # campaign still, slow push, logo + URL
                z = 1.0 + 0.05 * t / part[-1]; im = still.resize((round(W * z), round(H * z)), Image.BILINEAR)
                im = im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H)).convert('RGBA')
                a = min(1, t * 5); l2 = lg.copy(); l2.putalpha(l2.getchannel('A').point(lambda x: int(x * a)))
                im.paste(l2, ((W - lg.width) // 2, 275), l2); d = ImageDraw.Draw(im, 'RGBA'); f = B.font(B.FM, 44)
                tw = d.textlength('SickScienceLabs.com', font=f); d.text(((W - tw) / 2, 275 + lg.height + 18), 'SickScienceLabs.com', font=f, fill=url_ink + (int(255 * a),))
                im = im.convert('RGB')
            else:                                                           # the brand film's own logo ending
                im = next(g)
            if k < 3: im = R.whip(im, (1.0, 0.6, 0.25)[k], 1) if pi > 0 or part[0] != 'slam' else Image.blend(im, Image.new('RGB', (W, H), (255, 255, 255)), (0.5, 0.25, 0.1)[k])
            yield im

def render(v):
    head, segs, ecargs, END = VIDEOS[v]; END = sum(e[-1] for e in CUT[v]['end']); tmp = tempfile.mkdtemp(prefix=f'u32_{v}_')
    auds, sfx, tout, plan = [], [], 0.0, []
    for i, (a, b) in enumerate(segs):
        n = round((b - a) * FPS)
        raw = subprocess.run([FF, '-v', 'error', '-ss', str(a), '-t', str(n / FPS), '-i', SRC, '-ac', '2', '-ar', str(SR), '-f', 's16le', '-'],
                             capture_output=True).stdout
        x = np.frombuffer(raw, np.int16).reshape(-1, 2).astype(np.float32); m = round(n / FPS * SR)
        x = np.pad(x, ((0, max(0, m - len(x))), (0, 0)))[:m]
        f_ = int(.012 * SR); rr = np.linspace(0, 1, f_)[:, None]; x[:f_] *= rr; x[-f_:] *= rr[::-1]; auds.append(x)
        plan.append((a, b, n)); tout += n / FPS
    sfx.insert(0, (0.0, 'thump')); nend = round(END * FPS); sfx.append((round(tout, 3), 'whoosh')); sfx.append((round(tout, 3), 'thump')); sfx += [(round(tout + sum(x[-1] for x in CUT[v]['end'][:j]), 3), 'whoosh') for j in range(1, len(CUT[v]['end']))]
    total = sum(p[2] for p in plan) + nend
    auds.append(np.zeros((round(END * SR), 2), np.float32)); aud = np.concatenate(auds)
    json.dump({'duration': total / FPS, 'end': tout, 'sfx': sfx}, open(os.path.join(OUT, f'u32_{v}_cues.json'), 'w'))
    rawp = os.path.join(tmp, 'a.raw'); np.clip(aud, -32768, 32767).astype(np.int16).tofile(rawp); tmp_out = os.path.join(tmp, 'o.mp4')
    enc = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', rawp, '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18',
                            '-c:a', 'aac', '-b:a', '192k', '-shortest', tmp_out], stdin=subprocess.PIPE)
    q = collections.deque()
    def emit(im):
        q.append(im)
        if len(q) > 3: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    T, prev_cam, z = 0.0, None, 1.0
    for i, (a, b, n) in enumerate(plan):
        gs = groups(seg_words(a, b)); fr = frames(a, n / FPS)
        brs = [(round(o * FPS), round((o + du) * FPS), foot(c, c0, du + 0.2)) for (si, o, du, c, c0) in CUT[v]['broll'] if si == i]
        for k in range(n):
            t = k / FPS; im, cam = next(fr)
            br = next((g for k0, k1, g in brs if k0 <= k < k1), None)
            if k == 0 and i > 0: z = (1.14 if z == 1.0 else 1.0) if cam == prev_cam else 1.0   # punch-in only hides same-camera jump cuts
            zz = z * (1 + 0.25 * (1 - R.spring(T + t, 170, 16))) if i == 0 else z               # intro: fast push from 1.25x
            if zz > 1.001 and br is None:
                im = im.resize((round(W * zz), round(H * zz)), Image.BILINEAR)
                oy = int((im.height - H) * 0.3); im = im.crop(((im.width - W) // 2, oy, (im.width - W) // 2 + W, oy + H))
            if br is not None: im = next(br); zz = 1.0                       # cutaway: brand footage under the podcast voice
            if T + t < HOOK + 0.35: im = mid_shade(im); yb = slam_headline(im, head, T + t); credit(im, yb + 10)
            big_caption(im, gs, t)
            if br is not None and k in [k0 for k0, _, _ in brs]: im = R.whip(im, 0.6, 1)
            if i == 0 and k < 3: im = Image.blend(im, Image.new('RGB', (W, H), (255, 255, 255)), (0.55, 0.3, 0.1)[k])
            emit(im); prev_cam = cam
        T += n / FPS
    for j, amt in enumerate((0.25, 0.6, 1.0)[-len(q):]): q[j] = R.whip(q[j], amt, -1)
    for im in end_frames(v, END): emit(im)
    while q: enc.stdin.write(np.asarray(q.popleft().convert('RGB')).tobytes())
    enc.stdin.close(); enc.wait()
    shutil.copy(tmp_out, os.path.join(OUT, f'u32_{v}_voice.mp4')); shutil.rmtree(tmp, ignore_errors=True)
    subprocess.run([FF, '-v', 'error', '-y', '-i', os.path.join(OUT, f'u32_{v}_voice.mp4'), '-vf', 'fps=2,scale=180:-1,tile=8x5',
                    '-frames:v', '1', os.path.join(OUT, f'u32_{v}_contact.jpg')])
    print(v, 'ok', round(total / FPS, 1), 's')

if __name__ == '__main__':
    for v in sys.argv[1:] or list(VIDEOS): render(v)
