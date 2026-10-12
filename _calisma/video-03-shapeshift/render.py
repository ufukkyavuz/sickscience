"""Video 03 — ShapeShift product video (9:16, 1080x1920, 30 fps).
Clips: Veo 3.1 Fast image-to-video (Google Flow) from Higgsfield Unlimited start frames. VO: ElevenLabs (Sara), sped up 1.12x.
Text = site copy only (PDP): name, descriptor, ingredients, how to use, Real Results stat, award, price."""
import os, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import imageio_ffmpeg

HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
W, H, FPS = 1080, 1920, 30
FD = os.path.expanduser('~/Library/Fonts/')
XC, REG, MED, SEMI = FD + 'FoundersGroteskXCond-Bold.otf', FD + 'FoundersGrotesk-Regular.otf', FD + 'FoundersGrotesk-Medium.otf', FD + 'FoundersGrotesk-Semibold.otf'
INK, VIOLET, WHITE = (20, 20, 20), (115, 0, 199), (255, 255, 255)
ff = imageio_ffmpeg.get_ffmpeg_exe()
F = lambda p, s: ImageFont.truetype(p, s)

def read_clip(path):
    r = imageio_ffmpeg.read_frames(path, output_params=['-vf', f'scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}', '-r', str(FPS)])
    meta = next(r); return [np.frombuffer(f, np.uint8).reshape(H, W, 3) for f in r]

def still(path):
    im = Image.open(path).convert('RGB'); im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
    return np.array(im.crop((0, 0, W, H)))

clips = {k: read_clip(os.path.join(HERE, 'clips', k + '.mp4')) for k in ['hook', 'dispense', 'apply']}
hero = still(os.path.join(HERE, 'frames', 'hero.png'))
logo = Image.open(os.path.join(HERE, '..', 'video-01-bcrf', 'assets', 'logo.png')).convert('RGBA')
LOGO_S = logo.resize((320, round(logo.height * 320 / logo.width)), Image.LANCZOS)

# (start, end, source, source_offset_seconds, overlays)
SH = [
 (0.00, 2.55, 'hook', 0.4, [('head', ['CHISEL YOUR', 'JAWLINE IN 2 WEEKS.'], 300)]),
 (2.55, 6.40, 'dispense', 0.0, [('name', 'ShapeShift', 'V-Line Jaw Defining Serum', 300)]),
 (6.40, 12.60, 'hero', 0.0, [('list', 'KEY INGREDIENTS', ['NX35™ Sculpt Technology', '(Pineapple Exosomes)', 'Caffeine', 'Niacinamide (Vitamin B3)'], 262)]),
 (12.60, 16.85, 'apply', 0.3, [('chip', '1–2 PUMPS · UPWARD · TWICE DAILY', 300)]),
 (16.85, 20.15, 'hook', 4.0, [('stat', '92%', 'saw a more sculpted jawline', 262)]),
 (20.15, 25.60, 'hero', 0.0, [('end', None, None, 0)]),
]
XF = 0.25

def ease(x): return 1 - (1 - max(0.0, min(1.0, x))) ** 3

def frame_of(src, t, offset, dur):
    if src == 'hero':
        z = 1.0 + 0.05 * (t / dur); im = Image.fromarray(hero)
        cw, ch = W / z, H / z; x0, y0 = (W - cw) / 2, 0
        return im.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch))).resize((W, H), Image.LANCZOS)
    fr = clips[src]; i = min(len(fr) - 1, int((offset + t) * FPS))
    return Image.fromarray(fr[i])

def scrim(img, y0, y1, a=150):
    lay = Image.new('RGBA', img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    for y in range(y0, y1):
        k = 1 - abs((y - (y0 + y1) / 2) / ((y1 - y0) / 2)); d.line([(0, y), (W, y)], fill=(255, 255, 255, int(a * min(1, k * 1.6))))
    img.alpha_composite(lay)

def ctext(d, y, s, f, fill):
    w = d.textlength(s, font=f); d.text(((W - w) / 2, y), s, font=f, fill=fill)

def overlay(img, ov, t):
    a = ease((t - 0.1) / 0.4); A = int(255 * a); dy = int((1 - a) * 20)
    kind = ov[0]
    if kind == 'end':
        lay = Image.new('RGBA', img.size, (0, 0, 0, 0)); img.alpha_composite(lay)
        pass
        l = logo.resize((520, round(logo.height * 520 / logo.width)), Image.LANCZOS)
        if a < 1: l.putalpha(l.getchannel('A').point(lambda v: int(v * a)))
        img.alpha_composite(l, ((W - 520) // 2, 190 + dy))
        d = ImageDraw.Draw(img); ctext(d, 280 + dy, 'ShapeShift  $64', F(XC, 140), INK + (A,))
        a2 = ease((t - 0.6) / 0.5); A2 = int(255 * a2)
        ctext(d, 428, '2024 REAL SIMPLE Award Winner', F(SEMI, 40), VIOLET + (A2,))
        ctext(d, 476, 'Best Jawline & Neck Treatment', F(REG, 40), INK + (A2,))
        ctext(d, 530, 'SickScienceLabs.com', F(MED, 40), INK + (A2,))
        return
    d = ImageDraw.Draw(img)
    if kind == 'head':
        scrim(img, 230, 600, 170); f = F(XC, 130)
        for i, l in enumerate(ov[1]): ctext(d, ov[2] + i * 118 + dy, l, f, (INK if i == 0 else VIOLET) + (A,))
    elif kind == 'name':
        scrim(img, 240, 560, 120); ctext(d, ov[3] + dy, ov[1], F(XC, 170), INK + (A,)); ctext(d, ov[3] + 175 + dy, ov[2], F(REG, 48), INK + (A,))
    elif kind == 'list':
        ctext(d, ov[3] + dy, ov[1], F(SEMI, 40), VIOLET + (A,))
        for i, l in enumerate(ov[2]):
            ai = int(255 * ease((t - 0.5 - i * 0.6) / 0.4)); ctext(d, ov[3] + 58 + i * 58, l, F(MED if not l.startswith('(') else REG, 48), INK + (ai,))
    elif kind == 'chip':
        f = F(SEMI, 38); w = d.textlength(ov[1], font=f) + 64
        lay = Image.new('RGBA', img.size, (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
        dl.rounded_rectangle(((W - w) / 2, ov[2] + dy, (W + w) / 2, ov[2] + 76 + dy), 38, fill=(255, 255, 255, int(225 * a)))
        img.alpha_composite(lay); d = ImageDraw.Draw(img); ctext(d, ov[2] + 18 + dy, ov[1], f, INK + (A,))
    elif kind == 'stat':
        scrim(img, 230, 580, 190); ctext(d, ov[3] + dy, ov[1], F(XC, 220), VIOLET + (A,)); ctext(d, ov[3] + 215 + dy, ov[2], F(MED, 52), INK + (A,))

def render(t):
    for j, (s, e, src, off, ovs) in enumerate(SH):
        if s <= t < e: break
    lt = t - s; img = frame_of(src, lt, off, e - s).convert('RGBA')
    if ovs[0][0] != 'end': img.alpha_composite(LOGO_S, ((W - 320) // 2, 182))
    for ov in ovs: overlay(img, ov, lt)
    if j + 1 < len(SH) and t > e - XF:
        s2, e2, src2, off2, ovs2 = SH[j + 1]; nxt = frame_of(src2, 0, off2, e2 - s2).convert('RGBA')
        img = Image.blend(img, nxt, ease((t - (e - XF)) / XF))
    return img.convert('RGB')

total = SH[-1][1]
vo = os.path.join(HERE, 'vo_fast.mp3')
subprocess.run([ff, '-y', '-i', os.path.join(HERE, 'vo_raw.mp3'), '-filter:a', 'atempo=1.12', vo], stderr=subprocess.DEVNULL)
silent = os.path.join(OUT, 'silent.mp4')
p = subprocess.Popen([ff, '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-c:v', 'libx264',
                      '-pix_fmt', 'yuv420p', '-crf', '18', silent], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
for n in range(int(total * FPS)): p.stdin.write(render(n / FPS).tobytes())
p.stdin.close(); p.wait()
subprocess.run([ff, '-y', '-i', silent, '-i', vo, '-filter_complex', '[1:a]apad[a]', '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac',
                '-b:a', '192k', '-t', str(total), os.path.join(OUT, 'ShapeShift_video_9x16.mp4')], stderr=subprocess.DEVNULL)
print('done', total)
