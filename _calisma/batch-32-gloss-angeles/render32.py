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
CUT = {   # b-roll: (segment, offset s, dur s, clip | 'BA:<site image>', clip start)
    'g1': dict(broll=[(0, 1.9, 1.6, 'BA:ss_ba_profile_hi.jpg', 0), (1, 0.1, 1.8, 'product2', 9.8),
                      (1, 3.2, 1.3, 'BA:ss_ba_neck.jpg', 0), (1, 4.5, 1.3, 'BA:ss_ba_jaw.jpg', 0)],
               end=[('clip', 'product2', FD['product2'] - 2.6, 2.6)]),
    'g2': dict(broll=[(0, 1.6, 1.4, 'short7', 0.0), (0, 7.3, 1.8, 'BA:ss_ba_man.jpg', 0), (1, 0.2, 2.4, 'BA:ss_ba_2weeks.jpg', 0)],
               end=[('slam', 1.2), ('clip', 'short7', FD['short7'] - 2.6, 2.4)]),
    'g3': dict(broll=[(0, 0.9, 2.0, 'product2', 9.8)], end=[('slam', 1.3), ('still', 1.5)]),
    'g4': dict(broll=[(0, 4.6, 2.2, 'short10', 0.3), (1, 1.6, 1.8, 'product1', 9.2)],
               end=[('clip', 'short8', FD['short8'] - 2.7, 2.7)]),
}
# same full-bleed layout + centred captions everywhere; only the hook style changes per video
LAY = {
    'g1': dict(mode='full', cap='group', hook='block', hook_t=1.8),
    'g2': dict(mode='full', cap='group', hook='stack', hook_t=1.55),
    'g3': dict(mode='full', cap='group', hook='sticker', hook_t=2.6),
    'g4': dict(mode='full', cap='group', hook='slam', hook_t=2.6),
}
BA = {}
SITE_BA = os.path.join(HERE, 'src', 'site-ba')          # ShapeShift PDP before/afters (sicksciencelabs.com), labels included
HOOK = 2.6                                                     # hook headline shows, then leaves (per video: LAY hook_t)
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

def frames_wide(a, dur):
    """1080x960 podcast window for the split layout: 1215-wide crop around the speaker's face, scaled."""
    p = subprocess.Popen([FF, '-v', 'error', '-ss', f'{a:.3f}', '-t', f'{dur:.3f}', '-i', SRC, '-r', str(FPS),
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
    last, N = None, 1920 * 1080 * 3
    while True:
        b = p.stdout.read(N)
        if len(b) < N: break
        x = np.frombuffer(b, np.uint8).reshape(1080, 1920, 3); m = x[100:400:4, 1550:1900:4].mean((0, 1))
        x0 = 672 if (m[1] - m[0]) > -30 else 193
        last = (Image.fromarray(x[:, x0:x0 + 1215]).resize((W, 960), Image.LANCZOS), x0); yield last
    p.wait()
    while True: yield last

BA_AX = {'BA1': 0.08, 'BA2': 0.5}                    # horizontal crop anchor: BA1 jaws sit at the panel's left edge
def ba_frame(key, t, w, h, labels_y):
    """Before/after filling w x h. Wide panels (BA1) stack vertically on a full screen, otherwise side by side;
    the AFTER half slides in."""
    f_, bb, ab = BA[key]; src = Image.open(os.path.join(HERE, 'src', f_)).convert('RGB')
    vert = key == 'BA1' and h > 1000; out = Image.new('RGB', (w, h), (255, 255, 255))
    pw, ph = (w, h // 2) if vert else (w // 2, h); ax = BA_AX[key]
    for i, box in enumerate((bb, ab)):
        if i == 1 and t < 0.12: continue
        pnl = src.crop(box); sc = max(pw / pnl.width, ph / pnl.height)
        pnl = pnl.resize((round(pnl.width * sc), round(pnl.height * sc)), Image.LANCZOS)
        x0 = round((pnl.width - pw) * ax); pnl = pnl.crop((x0, (pnl.height - ph) // 2, x0 + pw, (pnl.height - ph) // 2 + ph))
        sp = 1 - R.spring(t - 0.12, 260, 22) if i == 1 else 0
        x, y = (0, ph + round(sp * ph)) if (vert and i) else ((pw + round(sp * pw), 0) if i else (0, 0))
        out.paste(pnl, (x, y))
        d = ImageDraw.Draw(out); fl = B.font(B.FB, 60); lab = 'BEFORE' if i == 0 else 'AFTER'
        ly = (labels_y if i == 0 else ph + 40 + round(sp * ph)) if vert else labels_y
        d.text((x + (pw - d.textlength(lab, font=fl)) / 2 if not vert else 65, ly), lab, font=fl, fill=(255, 255, 255), stroke_width=4, stroke_fill=(0, 0, 0))
    d = ImageDraw.Draw(out)
    if vert: d.rectangle((0, ph - 3, w, ph + 3), fill=(255, 255, 255))
    else: d.rectangle((pw - 3, 0, pw + 3, h), fill=(255, 255, 255))
    fc = B.font(B.FM, 32); txt = 'Gloss Angeles listeners'
    d.text(((w - d.textlength(txt, font=fc)) / 2, h - (130 if h > 1000 else 60)), txt, font=fc, fill=(255, 255, 255), stroke_width=2, stroke_fill=(0, 0, 0))
    return out

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

def slam_headline(img, text, t, y=HY, size=88, hook_t=HOOK):
    if t > hook_t + 0.35: return y
    out = max(0.0, (t - hook_t) / 0.35)                    # exit: slide up + fade
    if out > 0:
        lay = Image.new('RGBA', img.size, (0, 0, 0, 0)); slam_headline(lay, text, hook_t - 0.001, y, size, hook_t)
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

def shade(im, y0, y1, amt=0.45):
    g = np.interp(np.arange(im.height), [y0 - 120, y0, y1, y1 + 120], [0, amt, amt, 0])[:, None, None]
    a = np.asarray(im).astype(np.float32); a *= (1 - g); return Image.fromarray(a.astype(np.uint8))

def word_caption(img, ws, t, y=1010):
    """one huge word at a time, white with a brand-purple outline, pops in"""
    act = None
    for j, w in enumerate(ws):
        nxt = ws[j + 1][1] if j + 1 < len(ws) else w[2] + 0.3
        if w[1] - 0.02 <= t < min(nxt, w[2] + 0.35): act = w
    if not act: return
    wd = act[0].upper(); size = 150; f = B.font(B.FB, size); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    while d0.textlength(wd, font=f) > 960: size -= 8; f = B.font(B.FB, size)
    lay = Image.new('RGBA', (W, size + 60), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.text(((W - d.textlength(wd, font=f)) / 2, 20), wd, font=f, fill=(255, 255, 255, 255), stroke_width=9, stroke_fill=PURPLE + (255,))
    sc = 0.7 + 0.3 * R.spring(t - act[1] + 0.02, 450, 18)
    lay = lay.resize((round(W * sc), round(lay.height * sc)), Image.BILINEAR)
    img.paste(lay, ((W - lay.width) // 2, round(y + (size + 60) * (1 - sc) / 2)), lay)

def groups_n(ws, n):
    out, cur = [], []
    for w in ws:
        if cur and (len(cur) == n or w[1] - cur[-1][2] > 0.35): out.append(cur); cur = []
        cur.append(w)
        if w[3]: out.append(cur); cur = []
    if cur: out.append(cur)
    return out

LILAC = (214, 160, 255)
def left_caption(img, ws, t):
    """left-aligned two-line lower third; spoken words turn lilac, the group rises in"""
    gs = groups_n(ws, 5); g = next((g for g in gs if g[0][1] - 0.05 <= t < g[-1][2] + 0.3), None)
    if not g: return
    f = B.font(B.FB, 74); d = ImageDraw.Draw(img); lines, cur = [], []
    for w in g:
        if cur and d.textlength(' '.join(x[0].upper() for x in cur + [w]), font=f) > 900: lines.append(cur); cur = []
        cur.append(w)
    lines.append(cur); off = (1 - R.spring(t - g[0][1] + 0.05, 380, 22)) * 50
    y = 1180 - 82 * len(lines)
    for ln in lines:
        x = 65
        for w in ln:
            wd = w[0].upper(); col = LILAC if w[1] - 0.02 <= t else (255, 255, 255)
            d.text((x, y + off), wd, font=f, fill=col, stroke_width=4, stroke_fill=(0, 0, 0)); x += d.textlength(wd + ' ', font=f)
        y += 82

def bar_caption(img, ws, t):
    """brand-purple lower-third bar with a show label; active word on a white chip"""
    d = ImageDraw.Draw(img, 'RGBA'); d.rectangle((0, 1030, W, 1215), fill=PURPLE + (238,))
    fl = B.font(B.FM, 32); d.text((65, 1046), 'GLOSS ANGELES PODCAST', font=fl, fill=(255, 255, 255, 220))
    gs = groups_n(ws, 4); g = next((g for g in gs if g[0][1] - 0.05 <= t < g[-1][2] + 0.3), None)
    if not g: return
    f = B.font(B.FB, 66); x = 65; y = 1100
    act = max([j for j, w in enumerate(g) if w[1] - 0.03 <= t] or [0])
    for j, w in enumerate(g):
        wd = w[0].upper(); wl = d.textlength(wd, font=f)
        if x + wl > W - 40: break
        if j == act: d.rounded_rectangle((x - 10, y - 4, x + wl + 10, y + 74), radius=10, fill=(255, 255, 255, 255))
        d.text((x, y), wd, font=f, fill=(24, 18, 22) if j == act else (255, 255, 255)); x += wl + d.textlength(' ', font=f)

def block_headline(img, text, t, y=HY, size=84, hook_t=HOOK):
    """hook on brand-purple highlighter blocks, lines wipe in from the left, then leave"""
    if t > hook_t + 0.35: return y
    d = ImageDraw.Draw(img, 'RGBA'); f = B.font(B.FB, size); lines = R.wrap(d, text, f, 900); out = max(0.0, (t - hook_t) / 0.35)
    for li, ln in enumerate(lines):
        tt = t - li * 0.12; sp = R.spring(tt, 300, 22) if tt > 0 else 0
        lw = d.textlength(ln, font=f); yy = y + li * int(size * 1.22) - int(120 * out ** 2); a = int(255 * (1 - out))
        x1 = 65 - 18 + (lw + 36) * sp
        if sp > 0: d.rectangle((47, yy - 6, x1, yy + size + 14), fill=PURPLE + (a,))
        if sp > 0.6: d.text((65, yy), ln, font=f, fill=(255, 255, 255, a))
    return y + len(lines) * int(size * 1.22)

def ba_card(bg, key, t):
    """site before/after shown whole on a rounded card over the dimmed podcast; pops in"""
    src = Image.open(os.path.join(SITE_BA, key[3:])).convert('RGB'); cw = 1000; ch = round(src.height * cw / src.width)
    if ch > 1500: ch = 1500; cw = round(src.width * ch / src.height)
    card = src.resize((cw, ch), Image.LANCZOS); m = Image.new('L', card.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, cw, ch), 28, fill=255)
    im = Image.eval(bg, lambda v: int(v * 0.35)); sc = 0.86 + 0.14 * R.spring(t, 280, 18)
    c2 = card.resize((round(cw * sc), round(ch * sc)), Image.BILINEAR); m2 = m.resize(c2.size, Image.BILINEAR)
    y = 300 + (ch - c2.height) // 2 + round((1 - R.spring(t, 280, 18)) * 60)
    im.paste(c2, ((W - c2.width) // 2, y), m2); return im

def stack_headline(img, text, t, y=620, hook_t=HOOK):
    """hook as huge stacked words, centred, alternating white / brand purple, each pops in"""
    if t > hook_t + 0.35: return y
    out = max(0.0, (t - hook_t) / 0.35); d = ImageDraw.Draw(img, 'RGBA')
    words = [x.strip() for x in text.replace(':', ':|').split('|')] if ':' in text else R.wrap(d, text, B.font(B.FB, 150), 960)
    yy = y
    for i, wd in enumerate(words):
        f, size = fit_font(wd, 960, 150); tt = t - i * 0.14
        if tt > 0:
            sc = 0.6 + 0.4 * R.spring(tt, 380, 16); a = int(255 * min(1, tt * 8) * (1 - out))
            lay = Image.new('RGBA', (W, size + 40), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
            dl.text(((W - dl.textlength(wd, font=f)) / 2, 10), wd, font=f, fill=((255, 255, 255) if i % 2 == 0 else LILAC) + (a,),
                    stroke_width=5, stroke_fill=(0, 0, 0, a))
            lay = lay.resize((round(W * sc), round(lay.height * sc)), Image.BILINEAR)
            img.paste(lay, ((W - lay.width) // 2, yy + round((size + 40) * (1 - sc) / 2) - int(160 * out ** 2)), lay)
        yy += int(size * 0.98)
    return yy

def sticker_headline(img, text, t, y=700, hook_t=HOOK):
    """hook typed onto a tilted white sticker that pops in and flies off"""
    if t > hook_t + 0.35: return y
    out = max(0.0, (t - hook_t) / 0.35); f = B.font(B.FB, 82); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    lines = R.wrap(d0, text, f, 860); n = sum(len(l) for l in lines); shown = int(n * min(1, max(0, t - 0.15) / 0.7))
    bw = max(d0.textlength(l, font=f) for l in lines) + 80; bh = len(lines) * 96 + 60
    st = Image.new('RGBA', (int(bw), bh), (0, 0, 0, 0)); ds = ImageDraw.Draw(st); ds.rounded_rectangle((0, 0, bw, bh), 26, fill=(255, 255, 255, 255))
    k = 0
    for li, ln in enumerate(lines):
        part = ln[:max(0, shown - k)]; k += len(ln); ds.text((40, 30 + li * 96), part, font=f, fill=(24, 18, 22, 255))
    sc = 0.5 + 0.5 * R.spring(t, 300, 14); st = st.resize((max(1, round(st.width * sc)), max(1, round(st.height * sc))), Image.BILINEAR)
    st = st.rotate(-3 - 25 * out, expand=True, resample=Image.BICUBIC)
    if out: st.putalpha(st.getchannel('A').point(lambda v: int(v * (1 - out))))
    img.paste(st, ((W - st.width) // 2 + int(500 * out ** 2), y + (bh - st.height) // 2), st)
    return y + bh

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
    L = LAY[v]; HT = L['hook_t']; split = L['mode'] == 'split'
    bot = foot(L['bottom'][0], L['bottom'][1], tout + 0.5) if split else None
    def place(src, t_rel, key, w, h, labels_y):
        if key in BA: return ba_frame(key, t_rel, w, h, labels_y)
        im = next(src); return im if (w, h) == (W, H) else im.crop((0, (H - h) // 2, W, (H - h) // 2 + h))
    T, prev_cam, z = 0.0, None, 1.0
    for i, (a, b, n) in enumerate(plan):
        ws = seg_words(a, b); gs = groups(ws); fr = frames_wide(a, n / FPS) if split else frames(a, n / FPS)
        brs = [(round(o * FPS), round((o + du) * FPS), c, (None if c.startswith('BA:') else foot(c, c0, du + 0.2))) for (si, o, du, c, c0) in CUT[v]['broll'] if si == i]
        for k in range(n):
            t = k / FPS; Tt = T + t; pod, cam = next(fr); bk = bot and next(bot)
            br = next(((k0, c, g) for k0, k1, c, g in brs if k0 <= k < k1), None)
            if k == 0 and i > 0: z = (1.14 if z == 1.0 else 1.0) if cam == prev_cam else 1.0   # punch-in only on same-camera cuts
            zz = z * (1 + 0.25 * (1 - R.spring(Tt, 170, 16))) if i == 0 else z                 # intro: fast push from 1.25x
            if zz > 1.001:
                pw, ph = pod.size; pod = pod.resize((round(pw * zz), round(ph * zz)), Image.BILINEAR)
                oy = int((pod.height - ph) * 0.3); pod = pod.crop(((pod.width - pw) // 2, oy, (pod.width - pw) // 2 + pw, oy + ph))
            if split:                                                          # podcast on top, brand footage / B/A below
                im = Image.new('RGB', (W, H)); im.paste(pod, (0, 0))
                lower = place(br[2], (k - br[0]) / FPS, br[1], W, 960, 40) if br else bk.crop((0, 480, W, 1440))
                im.paste(lower, (0, 960))
                if Tt < HT + 0.35: im = shade(im, 990, 1250); yb = slam_headline(im, head, Tt, y=1000, size=84, hook_t=HT); credit(im, yb + 10)
                big_caption(im, gs, t, y=880)
            else:
                card = br is not None and br[1].startswith('BA:')
                im = ba_card(pod, br[1], (k - br[0]) / FPS) if card else (next(br[2]) if br else pod)
                if Tt < HT + 0.35 and not card:
                    im = mid_shade(im)
                    yb = {'block': lambda: block_headline(im, head, Tt, hook_t=HT), 'stack': lambda: stack_headline(im, head, Tt, hook_t=HT),
                          'sticker': lambda: sticker_headline(im, head, Tt, hook_t=HT), 'slam': lambda: slam_headline(im, head, Tt, hook_t=HT)}[L['hook']]()
                    credit(im, yb + 10)
                if not card: big_caption(im, gs, t)
            if br is not None and k == br[0] and not br[1].startswith('BA:'): im = R.whip(im, 0.6, 1)
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
