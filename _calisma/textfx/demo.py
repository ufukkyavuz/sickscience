"""Catalogue reel: every effect in textfx, each on its own look. python demo.py [sheet]"""
import sys, os, subprocess
from PIL import Image, ImageDraw, ImageEnhance
sys.path.insert(0, os.path.dirname(__file__))
from textfx import render, EFFECTS, BRAND, F

W, H, FPS, SEG = 1080, 1920, 30, 1.9
IMG = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience Brand Assets/Images/All Products - New Image/")

def photo(name, dim=.55):
    im = Image.open(IMG + name).convert('RGB'); r = max(W / im.width, H / im.height)
    im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1)); x = (im.width - W) // 2; y = (im.height - H) // 2
    im = im.crop((x, y, x + W, y + H)); return ImageEnhance.Brightness(im).enhance(dim).convert('RGBA')
def flat(c): return Image.new('RGBA', (W, H), c + (255,))

BG = {'ink': flat(BRAND['ink']), 'ivory': flat(BRAND['ivory']), 'white': flat((250, 250, 248)),
      'mag': flat(BRAND['magenta']), 'lab': photo('S_1143.jpg', .5), 'petri': photo('S_0893.jpg', .55),
      'cage': photo('S_0214.jpg', .45), 'water': photo('S_1114.jpg', .5)}
TEX = photo('S_0895.jpg', 1.0)
I, WH, MG = BRAND['ink'], BRAND['white'], BRAND['magenta']
# effect: (text, bg, kwargs)
DEMO = {
 'soft-blur-in': ('Science you\ncan feel.', 'lab', dict(weight='Medium', size=120, shadow=True)),
 'per-character-rise': ('SCULPTED', 'ivory', dict(color=I, size=180, accent=BRAND['ss'])),
 'drop-letters': ('JAWLINE', 'ink', dict(size=190, color=WH)),
 'bounce-letters': ('BOUNCE BACK', 'mag', dict(size=130, color=WH)),
 'stagger-from-center': ('NX35™', 'ink', dict(size=230, color=WH)),
 'stagger-from-edges': ('EXOSOMES', 'white', dict(size=150, color=I)),
 'wave': ('hydrated', 'water', dict(size=170, weight='Light', italic=True, color=WH, shadow=True)),
 'flip-letters': ('FIRMER', 'ink', dict(size=200, color=BRAND['nw'])),
 'elastic-stretch': ('STRETCH', 'ivory', dict(size=190, color=I)),
 'tracking-in': ('SICKSCIENCE', 'white', dict(size=110, weight='Medium', color=I)),
 'typewriter': ('Is it a myth?\nLet\'s test it.', 'ivory', dict(size=100, weight='Medium', color=I)),
 'scramble-decode': ('PLANT EXOSOMES', 'ink', dict(size=105, color=WH, accent=MG)),
 'weight-wave': ('Thicker-looking\nhair', 'ivory', dict(size=130, color=BRAND['pc'])),
 'word-pop': ('My jaw is\nback.', 'cage', dict(size=150, color=WH, shadow=True, accent_words={'back.'})),
 'short-slide-right': ('Two cancer\nresearchers.', 'lab', dict(size=120, color=WH, shadow=True)),
 'short-slide-down': ('Glow, not\ngreasy.', 'mag', dict(size=140, color=WH)),
 'shared-axis-y': ('Clinically\ninspired.', 'white', dict(size=130, weight='Medium', color=I)),
 'word-crossfade': ('Quietly\npowerful.', 'ink', dict(size=140, weight='Light', color=WH)),
 'depth-parallax': ('Delivered\nwhere it\'s\nneeded.', 'petri', dict(size=130, color=WH, shadow=True)),
 'kinetic-center-build': ('This changed\nmy routine', 'cage', dict(size=120, color=WH, shadow=True, accent_words={'routine'})),
 'karaoke-pill': ('Twice a day,\nupward strokes', 'lab', dict(size=110, color=WH, pill=WH, shadow=True)),
 'highlighter': ('92% saw a more\nsculpted jawline', 'white', dict(size=100, color=I, accent=(230, 190, 245), accent_words={'sculpted', 'jawline'})),
 'underline-sweep': ('Plant-derived\n& vegan', 'ivory', dict(size=120, color=I, accent=MG, accent_words={'vegan'})),
 'strike-through': ('Botox in\na bottle', 'ink', dict(size=140, color=WH, accent=MG, accent_words={'botox'})),
 'word-swap': ('Your skin, Sculpted.', 'white', dict(size=110, color=I, accent=MG, swap=['Sculpted.', 'Firmer.', 'Smoother.'])),
 'accent-color-shift': ('Meet NetWork.', 'ink', dict(size=140, color=WH, accent=BRAND['nw'], accent_words={'network.'})),
 'mask-reveal-up': ('The new era\nof biotech.', 'lab', dict(size=130, color=WH, shadow=True)),
 'mask-reveal-down': ('From cancer\nto skincare.', 'ivory', dict(size=125, color=I)),
 'line-by-line-slide': ('Sculpt.\nFirm.\nSmooth.', 'mag', dict(size=150, color=WH)),
 'focus-blur-resolve': ('Real results.', 'water', dict(size=140, color=WH, shadow=True)),
 'micro-scale-fade': ('Award winning', 'white', dict(size=120, weight='Medium', color=I)),
 'fade-through': ('Gel-serum\ntexture', 'petri', dict(size=130, color=WH, shadow=True)),
 'shared-axis-z': ('LAB TESTED', 'ink', dict(size=150, color=WH)),
 'slam-shake': ('STOP.', 'mag', dict(size=260, color=WH)),
 'glitch-rgb': ('MYTH', 'ink', dict(size=280, color=WH)),
 'glow-pulse': ('NetWork', 'ink', dict(size=180, color=WH, accent=MG)),
 'shimmer-sweep': ('ShapeShift', 'ink', dict(size=170, color=(205, 208, 214))),
 'outline-to-fill': ('DropOff', 'white', dict(size=200, color=BRAND['do'])),
 'texture-fill-rise': ('GEL', 'white', dict(size=380, color=I, texture=TEX, accent=MG)),
 'counter-roll': ('92%', 'ivory', dict(size=300, color=BRAND['ss'], number=92, suffix='%')),
 'odometer': ('98%', 'ink', dict(size=300, color=WH, number=98, suffix='%', accent=MG)),
}
EXITS = ['fade', 'blur-out-up', 'scale-down-fade', 'slide-out-left']

def frame(name, t, i):
    txt, bg, kw = DEMO[name]
    fr = BG[bg].copy()
    lay = render(name, txt, t, W, H, cy=820, dur=SEG, exit=EXITS[i % 4], **kw)
    fr.alpha_composite(lay)
    d = ImageDraw.Draw(fr); dark = bg in ('ivory', 'white')
    lab = f"{i + 1:02d}  {name}"
    d.text((W / 2, 300), lab, font=F('Medium', 34), anchor='mm', fill=(I if dark else WH) + (200,))
    return fr.convert('RGB')

if __name__ == '__main__':
    names = list(DEMO)
    assert set(names) == set(EFFECTS), set(EFFECTS) ^ set(names)
    out = os.path.join(os.path.dirname(__file__), 'out'); os.makedirs(out, exist_ok=True)
    if len(sys.argv) > 1 and sys.argv[1] == 'sheet':
        cols = 8; th = (180, 320); rows = (len(names) + cols - 1) // cols
        for tt in (0.25, 1.0):
            sh = Image.new('RGB', (cols * th[0], rows * th[1]))
            for k, n in enumerate(names):
                sh.paste(frame(n, tt, k).resize(th), ((k % cols) * th[0], (k // cols) * th[1]))
            sh.save(f'{out}/sheet_{tt}.jpg', quality=85)
        sys.exit()
    p = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
                          '-r', str(FPS), '-i', '-', '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p',
                          f'{out}/textfx-catalogue.mp4'], stdin=subprocess.PIPE)
    for k, n in enumerate(names):
        for fi in range(int(SEG * FPS)):
            p.stdin.write(frame(n, fi / FPS, k).tobytes())
    p.stdin.close(); p.wait(); print('done')
