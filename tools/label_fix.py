"""Pixel-fix garbled vertical capsule lettering in a generated photo.

Usage: python label_fix.py in.png out.png '<json specs>'
specs: [{"text": "ShapeShift", "x": 1141, "y0": 832, "y1": 892}, ...]
  x = centre column of the lettering, y0/y1 = top/bottom of the old word.
The old word is erased by interpolating each row between the chrome on its left
and right, then the word is redrawn in white, reading bottom-to-top, the same
length as the old one (Helvetica Bold, like the real label).
"""
import json, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT = ("/System/Library/Fonts/Helvetica.ttc", 1)


def erase(a, x, y0, y1, half):
    """Replace only the bright letter pixels (dilated) with the row's darker
    background, so the stripe/chrome around the word stays untouched."""
    xl, xr = x - half, x + half
    band = a[y0:y1 + 1, xl:xr + 1].astype(float)
    lum = band.mean(axis=2)
    mask = np.zeros(lum.shape, bool)
    fill = np.zeros_like(band)
    # chrome reflections run vertically, so fill each column from the clean
    # pixels just above and below the word
    top = a[y0 - 6, xl:xr + 1].astype(float)
    bot = a[y1 + 6, xl:xr + 1].astype(float)
    n = lum.shape[0]
    for r in range(n):
        row = lum[r]
        dark = row <= np.percentile(row, 50)
        mask[r] = row > row[dark].mean() + 35
        t = r / max(1, n - 1)
        fill[r] = top * (1 - t) + bot * t
    m = Image.fromarray((mask * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5))
    m = np.array(m.filter(ImageFilter.GaussianBlur(1))) / 255.0
    out = band * (1 - m[..., None]) + fill * m[..., None]
    a[y0:y1 + 1, xl:xr + 1] = out.astype(np.uint8)


def word(text, length):
    f = ImageFont.truetype(FONT[0], 200, index=FONT[1])
    l, t, r, b = f.getbbox(text)
    im = Image.new("L", (r - l + 20, b - t + 20), 0)
    ImageDraw.Draw(im).text((10 - l, 10 - t), text, font=f, fill=255)
    im = im.crop(im.getbbox())
    h = max(1, round(im.height * length / im.width))
    return im.resize((length, h), Image.LANCZOS).rotate(90, expand=True)


def main():
    src, dst, specs = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])
    img = Image.open(src).convert("RGB")
    a = np.array(img)
    for s in specs:
        length = s["y1"] - s["y0"]
        m = word(s["text"], length)
        half = m.width // 2 + 5
        erase(a, s["x"], s["y0"] - 4, s["y1"] + 4, half)
    img = Image.fromarray(a)
    for s in specs:
        # optional: repaint the real product's black stripe where the model faded it
        st = s.get("stripe")
        if st:
            # square top (starts at the cap seam), rounded bottom, soft gloss
            w, h = st["w"], st["y1"] - st["y0"]
            mask = Image.new("L", (w + 8, h + 8), 0)
            d = ImageDraw.Draw(mask)
            d.rounded_rectangle((4, 4, w + 3, h + 3), radius=w // 3, fill=240)
            d.rectangle((4, 4, w + 3, 4 + w), fill=240)
            mask = mask.filter(ImageFilter.GaussianBlur(1.0))
            col = np.zeros((h + 8, w + 8, 3), np.uint8)
            xs = np.linspace(-1, 1, w + 8)
            shade = 16 + 22 * np.exp(-((xs + 0.35) / 0.18) ** 2)  # thin highlight left of centre
            col[:] = np.stack([shade, shade, shade + 2], -1).astype(np.uint8)
            img.paste(Image.fromarray(col), (s["x"] - w // 2 - 4, st["y0"] - 4), mask)
    for s in specs:
        m = word(s["text"], s["y1"] - s["y0"]).filter(ImageFilter.GaussianBlur(0.4))
        white = Image.new("RGB", m.size, (250, 250, 250))
        img.paste(white, (s["x"] - m.width // 2, s["y0"]), m)
    img.save(dst)


if __name__ == "__main__":
    main()
