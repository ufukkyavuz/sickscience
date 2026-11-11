"""UGC viral 3 (2026-11-11): Polen / Ayşim raw shoots -> ≤20 s reels. Spec-driven (specs.py).
Rules: open on the peak, animated Founders text (pop / blur / slide), speech captions on talking parts, big word,
inserts (lab data images), emoji + punch on fun, real Pixabay track per video (new tracks), mgaudio SFX only,
colours untouched (SDR sources decoded with their own matrix; HLG raws pre-converted with Apple's tone map, tools/hlg2sdr),
output H.264 BT.709 tagged, -14 LUFS."""
import os, sys, math, json, subprocess, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
ROOT = os.path.dirname(os.path.abspath(__file__)); OUT = f'{ROOT}/out'; os.makedirs(OUT, exist_ok=True)
W, H, FPS, SR = 1080, 1920, 30, 48000
FB = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Bold.otf')
FM = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Medium.otf')
EMOJI = '/System/Library/Fonts/Apple Color Emoji.ttc'
PCOL = {'ss': (115, 0, 199), 'nw': (200, 30, 40), 'pc': (30, 130, 60), 'do': (25, 60, 190)}
_fc = {}
def font(s, f=FB):
    if (s, f) not in _fc: _fc[(s, f)] = ImageFont.truetype(f, s)
    return _fc[(s, f)]
def sh(c): subprocess.run(c, shell=True, check=True, capture_output=True)
def ease(p): p = max(0.0, min(1.0, p)); return 1 - (1 - p) ** 3

def text_img(txt, size=84, col=(255, 255, 255), fnt=FB, maxw=980):
    lines = txt.split('\n'); f = font(size, fnt); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    lh = int(size * 1.12); ws = [d0.textlength(l, font=f) for l in lines]
    im = Image.new('RGBA', (int(max(ws)) + 80, lh * len(lines) + 60), (0, 0, 0, 0))
    shd = Image.new('RGBA', im.size, (0, 0, 0, 0)); ds = ImageDraw.Draw(shd); d = None
    for i, l in enumerate(lines):
        x = (im.width - ws[i]) / 2; ds.text((x, 32 + i * lh), l, font=f, fill=(0, 0, 0, 190), stroke_width=3, stroke_fill=(0, 0, 0, 190))
    im = Image.alpha_composite(im, shd.filter(ImageFilter.GaussianBlur(8))); d = ImageDraw.Draw(im)
    for i, l in enumerate(lines):
        x = (im.width - ws[i]) / 2; d.text((x, 28 + i * lh), l, font=f, fill=col + (255,), stroke_width=1, stroke_fill=(30, 30, 30))
    if im.width > maxw: im = im.resize((maxw, int(im.height * maxw / im.width)), Image.LANCZOS)
    return im

def tag_img(name, sub):
    """OneSkin-style name tag: white box with dark caps name, white subtitle line under it (left aligned)."""
    fn = font(40, FM); fs = font(36, FM); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    nm = name.upper(); l, t_, r, b = d0.textbbox((0, 0), nm, font=fn); sw = d0.textlength(sub, font=fs)
    px, bh = 24, 66; bw = (r - l) + 2 * px; im = Image.new('RGBA', (int(max(bw, sw)) + 30, bh + 76), (0, 0, 0, 0))
    shd = Image.new('RGBA', im.size, (0, 0, 0, 0)); ImageDraw.Draw(shd).text((2, bh + 16), sub, font=fs, fill=(0, 0, 0, 170))
    im = Image.alpha_composite(im, shd.filter(ImageFilter.GaussianBlur(5))); d = ImageDraw.Draw(im)
    d.rectangle((0, 0, bw, bh), fill=(250, 250, 248, 245)); d.text((px - l, (bh - (b - t_)) / 2 - t_), nm, font=fn, fill=(20, 20, 20, 255))
    d.text((0, bh + 14), sub, font=fs, fill=(255, 255, 255, 255))
    return im

def big_img(text, col=(255, 255, 255), wfrac=0.85, maxsize=330):
    size = maxsize; f = font(size); d0 = ImageDraw.Draw(Image.new('RGBA', (1, 1)))
    while d0.textlength(text, font=f) > W * wfrac and size > 60: size -= 6; f = font(size)
    l, t, r, b = d0.textbbox((0, 0), text, font=f); pad = 40
    im = Image.new('RGBA', (r - l + 2 * pad, b - t + 2 * pad), (0, 0, 0, 0))
    s_ = Image.new('RGBA', im.size, (0, 0, 0, 0)); ImageDraw.Draw(s_).text((pad - l, pad - t + 6), text, font=f, fill=(0, 0, 0, 110))
    im = Image.alpha_composite(im, s_.filter(ImageFilter.GaussianBlur(14)))
    ImageDraw.Draw(im).text((pad - l, pad - t), text, font=f, fill=col + (255,)); return im

_em = {}
def emoji_img(e, px=360):
    if (e, px) not in _em:
        f = ImageFont.truetype(EMOJI, 160); im = Image.new('RGBA', (260, 260), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((20, 20), e, font=f, embedded_color=True); im = im.crop(im.getbbox())
        _em[(e, px)] = im.resize((px, int(im.height * px / im.width)), Image.LANCZOS)
    return _em[(e, px)]

def anim(im, style, age, dur):
    """returns (image, dx, dy, alpha) for an element of given age; fades out over last 0.15 s"""
    out_a = min(1.0, max(0.0, (dur - age) / 0.15)); dx = dy = 0
    if style == 'pop':
        p = min(1.0, age / 0.22); s = 0.75 + 0.25 * p + 0.08 * math.sin(p * math.pi); a = min(1, age / 0.08)
        im = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.BILINEAR)
    elif style == 'blur':
        p = min(1.0, age / 0.3); r = 18 * (1 - ease(p)); a = ease(p)
        if r > 0.5: im = im.filter(ImageFilter.GaussianBlur(r))
    elif style == 'slide':
        p = ease(age / 0.3); dy = int(70 * (1 - p)); a = p
    elif style == 'drop':
        p = min(1.0, age / 0.28); dy = int(-160 * (1 - ease(p)) + 18 * math.sin(p * math.pi)); a = min(1, age / 0.1)
    else:
        a = 1
    a *= out_a
    if a < 0.999:
        im = im.copy(); im.putalpha(im.split()[3].point(lambda v: int(v * a)))
    return im, dx, dy

def place(fr, im, cx, cy):
    fr.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))

def ring(fr, cx, cy, r, age, col=(255, 235, 59)):
    p = ease(age / 0.4); d = ImageDraw.Draw(fr); a0 = -90; a1 = -90 + 360 * p
    d.arc([cx - r, cy - r, cx + r, cy + r], a0, a1, fill=col + (255,), width=9)


def kin_render(fr, lines, age, dur, y0, stagger=0.09):
    """kinetic type: each word lands in turn (alternating from left/right/below) with overshoot; mixed sizes stack"""
    out_a = min(1.0, max(0.0, (dur - age) / 0.15)); y = y0; n = 0
    for line in lines:
        imgs = [(kin_word(it[0], it[1], tuple(it[2])), it[3] if len(it) > 3 else None) for it in line]
        lh = max(im.height for im, _ in imgs) - 72; tw = sum(im.width for im, _ in imgs) - 54 * (len(imgs) - 1)
        x = W / 2 - tw / 2
        for im, wt in imgs:
            a0 = (age - wt) if wt is not None else (age - n * stagger); n += 1
            if a0 > 0:
                p = min(1.0, a0 / 0.22); e = 1 - (1 - p) ** 3; ov = 0.10 * math.sin(p * math.pi)
                d = [(-180, 0), (180, 0), (0, 120)][n % 3]
                s = 0.6 + 0.4 * e + ov; im2 = im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.BILINEAR)
                al = min(1.0, a0 / 0.08) * out_a
                if al < 0.999: im2 = im2.copy(); im2.putalpha(im2.split()[3].point(lambda v: int(v * al)))
                cx = x + im.width / 2 + d[0] * (1 - e); cy = y + im.height / 2 + d[1] * (1 - e)
                fr.alpha_composite(im2, (int(cx - im2.width / 2), int(cy - im2.height / 2)))
            x += im.width - 54
        y += lh

_kw = {}
def kin_word(w, size, col):
    if (w, size, col) not in _kw: _kw[(w, size, col)] = text_img(w, size, col, maxw=1040)
    return _kw[(w, size, col)]

# ---------------- words / captions ----------------
FIXW = {'sixscience': 'SickScience', 'shapeshift': 'ShapeShift', 'network': 'NetWork', 'powercycle': 'PowerCycle'}
def load_words(src):
    p = f'{ROOT}/words/' + os.path.splitext(os.path.basename(src))[0] + '.json'
    return json.load(open(p)) if os.path.exists(p) else []
def cap_groups(words):
    gs, cur = [], []
    for j, w in enumerate(words):
        cur.append(w); nxt = words[j + 1] if j + 1 < len(words) else None
        brk_next = nxt is not None and nxt[2].lower().strip(',.') in ('which', 'and', 'but', 'taken', 'this', 'that', 'so')
        if nxt is None or w[2][-1:] in ',.?!' or nxt[0] - w[1] > 0.3 or len(cur) == 4 or (brk_next and len(cur) >= 2):
            gs.append(cur); cur = []
    out = []
    for g in gs:
        if out and len(g) == 1 and len(out[-1]) <= 4 and g[0][0] - out[-1][-1][1] < 0.35 and out[-1][-1][2][-1:] not in '.?!':
            out[-1] = out[-1] + g
        else:
            out.append(g)
    gs = out
    return gs

def envelope(src):
    a = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-map', '0:a:0', '-ac', '1', '-ar', '16000', '-f', 's16le', '-'], capture_output=True).stdout
    x = np.frombuffer(a, np.int16).astype(np.float32) / 32768; n = len(x) // 160
    return np.sqrt((x[:n * 160].reshape(n, 160) ** 2).mean(1)) if n else np.zeros(1)
def snap(env, t):
    i0, i1 = max(0, int((t - 0.06) * 100)), min(len(env) - 1, int((t + 0.22) * 100))
    if i1 <= i0: return t
    seg = env[i0:i1 + 1]; pk = seg.max()
    if pk < 0.01: return t
    return (i0 + int(np.argmax(seg > max(0.3 * pk, 0.008)))) / 100

def metal_clang(path):
    t = np.arange(int(SR * 2.2)) / SR; out = np.zeros_like(t)
    for ht, g in [(0.0, 1.0), (0.17, 0.55), (0.29, 0.35), (0.37, 0.2)]:
        tt = t - ht; m = tt >= 0
        for f, a_, d_ in [(523, 1.0, 1.1), (1347, .7, .8), (2311, .5, .6), (3420, .35, .45), (4870, .25, .3), (812, .5, .9)]:
            out[m] += g * a_ * np.sin(2 * np.pi * f * tt[m]) * np.exp(-tt[m] / (d_ * (0.5 + 0.5 * g)))
    out = out / np.abs(out).max() * 0.9; pcm = (np.stack([out, out], 1) * 32767).astype(np.int16)
    with wave.open(path, 'wb') as wv: wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes(pcm.tobytes())

# ---------------- render ----------------
def render(k, S):
    d = f'{OUT}/{k}'; os.makedirs(d, exist_ok=True)
    segs = S['segs']
    durs = [(s['b'] - s['a']) / s.get('speed', 1) for s in segs]
    starts = np.cumsum([0] + durs); total = float(starts[-1])
    nfr = [int(round(starts[i + 1] * FPS)) - int(round(starts[i] * FPS)) for i in range(len(segs))]
    # speech captions: words of audio segments mapped to out time
    caps = []
    if S.get('caps'):
        envs = {}
        for i, s in enumerate(segs):
            if not s.get('audio') or s.get('nocap'): continue
            if s['src'] not in envs: envs[s['src']] = envelope(s['src'])
            ws = [(snap(envs[s['src']], w[0]), w[1], w[2]) for w in load_words(s['src']) if s['a'] - 0.05 <= w[0] < s['b']]
            ws = [(t0, t1, S.get('fix', {}).get(wd, FIXW.get(wd.lower().rstrip(',.?!'), wd))) for t0, t1, wd in ws]
            ws = [(t0, min(t1, t0 + 0.6), wd) for t0, t1, wd in ws]
            for g in cap_groups(ws):
                if all(w[2].lower().strip(',.') in ('and', 'so', 'um', 'uh') for w in g): continue
                c0 = starts[i] + g[0][0] - s['a']; c1 = min(starts[i] + g[-1][1] - s['a'] + 0.08, starts[i + 1] - 0.02)
                caps.append((c0, c1, ' '.join(w[2] for w in g).upper().rstrip(',.')))
    texts = S.get('texts', []); bigs = S.get('big', []); inserts = S.get('inserts', []); emos = S.get('emoji', [])
    punches = S.get('punch', []); shakes = S.get('shake', [])
    cache = {}
    def timg(key, fn):
        if key not in cache: cache[key] = fn()
        return cache[key]
    enc = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-vf', 'scale=out_color_matrix=bt709', '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p',
                            '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', f'{d}/video.mp4'], stdin=subprocess.PIPE)
    fi = 0
    for si, s in enumerate(segs):
        sp = s.get('speed', 1); vf = (f"crop={s['crop']}," if s.get('crop') else '') + f'scale={W}:{H}:in_color_matrix=auto:flags=lanczos'
        if s.get('hflip'): vf += ',hflip'
        vf += f',setpts=PTS/{sp},fps={FPS}'
        dec = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-ss', f"{s['a']}", '-i', s['src'], '-t', f"{s['b'] - s['a'] + 0.4}", '-an',
                                '-vf', vf, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
        z0, z1 = s.get('zoom', (1.0, 1.0)); last = None
        for kf in range(nfr[si]):
            buf = dec.stdout.read(W * H * 3)
            if len(buf) == W * H * 3: last = buf
            fr = Image.frombuffer('RGB', (W, H), last); t = fi / FPS
            z = z0 + (z1 - z0) * kf / max(1, nfr[si] - 1); dx = dy = 0
            for tp in punches:
                if 0 <= t - tp < 0.6: z *= 1 + 0.12 * math.exp(-(t - tp) / 0.13)
            for tk in shakes:
                if 0 <= t - tk < 0.35: amp = 20 * (1 - (t - tk) / 0.35); dx = int(amp * math.sin(t * 90)); dy = int(amp * math.cos(t * 70))
            if z > 1.001 or dx or dy:
                cw, ch = W / z, H / z; x0 = min(max(0, (W - cw) / 2 + dx), W - cw); y0 = min(max(0, H * 0.4 - ch * 0.4 + dy), H - ch)
                fr = fr.resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + cw, y0 + ch))
            fr = fr.convert('RGBA')
            for (t0, t1, png, cx, cy, wd, st, rng) in inserts:
                if t0 <= t < t1:
                    im = timg(('ins', png, wd), lambda: (lambda i: i.resize((wd, int(i.height * wd / i.width)), Image.LANCZOS))(Image.open(png).convert('RGBA')))
                    if st == 'card':
                        im = timg(('card', png, wd), lambda: card(im))
                    im2, ddx, ddy = anim(im, 'drop' if st == 'card' else 'slide', t - t0, t1 - t0)
                    place(fr, im2, cx + ddx, cy + ddy)
                    if rng and t - t0 > rng[3]:
                        ring(fr, rng[0], rng[1], rng[2], t - t0 - rng[3])
            for tx in texts:
                t0, t1, txt, stl, y, size, col = tx[:7]; xx = tx[7] if len(tx) > 7 else W / 2
                if t0 <= t < t1:
                    im = timg(('t', txt, size, col), lambda: text_img(txt, size, col))
                    im2, ddx, ddy = anim(im, stl, t - t0, t1 - t0); place(fr, im2, xx + ddx, y + ddy)
            for (t0, t1, nm, sb, tx_, ty_) in S.get('tag', []):
                if t0 <= t < t1:
                    im = timg(('tag', nm, sb), lambda: tag_img(nm, sb))
                    im2, ddx, ddy = anim(im, 'blur', t - t0, t1 - t0); fr.alpha_composite(im2, (int(tx_), int(ty_)))
            for (t0, t1, lines, y) in S.get('kin', []):
                if t0 <= t < t1: kin_render(fr, lines, t - t0, t1 - t0, y)
            for bg in bigs:
                t0, t1, txt, y, col = bg[:5]
                if t0 <= t < t1:
                    im = timg(('b', txt, col), lambda: big_img(txt, col))
                    im2, ddx, ddy = anim(im, 'pop', t - t0, t1 - t0)
                    if len(bg) > 5 and bg[5] == 'behind':   # word sits behind her head: person mask (Vision) re-composited on top
                        base = fr.copy(); place(fr, im2, W / 2, y); fr.alpha_composite(person_cut(base))
                    else: place(fr, im2, W / 2, y)
            for (te, emo, side, y) in emos:
                age = t - te
                if 0 <= age < 1.0:
                    p = min(1.0, age / 0.14); s_ = 0.3 + 0.7 * p + 0.25 * math.sin(p * math.pi); al = min(1.0, (1.0 - age) / 0.15)
                    im = emoji_img(emo).rotate(-12 * side + 6 * math.sin(age * 9), expand=True, resample=Image.BICUBIC)
                    im = im.resize((max(1, int(im.width * s_)), max(1, int(im.height * s_))), Image.BILINEAR)
                    if al < 1: im = im.copy(); im.putalpha(im.split()[3].point(lambda v: int(v * al)))
                    fly = 1 - min(1.0, age / 0.18) ** 0.5
                    place(fr, im, W / 2 + side * (330 + 480 * fly), y - 70 * min(1, age / 0.6) + 120 * fly)
            for (c0, c1, txt) in caps:
                if c0 - 0.03 <= t <= c1:
                    if any(bg[0] <= t < bg[1] and bg[2].replace("'", '').upper() in txt.replace("'", '') for bg in bigs): break
                    im = timg(('c', txt), lambda: text_img(txt, 76))
                    age = t - c0; s_ = 1.0 if age > 0.15 else 0.88 + 0.12 * max(0, age) / 0.15
                    if abs(s_ - 1) > 0.01: im = im.resize((int(im.width * s_), int(im.height * s_)), Image.BILINEAR)
                    place(fr, im, W / 2, S.get('cap_y', 1180)); break
            enc.stdin.write(fr.convert('RGB').tobytes()); fi += 1
        dec.stdout.close(); dec.wait()
    enc.stdin.close(); enc.wait()
    # ---------------- audio ----------------
    parts = []; ins = []
    for i, s in enumerate(segs):
        dur = durs[i]
        if s.get('asrc'):   # voice-over: audio from another clip/time laid over this picture
            ins += ['-ss', f"{s['aa']}", '-t', f"{s['ab'] - s['aa']}", '-i', s['asrc']]
            parts.append(f"[{i}:a:0]aresample={SR},aformat=channel_layouts=stereo,asetpts=PTS-STARTPTS,afade=t=in:d=0.01,afade=t=out:st={s['ab'] - s['aa'] - 0.015}:d=0.015,apad,atrim=0:{dur}[s{i}]")
            continue
        ins += ['-ss', f"{s['a']}", '-t', f"{s['b'] - s['a']}", '-i', s['src']]
        if s.get('audio'):
            parts.append(f"[{i}:a:0]aresample={SR},aformat=channel_layouts=stereo,asetpts=PTS-STARTPTS,afade=t=in:d=0.01,afade=t=out:st={dur - 0.015}:d=0.015[s{i}]")
        else:
            parts.append(f"anullsrc=r={SR}:cl=stereo,atrim=0:{dur}[s{i}]")
    cc = ''.join(f'[s{i}]' for i in range(len(segs)))
    cmd = ['ffmpeg', '-loglevel', 'error', '-y', *ins, '-filter_complex', ';'.join(parts) + f';{cc}concat=n={len(segs)}:v=0:a=1[v]', '-map', '[v]', '-t', str(total), f'{d}/voice.wav']
    subprocess.run(cmd, check=True, capture_output=True)
    from mgaudio import recipes, sfx
    # sfx bed (silent base + sfx)
    sfxw = f'{d}/sfx.wav'
    from mgaudio import Mix
    mx = Mix(total + 0.5)
    for (t, kind) in S.get('sfx', []):
        snd = {'whoosh': lambda: sfx.whoosh(0.35), 'swish': lambda: sfx.swish(0.22), 'pop': lambda: sfx.pop(), 'tick': lambda: sfx.tick(),
               'ding': lambda: sfx.ding('E6'), 'impact': lambda: sfx.impact('punch', size=0.6)}[kind]()
        mx.sfx(snd, at=max(0, t), gain=-6)
    for te, _, _, _ in emos: mx.sfx(sfx.pop(), at=te, gain=-6)
    for tp in punches: mx.sfx(sfx.whoosh(0.3), at=max(0, tp - 0.15), gain=-8)
    if S.get('sfx') or emos or punches: mx.export(sfxw, lufs=-22.0, analyze=False)
    else: sh(f'ffmpeg -loglevel error -y -f lavfi -i anullsrc=r={SR}:cl=stereo -t {total} "{sfxw}"')
    music, moff, mgain = S['music']
    speech = any(s.get('audio') or s.get('asrc') for s in segs)
    extra = ''; inputs = f'-i "{d}/voice.wav" -ss {moff} -t {total} -i "{music}" -i "{sfxw}"'; n = 3
    if S.get('metal'):
        metal_clang(f'{d}/metal.wav'); ms = int(S['metal'] * 1000)
        inputs += f' -i "{d}/metal.wav"'; extra = f';[3:a]aresample={SR},volume=-8dB,adelay={ms}|{ms},apad[mt]'; n = 4
    tail = '[vB][md][fx]' + ('[mt]' if S.get('metal') else '')
    if speech:
        graph = (f'[0:a]highpass=f=90,afftdn=nf=-30,acompressor=threshold=0.08:ratio=3:attack=8:release=120:makeup=2,loudnorm=I=-16:TP=-2,aresample={SR},asplit[vA][vB];[1:a]aresample={SR},aformat=channel_layouts=stereo,volume={mgain}dB,'
                 f'afade=t=in:d=0.3,afade=t=out:st={total - 1.2}:d=1.2[mu];[mu][vA]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=400[md];'
                 f'[2:a]aresample={SR}[fx]{extra};{tail}amix=inputs={n}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[mx]')
    else:
        graph = (f'[0:a]aresample={SR}[vB];[1:a]aresample={SR},aformat=channel_layouts=stereo,afade=t=in:d=0.15,afade=t=out:st={total - 1.0}:d=1.0[md];'
                 f'[2:a]aresample={SR}[fx]{extra};{tail}amix=inputs={n}:normalize=0:duration=first,loudnorm=I=-14:TP=-1.5:LRA=11[mx]')
    sh(f'ffmpeg -loglevel error -y {inputs} -filter_complex "{graph}" -map "[mx]" -t {total} -ar {SR} "{d}/mix.wav"')
    o = subprocess.run(['ffmpeg', '-nostats', '-i', f'{d}/mix.wav', '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
    import re as _re
    I = float(_re.findall(r'I:\s+(-?[0-9.]+) LUFS', o)[-1]); g = -14.0 - I
    sh(f'ffmpeg -loglevel error -y -i "{d}/mix.wav" -af "volume={g:.2f}dB,alimiter=limit=0.89:level=false" -ar {SR} "{d}/mix2.wav"'); os.replace(f'{d}/mix2.wav', f'{d}/mix.wav')
    sh(f'ffmpeg -loglevel error -y -i "{d}/video.mp4" -i "{d}/mix.wav" -c:v copy -c:a aac -b:a 192k -shortest -movflags +faststart "{OUT}/{k} {S["name"]}.mp4"')
    print(k, round(total, 2), flush=True)

SEGVID = os.path.expanduser('~/sickscience-work/tools/segvid')
def person_cut(base):
    import tempfile
    td = tempfile.mkdtemp(dir='/private/tmp/claude-501'); os.makedirs(f'{td}/i'); base.convert('RGB').save(f'{td}/i/f.png')
    subprocess.run([SEGVID, f'{td}/i', f'{td}/m'], check=True, capture_output=True)
    m = Image.open(f'{td}/m/f.png').convert('L').filter(ImageFilter.GaussianBlur(1.5)); out = base.copy(); out.putalpha(m)
    import shutil; shutil.rmtree(td, ignore_errors=True)
    return out

def card(im):
    pad = 9; rr = 16
    m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, im.width - 1, im.height - 1], rr - 6, fill=255)
    im = im.copy(); im.putalpha(Image.fromarray(np.minimum(np.asarray(im.split()[3]), np.asarray(m))))
    c = Image.new('RGBA', (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0))
    sh_ = Image.new('RGBA', (c.width + 60, c.height + 60), (0, 0, 0, 0))
    ImageDraw.Draw(sh_).rounded_rectangle([30, 40, 30 + c.width, 40 + c.height], rr, fill=(0, 0, 0, 90)); sh_ = sh_.filter(ImageFilter.GaussianBlur(16))
    ImageDraw.Draw(c).rounded_rectangle([0, 0, c.width - 1, c.height - 1], rr, fill=(255, 255, 255, 255)); c.alpha_composite(im, (pad, pad))
    sh_.alpha_composite(c, (30, 30)); return sh_

if __name__ == '__main__':
    from specs import SPEC
    for k in (sys.argv[1:] or SPEC): render(k, SPEC[k])
