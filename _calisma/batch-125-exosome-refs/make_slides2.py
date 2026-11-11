# v2 (2026-11-10): same OneSkin carousel layouts, but the media are the client's REAL plant-exosome lab clips
# (Brand Assets/Videos/Lab mix, copied to ./lab) — user: "sana ürettiğin videoyu koy mu dedim, driveda exosomla alakalı videolar var".
# Layout measured on the reference frames (1080x1350):
#   V1 (post 1 video slide): full-bleed video, title 2 lines bold caps ~46 px with a small ⊗ / ✓ icon at x≈105, body ~36 px, text block x 105..930, y 95..
#   V2 (post 2 video slide): top ~460 px is a frosted (blurred + white veil) band of the same video holding title (medium ~52 px) + body (~36 px) at x=60;
#                            the sharp video fills the rest.
# Copy = verbatim site copy (NX35 page); 464x832 phone clips are enlarged with lanczos + light unsharp (no AI upscaler available here).
import os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(R, 'out2'); os.makedirs(OUT, exist_ok=True)
ROOT = os.path.abspath(os.path.join(R, '..', '..'))
LAB = os.path.join(R, 'lab')
LOGO = os.path.join(os.path.dirname(ROOT), 'SickScience Brand Assets', 'Logos', 'SickScience Logo Type Two Color Black and Pink.png')
F = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-')
W, H = 1080, 1350
INK = (18, 18, 22, 255)
font = lambda w, s: ImageFont.truetype(F + w + '.otf', s)

def wrap(d, text, f, maxw):
    out = []
    for para in text.split('\n'):
        cur = ''
        for w in para.split(' '):
            t = (cur + ' ' + w).strip()
            if d.textlength(t, font=f) <= maxw: cur = t
            else: out.append(cur); cur = w
        out.append(cur)
    return out

def icon(d, x, y, kind, r=15):
    d.ellipse([x, y, x + 2 * r, y + 2 * r], outline=INK, width=3)
    if kind == 'x': d.line([x + 9, y + 9, x + 2 * r - 9, y + 2 * r - 9], fill=INK, width=3); d.line([x + 2 * r - 9, y + 9, x + 9, y + 2 * r - 9], fill=INK, width=3)
    else: d.line([x + 8, y + r, x + r - 1, y + 2 * r - 9, x + 2 * r - 7, y + 9], fill=INK, width=3, joint='curve')

def text_v1(lines, body, logo=False):
    """lines: [(icon|None, 'TITLE LINE')] ; reference 1 style, text straight on the video"""
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    ft, fb = font('Bold', 47), font('Regular', 37); y = 92
    for ic, t in lines:
        if ic: icon(d, 105, y + 6, ic); d.text((160, y), t, font=ft, fill=INK)
        else: d.text((105, y), t, font=ft, fill=INK)
        y += 64
    y += 6
    for ln in wrap(d, body, fb, 830): d.text((105, y), ln, font=fb, fill=INK); y += 49
    if logo: lay = place_logo(lay)
    return lay

def text_v2(title, body, logo=False):
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    ft, fb = font('Medium', 52), font('Regular', 37); y = 70
    for ln in wrap(d, title, ft, 960): d.text((60, y), ln, font=ft, fill=INK); y += 62
    y += 14
    for ln in wrap(d, body, fb, 960): d.text((60, y), ln, font=fb, fill=INK); y += 49
    bottom = y
    if logo:
        lg = Image.open(LOGO).convert('RGBA'); w = 300; lg = lg.resize((w, int(lg.height * w / lg.width)), Image.LANCZOS)
        lay.alpha_composite(lg, (60, bottom + 26)); bottom += 26 + lg.height
    return lay, bottom + 56

def place_logo(lay):
    lg = Image.open(LOGO).convert('RGBA'); w = 330; lg = lg.resize((w, int(lg.height * w / lg.width)), Image.LANCZOS)
    lay = lay.copy(); lay.alpha_composite(lg, (60, H - 56 - lg.height)); return lay

def veil():
    v = Image.new('RGBA', (W, 560), (255, 255, 255, 0)); g = Image.new('L', (1, 560)); g.putdata([int(150 * (1 - i / 560) ** 1.3) for i in range(560)])
    v.putalpha(g.resize((W, 560))); full = Image.new('RGBA', (W, H), (0, 0, 0, 0)); full.alpha_composite(v, (0, 0)); return full

def render(name, clip, ss, cy, layout, ov):
    band = 470
    if layout == 'v2': ov, band = ov
    """clip 464x832 phone video; cy = top of the 464x580 4:5 window inside the frame"""
    ovp = os.path.join(OUT, name + '_text.png'); ov.save(ovp)
    vp = os.path.join(OUT, name + '_veil.png'); veil().save(vp)
    base = f'[0:v]crop=464:580:0:{cy},scale={W}:{H}:flags=lanczos,unsharp=5:5:0.9:3:3:0.0,fps=30,setsar=1[v]'
    if layout == 'v2':
        fl = (base + f';[v]split[a][b];[b]crop=1080:{band}:0:0,gblur=sigma=30,drawbox=x=0:y=0:w=1080:h={band}:color=white@0.42:t=fill[band];'
              '[a][band]overlay=0:0[c];[c][1:v]overlay=0:0,format=yuv420p[o]')
    else:
        fl = base + ';[v][2:v]overlay=0:0[vv];[vv][1:v]overlay=0:0,format=yuv420p[o]'
    out = os.path.join(OUT, name + '.mp4')
    inputs = ['-ss', str(ss), '-t', '8', '-i', os.path.join(LAB, clip), '-loop', '1', '-t', '8', '-i', ovp] + (['-loop', '1', '-t', '8', '-i', vp] if layout == 'v1' else [])
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', fl, '-map', '[o]', '-t', '8', '-r', '30', '-c:v', 'libx264', '-crf', '14', '-preset', 'slow',
                    '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-movflags', '+faststart', out], check=True)
    print(out)

# ---------- A: reference 1 ("Mask the past / Protect your future") ----------
render('A1_hook', '13.36.25.mp4', 0, 250, 'v1', text_v1([('x', 'SKIP THE SURFACE'), ('v', 'SPEAK TO THE CELL')],
       'NX35™ is our plant exosome technology: carriers that deliver specific coded messages to cells at a molecular level.'))
render('A2_plant', '13.39.01.mp4', 0.5, 120, 'v2', text_v2('From plant to formula', 'Our NX35™ exosomes are 100% plant-derived and vegan.'))
render('A3_lab', '13.36.30.mp4', 9, 180, 'v2', text_v2('Made in the SickScience lab', 'A marvel of biomimetics: the science of mimicking natural functions in our bodies.'))
render('A4_small', '13.51.41.mp4', 0, 150, 'v2', text_v2('Small enough to go where it matters',
       'Exosomes are 1/1000th the size of a cell, allowing them to easily navigate and deliver signals where it\'s needed most.', True))

# ---------- B: reference 2 ("Collagen is like gluten in bread") ----------
render('B1_hook', '13.50.26.mp4', 0, 230, 'v1', text_v1([(None, 'Exosomes are like text'), (None, 'messages for your cells')],
       '(hear us out)'))
render('B2_network', '13.54.59.mp4', 0, 200, 'v2', text_v2('Your Skin\'s Messaging Network', 'A text is tiny, carries a coded message, and lands exactly where it\'s sent. Exosomes work the same way: carriers that deliver specific coded messages to cells.'))
render('B3_messenger', '13.52.58.mp4', 0, 150, 'v2', text_v2('Don\'t Forget the Messenger', 'A message with no carrier never arrives. That\'s the job of an exosome: incredibly minuscule, built to navigate and deliver signals where it\'s needed most.'))
render('B4_effect', '13.52.44.mp4', 0, 150, 'v2', text_v2('The NX35™ Effect',
       'Our NX35™ technology targets specific cells and delivers "coded" messages. 100% plant-derived and vegan.', True))
