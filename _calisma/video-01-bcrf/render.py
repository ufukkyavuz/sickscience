"""Video 01 — NetWork × BCRF pilot (9:16, 1080x1920, 30 fps).
Free pipeline: Higgsfield Unlimited stills + local motion/typography (PIL) + ffmpeg mux. Voiceover: ElevenLabs (vo.mp3).
usage: python render.py [timings.json]   -> out/video-01.mp4 (with vo.mp3 if present)"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import imageio_ffmpeg

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
SS = os.path.abspath(os.path.join(HERE, '..'))
W, H, FPS = 1080, 1920, 30
FD = os.path.expanduser('~/Library/Fonts/')
F_XC = FD + 'FoundersGroteskXCond-Bold.otf'
F_REG = FD + 'FoundersGrotesk-Regular.otf'
F_MED = FD + 'FoundersGrotesk-Medium.otf'
F_SEMI = FD + 'FoundersGrotesk-Semibold.otf'
INK = (20, 20, 20); ROSE = (199, 36, 92); WHITE = (255, 255, 255)

def font(p, s): return ImageFont.truetype(p, s)

# ---------- scenes ----------
T = json.load(open(sys.argv[1])) if len(sys.argv) > 1 else {
    'phone': 3.6, 'set': 3.0, 'pair': 2.8, 'donation': 6.0, 'end': 2.6}
XF = 0.35  # crossfade

def photo(path, offset_y=0, fill=None):
    im = Image.open(path).convert('RGB')
    im = im.resize((W, round(im.height * W / im.width)), Image.LANCZOS)
    base = Image.new('RGB', (W, H), fill or im.getpixel((W // 2, 4)))
    base.paste(im, (0, offset_y))
    return base

def lockscreen(base, cx=412, time_y=760, card_y=920, card_w=316):
    d = ImageDraw.Draw(base, 'RGBA')
    t = '8:14'; f = font(F_MED, 120); w = d.textlength(t, font=f)
    d.text((cx - w / 2, time_y), t, font=f, fill=(255, 255, 255, 242))
    x0 = cx - card_w / 2; card_h = 162
    d.rounded_rectangle((x0, card_y, x0 + card_w, card_y + card_h), 26, fill=(245, 240, 242, 225))
    g = (115, 107, 112)
    d.text((x0 + 20, card_y + 16), 'REMINDERS', font=font(F_MED, 32), fill=g)
    nw = d.textlength('now', font=font(F_REG, 32)); d.text((x0 + card_w - 20 - nw, card_y + 16), 'now', font=font(F_REG, 32), fill=g)
    d.text((x0 + 20, card_y + 58), 'Monthly self-check', font=font(F_SEMI, 32), fill=INK)
    d.text((x0 + 20, card_y + 100), 'Today', font=font(F_REG, 32), fill=(64, 61, 64))
    return base

P13 = os.path.join(SS, 'batch-13-bcrf-selfcheck'); P15 = os.path.join(SS, 'batch-15-bcrf-xray-pair')
logo = Image.open(os.path.join(HERE, 'assets', 'logo.png')).convert('RGBA')
prod = Image.open(os.path.join(SS, '..', 'Products', 'png', 'fixed', 'network-product-517x1600.png')).convert('RGBA')

SCENES = [
 dict(k='phone', base=lambda: photo(os.path.join(P13, 'phone.png')), zoom=(1.0, 1.05), focus=(540, 980),
      head=['ADD ONE STEP', 'TO YOUR ROUTINE.'], head_y=290, logo=True, lock_at=0.5),
 dict(k='set', base=lambda: photo(os.path.join(P13, 'set2_story.png'), 200, (221, 221, 222)), zoom=(1.0, 1.06), focus=(560, 1000),
      head=['THE MONTHLY', 'SELF-CHECK.'], head_y=290),
 dict(k='pair', base=lambda: photo(os.path.join(P15, 'pair_a.png')), zoom=(1.04, 1.0), focus=(540, 970),
      head=['A PAIR WORTH', 'CHECKING.'], head_y=290),
 dict(k='donation', base=lambda: photo(os.path.join(P13, 'hand2.png')), zoom=(1.0, 1.05), focus=(540, 1200),
      big='20%', body='of NetWork sales on SickScienceLabs.com go to The Breast Cancer Research Foundation this October.', head_y=270),
 dict(k='end', base=None, zoom=(1.0, 1.0)),
]

def ease(x): return 1 - (1 - max(0, min(1, x))) ** 3

def fit_head(lines, size=124, maxw=960):
    f = font(F_XC, size); d = ImageDraw.Draw(Image.new('RGB', (1, 1)))
    w = max(d.textlength(l, font=f) for l in lines)
    if w > maxw: f = font(F_XC, int(size * maxw / w))
    return f

def draw_head(img, lines, y, a, f):
    lay = Image.new('RGBA', img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    lh = int(f.size * 0.92); dy = int((1 - a) * 24)
    for i, l in enumerate(lines):
        w = d.textlength(l, font=f); c = INK if i == 0 else ROSE
        d.text(((W - w) / 2, y + i * lh + dy), l, font=f, fill=c + (int(255 * a),))
    img.alpha_composite(lay)

def draw_logo(img, y, a, w=398):
    l = logo.resize((w, round(logo.height * w / logo.width)), Image.LANCZOS)
    if a < 1: l.putalpha(l.getchannel('A').point(lambda v: int(v * a)))
    img.alpha_composite(l, ((W - w) // 2, y))

def wrap(d, text, f, maxw):
    out, line = [], ''
    for wd in text.split():
        t = (line + ' ' + wd).strip()
        if d.textlength(t, font=f) <= maxw: line = t
        else: out.append(line); line = wd
    out.append(line); return out

CACHE = {}
def scene_frame(s, t, dur):
    if s['k'] == 'end':
        img = Image.new('RGBA', (W, H), (245, 225, 228, 255))
        a = ease(t / 0.5)
        draw_logo(img, 520, a, 620)
        p = prod.resize((230, round(prod.height * 230 / prod.width)), Image.LANCZOS)
        img.alpha_composite(p, ((W - 230) // 2, 680 + int((1 - a) * 30)))
        d = ImageDraw.Draw(img)
        for i, (txt, f) in enumerate([('NetWork Rich Concentrated Serum', font(F_MED, 44)), ('SickScienceLabs.com', font(F_REG, 40))]):
            w = d.textlength(txt, font=f); d.text(((W - w) / 2, 1430 + i * 60), txt, font=f, fill=INK + (int(255 * ease((t - 0.3) / 0.5)),))
        return img
    if s['k'] not in CACHE:
        b = s['base']()
        if s.get('lock_at') is not None: CACHE[s['k'] + '_lock'] = lockscreen(b.copy())
        CACHE[s['k']] = b
    base = CACHE[s['k']]
    if s.get('lock_at') is not None and t >= s['lock_at']:
        lk = CACHE[s['k'] + '_lock']; al = ease((t - s['lock_at']) / 0.35)
        base = Image.blend(base, lk, al)
    z0, z1 = s['zoom']; z = z0 + (z1 - z0) * (t / dur)
    fx, fy = s['focus']; cw, ch = W / z, H / z
    x0 = min(max(fx - cw / 2, 0), W - cw); y0 = min(max(fy - ch / 2, 0), H - ch)
    img = base.crop((round(x0), round(y0), round(x0 + cw), round(y0 + ch))).resize((W, H), Image.LANCZOS).convert('RGBA')
    a = ease((t - 0.15) / 0.45)
    if s.get('logo'): draw_logo(img, 190, a)
    if 'head' in s: draw_head(img, s['head'], s['head_y'], a, fit_head(s['head']))
    if 'big' in s:
        lay = Image.new('RGBA', img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
        fb = font(F_XC, 300); w = d.textlength(s['big'], font=fb)
        d.text(((W - w) / 2, s['head_y'] + int((1 - a) * 24)), s['big'], font=fb, fill=ROSE + (int(255 * a),))
        a2 = ease((t - 0.6) / 0.5); fr = font(F_REG, 44)
        for i, l in enumerate(wrap(d, s['body'], fr, 860)):
            w = d.textlength(l, font=fr); d.text(((W - w) / 2, s['head_y'] + 300 + i * 54 + int((1 - a2) * 16)), l, font=fr, fill=INK + (int(255 * a2),))
        img.alpha_composite(lay)
    return img

def frames():
    starts, t0 = [], 0.0
    for s in SCENES: starts.append(t0); t0 += T[s['k']]
    total = t0
    for n in range(int(total * FPS)):
        t = n / FPS
        i = max(j for j, st in enumerate(starts) if st <= t)
        s = SCENES[i]; lt = t - starts[i]
        img = scene_frame(s, lt, T[s['k']])
        if i + 1 < len(SCENES) and lt > T[s['k']] - XF:  # crossfade into next
            nxt = scene_frame(SCENES[i + 1], 0.0, T[SCENES[i + 1]['k']])
            img = Image.blend(img, nxt, ease((lt - (T[s['k']] - XF)) / XF))
        yield img.convert('RGB').tobytes()
    print('duration', round(total, 2))

ff = imageio_ffmpeg.get_ffmpeg_exe()
vo = os.path.join(HERE, 'vo.mp3')
silent = os.path.join(OUT, 'video-01-silent.mp4')
p = subprocess.Popen([ff, '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                      '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-preset', 'medium', silent], stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
for fr in frames(): p.stdin.write(fr)
p.stdin.close(); p.wait()
if os.path.exists(vo):
    subprocess.run([ff, '-y', '-i', silent, '-i', vo, '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest',
                    os.path.join(OUT, 'video-01.mp4')], stderr=subprocess.DEVNULL)
    print('muxed with vo')
print('done', silent)
