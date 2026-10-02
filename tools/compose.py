"""Place a 9:16 master into Story/Feed/Square canvases so the product top lands at a target y.
Missing areas are filled by mirrored + blurred edge strips. Usage: compose.py src.png top_frac out_prefix t_story t_feed t_square [scale]"""
import sys
from PIL import Image, ImageFilter

def place(src, top_frac, W, H, target_top, scale=1.0):
    im = Image.open(src).convert('RGB')
    w = round(W * scale); h = round(im.height * w / im.width)
    im = im.resize((w, h), Image.LANCZOS)
    x = (W - w) // 2
    y = round(target_top - top_frac * h)
    canvas = Image.new('RGB', (W, H))
    # vertical padding: mirror the edge band, blurred
    if y > 0:
        band = im.crop((0, 0, w, min(h, y))).transpose(Image.FLIP_TOP_BOTTOM).filter(ImageFilter.GaussianBlur(18))
        canvas.paste(band, (x, y - band.height))
    if y + h < H:
        need = H - (y + h)
        band = im.crop((0, max(0, h - need), w, h)).transpose(Image.FLIP_TOP_BOTTOM).filter(ImageFilter.GaussianBlur(18))
        canvas.paste(band, (x, y + h))
    canvas.paste(im, (x, y))
    # soften the seams
    if y + h < H:
        seam = canvas.crop((0, y + h - 40, W, y + h + 40)).filter(ImageFilter.GaussianBlur(12))
        canvas.paste(seam, (0, y + h - 40))
    if y > 0:
        seam = canvas.crop((0, y - 40, W, y + 40)).filter(ImageFilter.GaussianBlur(12))
        canvas.paste(seam, (0, y - 40))
    return canvas

if __name__ == '__main__':
    src, tf, out = sys.argv[1], float(sys.argv[2]), sys.argv[3]
    ts, tfd, tsq = map(float, sys.argv[4:7])
    sc = float(sys.argv[7]) if len(sys.argv) > 7 else 1.0
    place(src, tf, 1080, 1920, ts, sc).save(out + '-story.jpg', quality=92)
    place(src, tf, 1080, 1350, tfd, sc).save(out + '-feed.jpg', quality=92)
    place(src, tf, 1080, 1080, tsq, sc).save(out + '-square.jpg', quality=92)

def place_feather(src, top_frac, W, H, target_top, scale, feather=90):
    """Scaled-down master over a blurred cover copy of itself; edges feathered."""
    from PIL import ImageDraw
    im = Image.open(src).convert('RGB')
    cov_s = max(W / im.width, H / im.height)
    bg = im.resize((round(im.width * cov_s), round(im.height * cov_s)), Image.LANCZOS)
    bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2, (bg.width - W) // 2 + W, (bg.height - H) // 2 + H)).filter(ImageFilter.GaussianBlur(60))
    w = round(W * scale); h = round(im.height * w / im.width)
    fg = im.resize((w, h), Image.LANCZOS)
    mask = Image.new('L', (w, h), 255); d = ImageDraw.Draw(mask)
    for i in range(feather):
        v = round(255 * i / feather)
        d.rectangle([i, i, w - 1 - i, h - 1 - i], outline=v)
    x = (W - w) // 2; y = round(target_top - top_frac * h)
    bg.paste(fg, (x, y), mask)
    return bg

def run_feather(src, tf, out, ts, tfd, tsq, s_story, s_feed, s_sq):
    place_feather(src, tf, 1080, 1920, ts, s_story).save(out + '-story.jpg', quality=92)
    place_feather(src, tf, 1080, 1350, tfd, s_feed).save(out + '-feed.jpg', quality=92)
    place_feather(src, tf, 1080, 1080, tsq, s_sq).save(out + '-square.jpg', quality=92)

def place_feather(src, top_frac, W, H, target_top, scale, feather=70):
    """Scaled-down master; outside area filled by edge-pixel extension, blurred; feathered seam."""
    import numpy as np
    from PIL import ImageDraw
    im = Image.open(src).convert('RGB')
    w = round(W * scale); h = round(im.height * w / im.width)
    fg = im.resize((w, h), Image.LANCZOS)
    x = (W - w) // 2; y = round(target_top - top_frac * h)
    a = np.asarray(fg)
    # crop fg to canvas if it overflows vertically
    y0 = max(0, -y); y1 = min(h, H - y)
    a = a[y0:y1]
    top = max(0, y); bot = H - top - a.shape[0]
    ext = np.pad(a, ((0, 0), (x, W - w - x), (0, 0)), mode='edge')
    ext = np.pad(ext, ((top, bot), (0, 0), (0, 0)), mode='edge')
    bg = Image.fromarray(ext).filter(ImageFilter.GaussianBlur(110))
    sharp = Image.fromarray(a)
    mask = Image.new('L', sharp.size, 255); d = ImageDraw.Draw(mask)
    for i in range(feather):
        d.rectangle([i, i, sharp.width - 1 - i, sharp.height - 1 - i], outline=round(255 * i / feather))
    bg.paste(sharp, (x, top), mask)
    return bg

def place_mirror(src, top_frac, W, H, target_top, scale, feather=40):
    """Scaled master; outside filled by mirrored image (light blur) — good for natural scenery."""
    import numpy as np
    from PIL import ImageDraw
    im = Image.open(src).convert('RGB')
    w = round(W * scale); h = round(im.height * w / im.width)
    fg = im.resize((w, h), Image.LANCZOS)
    x = (W - w) // 2; y = round(target_top - top_frac * h)
    a = np.asarray(fg); y0 = max(0, -y); y1 = min(h, H - y); a = a[y0:y1]
    top = max(0, y); bot = H - top - a.shape[0]
    ext = np.pad(a, ((top, bot), (x, W - w - x), (0, 0)), mode='symmetric')
    bg = Image.fromarray(ext).filter(ImageFilter.GaussianBlur(10))
    sharp = Image.fromarray(a)
    mask = Image.new('L', sharp.size, 255); d = ImageDraw.Draw(mask)
    for i in range(feather):
        d.rectangle([i, i, sharp.width - 1 - i, sharp.height - 1 - i], outline=round(255 * i / feather))
    bg.paste(sharp, (x, top), mask)
    return bg

def run_mirror(src, tf, out, ts, tfd, tsq, s_story, s_feed, s_sq):
    place_mirror(src, tf, 1080, 1920, ts, s_story).save(out + '-story.jpg', quality=92)
    place_mirror(src, tf, 1080, 1350, tfd, s_feed).save(out + '-feed.jpg', quality=92)
    place_mirror(src, tf, 1080, 1080, tsq, s_sq).save(out + '-square.jpg', quality=92)

def place_mirror(src, top_frac, W, H, target_top, scale, feather=40, band=0.18):
    """Scaled master; sides mirrored, top extended from the top edge, bottom mirrored from the lowest `band` of the image only."""
    import numpy as np
    from PIL import ImageDraw
    im = Image.open(src).convert('RGB')
    w = round(W * scale); h = round(im.height * w / im.width)
    a = np.asarray(im.resize((w, h), Image.LANCZOS))
    x = (W - w) // 2; y = round(target_top - top_frac * h)
    y0 = max(0, -y); y1 = min(h, H - y); a = a[y0:y1]
    top = max(0, y); bot = H - top - a.shape[0]
    a2 = np.pad(a, ((0, 0), (x, W - w - x), (0, 0)), mode='symmetric')
    parts = []
    if top: parts.append(np.repeat(a2[:1], top, axis=0))
    parts.append(a2)
    if bot:
        blk = a2[-max(8, int(band * h)):]
        rows = []; flip = True; need = bot
        while need > 0:
            b = blk[::-1] if flip else blk
            rows.append(b[:need]); need -= len(b[:need]); flip = not flip
        parts.append(np.concatenate(rows, axis=0))
    ext = np.concatenate(parts, axis=0)
    bg = Image.fromarray(ext).filter(ImageFilter.GaussianBlur(10))
    sharp = Image.fromarray(a)
    mask = Image.new('L', sharp.size, 255); d = ImageDraw.Draw(mask)
    for i in range(feather):
        d.rectangle([i, i, sharp.width - 1 - i, sharp.height - 1 - i], outline=round(255 * i / feather))
    bg.paste(sharp, (x, top), mask)
    return bg

def place_shift(src, top_frac, W, H, target_top, scale, cx_src=0.5, cx_dst=None, feather=40):
    """Like place_mirror but the source point cx_src lands at canvas x cx_dst; overflow cropped, gaps mirrored."""
    import numpy as np
    from PIL import ImageDraw
    im = Image.open(src).convert('RGB')
    w = round(W * scale); h = round(im.height * w / im.width)
    a = np.asarray(im.resize((w, h), Image.LANCZOS))
    x = round((cx_dst if cx_dst is not None else W / 2) - cx_src * w); y = round(target_top - top_frac * h)
    a = a[max(0, -y):min(h, H - y), max(0, -x):min(w, W - x)]
    top = max(0, y); left = max(0, x)
    bot = H - top - a.shape[0]; right = W - left - a.shape[1]
    ext = np.pad(a, ((0, 0), (left, right), (0, 0)), mode='edge')
    parts = []
    if top: parts.append(np.repeat(ext[:1], top, axis=0))
    parts.append(ext)
    if bot:
        blk = ext[-max(8, int(0.15 * h)):]; rows = []; flip = True; need = bot
        while need > 0:
            b = blk[::-1] if flip else blk; rows.append(b[:need]); need -= len(b[:need]); flip = not flip
        parts.append(np.concatenate(rows, axis=0))
    bg = Image.fromarray(np.concatenate(parts, axis=0)).filter(ImageFilter.GaussianBlur(24))
    sharp = Image.fromarray(a); mask = Image.new('L', sharp.size, 255); d = ImageDraw.Draw(mask)
    edges = [left > 0, top > 0, right > 0, bot > 0]
    for i in range(feather):
        v = round(255 * i / feather)
        if edges[0]: d.line([(i, 0), (i, sharp.height)], fill=v)
        if edges[2]: d.line([(sharp.width - 1 - i, 0), (sharp.width - 1 - i, sharp.height)], fill=v)
        if edges[1]: d.line([(0, i), (sharp.width, i)], fill=v)
        if edges[3]: d.line([(0, sharp.height - 1 - i), (sharp.width, sharp.height - 1 - i)], fill=v)
    bg.paste(sharp, (left, top), mask)
    return bg
