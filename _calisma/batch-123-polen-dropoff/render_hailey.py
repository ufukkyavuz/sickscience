# Polen x DropOff, Hailey hook (2026-11-10, user: "baştaki gibi 2ye böl, sonra alttan polenin videosu büyüyüp ekranı kaplasın
# ve kendi sesiyle anlatmaya başlasın"). Top = Hailey/TIME reel (ref/hailey_full.mp4, 90.55-94.25, her own audio),
# bottom = Polen's clip (mirrored front camera -> hflip). Then Polen's panel grows to full screen; Polen's cloned voice
# (Higgsfield element "Polen IG clean", approved 2026-11-10) narrates. Colour: explicit BT.709 in and out, checked vs source.
import json, os, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R = os.path.dirname(os.path.abspath(__file__))
PSRC, HSRC = os.path.join(R, 'src_polen_wa.mp4'), os.path.join(R, 'ref', 'hailey_full.mp4')
W, H, FPS = 1080, 1920, 30
SEAM = 940                      # Hailey rows 0..SEAM-1 are clean (the reel's own label box starts below)
VAR = os.environ.get('VAR', 'O')            # A = original; B, C = variants (user 2026-11-10: "2 tane daha varyant")
# hook pieces: (out start, out end, Hailey src start, lift px, box text) ; Polen hook-bottom src ; src overrides for later segments
CFG = {   # user 2026-11-10: "haileyin video kısmını daha çok tutalım soruyla beraber" -> every variant opens on the question, longer Hailey
    'O': ([(0.0, 2.30, 90.55, 0, 'Lymphatic drainage massages'), (2.30, 3.40, 93.15, 220, 'Totally underrated.')], 63.0, {}),
    'A': ([(0.0, 2.30, 90.55, 0, 'Lymphatic drainage massages'), (2.30, 3.35, 93.15, 220, 'Totally underrated.'),
           (3.35, 5.25, 94.20, 220, 'I swear by them.'), (5.25, 6.55, 96.10, 140, 'Live by them.')], 61.0, {4: 68.5}),
    'B': ([(0.0, 2.30, 90.55, 0, 'Lymphatic drainage massages'), (2.30, 4.85, 97.45, 220, 'Like, obsessed with\nlymphatic drainage anything,'),
           (4.85, 6.60, 100.10, 220, 'but the massages\nspecifically.')], 30.0, {}),
    'C': ([(0.0, 2.30, 90.55, 0, 'Lymphatic drainage massages'), (2.30, 3.35, 93.15, 220, 'Totally underrated.'),
           (3.35, 5.40, 101.70, 100, 'It is really crazy\nhow much water'), (5.40, 7.70, 103.75, 100, 'we hold on to\nin our bodies.')], 22.3, {3: 35.0}),
}[VAR]
HK = CFG[0]
G0 = HK[-1][1]; G1 = G0 + 0.45                            # grow
V0 = G0 + 0.15                                            # VO start
words = json.load(open(os.path.join(R, 'polen_real_words.json')))
VOD = 20.53; END = round(V0 + VOD + 0.35, 2)      # Polen's real recording (WhatsApp 2026-11-10), not the clone
TS = [2.72, 8.66, 9.84, 13.96, 17.86]            # sentence starts of the real recording, seconds after the VO starts
SEG = [(0.0, CFG[1]), (G1, 1.5), (V0 + TS[0], 15.5), (V0 + TS[1] - 0.06, 22.0), (V0 + TS[2] - 0.06, 67.0), (V0 + TS[3] - 0.06, 45.5), (V0 + TS[4] - 0.06, 96.0)]
for k, v in CFG[2].items(): SEG[k] = (SEG[k][0], v)
LINES = [(0.0, 2.38, 'Okay, my nightly body routine!'), (2.72, 8.38, 'This is DropOff, our Body Sculpting Serum,\nmade with plant exosome technology.'),
         (8.66, 9.66, 'I smooth it on,'), (9.84, 13.52, 'then I do my lymphatic drainage\nmassage with my sculpting tools.'),
         (13.96, 17.58, 'Smoother, firmer-looking skin,\nand a more defined contour.'), (17.86, 20.12, 'Honestly? My favorite\npart of the night!')]
F = os.path.expanduser('~/Library/Fonts/FoundersGrotesk')
fs = lambda s: ImageFont.truetype(F + '-Semibold.otf', s); fbd = lambda s: ImageFont.truetype(F + '-Bold.otf', s)
IN = 'in_color_matrix=bt709:in_range=tv'
def grab(src, s0, dur, vf):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(s0), '-t', str(dur + 0.2), '-i', src, '-vf', f'{vf},fps={FPS},scale={W}:{H}:{IN}:flags=lanczos,format=rgb24',
                          '-f', 'rawvideo', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
# Polen frames, one array per output frame
total = int(round(END * FPS))
hail = []
for a, b, s, up, _ in HK:
    n = int(round(b * FPS)) - int(round(a * FPS)); fr = grab(HSRC, s, n / FPS, f'crop=iw:ih-{up}:0:{up},pad=iw:ih+{up}:0:0' if up else 'null'); hail += [fr[min(k, len(fr) - 1)] for k in range(n)]
# product cut-outs in the middle, like the reference (user 2026-11-10): real DropOff front PNG + steel gua sha PNG
PP = os.path.join(R, '..', '..', 'Products', 'png')
def _cut(f, h=None, w=None, rot=0):
    im = Image.open(os.path.join(PP, f)).convert('RGBA'); im = im.crop(im.getbbox())
    im = im.resize((int(im.width * h / im.height), h) if h else (w, int(im.height * w / im.width)), Image.LANCZOS)
    return im.rotate(rot, Image.BICUBIC, expand=True)
_do = _cut('ERH_7488.png', h=470)                      # user 2026-11-10: only DropOff, cleaner shadow
_sh = Image.new('RGBA', (_do.width + 80, _do.height + 80), (0, 0, 0, 0))
_m = Image.new('L', _sh.size, 0); _m.paste(_do.getchannel('A').point(lambda v: int(v * 0.28)), (40 + 6, 40 + 12))
_sh.putalpha(_m.filter(ImageFilter.GaussianBlur(9)))
PRODS = _sh.copy(); PRODS.alpha_composite(_do, (40, 40))
ease = lambda p: 1 - (1 - min(max(p, 0), 1)) ** 3
def box(im, text, y):
    """white label box(es) centred on the seam; one box per line, like the reference"""
    d = ImageDraw.Draw(im); f = fbd(58); pad = 20; lines = text.split('\n'); lh = 86
    y = y - (len(lines) - 1) * lh / 2
    for k, ln in enumerate(lines):
        l, t, r, b = d.textbbox((0, 0), ln, font=f, anchor='lt'); x = (W - (r - l)) / 2; yy = y + k * lh
        d.rectangle([x - pad, yy - pad + t, x + (r - l) + pad, yy + b + pad], fill=(255, 255, 255)); d.text((x, yy), ln, font=f, fill=(10, 10, 10), anchor='lt')
def caption(im, t):
    tv = t - V0; d = ImageDraw.Draw(im)
    for a, b, s in LINES:
        if a - 0.05 <= tv < b + 0.25:
            f = fs(52); y = 1110
            sh = Image.new('L', im.size, 0); ImageDraw.Draw(sh).multiline_text((W / 2, y + 4), s, font=f, fill=200, anchor='ma', align='center', spacing=10)
            im.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(10)))
            d.multiline_text((W / 2, y), s, font=f, fill=(255, 255, 255), anchor='ma', align='center', spacing=10)
def frame(i, P):
    t = i / FPS
    if t >= G1: im = Image.fromarray(P)
    else:
        p = ease((t - G0) / (G1 - G0)) if t >= G0 else 0.0
        top = round(SEAM * (1 - p)); h = H - top                         # Polen panel: rows top..H
        c = 1250 + (960 - 1250) * p                                       # source centre line drifts to the middle
        y0 = int(np.clip(c - h / 2, 0, H - h)); im = Image.new('RGB', (W, H))
        Hf = hail[min(i, len(hail) - 1)]
        if top > 0: im.paste(Image.fromarray(Hf[SEAM - top:SEAM]), (0, 0))   # Hailey slides up with the seam
        im.paste(Image.fromarray(P[y0:y0 + h]), (0, top))
        a = 1 - min(max((t - G0) / 0.25, 0), 1)
        if a > 0:
            pr = PRODS if a >= 1 else PRODS.copy()
            if a < 1: pr.putalpha(PRODS.getchannel('A').point(lambda v: int(v * a)))
            im = im.convert('RGBA'); im.alpha_composite(pr, ((W - PRODS.width) // 2, SEAM + 70)); im = im.convert('RGB')
        if p == 0:
            box(im, next(x[4] for x in HK if x[0] <= t < x[1]) if t < HK[-1][1] else HK[-1][4], SEAM - 34)
    caption(im, t); return np.asarray(im)
out = os.path.join(R, f'hailey_noaudio_{VAR}.mp4')
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-vf', 'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p', '-c:v', 'libx264', '-crf', '17',
                        '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', out], stdin=subprocess.PIPE)
i = 0
for k, (t0, s0) in enumerate(SEG):                       # stream one segment at a time (16 GB machine)
    t1 = SEG[k + 1][0] if k + 1 < len(SEG) else END
    n = int(round(t1 * FPS)) - int(round(t0 * FPS)); fr = grab(PSRC, s0, n / FPS, 'hflip')
    for j in range(n): enc.stdin.write(frame(i, fr[min(j, len(fr) - 1)]).tobytes()); i += 1
    del fr
enc.stdin.close(); enc.wait(); print('frames', total, 'END', END)
