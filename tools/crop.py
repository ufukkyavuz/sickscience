"""Pure crop for format variants — NO padding, NO blur, NO downscaling below cover.
crop(src, W, H, scale, top_frac, target_top, cx_src=.5, cx_dst=W/2) -> (image, actual_product_top, x, y, w, h)
scale >= 1 means the source covers the 1080-wide frame; the window is clamped inside the image."""
from PIL import Image

def crop(src, W, H, scale=1.0, top_frac=0.0, target_top=0, cx_src=0.5, cx_dst=None):
    im = Image.open(src).convert('RGB')
    w = round(W * scale); h = round(im.height * w / im.width)
    if h < H:  # must cover
        h = H; w = round(im.width * h / im.height)
    im = im.resize((w, h), Image.LANCZOS)
    y = min(0, max(H - h, round(target_top - top_frac * h)))
    cx_dst = W / 2 if cx_dst is None else cx_dst
    x = min(0, max(W - w, round(cx_dst - cx_src * w)))
    out = im.crop((-x, -y, -x + W, -y + H))
    return out, round(top_frac * h + y), x, y, w, h
