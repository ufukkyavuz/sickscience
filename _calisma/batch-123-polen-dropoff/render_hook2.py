# Polen x DropOff, two structurally different hooks (user 2026-11-10: "daha farklı hook dene, biri çalışmazsa diğeri çalışsın,
# hepsi aynı neredeyse; ilk videoya dokunma"). The split-screen original (render_hailey.py VAR=A short) stays untouched.
#   MODE=B  greenscreen / stitch: Polen full screen from frame 0, Hailey talks from a floating card above her, card flies off.
#   MODE=C  question hook: big "OVERRATED OR UNDERRATED?" over Polen's massage, hard cut to full-screen Hailey "Totally
#           underrated.", hard cut back to Polen who starts talking.
# Same Polen VO (cloned voice, approved), same captions, explicit BT.709 in/out.
import json, os, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(R, 'render_hailey.py')).read()
g = {'__file__': os.path.join(R, 'render_hailey.py')}
exec(src[:src.index('def frame(i, P):')], g)               # grab, box, caption fonts, PRODS ... (VAR=A config)
MODE = os.environ.get('MODE', 'B')
W, H, FPS = 1080, 1920, 30
grab, box, fbd, fs = g['grab'], g['box'], g['fbd'], g['fs']
PSRC, HSRC = g['PSRC'], g['HSRC']
HK = [(0.0, 2.30, 90.55, 'Lymphatic drainage massages'), (2.30, 3.40, 93.15, 'Totally underrated.')]
HEND = 3.40; V0 = 3.55; VOD = 20.53; END = round(V0 + VOD + 0.35, 2); TS = g['TS']
g['V0'] = V0
LINES = g['LINES']
def caption(im, t):
    tv = t - V0; d = ImageDraw.Draw(im)
    for a, b, s in LINES:
        if a - 0.05 <= tv < b + 0.25:
            f = fs(52); y = 1110
            sh = Image.new('L', im.size, 0); ImageDraw.Draw(sh).multiline_text((W / 2, y + 4), s, font=f, fill=200, anchor='ma', align='center', spacing=10)
            im.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(10)))
            d.multiline_text((W / 2, y), s, font=f, fill=(255, 255, 255), anchor='ma', align='center', spacing=10)
if MODE == 'B':
    SEG = [(0.0, 1.5), (V0 + TS[0] - 0.06, 15.5), (V0 + TS[1] - 0.06, 22.0), (V0 + TS[2] - 0.06, 63.0), (V0 + TS[3] - 0.06, 45.5), (V0 + TS[4] - 0.06, 96.0)]   # opens on Polen showing her kit
else:
    SEG = [(0.0, 61.0), (HEND, 1.5), (V0 + TS[0] - 0.06, 15.5), (V0 + TS[1] - 0.06, 22.0), (V0 + TS[2] - 0.06, 67.0), (V0 + TS[3] - 0.06, 45.5), (V0 + TS[4] - 0.06, 96.0)]
# Hailey frames
hail = []
for a, b, s, _ in HK:
    n = int(round(b * FPS)) - int(round(a * FPS)); fr = grab(HSRC, s, n / FPS, 'null'); hail += [fr[min(k, len(fr) - 1)] for k in range(n)]
ease = lambda p: 1 - (1 - min(max(p, 0), 1)) ** 3
def rounded(im, r):
    m = Image.new('L', im.size, 0); ImageDraw.Draw(m).rounded_rectangle([0, 0, im.width - 1, im.height - 1], r, fill=255); return m
CW, CH = 420, 400                                   # Hailey card (PiP, top-left, clear of Polen's face)
def card(Hf, i):
    """Hailey's face crop (piece 2 is framed lower in the source, lift it like piece 1)"""
    t = i / FPS; up = 0 if t < HK[1][0] else 220
    c = Image.fromarray(Hf).crop((60, 40 + up, 1020, 940 + up)).resize((CW, CH), Image.LANCZOS)
    out = Image.new('RGBA', (CW + 16, CH + 16), (255, 255, 255, 255)); out.putalpha(rounded(out, 40))
    c = c.convert('RGBA'); c.putalpha(rounded(c, 32)); out.alpha_composite(c, (8, 8)); return out
def title(im, t):
    """MODE C opening question, big, centred in the safe band"""
    d = ImageDraw.Draw(im); a = ease((t - 0.05) / 0.25)
    f1, f2 = fbd(150), fs(56)
    for k, (s, f, y) in enumerate((('OVERRATED', f1, 520), ('OR UNDERRATED?', fbd(118), 690), ('Lymphatic drainage massages', f2, 860))):
        p = ease((t - 0.05 - k * 0.12) / 0.25)
        if p <= 0: continue
        lay = Image.new('RGBA', im.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(lay)
        sh = Image.new('L', im.size, 0); ImageDraw.Draw(sh).text((W / 2, y + 6 + 30 * (1 - p)), s, font=f, fill=int(190 * p), anchor='ma')
        im.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(16)))
        col = (255, 255, 255) if k != 1 else (255, 255, 255)
        ld.text((W / 2, y + 30 * (1 - p)), s, font=f, fill=col + (int(255 * p),), anchor='ma')
        im.paste(lay, (0, 0), lay)
def frame(i, P):
    t = i / FPS; im = Image.fromarray(P)
    if MODE == 'B' and t < HEND + 0.4:
        Hf = hail[min(i, len(hail) - 1)]; cd = card(Hf, i)
        p = ease((t - HEND) / 0.4) if t >= HEND else 0
        x = int(60 - 700 * p); y = 280
        if p > 0: cd.putalpha(cd.getchannel('A').point(lambda v: int(v * (1 - p))))
        sh = Image.new('RGBA', im.size, (0, 0, 0, 0)); m = Image.new('L', im.size, 0); m.paste(cd.getchannel('A').point(lambda v: int(v * 0.35)), (x + 10, y + 18))
        sh.putalpha(m.filter(ImageFilter.GaussianBlur(18)))
        im = im.convert('RGBA'); im.alpha_composite(sh); im.alpha_composite(cd, (x, max(-cd.height, y))); im = im.convert('RGB')
        if p == 0:
            lab = next(h[3] for h in HK if h[0] <= t < h[1]) if t < HEND else HK[-1][3]
            d = ImageDraw.Draw(im); f = fbd(40); l, tt, r, b = d.textbbox((0, 0), lab, font=f, anchor='lt')
            d.rectangle([60, 280 + cd.height + 14, 60 + (r - l) + 32, 280 + cd.height + 14 + b + 24], fill=(255, 255, 255))
            d.text((76, 280 + cd.height + 26), lab, font=f, fill=(10, 10, 10), anchor='lt')
    if MODE == 'C':
        if HK[1][0] <= t < HEND:                                     # full-screen Hailey answer
            im = Image.fromarray(hail[min(i, len(hail) - 1)])      # her own burned subtitle reads 'Totally underrated.'
        elif t < HK[1][0]:
            title(im, t)
    caption(im, t); return np.asarray(im)
out = os.path.join(R, f'hook2_noaudio_{MODE}.mp4'); total = int(round(END * FPS))
enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                        '-vf', 'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p', '-c:v', 'libx264', '-crf', '17',
                        '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', out], stdin=subprocess.PIPE)
i = 0
for k, (t0, s0) in enumerate(SEG):
    t1 = SEG[k + 1][0] if k + 1 < len(SEG) else END
    n = int(round(t1 * FPS)) - int(round(t0 * FPS)); fr = grab(PSRC, s0, n / FPS, 'hflip')
    for j in range(n): enc.stdin.write(frame(i, fr[min(j, len(fr) - 1)]).tobytes()); i += 1
    del fr
enc.stdin.close(); enc.wait(); print('frames', i, 'END', END)
