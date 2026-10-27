"""Batch 48 v4 (2026-10-16): stat-as-headline B/A countdown.
User: first DropOff legs were better (no rear-focused crop); drop the top headline, use 88% / 92% as the headline,
put a clean countdown under it; the colon must NOT blink.
Layout (top -> bottom): logo, big stat + PDP label, countdown block, B/A photo (whole width, never covered)."""
import os, sys, subprocess
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..', '..'); C47 = os.path.join(ROOT, '_calisma', 'batch-47-characters')
FONTS = os.path.expanduser('~/Library/Fonts')
def font(style, size): return ImageFont.truetype(os.path.join(FONTS, f'FoundersGrotesk-{style}.otf'), size)
FPS, SECS = 30, 12
MAGENTA, INK, GREY = (169, 33, 192), (18, 14, 24), (88, 80, 98)
SIZES = {'story': (1080, 1920), 'feed': (1080, 1350), 'square': (1080, 1080)}
K = {
 'do': dict(src='ba_do_zara.png', top=0.36, stat='88%', label='experienced reduced cellulite & dimpling', days=('DAY 0', 'DAY 56'), name='DropOff'),
 'ss': dict(src='ba3_ss_full.png', top=0.0, stat='92%', label='saw a more sculpted jawline', days=('DAY 0', 'DAY 14'), name='ShapeShift'),
 'pc': dict(src='ba3_pc_macro.png', top=0.0, stat='29%', label='average increase in hair thickness', days=('DAY 0', 'DAY 14'), name='PowerCycle'),
 'nw': dict(src='ba3_nw_ama.png', top=0.0, stat='90%', label='saw a visibly brighter complexion', days=('DAY 0', 'DAY 14'), name='NetWork'),
}
# logo_y, logo_w, stat_y, stat_size, label_size, label_w, cd_y, cd_box, img_y
L = {'story':  dict(logo_y=190, logo_w=330, stat_y=262, ss=210, ls=46, lw=900, cd_y=560, box=118, img_y=820),
     'feed':   dict(logo_y=44, logo_w=260, stat_y=96, ss=150, ls=40, lw=940, cd_y=320, box=96, img_y=580),
     'square': dict(logo_y=34, logo_w=230, stat_y=78, ss=124, ls=36, lw=940, cd_y=250, box=84, img_y=500)}

def logo(w):
    lg = Image.open(os.path.join(ROOT, '_calisma', 'video-01-bcrf', 'assets', 'logo.png')).convert('RGBA')
    return lg.resize((w, round(lg.height * w / lg.width)), Image.LANCZOS)

def pill(img, cx, cy, s, bg, fg=(255, 255, 255), size=32):
    d = ImageDraw.Draw(img); f = font('Semibold', size)
    l, t, r, b = d.textbbox((0, 0), s, font=f, anchor='mm'); w, h = r - l + 48, b - t + 24
    d.rounded_rectangle((cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2), radius=h / 2, fill=bg)
    d.text((cx, cy), s, font=f, fill=fg, anchor='mm')

def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w
    return lines + [cur]

def photo(kind, W, H, img_y):
    k = K[kind]; ph = Image.open(os.path.join(C47, k['src'])).convert('RGB')
    if k['top']: ph = ph.crop((0, round(ph.height * k['top']), ph.width, ph.height))
    top = ph.crop((0, 0, ph.width, 6)).getdata(); paper = [p for p in top if sum(p) > 600] or list(top)
    bg = tuple(sum(c[i] for c in paper) // len(paper) for i in range(3))
    sc = W / ph.width; ph = ph.resize((W, round(ph.height * sc)), Image.LANCZOS)   # whole width; the photo runs to the frame bottom
    return ph, bg

GAP = {'story': 64, 'feed': 44, 'square': 32}          # one spacing unit between blocks; related lines use 0.35 of it
TOP = {'story': 200, 'feed': 48, 'square': 36}          # story keeps clear of the top UI band

def ink(d, text, f):
    l, t, r, b = d.textbbox((0, 0), text, font=f, anchor='mt'); return t, b   # ink top/bottom when drawn at y=0 with anchor 'mt'

def put(d, W, y_top, text, f, fill):
    t, b = ink(d, text, f); d.text((W / 2, y_top - t), text, font=f, fill=fill, anchor='mt'); return y_top + (b - t)

def layout(kind, fmt):
    """measure every block and stack them with even spacing; returns y positions"""
    k, l = K[kind], L[fmt]; W, H = SIZES[fmt]; G = GAP[fmt]
    d = ImageDraw.Draw(Image.new('RGB', (10, 10)))
    y = TOP[fmt]; pos = {'logo': y}; y += logo(l['logo_w']).height + G
    pos['stat'] = y; t, b = ink(d, k['stat'], font('Bold', l['ss'])); y += (b - t) + round(G * 0.35)
    fl = font('Medium', l['ls']); pos['label'] = y; lines = wrap(d, k['label'], fl, l['lw'])
    lt, lb = ink(d, 'Ag', fl); y += len(lines) * (lb - lt) + (len(lines) - 1) * round(l['ls'] * 0.3) + G
    pos['cd'] = y; tt, tb = ink(d, 'ENDS IN', font('Semibold', 32)); ut, ub = ink(d, 'MIN', font('Medium', 32))
    y += (tb - tt) + 18 + l['box'] + 12 + (ub - ut) + G
    pos['img'] = y; pos['lines'] = lines; return pos

def countdown(img, pos, box, sec):
    """'15% OFF FIRST ORDER · ENDS IN' over two flat boxes MM : SS with unit labels. Static colon."""
    W = img.size[0]; d = ImageDraw.Draw(img)
    y = put(d, W, pos['cd'], '15% OFF FIRST ORDER  ·  ENDS IN', font('Semibold', 32), MAGENTA)
    by = y + 18; bw = round(box * 1.25); gap = 54; fd = font('Bold', round(box * 0.66)); fl = font('Medium', 32)
    for k, (val, lab) in enumerate((('00', 'MIN'), (f'{sec:02d}', 'SEC'))):
        x0 = W / 2 - gap / 2 - bw if k == 0 else W / 2 + gap / 2
        d.rounded_rectangle((x0, by, x0 + bw, by + box), radius=round(box * 0.2), fill=INK)
        d.text((x0 + bw / 2, by + box / 2), val, font=fd, fill=(255, 255, 255), anchor='mm')
        t, _ = ink(d, lab, fl); d.text((x0 + bw / 2, by + box + 12 - t), lab, font=fl, fill=GREY, anchor='mt')
    d.text((W / 2, by + box / 2 - 4), ':', font=font('Bold', round(box * 0.6)), fill=INK, anchor='mm')

def base(kind, fmt):
    k, l = K[kind], L[fmt]; W, H = SIZES[fmt]; pos = layout(kind, fmt)
    ph, bg = photo(kind, W, H, pos['img'])
    img = Image.new('RGBA', (W, H), bg + (255,)); img.paste(ph, (0, pos['img']))
    lg = logo(l['logo_w']); img.alpha_composite(lg, ((W - lg.width) // 2, pos['logo']))
    d = ImageDraw.Draw(img)
    put(d, W, pos['stat'], k['stat'], font('Bold', l['ss']), MAGENTA)
    fl = font('Medium', l['ls']); y = pos['label']; lt, lb = ink(d, 'Ag', fl)
    for ln in pos['lines']:
        t, _ = ink(d, ln, fl); d.text((W / 2, y - lt), ln, font=fl, fill=INK, anchor='mt'); y += (lb - lt) + round(l['ls'] * 0.3)
    py = pos['img'] + 46
    pill(img, W / 4, py, k['days'][0], INK); pill(img, W * 3 / 4, py, k['days'][1], MAGENTA)
    d.text((W / 2, H - 18), 'Simulated results.', font=font('Regular', 20), fill=(255, 255, 255), anchor='mb', stroke_width=1, stroke_fill=(110, 95, 90))
    return img, pos

def render(kind, fmt, preview_only=False):
    b, pos = base(kind, fmt); W, H = b.size; l = L[fmt]
    def frame(sec): f = b.copy(); countdown(f, pos, l['box'], sec); return f
    frame(59).convert('RGB').save(os.path.join(HERE, f'v4_{kind}_{fmt}_preview.jpg'), quality=90)
    if preview_only: return
    out = os.path.join(HERE, f"{K[kind]['name']} – Countdown v4 Before-After – {fmt}.mp4")
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                          '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-movflags', '+faststart', out], stdin=subprocess.PIPE)
    for s in range(SECS):
        raw = frame(59 - s).convert('RGB').tobytes()
        for _ in range(FPS): p.stdin.write(raw)
    p.stdin.close(); p.wait()
    wav = os.path.join(HERE, 'audio', 'countdown_sfx.wav')
    if os.path.exists(wav):                                   # tick-per-second soundtrack (mgaudio)
        tmp = out + '.tmp.mp4'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', out, '-i', wav, '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', tmp], check=True)
        os.replace(tmp, out)
    print('ok', out)

if __name__ == '__main__':
    kinds = [sys.argv[1]] if len(sys.argv) > 1 else ['do', 'ss']
    fmts = [sys.argv[2]] if len(sys.argv) > 2 else ['story', 'feed', 'square']
    for kd in kinds:
        if not os.path.exists(os.path.join(C47, K[kd]['src'])): print('missing source', K[kd]['src']); continue
        for f in fmts: render(kd, f, preview_only='--preview' in sys.argv)
