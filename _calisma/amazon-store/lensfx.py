"""Magnifier effect for concern cards (user ref: DUMAIN glasses through a lens): outside = soft DOF blur, inside = sharp 2.2x zoom, thin glass rim."""
import sys
from PIL import Image, ImageFilter, ImageDraw, ImageChops
def lens(src, out, cx, cy, r, zoom=2.2, focus=None, blur=10):
    im = Image.open(src).convert('RGB'); W, H = im.size
    cx, cy, R = int(cx*W), int(cy*H), int(r*W)
    fx, fy = (int(focus[0]*W), int(focus[1]*H)) if focus else (cx, cy)
    bg = im.filter(ImageFilter.GaussianBlur(blur))
    # inside: crop around focus point, zoomed
    cr = int(R/zoom); crop = im.crop((fx-cr, fy-cr, fx+cr, fy+cr)).resize((2*R, 2*R), Image.LANCZOS)
    # slight barrel feel: none (keep clean); mild edge darkening inside rim for glass depth
    mask = Image.new('L', (2*R, 2*R), 0); ImageDraw.Draw(mask).ellipse((0, 0, 2*R-1, 2*R-1), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(1.2))
    bg.paste(crop, (cx-R, cy-R), mask)
    # rim: thin bright line + faint dark inner line (refraction)
    ov = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    d.ellipse((cx-R, cy-R, cx+R, cy+R), outline=(255, 255, 255, 235), width=max(3, W//450))
    d.ellipse((cx-R+5, cy-R+5, cx+R-5, cy+R-5), outline=(60, 60, 70, 70), width=max(2, W//800))
    d.ellipse((cx-R-4, cy-R-4, cx+R+4, cy+R+4), outline=(120, 120, 130, 60), width=max(2, W//900))
    hl = Image.new('RGBA', (W, H), (0, 0, 0, 0)); ImageDraw.Draw(hl).arc((cx-R+10, cy-R+10, cx+R-10, cy+R-10), 200, 250, fill=(255, 255, 255, 120), width=max(6, W//200))
    hl = hl.filter(ImageFilter.GaussianBlur(4))
    out_im = Image.alpha_composite(Image.alpha_composite(bg.convert('RGBA'), ov), hl).convert('RGB')
    out_im.save(out, quality=94)
if __name__ == '__main__':
    a = sys.argv; lens(a[1], a[2], *map(float, a[3:6]), zoom=float(a[6]), focus=(float(a[7]), float(a[8])) if len(a) > 8 else None)
