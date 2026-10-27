"""Batch 48 v3 (2026-10-16): B/A countdown where the photo is never covered or cropped.
User: "yazılardan görsel gözükmüyo … alttan kesik kalmış bacaklar … kesik görüntü sevmeyiz".
Square (1:1) B/A diptych with the whole subject inside the frame sits at the bottom, on a background that matches the photo's own backdrop.
Headline, stat and countdown sticker live above it on the same colour, never on top of the subject.
Usage: python render48v3.py [kind] [fmt]"""
import os, sys, subprocess
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..', '..'); C47 = os.path.join(ROOT, '_calisma', 'batch-47-characters')
FONTS = os.path.expanduser('~/Library/Fonts')
def font(style, size): return ImageFont.truetype(os.path.join(FONTS, f'FoundersGrotesk-{style}.otf'), size)
FPS, SECS = 30, 12
MAGENTA, INK, GREY = (169, 33, 192), (18, 14, 24), (95, 88, 104)
SIZES = {'story': (1080, 1920), 'feed': (1080, 1350), 'square': (1080, 1080)}
K = {
 'do': dict(src='ba3_do_full.png', top=0.09, head=('A MORE', 'SCULPTED BODY.'), stat='88%', label=('experienced reduced', 'cellulite & dimpling'), days=('DAY 0', 'DAY 56'), name='DropOff'),
 'ss': dict(src='ba3_ss_full.png', head=('CHISEL YOUR', 'JAWLINE.'), stat='92%', label=('saw a more', 'sculpted jawline'), days=('DAY 0', 'DAY 14'), name='ShapeShift'),
 'pc': dict(src='ba3_pc_macro.png', head=('STRONGER,', 'FULLER-LOOKING HAIR.'), stat='29%', label=('average increase in', 'hair thickness'), days=('DAY 0', 'DAY 14'), name='PowerCycle'),
 'nw': dict(src='ba3_nw_ama.png', head=('REVEAL', 'YOUR GLOW.'), stat='90%', label=('saw a visibly', 'brighter complexion'), days=('DAY 0', 'DAY 14'), name='NetWork'),
}
# logo_y, logo_w, head_y, head_size, row_y, img_size, img_y
L = {'story':  dict(logo_y=190, logo_w=360, head_y=280, hs=96, row_y=500, img_y=860, side=0, bottom=0),
     'feed':   dict(logo_y=46, logo_w=270, head_y=104, hs=74, row_y=215, img_y=500, side=0, bottom=0),
     'square': dict(logo_y=34, logo_w=240, head_y=84, hs=62, row_y=165, img_y=410, side=0, bottom=0)}

def logo(w):
    lg = Image.open(os.path.join(ROOT, '_calisma', 'video-01-bcrf', 'assets', 'logo.png')).convert('RGBA')
    return lg.resize((w, round(lg.height * w / lg.width)), Image.LANCZOS)

def pill(img, cx, cy, s, bg, fg=(255, 255, 255), size=32):
    d = ImageDraw.Draw(img); f = font('Semibold', size)
    l, t, r, b = d.textbbox((0, 0), s, font=f, anchor='mm'); w, h = r - l + 48, b - t + 24
    d.rounded_rectangle((cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2), radius=h / 2, fill=bg)
    d.text((cx, cy), s, font=f, fill=fg, anchor='mm')

def sticker(sec, blink, scale=1.0):
    W, H = round(430 * scale), round(250 * scale); pad = 30
    s = Image.new('RGBA', (W + 2 * pad, H + 2 * pad), (0, 0, 0, 0)); d = ImageDraw.Draw(s)
    d.rounded_rectangle((pad, pad + 6, pad + W, pad + H + 6), radius=34 * scale, fill=(0, 0, 0, 40))
    d.rounded_rectangle((pad, pad, pad + W, pad + H), radius=34 * scale, fill=INK)
    d.text((pad + W / 2, pad + 62 * scale), '15% OFF', font=font('Bold', round(72 * scale)), fill=(255, 255, 255), anchor='mm')
    d.text((pad + W / 2, pad + 118 * scale), 'FIRST ORDER · ENDS IN' if scale >= 1 else 'ENDS IN', font=font('Semibold', 32), fill=(215, 190, 230), anchor='mm')
    d.text((pad + W / 2, pad + 190 * scale), f'00{":" if blink else " "}{sec:02d}', font=font('Bold', round(84 * scale)), fill=MAGENTA, anchor='mm')
    return s.rotate(3, resample=Image.BICUBIC, expand=True)

def base(kind, fmt):
    k, l = K[kind], L[fmt]; W, H = SIZES[fmt]
    ph = Image.open(os.path.join(C47, k['src'])).convert('RGB')
    if k.get('top'): ph = ph.crop((0, round(ph.height * k['top']), ph.width, ph.height))  # body shots start at the waist, like the brand's own B/A
    # backdrop colour = the photo's own top corners (studio paper), so the page and photo are one surface
    top = ph.crop((0, 0, ph.width, 6)).getdata()
    paper = [px for px in top if sum(px) > 600] or list(top)                       # studio paper pixels on the top edge (skip hair/skin)
    bg = tuple(sum(c[i] for c in paper) // len(paper) for i in range(3))
    # FIT the whole photo (never crop): largest size that fits the box under the copy block
    box_w, box_h = W - 2 * l['side'], H - l['img_y'] - l['bottom']
    # does the subject touch the photo's left/right edges? (then we cannot blend the sides: span the full width instead)
    cols = [ph.getpixel((x, y)) for x in (1, ph.width - 2) for y in range(0, ph.height, 8)]
    touches = sum(1 for c in cols if sum(c) < 600) / len(cols) > 0.08
    sc = (W / ph.width) if touches else min(box_w / ph.width, box_h / ph.height)
    pw, phh = round(ph.width * sc), round(ph.height * sc)
    ph = ph.resize((pw, phh), Image.LANCZOS); px = (W - pw) // 2
    py0 = l['img_y'] if touches else H - l['bottom'] - phh   # portrait spans the width from the top of the photo area; it ends at the chest below the frame
    img = Image.new('RGBA', (W, H), bg + (255,))
    if pw < W:   # page colour per row = the photo's own backdrop at its left/right edge, so the photo sits on one continuous paper (no box edge)
        from PIL import ImageFilter
        edge = Image.new('RGB', (1, phh))
        for yy in range(phh):
            a, b = ph.getpixel((2, yy)), ph.getpixel((pw - 3, yy)); edge.putpixel((0, yy), tuple((x + y) // 2 for x, y in zip(a, b)))
        edge = edge.filter(ImageFilter.BoxBlur(6)).resize((W, phh))
        img.paste(edge, (0, py0))
        ramp = Image.new('RGBA', (W, 120)); top = edge.getpixel((0, 0))
        for yy in range(120): ImageDraw.Draw(ramp).line((0, yy, W, yy), fill=tuple(round(bg[i] + (top[i] - bg[i]) * yy / 119) for i in range(3)) + (255,))
        img.alpha_composite(ramp, (0, max(0, py0 - 120)))
    img.paste(ph, (px, py0))
    l = dict(l, img=pw, img_x=px, img_top=py0)
    lg = logo(l['logo_w']); img.alpha_composite(lg, ((W - lg.width) // 2, l['logo_y']))
    d = ImageDraw.Draw(img); fh = font('Bold', l['hs']); y = l['head_y']
    lines = k['head'] if fmt == 'story' else (' '.join(k['head']),)
    for ln in lines: d.text((W / 2, y), ln, font=fh, fill=INK, anchor='mt'); y += round(l['hs'] * 0.98)
    ry = l['row_y'] if fmt != 'story' else max(l['row_y'], y + 30)
    fs = {'story': 130, 'feed': 104, 'square': 88}[fmt]
    d.text((70, ry), k['stat'], font=font('Bold', fs), fill=MAGENTA, anchor='lt')
    ly = ry + round(fs * 0.98)
    for ln in k['label']: d.text((74, ly), ln, font=font('Medium', 34), fill=GREY, anchor='lt'); ly += 40
    hw = l['img'] / 2; x0 = l['img_x']
    py = l['img_top'] - 34
    pill(img, x0 + hw / 2, py, k['days'][0], INK); pill(img, x0 + hw * 1.5, py, k['days'][1], MAGENTA)
    d.text((W / 2, H - 18), 'Simulated results.', font=font('Regular', 20), fill=GREY, anchor='mb')
    return img, ry

def render(kind, fmt, preview_only=False):
    b, ry = base(kind, fmt); W, H = b.size; sc = {'story': 1.0, 'feed': 0.82, 'square': 0.7}[fmt]
    def frame(sec, blink):
        f = b.copy(); st = sticker(sec, blink, sc); f.alpha_composite(st, (W - st.width - 30, ry - 24)); return f
    frame(59, True).convert('RGB').save(os.path.join(HERE, f'v3_{kind}_{fmt}_preview.jpg'), quality=88)
    if preview_only: return
    out = os.path.join(HERE, f"{K[kind]['name']} – Countdown v3 Before-After – {fmt}.mp4")
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    for s in range(SECS):
        for half in (True, False):
            raw = frame(59 - s, half).convert('RGB').tobytes()
            for _ in range(FPS // 2): p.stdin.write(raw)
    p.stdin.close(); p.wait(); print('ok', out)

if __name__ == '__main__':
    kinds = [sys.argv[1]] if len(sys.argv) > 1 else list(K)
    fmts = [sys.argv[2]] if len(sys.argv) > 2 else ['story', 'feed', 'square']
    for kd in kinds:
        if not os.path.exists(os.path.join(C47, K[kd]['src'])): print('missing source', K[kd]['src']); continue
        for f in fmts: render(kd, f)
