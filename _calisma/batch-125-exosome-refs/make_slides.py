# OneSkin-style science carousels with OUR exosome loops (2026-11-10, Merve: "bunun benzerini bizim exosome videolarıyla,
# giriş bizim exosome videosu olsun" + "exosomlarla çalışma yapalım").
# 1080x1350 (4:5). Layout copied from the references: small grotesque title top-left, body text under it, science animation fills the slide.
# Copy = verbatim site copy (NX35 page / sicksciencelabs.com). Video slides = our 3D loops (network-web3d) cropped 16:9 -> 4:5.
import os, subprocess, textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(R, 'out'); os.makedirs(OUT, exist_ok=True)
ROOT = os.path.abspath(os.path.join(R, '..', '..'))
V3D = os.path.join(ROOT, '_calisma', 'network-web3d')
LOGO = os.path.join(os.path.dirname(ROOT), 'SickScience Brand Assets', 'Logos', 'SickScience Logo Type Two Color Black and Pink.png')
PHOTO = os.path.join(os.path.dirname(ROOT), 'SickScience Brand Assets', 'Images', 'All Products - New Image', 'S_0883.jpg')
F = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-')
W, H = 1080, 1350
INK, MAG = (20, 20, 24), (169, 33, 192)
font = lambda w, s: ImageFont.truetype(F + w + '.otf', s)

def wrap(d, text, f, maxw):
    lines = []
    for para in text.split('\n'):
        cur = ''
        for w in para.split(' '):
            t = (cur + ' ' + w).strip()
            if d.textlength(t, font=f) <= maxw: cur = t
            else: lines.append(cur); cur = w
        lines.append(cur)
    return lines

def glow(layer, text_layer_alpha, radius=14, strength=0.9):
    """soft white halo under dark text so it reads on the moving spheres"""
    a = text_layer_alpha.filter(ImageFilter.GaussianBlur(radius)).point(lambda v: min(255, int(v * strength * 2)))
    halo = Image.new('RGBA', layer.size, (255, 255, 255, 0)); halo.putalpha(a); return halo

def overlay_top(title, body, extra_logo=False):
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    ft, fb = font('Medium', 50), font('Regular', 38)
    y = 70
    for ln in wrap(d, title, ft, 920): d.text((64, y), ln, font=ft, fill=INK + (255,)); y += 58
    y += 18
    for ln in wrap(d, body, fb, 900): d.text((64, y), ln, font=fb, fill=INK + (235,)); y += 50
    a = lay.getchannel('A'); out = Image.alpha_composite(glow(lay, a), lay)
    if extra_logo: out = place_logo(out)
    return out

def overlay_hook(line1, line2, small, label):
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    f1, f2, fs_, fl = font('Medium', 84), font('Medium', 84), font('Regular', 42), font('Medium', 32)
    L = wrap(d, line1, f1, 900) + ([''] if False else [])
    block = L + wrap(d, line2, f2, 900) if line2 else L
    total = len(block) * 96 + (70 if small else 0); y = (H - total) // 2 - 40
    for i, ln in enumerate(block):
        w = d.textlength(ln, font=f1); d.text(((W - w) / 2, y), ln, font=f1, fill=INK + (255,)); y += 96
    if small:
        w = d.textlength(small, font=fs_); d.text(((W - w) / 2, y + 12), small, font=fs_, fill=INK + (225,))
    w = d.textlength(label, font=fl); d.text(((W - w) / 2, H - 120), label, font=fl, fill=INK + (235,))
    a = lay.getchannel('A'); return Image.alpha_composite(glow(lay, a, 18, 1.0), lay)

def place_logo(img):
    lg = Image.open(LOGO).convert('RGBA'); w = 330; lg = lg.resize((w, int(lg.height * w / lg.width)), Image.LANCZOS)
    img = img.copy(); img.alpha_composite(lg, (64, H - 64 - lg.height)); return img

def video_slide(name, src, x0, ss, ov):
    ovp = os.path.join(OUT, name + '_overlay.png'); ov.save(ovp)
    fl = f'[0:v]crop=864:1080:{x0}:0,scale={W}:{H}:flags=lanczos,setsar=1[v];[v][1:v]overlay=0:0,format=yuv420p[o]'
    out = os.path.join(OUT, name + '.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(ss), '-i', os.path.join(V3D, src), '-loop', '1', '-t', '10', '-i', ovp,
                    '-filter_complex', fl, '-map', '[o]', '-t', '8', '-r', '30', '-c:v', 'libx264', '-crf', '15', '-preset', 'slow',
                    '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-movflags', '+faststart', out], check=True)
    print('video', out)

def photo_slide(name, ov):
    ph = Image.open(PHOTO).convert('RGB'); ph = ph.resize((W, int(ph.height * W / ph.width)), Image.LANCZOS)
    top = max(0, (ph.height - H) // 2 - 40); ph = ph.crop((0, top, W, top + H))
    base = ph.convert('RGBA'); veil = Image.new('RGBA', (W, 430), (255, 255, 255, 0))
    g = Image.new('L', (1, 430)); g.putdata([int(235 * (1 - i / 430) ** 1.4) for i in range(430)]); veil.putalpha(g.resize((W, 430)))
    base.alpha_composite(veil, (0, 0)); base.alpha_composite(ov); out = os.path.join(OUT, name + '.png'); base.convert('RGB').save(out, quality=95); print('photo', out)

# ---------- Carousel A: "Your cells talk" (reference 1: hook -> lab -> mechanism -> finale) ----------
video_slide('A1_hook', 'A-exosome-field.mp4', 528, 1.0, overlay_hook('Your cells talk.', 'Exosomes carry\nthe message.', '', 'NX35™  ·  PLANT EXOSOME TECHNOLOGY'))
photo_slide('A2_lab', overlay_top('FROM THE SICKSCIENCE LAB', 'NX35™ is a marvel of biomimetics: the science of mimicking natural functions in our bodies. 100% plant-derived and vegan.'))
video_slide('A3_message', 'B-signal-to-cell.mp4', 500, 0.5, overlay_top('How the message arrives', 'Exosomes are carriers that deliver specific coded messages to cells at a molecular level.'))
video_slide('A4_small', 'A-exosome-field.mp4', 330, 3.0, overlay_top('Small enough to go where it matters', 'Exosomes are 1/1000th the size of a cell. They are incredibly minuscule, allowing them to easily navigate and deliver signals where it\'s needed most.', True))

# ---------- Carousel B: analogy (reference 2: "Collagen is like gluten in bread") ----------
video_slide('B1_hook', 'B-signal-to-cell.mp4', 480, 2.0, overlay_hook('Exosomes are like\ntext messages', 'for your cells', '(hear us out)', 'SWIPE TO LEARN MORE  →'))
video_slide('B2_network', 'A-exosome-field.mp4', 600, 4.0, overlay_top('Your Skin\'s Messaging Network', 'A text is tiny, carries a coded message, and lands exactly where it\'s sent.\nExosomes work the same way: carriers that deliver specific coded messages to cells.'))
photo_slide('B3_messenger', overlay_top('Don\'t Forget the Messenger', 'A message with no carrier never arrives. Exosomes are the carriers: incredibly minuscule, so they can navigate and deliver signals where it\'s needed most.'))
video_slide('B4_effect', 'B-signal-to-cell.mp4', 520, 5.0, overlay_top('The NX35™ Effect', 'Our NX35™ technology targets specific cells and delivers "coded" messages. 100% plant-derived and vegan.', True))
