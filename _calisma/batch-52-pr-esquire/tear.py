"""Torn-paper clippings from real article screenshots (same look as batch-07 CNN)."""
import sys, os, random
from PIL import Image, ImageDraw, ImageFilter, ImageChops
HERE = os.path.dirname(os.path.abspath(__file__))
PAPER = (247, 245, 240)
def tear(src, out, pad=(70, 60), seed=1, edges='tb'):
    random.seed(seed)
    im = Image.open(os.path.join(HERE, src)).convert('RGB')
    # page white -> warm paper, ink stays
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            r, g, b = px[x, y]
            if r > 238 and g > 238 and b > 238: px[x, y] = PAPER
    W, H = im.width + 2 * pad[0], im.height + 2 * pad[1]
    paper = Image.new('RGB', (W, H), PAPER); paper.paste(im, pad)
    # subtle paper grain
    noise = Image.effect_noise((W, H), 9).convert('RGB')
    paper = ImageChops.multiply(paper, Image.blend(Image.new('RGB', (W, H), 'white'), noise, 0.06))
    mask = Image.new('L', (W, H), 0); d = ImageDraw.Draw(mask)
    def jag(y0, n, amp):
        pts = []; x = 0
        while x <= W:
            pts.append((x, y0 + random.uniform(-amp, amp))); x += random.uniform(6, n)
        pts.append((W, y0)); return pts
    top = jag(14, 22, 10) if 't' in edges else [(0, 0), (W, 0)]
    bot = jag(H - 14, 22, 10) if 'b' in edges else [(W, H), (0, H)]
    d.polygon(top + list(reversed(bot)) if 'b' in edges else top + bot, fill=255)
    clip = paper.convert('RGBA'); clip.putalpha(mask)
    # white fibre rim along torn edges
    rim = mask.filter(ImageFilter.MaxFilter(5)); fib = Image.new('RGBA', (W, H), (255, 255, 255, 255)); fib.putalpha(rim)
    base = Image.alpha_composite(fib, clip)
    # soft drop shadow baked in
    S = 40; out_im = Image.new('RGBA', (W + 2 * S, H + 2 * S), (0, 0, 0, 0))
    sh = Image.new('RGBA', out_im.size, (0, 0, 0, 0)); sm = Image.new('L', out_im.size, 0); sm.paste(rim, (S + 6, S + 12))
    sh.putalpha(sm.filter(ImageFilter.GaussianBlur(14)).point(lambda v: int(v * 0.28)))
    out_im = Image.alpha_composite(out_im, sh); out_im.alpha_composite(base, (S, S))
    out_im.save(os.path.join(HERE, out)); print(out, out_im.size)
tear('src-headline.png', 'clip-headline-shadow.png', pad=(60, 50), seed=3)
tear('src-card.png', 'clip-card-shadow.png', pad=(50, 50), seed=8)
