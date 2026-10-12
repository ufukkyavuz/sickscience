"""Batch 28 — ShapeShift problem→solution UGC video, flow copied from Spoiled Child "TRY BEFORE YOU BUY".
Kling 3.0 clips with their own voices (clips/*.mp4) + word timings (clips/words.json, mlx-whisper) + PIL overlays + ffmpeg.
usage: python render28.py -> out/u28_shapeshift_flow.mp4 (9:16 1080x1920, 24 fps)"""
import os, json, shutil, subprocess, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__)); SS = os.path.abspath(os.path.join(HERE, '..', '..'))
CL = os.path.join(HERE, 'clips'); OUT = os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
W, H, FPS, SR = 1080, 1920, 24, 48000
FF = shutil.which('ffmpeg')
FD = os.path.expanduser('~/Library/Fonts/')
FB, FM = FD + 'FoundersGrotesk-Bold.otf', FD + 'FoundersGrotesk-Medium.otf'
WORDS = json.load(open(os.path.join(CL, 'words.json')))
FIX = {'shapefith': 'ShapeShift', 'shapefifth': 'ShapeShift', 'shape': 'Shape', 'nx35': 'NX35™', 'nx': 'NX', '15': '15', '%': '%'}

def font(p, s): return ImageFont.truetype(p, s)

_cache = {}
def frames(name, zoom=1.0):
    key = (name, zoom)
    if key not in _cache:
        vf = f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}'
        if zoom != 1.0:  # zoom anchored top-centre (hides props at the bottom of the frame)
            zw, zh = round(W * zoom), round(H * zoom)
            vf += f',scale={zw}:{zh},crop={W}:{H}:{(zw - W) // 2}:0'
        raw = subprocess.run([FF, '-v', 'error', '-i', os.path.join(CL, name + '.mp4'), '-vf', vf, '-r', str(FPS),
                              '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
        _cache[key] = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
    return _cache[key]

def audio(name, a0, a1):
    raw = subprocess.run([FF, '-v', 'error', '-ss', str(a0), '-t', str(a1 - a0), '-i', os.path.join(CL, name + '.mp4'),
                          '-ac', '2', '-ar', str(SR), '-f', 's16le', '-'], capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).reshape(-1, 2).astype(np.float32)
    n = round((a1 - a0) * SR); a = np.pad(a, ((0, max(0, n - len(a))), (0, 0)))[:n]
    f = min(len(a), int(0.02 * SR)); ramp = np.linspace(0, 1, f)[:, None]
    a[:f] *= ramp; a[-f:] *= ramp[::-1]
    return a

def words(name, a0, a1):
    out = []
    for w, s, e in WORDS[name]:
        if s >= a0 - 0.05 and s < a1:
            k = w.strip('.,!?').lower(); txt = FIX.get(k, w.strip('.,!?'))
            if txt in ('%',) and out: out[-1] = (out[-1][0] + '%', out[-1][1], e - a0); continue
            out.append((txt, s - a0, e - a0))
    return out

# ---------- overlay drawing (reference language: top-left white caps + ☑ rows, small boxed captions low-centre)
def top_shade(img):
    g = np.linspace(0.55, 0, 760)[:, None, None]
    a = np.asarray(img).astype(np.float32); a[:760] *= (1 - g)
    return Image.fromarray(a.astype(np.uint8))

def wrap(d, text, f, maxw):
    lines, cur = [], ''
    for word in text.split():
        t = (cur + ' ' + word).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = word
    return lines + [cur]

def headline(img, text, y=300, size=78):
    d = ImageDraw.Draw(img); f = font(FB, size)
    for i, ln in enumerate(wrap(d, text, f, 950)):
        d.text((65, y + i * int(size * 1.02)), ln, font=f, fill='white', stroke_width=2, stroke_fill=(0, 0, 0))
    return y + len(wrap(d, text, f, 950)) * int(size * 1.02)

def checklist(img, items, t, y0):
    d = ImageDraw.Draw(img); f = font(FB, 44)
    for i, (ts, txt) in enumerate(items):
        if t < ts: continue
        y = y0 + 22 + i * 74; x = 65
        d.rectangle((x, y + 4, x + 44, y + 48), outline='white', width=5)
        a = min(1, (t - ts) / 0.15)
        if a > 0.3: d.line([(x + 9, y + 26), (x + 19, y + 37), (x + 37, y + 13)], fill='white', width=6, joint='curve')
        d.text((x + 64, y), txt, font=f, fill='white', stroke_width=2, stroke_fill=(0, 0, 0))

def caption(img, ws, t, y=1120):
    if not ws: return
    chunks, cur = [], []
    for w in ws:
        cur.append(w)
        if len(cur) == 4 or w[0].endswith(('.', ',')): chunks.append(cur); cur = []
    if cur: chunks.append(cur)
    cur = None
    for c in chunks:
        if c[0][1] - 0.05 <= t <= c[-1][2] + 0.25: cur = c
    if not cur: return
    txt = ' '.join(w[0] for w in cur).strip(' ,.')
    d = ImageDraw.Draw(img, 'RGBA'); f = font(FM, 46); tw = d.textlength(txt, font=f)
    x = (W - tw) / 2; d.rounded_rectangle((x - 20, y - 10, x + tw + 20, y + 58), 10, fill=(255, 255, 255, 240))
    d.text((x, y), txt, font=f, fill=(15, 15, 15))

def label(img, txt, y=1060):
    d = ImageDraw.Draw(img, 'RGBA'); f = font(FM, 34); tw = d.textlength(txt, font=f)
    x = (W - tw) / 2; d.rounded_rectangle((x - 16, y - 6, x + tw + 16, y + 44), 22, fill=(0, 0, 0, 150))
    d.text((x, y), txt, font=f, fill='white')

def review_card(img, name, text, y, a):
    if a <= 0: return
    d = ImageDraw.Draw(img, 'RGBA'); x = 65 + int(60 * (1 - a)); w = 600
    lines = wrap(d, text, font(FM, 34), w - 48); h = 120 + len(lines) * 40
    d.rounded_rectangle((x, y, x + w, y + h), 18, fill=(255, 255, 255, int(245 * a)))
    d.text((x + 24, y + 18), name, font=font(FB, 34), fill=(20, 20, 20, int(255 * a)))
    stars(d, x + 24, y + 60, 28, (169, 33, 192, int(255 * a)))
    for i, ln in enumerate(lines): d.text((x + 24, y + 98 + i * 40), ln, font=font(FM, 34), fill=(30, 30, 30, int(255 * a)))

def stars(d, x, y, size, color, n=5):
    import math
    for k in range(n):
        cx, cy = x + size / 2 + k * size * 1.08, y + size / 2
        pts = [(cx + (size / 2 if i % 2 == 0 else size / 4.6) * math.sin(i * math.pi / 5), cy - (size / 2 if i % 2 == 0 else size / 4.6) * math.cos(i * math.pi / 5)) for i in range(10)]
        d.polygon(pts, fill=color)

def ease(x): x = max(0, min(1, x)); return 1 - (1 - x) ** 3

def wstart(ws, key, default=0):
    for w, s, e in ws:
        if w.lower().strip('.,').startswith(key.lower()): return s
    return default

# ---------- segments
SEGS = []
def seg(audio_clip, a0, a1, shots, draw):
    """shots: list of (start_t_in_segment, clip, clip_start, zoom)"""
    SEGS.append(dict(ac=audio_clip, a0=a0, a1=a1, shots=shots, draw=draw))

def build():
    # 1 hook — A at the mirror
    w = WORDS['c11_A_hook']; a0 = max(0, w[0][1] - 0.35); a1 = w[-1][2] + 0.3
    seg('c11_A_hook', a0, a1, [(0, 'c11_A_hook', a0, 1.0)],
        lambda im, t, ws: _hook(im, t, ws))
    # 2 B — give it a try
    w = WORDS['c12_B_try']; a0 = max(0, w[0][1] - 0.1); a1 = w[-1][2] + 0.25
    seg('c12_B_try', a0, a1, [(0, 'c12_B_try', a0, 1.0)], lambda im, t, ws: _cap(im, t, ws))
    # 3 product + ingredients — macro cutaway, then C talking
    n = 'c15b_C_ingredients' if 'c15b_C_ingredients' in WORDS else 'c15_C_ingredients'
    w = WORDS[n]; a0 = max(0, w[0][1] - 0.1); a1 = w[-1][2] + 0.3
    ws = words(n, a0, a1); t_with = wstart(ws, 'with', 2.6)
    seg(n, a0, a1, [(0, 'c20_macro', 0.3, 1.0), (t_with, n, a0 + t_with, 1.0)], _ingr(ws, t_with))
    # 4 problem — D talking, cut to pinch + profile check during the checklist
    w = WORDS['c16_D_problem']; a0 = max(0, w[0][1] - 0.1); a1 = w[-1][2] + 0.3
    ws = words('c16_D_problem', a0, a1)
    td, ts = wstart(ws, 'deliver', 2.2), wstart(ws, 'still', 4.0)
    seg('c16_D_problem', a0, a1, [(0, 'c16_D_problem', a0, 1.0), (td, 'c19_A_pinch', 0.2, 1.0), (ts, 'c14_profilecheck', 0.5, 1.0)], _prob(ws))
    # 5 testimony — B, attributed to the real review
    # Kling mispronounces the product name, so 'ShapeShift' is replaced by 'it' spliced from the same woman's c12 take
    n = 'c13b_B_testimony'; w = WORDS[n]; a0 = max(0, w[0][1] - 0.1); a1 = w[-1][2] + 0.3
    bad = [x for x in w if x[0].lower().startswith('shape')][0]
    it = [x for x in WORDS['c12_B_try'] if x[0].lower().strip('.,') == 'it'][0]
    seg(n, a0, bad[1], [(0, n, a0, 1.0)], lambda im, t, ws: _testi(im, t, ws))
    seg('c12_B_try', it[1] - 0.02, it[2] + 0.06, [(0, n, bad[1], 1.0)], lambda im, t, ws: _testi(im, t, ws))
    seg(n, bad[2], a1, [(0, n, bad[2], 1.0)], lambda im, t, ws: _testi(im, t, ws))
    # 6 offer + reviews — A with bottle, cut to A smiling under review cards before she pushes the bottle to the lens
    w = WORDS['c17_A_offer']; a0 = max(0, w[0][1] - 0.1); a1 = w[-1][2] + 0.3
    ws = words('c17_A_offer', a0, a1); tj = wstart(ws, 'and', 2.0)
    seg('c17_A_offer', a0, a1, [(0, 'c17_A_offer', a0, 1.0), (tj, 'c11_A_hook', 1.2, 1.0)], _offer(ws, tj))
    # 7 usage + timeline — C with the steel gua sha (zoomed to hide the props on the vanity)
    w = WORDS['c18_C_howto']; a0 = max(0, w[0][1] - 0.6); a1 = w[-1][2] + 0.3
    ws = words('c18_C_howto', a0, a1); tc = wstart(ws, 'chisel', 3.5)
    seg('c18_C_howto', a0, a1, [(0, 'c18_C_howto', a0, 1.42)], _howto(tc))

def _cap(im, t, ws): caption(im, ws, t); return im
def _hook(im, t, ws):
    im = top_shade(im); headline(im, "WHY EVERYONE'S OBSESSED WITH THIS"); caption(im, ws, t); return im
def _ingr(ws, t_with):
    def f(im, t, w_):
        im = top_shade(im)
        if t < t_with: headline(im, 'SHAPESHIFT HELPS VISIBLY TIGHTEN & FIRM THE NECK')
        else:
            y = headline(im, 'WITH')
            checklist(im, [(wstart(ws, 'nx', t_with), 'NX35™ SCULPT TECHNOLOGY'), (wstart(ws, 'caffeine', t_with + 1), 'CAFFEINE'),
                           (wstart(ws, 'niacinamide', t_with + 2), 'NIACINAMIDE (VITAMIN B3)')], t, y)
        caption(im, w_, t); return im
    return f
def _prob(ws):
    def f(im, t, w_):
        im = top_shade(im); y = headline(im, 'MOST NECK CREAMS…')
        checklist(im, [(wstart(ws, 'only', 0.3), 'ONLY WORK ON THE SURFACE'), (wstart(ws, 'deliver', 2), 'DELIVER TEMPORARY RESULTS'),
                       (wstart(ws, 'leave', 4), 'LEAVE YOU DEPENDENT ON PROCEDURES')], t, y)
        caption(im, w_, t); return im
    return f
def _testi(im, t, ws):
    label(im, 'Venus B., verified review'); caption(im, ws, t); return im
def _offer(ws, tj):
    def f(im, t, w_):
        im = top_shade(im)
        if t < tj: headline(im, 'SUBSCRIBE & SAVE 15%')
        else:
            d = ImageDraw.Draw(im); f = font(FB, 78)
            d.text((65, 300), '4.7', font=f, fill='white', stroke_width=2, stroke_fill=(0, 0, 0))
            stars(d, 65 + d.textlength('4.7 ', font=f), 306, 62, (255, 255, 255))
            d.text((65, 380), 'FROM 576 REVIEWS', font=f, fill='white', stroke_width=2, stroke_fill=(0, 0, 0))
            review_card(im, 'Carol F.', 'I can see a difference in my jawline in two weeks. Impressed with this product.', 520, ease((t - tj) / 0.35))
            review_card(im, 'Katie W.', 'I was considering cosmetic surgery for my neck. This product changed my mind!', 780, ease((t - tj - 0.7) / 0.35))
        caption(im, w_, t); return im
    return f
def _howto(tc):
    def f(im, t, w_):
        im = top_shade(im)
        headline(im, '1–2 PUMPS · TWICE DAILY' if t < tc else 'CHISEL YOUR JAWLINE IN 2 WEEKS')
        caption(im, w_, t); return im
    return f

# ---------- end card (lilac, real PNG, official logo)
def endcard():
    bg = Image.new('RGB', (W, H), (232, 222, 245)); y, x = np.mgrid[0:H, 0:W]
    r = np.sqrt((x - W / 2) ** 2 + ((y - 900) * 0.8) ** 2); g = np.clip(1 - r / 900, 0, 1) ** 2
    a = np.asarray(bg).astype(float) + g[..., None] * np.array([18, 22, 10]); bg = Image.fromarray(a.clip(0, 255).astype(np.uint8))
    p = Image.open(os.path.join(SS, 'Products/png/ERH_7470B.png')).convert('RGBA'); p = p.crop(p.split()[-1].getbbox())
    nh = 560; p = p.resize((round(p.width * nh / p.height), nh), Image.LANCZOS)
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).ellipse((W / 2 - 110, 1200 - 14, W / 2 + 110, 1200 + 16), fill=120)
    bg = Image.composite(Image.new('RGB', (W, H), (150, 130, 175)), bg, sh.filter(ImageFilter.GaussianBlur(12)))
    bg.paste(p, (W // 2 - p.width // 2, 1200 - nh), p)
    lg = Image.open(os.path.join(SS, 'output/video-01-bcrf/assets/logo.png')).convert('RGBA').resize((398, 54), Image.LANCZOS)
    bg.paste(lg, (W // 2 - 199, 300), lg); d = ImageDraw.Draw(bg)
    for txt, yy, col in (('SUBSCRIBE &', 390, (20, 20, 20)), ('SAVE 15%', 490, (115, 0, 199))):
        f = font(FB, 104); tw = d.textlength(txt, font=f); d.text(((W - tw) / 2, yy), txt, font=f, fill=col)
    f = font(FM, 40); txt = 'ShapeShift V-Line Jaw Defining Serum'; tw = d.textlength(txt, font=f); d.text(((W - tw) / 2, 1236), txt, font=f, fill=(40, 40, 40))
    return bg

def main():
    build()
    auds, vids = [], []
    for s in SEGS:
        dur = s['a1'] - s['a0']; n = round(dur * FPS); auds.append(audio(s['ac'], s['a0'], s['a1']))
        ws = words(s['ac'], s['a0'], s['a1'])
        for k in range(n):
            t = k / FPS; shot = [x for x in s['shots'] if x[0] <= t][-1]
            fr = frames(shot[1], shot[3]); idx = min(len(fr) - 1, round((shot[2] + (t - shot[0])) * FPS))
            vids.append(s['draw'](Image.fromarray(fr[idx]).copy(), t, ws))
    END = 2.6; ec = endcard()
    for k in range(round(END * FPS)):
        sc = 1 + 0.03 * ease(k / (END * FPS)); im = ec.resize((round(W * sc), round(H * sc)), Image.LANCZOS)
        vids.append(im.crop(((im.width - W) // 2, (im.height - H) // 2, (im.width - W) // 2 + W, (im.height - H) // 2 + H)))
    auds.append(np.zeros((round(END * SR), 2), np.float32))
    a = np.concatenate(auds); a = np.clip(a, -32768, 32767).astype(np.int16); a.tofile(os.path.join(OUT, '_a.raw'))
    p = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-f', 's16le', '-ar', str(SR), '-ac', '2', '-i', os.path.join(OUT, '_a.raw'),
                          '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-c:a', 'aac', '-b:a', '192k',
                          os.path.join(OUT, 'u28_shapeshift_flow.mp4')], stdin=subprocess.PIPE)
    for im in vids: p.stdin.write(np.asarray(im.convert('RGB')).tobytes())
    p.stdin.close(); p.wait(); os.remove(os.path.join(OUT, '_a.raw'))
    print('ok', len(vids) / FPS, 's')

if __name__ == '__main__':
    main()
