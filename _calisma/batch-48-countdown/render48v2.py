"""Batch 48 v2 (2026-10-16): 'cooler' before/after countdown layout.
Full-bleed side-by-side B/A, dark gradient bands, site headline + one site stat, dotted focus circles (like the PDP B/As),
DAY labels, tilted countdown sticker. Copy = PDP 'Real Results' wording only.
Usage: python render48v2.py [kind] [fmt]   kinds: do ss (pc nw once re-generated)"""
import os, sys, subprocess, math
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..', '..'); C47 = os.path.join(ROOT, '_calisma', 'batch-47-characters')
FONTS = os.path.expanduser('~/Library/Fonts')
def font(style, size): return ImageFont.truetype(os.path.join(FONTS, f'FoundersGrotesk-{style}.otf'), size)
FPS, SECS = 30, 12
MAGENTA, PURPLE, INK, WHITE = (169, 33, 192), (115, 0, 199), (16, 12, 22), (255, 255, 255)
SIZES = {'story': (1080, 1920), 'feed': (1080, 1350), 'square': (1080, 1080)}

# kind: source, headline, sub, stat, stat label, day labels, focus circle (x,y,r as fraction of one half: x of half width, y/r of full height)
K = {
 'do': dict(src='ba_do_zara.png', crop_top={'story': 0.08, 'feed': 0.20, 'square': 0.24}, head='A MORE\nSCULPTED BODY.', sub='Visible change in 2 weeks.',
            stat='88%', label='experienced reduced\ncellulite & dimpling', days=('DAY 0', 'DAY 56'), circle=(0.42, 0.49, 0.075), name='DropOff', sim=True),
 'ss': dict(src='ba2_ss_leila.png', crop_top={'story': 0.0, 'feed': 0.06, 'square': 0.10}, head='CHISEL YOUR\nJAWLINE.', sub='In 2 weeks.',
            stat='92%', label='saw a more\nsculpted jawline', days=('DAY 0', 'DAY 14'), circle=(0.55, 0.47, 0.10), name='ShapeShift', sim=True),
 'pc': dict(src='ba3_pc_macro.png', crop_top={'story': 0.0, 'feed': 0.05, 'square': 0.10}, head='STRONGER,\nFULLER-LOOKING HAIR.', sub='In 2 weeks.',
            stat='29%', label='average increase in\nhair thickness', days=('DAY 0', 'DAY 14'), circle=(0.5, 0.55, 0.12), name='PowerCycle', sim=True),
 'nw': dict(src='ba3_nw_ama.png', crop_top={'story': 0.0, 'feed': 0.05, 'square': 0.10}, head='REVEAL\nYOUR GLOW.', sub='In 2 weeks.',
            stat='90%', label='saw a visibly\nbrighter complexion', days=('DAY 0', 'DAY 14'), circle=(0.5, 0.5, 0.11), name='NetWork', sim=True),
}
# per-format layout: logo_y, logo_w, head_y, head_size, sub_gap, days_y, stat_y, sticker_cy, top_band, bottom_band_from
L = {'story':  dict(logo_y=190, logo_w=340, head_y=290, hs=104, days_y=780, stat_y=1000, st_cy=1095, top=820, bot=880),
     'feed':   dict(logo_y=54, logo_w=280, head_y=130, hs=96, days_y=560, stat_y=990, st_cy=1085, top=620, bot=820),
     'square': dict(logo_y=40, logo_w=260, head_y=104, hs=84, days_y=470, stat_y=780, st_cy=865, top=520, bot=640)}

def logo_white(w):
    lg = Image.open(os.path.join(ROOT, '_calisma', 'video-01-bcrf', 'assets', 'logo.png')).convert('RGBA'); px = lg.load()
    for y in range(lg.height):
        for x in range(lg.width):
            r, g, b, a = px[x, y]
            if a and max(r, g, b) < 90: px[x, y] = (255, 255, 255, a)
    return lg.resize((w, round(lg.height * w / lg.width)), Image.LANCZOS)

def grad(W, H, y0, y1, a0, a1, color=INK):
    g = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(g)
    for y in range(max(0, y0), min(H, y1)):
        t = (y - y0) / max(1, y1 - y0); d.line((0, y, W, y), fill=color + (round(255 * (a0 + (a1 - a0) * t)),))
    return g

def dotted_circle(img, cx, cy, r, dots=46, dr=5):
    d = ImageDraw.Draw(img)
    for k in range(dots):
        a = 2 * math.pi * k / dots; x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        d.ellipse((x - dr, y - dr, x + dr, y + dr), fill=WHITE)

def pill(img, cx, cy, s, bg, fg=WHITE, size=34):
    d = ImageDraw.Draw(img); f = font('Semibold', size)
    l, t, r, b = d.textbbox((0, 0), s, font=f, anchor='mm'); w, h = r - l + 52, b - t + 26
    d.rounded_rectangle((cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2), radius=h / 2, fill=bg)
    d.text((cx, cy), s, font=f, fill=fg, anchor='mm')

def sticker(sec, blink):
    W, H = 430, 250; s = Image.new('RGBA', (W + 60, H + 60), (0, 0, 0, 0)); d = ImageDraw.Draw(s)
    d.rounded_rectangle((30, 34, 30 + W, 34 + H), radius=34, fill=(0, 0, 0, 70))            # soft drop
    d.rounded_rectangle((30, 28, 30 + W, 28 + H), radius=34, fill=WHITE)
    d.text((30 + W / 2, 28 + 62), '15% OFF', font=font('Bold', 72), fill=MAGENTA, anchor='mm')
    d.text((30 + W / 2, 28 + 118), 'FIRST ORDER · ENDS IN', font=font('Semibold', 32), fill=(90, 80, 100), anchor='mm')
    t = f'00{":" if blink else " "}{sec:02d}'
    d.text((30 + W / 2, 28 + 190), t, font=font('Bold', 84), fill=INK, anchor='mm')
    return s.rotate(4, resample=Image.BICUBIC, expand=True)

def base(kind, fmt):
    k, l = K[kind], L[fmt]; W, H = SIZES[fmt]
    ph = Image.open(os.path.join(C47, k['src'])).convert('RGBA'); ct = k['crop_top'][fmt]
    ph = ph.crop((0, round(ph.height * ct), ph.width, ph.height)); sc = W / ph.width; ph = ph.resize((W, round(ph.height * sc)), Image.LANCZOS)
    img = Image.new('RGBA', (W, H), ph.crop((0, 0, W, 4)).convert('RGB').resize((1, 1)).getpixel((0, 0)) + (255,)); img.alpha_composite(ph, (0, 0))
    # focus circles, same spot in both halves
    hw = W / 2; fx, fy, fr = k['circle']; fy_px = (fy - ct) / (1 - ct) * ph.height; r = fr * ph.height
    if 0 < fy_px < H:
        for side in (0, 1): dotted_circle(img, side * hw + fx * hw, fy_px, r)
    img.alpha_composite(grad(W, H, 0, l['top'], 0.78, 0.0)); img.alpha_composite(grad(W, H, l['bot'], H, 0.0, 0.82))
    lg = logo_white(l['logo_w']); img.alpha_composite(lg, ((W - lg.width) // 2, l['logo_y']))
    d = ImageDraw.Draw(img); fh = font('Bold', l['hs'])
    y = l['head_y']
    for line in k['head'].split('\n'):
        d.text((W / 2, y), line, font=fh, fill=WHITE, anchor='mt'); y += round(l['hs'] * 0.98)
    d.text((W / 2, y + 14), k['sub'], font=font('RegularItalic', 48), fill=(235, 225, 245), anchor='mt')
    dy = round(fy_px - r - 36) if 0 < fy_px < H and fy_px - r - 36 > y + 90 else l['days_y']   # day labels sit just above the circles
    pill(img, hw / 2, dy, k['days'][0], (16, 12, 22, 230)); pill(img, hw * 1.5, dy, k['days'][1], MAGENTA + (255,))
    d.line((hw, l['top'] - 60, hw, H), fill=WHITE, width=4)
    d.text((70, l['stat_y']), k['stat'], font=font('Bold', 150), fill=WHITE, anchor='lt')
    sy = l['stat_y'] + 160
    for line in k['label'].split('\n'):
        d.text((74, sy), line, font=font('Medium', 40), fill=WHITE, anchor='lt'); sy += 46
    if k['sim']: d.text((W / 2, H - 22), 'Simulated results.', font=font('Regular', 20), fill=(220, 215, 225), anchor='mb')
    return img

def render(kind, fmt):
    b = base(kind, fmt); W, H = b.size; l = L[fmt]
    out = os.path.join(HERE, f"{K[kind]['name']} – Countdown v2 Before-After – {fmt}.mp4")
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    for s in range(SECS):
        for half in (True, False):                       # colon blinks every half second
            fr = b.copy(); st = sticker(59 - s, half); fr.alpha_composite(st, (W - st.width - 40, l['st_cy'] - st.height // 2))
            if s == 0 and half: fr.convert('RGB').save(os.path.join(HERE, f'v2_{kind}_{fmt}_preview.jpg'), quality=88)
            raw = fr.convert('RGB').tobytes()
            for _ in range(FPS // 2): p.stdin.write(raw)
    p.stdin.close(); p.wait(); print('ok', out)

if __name__ == '__main__':
    kinds = [sys.argv[1]] if len(sys.argv) > 1 else ['do', 'ss']
    fmts = [sys.argv[2]] if len(sys.argv) > 2 else ['story', 'feed', 'square']
    for kd in kinds:
        for f in fmts: render(kd, f)
