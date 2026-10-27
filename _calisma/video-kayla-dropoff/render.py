"""DropOff × Kayla Greaves UGC — 5 cut-downs (≤20 s) from the creator's 41 s edit (user 2026-10-21: "5 varyant, kurallara dikkat").
Rules: cuts only at sentence ends (word gaps), big 1-3 word captions with the active word on a purple block (bbox-centred),
hook 2-3 s then gone, brand SITE before/after shown whole on a pop-in card, PDP stats verbatim, plain logo + URL end card,
no dark plates. Source audio kept; pop bed ducked under it."""
import json, os, sys, subprocess, math, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = f'{ROOT}/src/kayla.mp4'; A = f'{ROOT}/assets'
OUT = f'{ROOT}/out'; os.makedirs(OUT, exist_ok=True)
FB = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Bold.otf')
FM = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Medium.otf')
W, H, FPS, SR = 1080, 1920, 30, 48000
PURPLE = (169, 33, 192); COBALT = (35, 64, 201); INK = (26, 26, 31)

# ---------- words with caption fixes ----------
RAW = [w for s in json.load(open(f'{ROOT}/src/transcript.json'))['segments'] for w in s['words']]
def build_tokens():
    ws = [(w['start'], w['end'], w['word'].strip()) for w in RAW]; out = []; i = 0
    while i < len(ws):
        s, e, t = ws[i]; nxt = lambda k: ws[i + k][2] if i + k < len(ws) else ''
        low = t.lower()
        if low == 'six' and nxt(1).lower().startswith('signs'):
            if nxt(2).lower() == 'labs':
                out.append((s, ws[i + 3][1], 'SickScienceLabs.com.')); i += 4; continue
            out.append((s, ws[i + 1][1], "SickScience's")); i += 2; continue
        if low == 'drop' and nxt(1).lower().startswith('off'):
            out.append((s, ws[i + 1][1], 'DropOff' + nxt(1)[3:])); i += 2; continue
        if low == 'plant' and nxt(1).startswith('-'):
            out.append((s, ws[i + 1][1], 'plant-derived')); i += 2; continue
        if low == 'gel' and nxt(1).lower() == 'light':
            out.append((s, ws[i + 1][1], 'gel-like')); i += 2; continue
        if low == 'to' and nxt(1).lower() == 'snatch': out.append((s, e, 'the')); i += 1; continue
        if low == 'snatch': out.append((s, e, 'snatched')); i += 1; continue
        out.append((s, e, t)); i += 1
    return out
TOK = build_tokens()

# ---------- variants: segments in source time; ('hold', src_start, dur) = muted b-roll under the B/A card ----------
CTA = (36.86, 41.25)
V = {
 'v1': dict(name='Exercise alone isnt enough', hook=(['EXERCISE', 'ALONE ISN\'T', 'ENOUGH'], 'blocks'),
            segs=[(8.28, 13.22), (15.76, 20.98), (34.00, 36.40), ('hold', 4.0, 1.3), CTA], ba='dropoff_07', ba_at=2,
            stat=('88%', 'Experienced reduced\ncellulite & dimpling', 1, 1.2)),
 'v2': dict(name='Snatched jawline now the body', hook=(['FIRST THE JAWLINE.', 'NOW THE BODY.'], 'sticker'),
            segs=[(0.0, 8.28), (34.00, 36.40), ('hold', 5.0, 1.3), CTA], ba='dropoff_06', ba_at=1,
            stat=('92%', 'Experienced reduction in\ncircumference of thighs & belly', 0, 4.6)),
 'v3': dict(name='Post-shower body step', hook=(['MY POST-SHOWER', 'BODY STEP'], 'slam'),
            segs=[(21.02, 26.95), (27.12, 33.96), CTA], ba=None, ba_at=None,
            stat=('87%', 'Feels smoother and\nskin texture improved', 1, 2.6)),
 'v4': dict(name='Exosomes for your body', hook=(['EXOSOMES', 'FOR YOUR BODY?'], 'blocks'),
            segs=[(1.44, 8.28), (15.76, 20.98), (34.00, 36.40), ('hold', 4.0, 1.0), CTA], ba='dropoff_07', ba_at=2,
            stat=('88%', 'Experienced reduced\ncellulite & dimpling', 1, 2.4)),
 'v5': dict(name='Smoother body skin in 56 days', hook=(['SMOOTHER BODY SKIN', 'IN 56 DAYS'], 'slam'),
            segs=[(34.00, 36.40), ('hold', 5.0, 1.4), (8.28, 13.22), (27.12, 31.78), CTA], ba='dropoff_06', ba_at=0, ba_from_start=True,
            stat=('87%', 'Feels smoother and\nskin texture improved', 3, 1.0)),
}

_fc = {}
def font(p, s):
    if (p, s) not in _fc: _fc[(p, s)] = ImageFont.truetype(p, s)
    return _fc[(p, s)]
def stroke_text(d, xy, t, f, fill=(255, 255, 255), sw=6): d.text(xy, t, font=f, fill=fill, stroke_width=sw, stroke_fill=(0, 0, 0))

def hook_layer(lines, style, n):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im); left = n
    if style == 'sticker':
        f = font(FB, 92); lh = 106; vis = []
        for ln in lines:
            ws = ln.split(); vis.append(' '.join(ws[:max(0, left)])); left -= len(ws)
        bb = [d.textbbox((0, 0), l, font=f) for l in lines]; top0 = bb[0][1]; bot = (len(lines) - 1) * lh + bb[-1][3]
        wmax = max(d.textlength(l, font=f) for l in lines) + 80; hh = (bot - top0) + 64
        card = Image.new('RGBA', (int(wmax), int(hh)), (0, 0, 0, 0)); cd = ImageDraw.Draw(card)
        cd.rounded_rectangle([0, 0, wmax - 1, hh - 1], radius=36, fill=(255, 255, 255, 250))
        for i, l in enumerate(vis):
            tw = cd.textlength(l, font=f); cd.text(((wmax - tw) / 2, 32 - top0 + i * lh), l, font=f, fill=INK if i < len(lines) - 1 else COBALT)
        card = card.rotate(-4, expand=True, resample=Image.BICUBIC); im.alpha_composite(card, (int((W - card.width) / 2), 300)); return im
    size = 120 if style == 'blocks' else 132
    while max(d.textlength(l, font=font(FB, size)) for l in lines) > (900 if style == 'blocks' else 960): size -= 4
    f = font(FB, size); lh = int(size * 1.12); y = 300
    for li, ln in enumerate(lines):
        ws = ln.split(); txt = ' '.join(ws[:max(0, left)]); left -= len(ws)
        x = (W - d.textlength(ln, font=f)) / 2
        if txt:
            if style == 'blocks':
                l, t_, r, b_ = d.textbbox((x, y), txt, font=f); px, py = 26, 20
                last = li == len(lines) - 1
                d.rounded_rectangle([l - px, t_ - py, r + px, b_ + py], radius=22, fill=(COBALT if last else (255, 255, 255)) + (255,))
                d.text((x, y), txt, font=f, fill=(255, 255, 255) if last else INK)
            else:
                stroke_text(d, (x, y), txt, f, fill=(255, 255, 255) if li != len(lines) - 1 else (150, 175, 255), sw=8)
        y += lh + (24 if style == 'blocks' else 0)
    return im

_cc = {}
def caption_img(group, active):
    k = (tuple(t for _, _, t in group), active)
    if k in _cc: return _cc[k]
    f = font(FB, 86); words = [t.upper().rstrip(',') if not t.lower().endswith('.com.') else t.upper()[:-1] for _, _, t in group]
    words = [w.rstrip('.') if not w.endswith('.COM') else w for w in words]
    d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1))); sp = 22
    ws = [d0.textlength(w, font=f) for w in words]; tw = sum(ws) + sp * (len(ws) - 1)
    im = Image.new('RGBA', (int(tw) + 80, 150), (0, 0, 0, 0)); d = ImageDraw.Draw(im); x = 40
    for j, (w, wl) in enumerate(zip(words, ws)):
        if j == active:
            l, t_, r, b_ = d.textbbox((x, 30), w, font=f); px, py = 16, 14
            d.rounded_rectangle([l - px, t_ - py, r + px, b_ + py], radius=18, fill=PURPLE + (255,)); d.text((x, 30), w, font=f, fill=(255, 255, 255))
        else: stroke_text(d, (x, 30), w, f, sw=6)
        x += wl + sp
    if im.width > 980: im = im.resize((980, int(im.height * 980 / im.width)), Image.LANCZOS)
    _cc[k] = im; return im

def groups_of(toks):
    gs, cur = [], []
    for j, tk in enumerate(toks):
        cur.append(tk)
        nxt = toks[j + 1] if j + 1 < len(toks) else None
        if len(cur) == 3 or tk[2][-1:] in ',.?!' or (nxt and nxt[0] - tk[1] > 0.25): gs.append(cur); cur = []
    if cur: gs.append(cur)
    return gs

def ba_card(key):
    im = Image.open(f'{A}/{key}.jpg').convert('RGB'); tw = 820; im = im.resize((tw, int(im.height * tw / im.width)), Image.LANCZOS)
    b = 12; card = Image.new('RGBA', (im.width + 2 * b, im.height + 2 * b), (0, 0, 0, 0))
    m = Image.new('L', card.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, card.width - 1, card.height - 1], radius=34, fill=255)
    wh = Image.new('RGBA', card.size, (255, 255, 255, 255)); wh.putalpha(m); card.alpha_composite(wh)
    m2 = Image.new('L', im.size, 0); ImageDraw.Draw(m2).rounded_rectangle([0, 0, im.width - 1, im.height - 1], radius=24, fill=255)
    ir = im.convert('RGBA'); ir.putalpha(m2); card.alpha_composite(ir, (b, b))
    sh = Image.new('RGBA', (card.width + 120, card.height + 120), (0, 0, 0, 0)); sm = Image.new('L', sh.size, 0)
    ImageDraw.Draw(sm).rounded_rectangle([60, 80, 60 + card.width, 80 + card.height], radius=34, fill=110); sh.putalpha(sm.filter(ImageFilter.GaussianBlur(28)))
    sh.alpha_composite(card, (60, 60)); return sh

def stat_card(num, label):
    f1, f2 = font(FB, 96), font(FM, 40); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    lines = label.split('\n'); lw = max(d0.textlength(l, font=f2) for l in lines); nw = d0.textlength(num, font=f1)
    pad = 36; w = int(max(lw, nw) + 2 * pad)
    nb = d0.textbbox((0, 0), num, font=f1); lb = [d0.textbbox((0, 0), l, font=f2) for l in lines]; lh = 48
    h = int(pad + (nb[3] - nb[1]) + 18 + (len(lines) - 1) * lh + (lb[-1][3] - lb[0][1]) + pad)
    card = Image.new('RGBA', (w + 80, h + 80), (0, 0, 0, 0)); sm = Image.new('L', card.size, 0)
    ImageDraw.Draw(sm).rounded_rectangle([40, 52, 40 + w, 52 + h], radius=32, fill=90); card.putalpha(sm.filter(ImageFilter.GaussianBlur(20)))
    d = ImageDraw.Draw(card); d.rounded_rectangle([40, 40, 40 + w, 40 + h], radius=32, fill=(255, 255, 255, 250))
    y = 40 + pad - nb[1]; d.text((40 + pad, y), num, font=f1, fill=COBALT)
    y2 = 40 + pad + (nb[3] - nb[1]) + 18 - lb[0][1]
    for i, l in enumerate(lines): d.text((40 + pad, y2 + i * lh), l, font=f2, fill=INK)
    return card

LOGO = Image.open(f'{A}/logo.png').convert('RGBA'); LOGO = LOGO.crop(LOGO.getbbox())
def end_layer():
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); lw = 560; lg = LOGO.resize((lw, int(LOGO.height * lw / LOGO.width)), Image.LANCZOS)
    im.alpha_composite(lg, ((W - lw) // 2, 250)); d = ImageDraw.Draw(im); f = font(FM, 48)
    for i, t in enumerate(['DropOff Body Sculpting Serum', 'Ulta Beauty · sicksciencelabs.com']):
        x = (W - d.textlength(t, font=f)) / 2; d.text((x, 250 + lg.height + 34 + i * 62), t, font=f, fill=INK)
    return im

def src_audio(a, b):
    raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-ss', f'{a}', '-t', f'{b - a}', '-i', SRC, '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True).stdout
    y = np.frombuffer(raw, np.float32).reshape(-1, 2).copy(); n = int(0.015 * SR)
    if len(y) > 2 * n: y[:n] *= np.linspace(0, 1, n)[:, None]; y[-n:] *= np.linspace(1, 0, n)[:, None]
    return y

def render(key):
    spec = V[key]; d = f'{OUT}/{key}'; os.makedirs(d, exist_ok=True)
    plan = []; t = 0.0
    for s in spec['segs']:
        if s[0] == 'hold': plan.append(dict(kind='hold', ss=s[1], dur=s[2], t0=t)); t += s[2]
        else: plan.append(dict(kind='seg', ss=s[0], dur=s[1] - s[0], t0=t, a=s[0], b=s[1])); t += s[1] - s[0]
    total = round(t, 3)
    words = []  # output-timed tokens
    for p in plan:
        if p['kind'] != 'seg': continue
        for s, e, txt in TOK:
            if s >= p['a'] - 0.02 and e <= p['b'] + 0.05: words.append((s - p['a'] + p['t0'], e - p['a'] + p['t0'], txt))
    groups = groups_of(words)
    hl, style = spec['hook']; hw = sum(len(l.split()) for l in hl); hook_end = 2.6
    hooks = [hook_layer(hl, style, n) for n in range(hw + 1)]
    end_t = plan[-1]['t0'] + 1.3; endimg = end_layer()
    ba = ba_card(spec['ba']) if spec['ba'] else None
    if ba is not None:
        ba_t0 = plan[spec['ba_at']]['t0'] + (0.0 if spec.get('ba_from_start') else 0.9)
        hold = next((p for p in plan if p['kind'] == 'hold'), None); ba_t1 = hold['t0'] + hold['dur'] - 0.05
    sn, sl, sseg, soff = spec['stat']; sc_img = stat_card(sn, sl); st0 = plan[sseg]['t0'] + soff; st1 = st0 + 2.6
    enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p', f'{d}/video.mp4'], stdin=subprocess.PIPE)
    fi = 0; cuts = []
    for si, p in enumerate(plan):
        nfr = int(round((p['t0'] + p['dur']) * FPS)) - int(round(p['t0'] * FPS)); cuts.append(p['t0'])
        dec = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-ss', f"{p['ss']}", '-i', SRC, '-t', f"{p['dur'] + 0.4}", '-vf', f'scale={W}:{H}',
                                '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
        z0, z1 = (1.18, 1.0) if si == 0 else ((1.0, 1.06) if si % 2 else (1.06, 1.0))
        last = None
        for k in range(nfr):
            buf = dec.stdout.read(W * H * 3)
            if len(buf) == W * H * 3: last = buf
            frame = Image.frombuffer('RGB', (W, H), last)
            pr = k / max(1, nfr - 1); pr = 1 - (1 - pr) ** 2 if si == 0 else pr; z = z0 + (z1 - z0) * pr
            if abs(z - 1) > 1e-3:
                cw, ch = W / z, H / z; box = ((W - cw) / 2, (H - ch) * 0.42, (W + cw) / 2, (H - ch) * 0.42 + ch)
                frame = frame.resize((W, H), Image.BILINEAR, box=box)
            frame = frame.convert('RGBA'); tt = fi / FPS
            card_on = ba is not None and ba_t0 <= tt < ba_t1
            if tt < hook_end:
                per = (hook_end - 0.6) / hw; frame.alpha_composite(hooks[min(hw, int(tt / per) + 1)])
            if tt >= end_t: frame.alpha_composite(endimg)
            if card_on:
                age = tt - ba_t0; s = min(1.0, 0.86 + 0.14 * age / 0.18) + (0.03 * math.sin(min(1, age / 0.3) * math.pi) if age < 0.3 else 0)
                im2 = ba if abs(s - 1) < 0.005 else ba.resize((int(ba.width * s), int(ba.height * s)), Image.BILINEAR)
                cy = 860 if tt >= hook_end else 1160
                frame.alpha_composite(im2, (int((W - im2.width) / 2), int(cy - im2.height / 2)))
            if st0 <= tt < st1 and not card_on:
                age, out = tt - st0, st1 - tt; s = min(1.0, age / 0.14) * (min(1.0, out / 0.14))
                if s > 0.03:
                    im2 = sc_img.resize((max(1, int(sc_img.width * s)), max(1, int(sc_img.height * s))), Image.BILINEAR)
                    frame.alpha_composite(im2, (int(80 + sc_img.width / 2 - im2.width / 2), int(330 + sc_img.height / 2 - im2.height / 2)))
            if tt >= hook_end - 0.2 and tt < end_t and not card_on:
                for g in groups:
                    gs, ge = g[0][0], g[-1][1] + 0.12
                    if gs - 0.05 <= tt <= ge:
                        act = 0
                        for j, w in enumerate(g):
                            if w[0] <= tt: act = j
                        img = caption_img(g, act); age = tt - gs
                        s = 1.0 if age > 0.18 else 0.82 + 0.18 * (age / 0.18) + 0.06 * math.sin(age / 0.18 * math.pi)
                        if abs(s - 1) > 0.01: img = img.resize((int(img.width * s), int(img.height * s)), Image.BILINEAR)
                        frame.alpha_composite(img, (int((W - img.width) / 2), int(1180 - img.height / 2))); break
            if tt < 0.12: frame.alpha_composite(Image.new('RGBA', (W, H), (255, 255, 255, int(220 * (1 - tt / 0.12)))))
            enc.stdin.write(frame.convert('RGB').tobytes()); fi += 1
        dec.stdout.close(); dec.wait()
    enc.stdin.close(); enc.wait()
    # audio: source speech (holds = silence) + ducked bed + SFX
    parts = []
    for p in plan:
        n = int(round((p['t0'] + p['dur']) * SR)) - int(round(p['t0'] * SR))
        y = src_audio(p['a'], p['b']) if p['kind'] == 'seg' else np.zeros((n, 2), np.float32)
        y = y[:n] if len(y) >= n else np.vstack([y, np.zeros((n - len(y), 2), np.float32)]); parts.append(y)
    v = np.vstack(parts)
    with wave.open(f'{d}/vo.wav', 'wb') as wv:
        wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes((np.clip(v, -1, 1) * 32767).astype(np.int16).tobytes())
    from mgaudio import recipes, sfx
    m = recipes.pop(duration=total + 0.5, bpm=112, key='A', drop=0.0)
    m.sfx(sfx.impact('cinematic', size=0.8), at=0.0, gain=-5)
    for j, c in enumerate(cuts[1:]): m.sfx(sfx.swish(0.22), at=max(0, c - 0.1), gain=-11)
    if ba is not None: m.sfx(sfx.pop('mouth'), at=max(0, ba_t0 - 0.02), gain=-6)
    m.sfx(sfx.pop('mouth'), at=max(0, st0 - 0.02), gain=-8); m.sfx(sfx.ding('E6'), at=end_t, gain=-9)
    m.export(f'{d}/bed.wav', lufs=-30.0, analyze=False)
    subprocess.run(f'ffmpeg -loglevel error -y -i "{d}/vo.wav" -i "{d}/bed.wav" -filter_complex '
       f'"[0:a]loudnorm=I=-16:TP=-2,aresample=48000,aformat=channel_layouts=stereo,apad=whole_dur={total},asplit[vA][vB];'
       f'[1:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{total}[b];[b][vA]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=300[bd];'
       f'[bd][vB]amix=inputs=2:normalize=0,alimiter=limit=0.89[mx]" -map "[mx]" -t {total} -ar 48000 "{d}/mix.wav"', shell=True, check=True)
    subprocess.run(f'ffmpeg -loglevel error -y -i "{d}/video.mp4" -i "{d}/mix.wav" -c:v copy -c:a aac -b:a 192k -shortest "{d}/{key}.mp4"', shell=True, check=True)
    print(key, total)

if __name__ == '__main__':
    for k in (sys.argv[1:] or V): render(k)
