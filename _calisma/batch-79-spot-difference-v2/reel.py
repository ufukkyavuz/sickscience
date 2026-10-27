"""Batch 79 — 'Farkı bul' v2: selfie background (Veo clip or still), reference-style white overlay text,
white card with two cartoon images (the one difference = the product result), soft card pop at 0.3 s,
reveal circle at 7 s. Usage: ~/motion-tools/.venv/bin/python reel.py <key> [--still]   (keys in spec.json)
Also writes still parts for Figma: out/<key>_card.png (card with shadow) and out/bg_still.png."""
import sys, os, json, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, DUR = 1080, 1920, 24, 10.0
FD = os.path.expanduser('~/sickscience-work/opuscar/ss-swiss/fonts/FoundersGrotesk-%s.otf')
font = lambda w, s: ImageFont.truetype(FD % w, s)
SPEC = json.load(open(os.path.join(HERE, 'spec.json')))

# background: zoom 1.3 and lift the face so the text + card sit on the calm sweater/sofa area
BG_Z, BG_X0, BG_Y0 = 1.3, 0.065, 0.22
T_Y = 253                         # first text line top
CARD = (78, 514, 1002, None)     # x0, y0, x1 (height from the 2:3 cells)
PAD, DIV, REVEAL = 14, 3, 7.0

def ease_out_back(x, s=1.4):
    x = min(1, max(0, x)); x -= 1; return 1 + x * x * ((s + 1) * x + s)

def ease(x):
    x = min(1, max(0, x)); return x * x * (3 - 2 * x)

def bg_crop(im, push=0.0):
    sw, sh = im.size; z = BG_Z * (1 + push); cw, ch = sw / z, sh / z
    cx = sw * (BG_X0 + 0.5 / BG_Z); cy = sh * (BG_Y0 + 0.5 / BG_Z)
    x0 = min(max(0, cx - cw / 2), sw - cw); y0 = min(max(0, cy - ch / 2), sh - ch)
    base = im.resize((W, H), Image.LANCZOS, box=(x0, y0, x0 + cw, y0 + ch))
    # user's Figma Story: Photo 1242x2208 at (-81,-288) over the 1080x1920 base crop
    return base.resize((W, H), Image.LANCZOS, box=(81 / 1.15, 288 / 1.15, (81 + W) / 1.15, (288 + H) / 1.15))

def bg_frames(n, clip=None):
    if clip:
        raw = subprocess.run(['ffmpeg', '-loglevel', 'error', '-i', clip, '-vf', f'fps={FPS}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'],
                             capture_output=True, check=True).stdout
        pr = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v', '-show_entries', 'stream=width,height', '-of', 'json', clip],
                                       capture_output=True).stdout)['streams'][0]
        cw, chh = pr['width'], pr['height']; fs = len(raw) // (cw * chh * 3)
        for i in range(n):
            k = min(i, fs - 1)   # hold the last frame if the clip is shorter
            yield bg_crop(Image.frombuffer('RGB', (cw, chh), raw[k * cw * chh * 3:(k + 1) * cw * chh * 3]), 0.03 * i / n)
    else:
        im = Image.open(os.path.join(HERE, 'selfie.png')).convert('RGB')
        for i in range(n): yield bg_crop(im, 0.05 * i / n)

def shadow_text(img, cx, y, s, f, a=1.0):
    d = ImageDraw.Draw(img); bb = d.textbbox((0, 0), s, font=f); x = cx - (bb[2] - bb[0]) // 2 - bb[0]
    sh = Image.new('RGBA', img.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).text((x + 2, y + 3), s, font=f, fill=(0, 0, 0, int(140 * a)))
    img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(5))); ImageDraw.Draw(img).text((x, y), s, font=f, fill=(255, 255, 255, int(255 * a)))

def cell_crop(im, c):
    iw, ih = im.size; w = c[2] * iw; h = min(ih, w * 1.5); w = h / 1.5
    x0 = min(max(0, c[0] * iw - w / 2), iw - w); y0 = min(max(0, c[1] * ih - h / 2), ih - h)
    return (x0, y0, x0 + w, y0 + h)

def build_card(sp):
    x0, y0, x1, _ = CARD; cw = x1 - x0
    cellw = (cw - 2 * PAD - DIV) // 2; cellh = int(cellw * 1.5); chh = cellh + 2 * PAD
    card = Image.new('RGBA', (cw, chh), (255, 255, 255, 255))
    L, R = [Image.open(os.path.join(HERE, sp[k])).convert('RGB') for k in ('left', 'right')]
    box = cell_crop(L, sp['crop'])
    for k, im in enumerate([L, R]):
        card.paste(im.resize((cellw, cellh), Image.LANCZOS, box=box), (PAD + k * (cellw + DIV), PAD))
    ImageDraw.Draw(card).rectangle([PAD + cellw, PAD, PAD + cellw + DIV - 1, chh - PAD], fill=(60, 60, 70, 255))
    # reveal circle centre (card coords, right cell)
    bx0, by0, bx1, by1 = sp['diff']; iw, ih = R.size; s = cellw / (box[2] - box[0])
    rcx = PAD + cellw + DIV + ((bx0 + bx1) / 2 * iw - box[0]) * s; rcy = PAD + ((by0 + by1) / 2 * ih - box[1]) * s
    rr = max((bx1 - bx0) * iw, (by1 - by0) * ih) * s * 0.62 + 12
    return card, (rcx, rcy, rr)

def draw_circle(card, circ, q):
    rcx, rcy, rr = circ
    ImageDraw.Draw(card).arc([rcx - rr, rcy - rr, rcx + rr, rcy + rr], -90, -90 + 360 * q, fill=(169, 33, 192, 255), width=7)

def darken():
    # vertical black gradient: light at the top (eyes), ~40 % behind the text, card and bottom
    return Image.new('RGBA', (W, H), (0, 0, 0, 128))   # user's Figma 'Darken': solid black 50 %
DARK = None

def compose(fr, t, sp, card, circ):
    global DARK
    DARK = DARK or darken(); fr.alpha_composite(DARK)
    f1, f2, f3, f4 = font('Bold', 64), font('Semibold', 48), font('Semibold', 38), font('Regular', 22)
    shadow_text(fr, W // 2, T_Y, 'How sharp are you?', f1)
    shadow_text(fr, W // 2, 344, "What's the 1 difference", f2)
    shadow_text(fr, W // 2, 399, 'between these 2 images?', f2)
    cy0 = CARD[1]; cw, chh = card.size
    if t >= 0.3:
        sc = ease_out_back((t - 0.3) / 0.35); c = card.copy()
        if t >= REVEAL: draw_circle(c, circ, ease((t - REVEAL) / 0.6))
        tw, th = max(1, int(cw * (0.9 + 0.1 * sc))), max(1, int(chh * (0.9 + 0.1 * sc)))
        cs = c.resize((tw, th), Image.LANCZOS); a = min(1.0, (t - 0.3) / 0.15)
        if a < 1: cs.putalpha(cs.getchannel('A').point(lambda v: int(v * a)))
        sh = Image.new('RGBA', (tw + 80, th + 80), (0, 0, 0, 0)); ImageDraw.Draw(sh).rectangle([40, 50, tw + 40, th + 50], fill=(0, 0, 0, int(80 * a)))
        sh = sh.filter(ImageFilter.GaussianBlur(18)); cx, cyc = W // 2, cy0 + chh // 2
        fr.alpha_composite(sh, (cx - tw // 2 - 40, cyc - th // 2 - 40)); fr.alpha_composite(cs, (cx - tw // 2, cyc - th // 2))
        shadow_text(fr, W // 2, 1287, sp['line'], f3, a)
    if t >= REVEAL + 0.3:
        shadow_text(fr, W // 2, 1339, sp['found'], f3, ease((t - REVEAL - 0.3) / 0.4))
    return fr

def main(key, clip):
    sp = SPEC[key]; card, circ = build_card(sp); n = int(DUR * FPS)
    os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
    c2 = card.copy(); c2.save(os.path.join(HERE, 'out', key + '_card.png'))
    draw_circle(c2, circ, 1.0); c2.save(os.path.join(HERE, 'out', key + '_card_found.png'))
    vid = os.path.join(HERE, 'out', key + '_v.mp4')
    p = subprocess.Popen(['ffmpeg', '-loglevel', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p', vid], stdin=subprocess.PIPE)
    for i, bg in enumerate(bg_frames(n, clip)):
        fr = compose(bg.convert('RGBA'), i / FPS, sp, card, circ)
        if i in (12, int(5 * FPS), int(9 * FPS)): fr.convert('RGB').save(os.path.join(HERE, 'out', f'{key}_f{i}.png'))
        p.stdin.write(fr.convert('RGB').tobytes())
    p.stdin.close(); p.wait()
    final = os.path.join(HERE, 'out', key + '.mp4')
    subprocess.run(['ffmpeg', '-loglevel', 'error', '-y', '-i', vid, '-i', os.path.join(HERE, 'music.wav'), '-map', '0:v', '-map', '1:a',
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', final], check=True)
    print(final)

if __name__ == '__main__':
    clip = os.path.join(HERE, 'clips', 'selfie_loop.mp4')
    main(sys.argv[1], None if '--still' in sys.argv or not os.path.exists(clip) else clip)
