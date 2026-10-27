"""Batch 45 variants — Dr. Merve's 14-day ShapeShift challenge, Meta cuts (9:16, ≤20 s), hook-first and purchase-led.
Frame-by-frame compositor (streams to ffmpeg): raw 4K clips, aligned profile stills (align45.py), wipe reveals, splits,
captions from the isolated VO, day chips and an end card. Pill/chip text is centred with anchor='mm' on the pill centre.
usage: ~/motion-tools/.venv/bin/python render45v.py v1|v2|v3"""
import os, sys, json, subprocess, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import recipes, sfx

HERE = os.path.dirname(os.path.abspath(__file__)); RAW = os.path.join(HERE, 'raw'); AU = os.path.join(HERE, 'audio')
AL = os.path.join(HERE, 'align'); OUT = os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
FD = os.path.expanduser('~/Library/Fonts/'); FB = FD + 'FoundersGrotesk-Bold.otf'; FM = FD + 'FoundersGrotesk-Medium.otf'
W, H, FPS, FF = 1080, 1920, 30, 'ffmpeg'
VO, INTRO = os.path.join(AU, 'vo_edit_vocals.wav'), os.path.join(AU, 'merve_intro_vocals.wav')
MAG, INK, WHITE = (169, 33, 192), (12, 10, 14), (255, 255, 255)
FIX = {'Shapeshift': 'ShapeShift', 'Meriwe,': 'Merve,', 'Six': 'SickScience', 'Science': None}
DAYS = [('d0', 'DAY 0'), ('d3', 'DAY 3'), ('d5', 'DAY 5'), ('d8', 'DAY 8'), ('d10', 'DAY 10'), ('d14', 'DAY 14')]

def font(p, s): return ImageFont.truetype(p, s)

# ---------- sources ----------
def video(name, t0, dur):
    p = subprocess.Popen([FF, '-v', 'error', '-ss', f'{t0:.3f}', '-i', os.path.join(RAW, name + '.MOV'), '-t', f'{dur + 0.2:.3f}',
                          '-vf', f'scale={W}:{H}:flags=lanczos', '-r', str(FPS), '-an', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                         stdout=subprocess.PIPE)
    last = None
    while True:
        b = p.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        last = Image.frombytes('RGB', (W, H), b); yield last
    p.wait()
    while True: yield last

def still(key):
    im = Image.open(os.path.join(AL, key + '_full.png')).convert('RGB')
    while True: yield im

def split(a, b):
    im = Image.new('RGB', (W, H)); im.paste(Image.open(os.path.join(AL, a + '_half.png')).convert('RGB'), (0, 0))
    im.paste(Image.open(os.path.join(AL, b + '_half.png')).convert('RGB'), (540, 0))
    ImageDraw.Draw(im).rectangle((537, 0, 542, H), fill=WHITE)
    while True: yield im

def wipe(a, b, dur, passes=2):
    """vertical line sweeps across: left of the line = a (before), right = b (after); back and forth `passes` times"""
    A = np.asarray(Image.open(os.path.join(AL, a + '_full.png')).convert('RGB')); B = np.asarray(Image.open(os.path.join(AL, b + '_full.png')).convert('RGB'))
    n = round(dur * FPS)
    for k in range(n):
        u = (k / max(1, n - 1)) * passes; ph = u % 1; ph = ph if int(u) % 2 == 0 else 1 - ph
        e = 0.5 - 0.5 * np.cos(np.pi * ph); x = int(140 + e * (W - 280))
        im = B.copy(); im[:, :x] = A[:, :x]; img = Image.fromarray(im); d = ImageDraw.Draw(img)
        d.rectangle((x - 3, 0, x + 3, H), fill=WHITE); d.ellipse((x - 30, 870, x + 30, 930), fill=WHITE)
        d.polygon([(x - 18, 900), (x - 6, 890), (x - 6, 910)], fill=INK); d.polygon([(x + 18, 900), (x + 6, 890), (x + 6, 910)], fill=INK)
        yield img, x
    while True: yield img, x

# ---------- overlays ----------
def pill(d, cx, cy, txt, size, fill=MAG, ink=WHITE, padx=34, pady=18):
    f = font(FB, size); l, t, r, b = d.textbbox((0, 0), txt, font=f, anchor='mm')
    w, h = (r - l) + 2 * padx, (b - t) + 2 * pady
    d.rounded_rectangle((cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2), h / 2, fill=fill)
    d.text((cx, cy), txt, font=f, fill=ink, anchor='mm')          # true centre of the ink box = pill centre

def headline(d, lines, y, size=120, ink=WHITE):
    f = font(FB, size)
    while max(d.textlength(l, font=f) for l in lines) > W - 140: size -= 4; f = font(FB, size)
    lh = int(size * 1.08)
    for i, l in enumerate(lines):
        d.text((W / 2, y + i * lh), l, font=f, fill=ink, anchor='ma', stroke_width=6, stroke_fill=INK + (200,))

def caption(d, txt, y):
    f = font(FB, 84)
    while d.textlength(txt, font=f) > W - 140: f = font(FB, f.size - 4)
    d.text((W / 2, y), txt, font=f, fill=WHITE, anchor='mm', stroke_width=7, stroke_fill=INK + (220,))

_END = {}
def end_layer(txt):
    """logo + text layer and a blurred light halo layer, cached per text"""
    if txt not in _END:
        ink = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ink)
        lg = Image.open(os.path.join(HERE, '..', 'video-01-bcrf', 'assets', 'logo.png')).convert('RGBA')
        lg = lg.resize((520, round(lg.height * 520 / lg.width)), Image.LANCZOS); ink.paste(lg, ((W - 520) // 2, 445), lg)
        d.text((W / 2, 445 + lg.height + 52), txt, font=font(FM, 42), fill=(20, 16, 20, 255), anchor='mm')
        from PIL import ImageFilter
        m = ink.getchannel('A').filter(ImageFilter.GaussianBlur(14)).point(lambda p: int(min(255, p * 1.6)))
        halo = Image.new('RGBA', (W, H), (255, 255, 255, 0)); halo.putalpha(m.point(lambda p: int(p * 120 / 255)))
        _END[txt] = (halo, ink)
    return _END[txt]

def fade(layer, a):
    if a >= 1: return layer
    l2 = layer.copy(); l2.putalpha(layer.getchannel('A').point(lambda p: int(p * a))); return l2

def logo_img(width):
    lg = Image.open(os.path.join(HERE, '..', 'video-01-bcrf', 'assets', 'logo.png')).convert('RGBA'); px = lg.load()
    for yy in range(lg.height):
        for xx in range(lg.width):
            r, g, b, a = px[xx, yy]
            if a and max(r, g, b) < 90: px[xx, yy] = (255, 255, 255, a)
    return lg.resize((width, round(lg.height * width / lg.width)), Image.LANCZOS)

# ---------- captions from the isolated voice ----------
WORDS = json.load(open(os.path.join(AU, 'words.json')))
def cap_groups(key, a, b, t0):
    ws = []
    for w, s, e in WORDS[key]:
        if s >= a - 0.05 and s < b:
            if w in FIX:
                if FIX[w] is None: continue
                w = FIX[w]
            if w.startswith('-') and ws: pw, ps, _ = ws[-1]; ws[-1] = (pw + w, ps, e)
            else: ws.append((w, s, e))
    gs, cur = [], []
    for w in ws:
        cur.append(w)
        if len(cur) == 3 or w[0][-1:] in '.,': gs.append(cur); cur = []
    if cur: gs.append(cur)
    return [(' '.join(x[0] for x in g), t0 + g[0][1] - a - 0.03, t0 + g[-1][2] - a + 0.12) for g in gs]

# ---------- variants ----------
# each segment: dict(kind, dur, src..., vo=(key, a, b) or None, chip, chip2, head, capy)
HOOK = ('vo', 0.00, 3.40)          # "Not another peptide. It's an exosome."
INTRO_L = ('intro', 3.00, 8.50)    # "I'm Dr. Merve, co-founder of SickScience Labs. Today I'm starting my ShapeShift challenge."
MECH_A = ('vo', 6.60, 9.42)        # "Plant-derived exosomes help signal skin"
MECH_B = ('vo', 9.42, 12.55)       # "for a firmer, more sculpted-looking jawline."
LOOK = ('vo', 19.25, 21.15)        # "Look at that difference."

def jumps(step=0.4):
    return [dict(kind='still', key=k, dur=step, chip=lab, big=True) for k, lab in DAYS]

def endcard(dur, base):
    return dict(kind=base[0], key=base[1] if len(base) > 1 else None, dur=dur, end=True)

VARIANTS = {
    # V1 — result first: split hook, founder, mechanism, jump cuts, held split with price + URL
    'v1': [dict(kind='split', a='d0', b='d14', dur=3.4, vo=HOOK, chip2=('DAY 0', 'DAY 14'), capy=480),
           dict(kind='video', name='IMG_2162', t=3.0, dur=5.5, vo=INTRO_L, chip='DAY 0'),
           dict(kind='video', name='IMG_2164', t=13.0, dur=2.82, vo=MECH_A, chip='DAY 0'),
           dict(kind='video', name='IMG_2602', t=8.0, dur=3.13, vo=MECH_B, chip='DAY 8'),
           *jumps(0.4),
           dict(kind='split', a='d0', b='d14', dur=2.7, vo=LOOK, chip2=('DAY 0', 'DAY 14'), capy=480, end=True)],
    # V2 — wipe reveal hook (fast, curiosity): drag line Day 0 ⇄ Day 14, mechanism over jump cuts, product + price
    'v2': [dict(kind='wipe', a='d0', b='d14', dur=3.4, vo=HOOK, sides=True, capy=480),
           *[dict(kind='still', key=k, dur=0.47, chip=lab, big=True, vo=(MECH_A if i == 0 else None)) for i, (k, lab) in enumerate(DAYS)],
           dict(kind='video', name='IMG_2602', t=8.0, dur=3.13, vo=MECH_B, chip='DAY 8'),
           dict(kind='split', a='d0', b='d14', dur=2.0, vo=LOOK, chip2=('DAY 0', 'DAY 14'), capy=480),
           dict(kind='video', name='IMG_2164', t=1.5, dur=2.0, end=True, price=True)],
    # V3 — founder challenge: headline "I tested my own serum for 14 days", intro, countdown jump cuts, wipe to result
    'v3': [dict(kind='video', name='IMG_2162', t=3.0, dur=5.5, vo=INTRO_L, head=['I TESTED MY OWN', 'SERUM FOR 14 DAYS'], headdur=2.6),
           *jumps(0.45),
           dict(kind='wipe', a='d0', b='d14', dur=3.0, vo=MECH_A, capy=480),
           dict(kind='video', name='IMG_2602', t=8.0, dur=3.13, vo=MECH_B, chip='DAY 8'),
           dict(kind='split', a='d0', b='d14', dur=3.0, vo=LOOK, chip2=('DAY 0', 'DAY 14'), capy=480, end=True, price=True)],
}

def main(v):
    S = VARIANTS[v]; t = 0.0; caps = []; vo_parts = []
    for sg in S:
        sg['dur'] = round(sg['dur'] * FPS) / FPS          # snap to whole frames so voice/captions stay on the picture
        sg['t0'] = t
        if sg.get('vo'):
            key, a, b = sg['vo']; caps += [(c, s, e, sg.get('capy', 1080)) for c, s, e in cap_groups(key, a, b, t)]
            vo_parts.append((VO if key == 'vo' else INTRO, a, b - a, t))
        t += sg['dur']
    total = t; assert total <= 20.0, total
    lg = logo_img(520)
    tmp = tempfile.mkdtemp(prefix='b45v_'); vid = os.path.join(tmp, 'v.mp4')
    enc = subprocess.Popen([FF, '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                            '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', vid], stdin=subprocess.PIPE)
    for sg in S:
        n = round(sg['dur'] * FPS); k0 = sg['kind']
        gen = (video(sg['name'], sg['t'], sg['dur']) if k0 == 'video' else still(sg['key']) if k0 == 'still'
               else split(sg['a'], sg['b']) if k0 == 'split' else wipe(sg['a'], sg['b'], sg['dur']))
        for k in range(n):
            tt = sg['t0'] + k / FPS; fr = next(gen)
            if k0 == 'wipe': fr, x = fr
            im = fr.copy(); d = ImageDraw.Draw(im, 'RGBA')
            if sg.get('chip'): pill(d, W / 2, 340, sg['chip'], 72 if sg.get('big') else 52)
            if sg.get('chip2'): pill(d, W / 4, 340, sg['chip2'][0], 52); pill(d, 3 * W / 4, 340, sg['chip2'][1], 52)
            if sg.get('sides'):                                      # big side labels over the wipe (no arrow glyph in Founders)
                f = font(FB, 120)
                for txt, cx in (('DAY 0', W / 4), ('DAY 14', 3 * W / 4)):
                    d.text((cx, 340), txt, font=f, fill=WHITE, anchor='mm', stroke_width=6, stroke_fill=INK + (200,))
            elif k0 == 'wipe' and not sg.get('head'): pill(d, W / 4, 340, 'DAY 0', 52); pill(d, 3 * W / 4, 340, 'DAY 14', 52)
            if sg.get('head') and (k / FPS) < sg.get('headdur', sg['dur']): headline(d, sg['head'], 300)
            for c, s, e, y in caps:
                if s <= tt < e: caption(d, c, y)
            if sg.get('end') and tt >= total - 1.3:              # no plate, no glow: brand logo (black + magenta) + dark text
                a = min(1, (tt - (total - 1.3)) * 5)
                txt = ('ShapeShift  ·  $64  ·  ' if sg.get('price') else '') + 'SickScienceLabs.com'
                card = end_layer(txt); halo, ink = card
                im = Image.alpha_composite(im.convert('RGBA'), fade(ink, a)).convert('RGB')   # plain, no halo (user: 'glow atma… dümdüz koy')
            enc.stdin.write(im.tobytes())
    enc.stdin.close(); enc.wait()
    # audio: voice pieces on the timeline + lo-fi bed ducked under the voice
    m = recipes.lofi(duration=round(total, 3), drop=0.0, outro=total - 1.3, keys='rhodes', flavor='chill')
    for sg in S:
        if sg['kind'] in ('still',): m.sfx(sfx.pop('soft'), at=sg['t0'], gain=-16)
    bed = os.path.join(tmp, 'bed.wav'); m.export(bed)
    ins, fc, labs = ['-i', vid], [], []
    for j, (af, a, dur, st) in enumerate(vo_parts):
        ins += ['-i', af]
        fc.append(f'[{j + 1}:a]atrim={a:.3f}:{a + dur:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={max(0, dur - 0.04):.3f}:d=0.04,'
                  f'adelay={int(st * 1000)}|{int(st * 1000)},aresample=48000[va{j}]'); labs.append(f'[va{j}]')
    ins += ['-i', bed]; bi = len(vo_parts) + 1
    fc.append(''.join(labs) + f'amix=inputs={len(labs)}:duration=longest:normalize=0,apad=whole_dur={total:.3f},asplit=2[vox][sc]')
    fc.append(f'[{bi}:a]aresample=48000,volume=-9dB[mus];[mus][sc]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=300[duck]')
    fc.append('[vox][duck]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[ao]')
    out = os.path.join(OUT, f'ss_challenge_{v}.mp4')
    subprocess.run([FF, '-v', 'error', '-y', *ins, '-filter_complex', ';'.join(fc), '-map', '0:v', '-map', '[ao]', '-t', f'{total:.3f}',
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', out], check=True)
    print('->', out, round(total, 2), 's')

if __name__ == '__main__':
    main(sys.argv[1])
