"""Shared builder for trend re-creations (2026-10-17): cut real footage to a reference reel's exact cut times,
overlay per-shot text (Founders Grotesk), mux the reference audio at -14 LUFS."""
import os, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
FONTS = os.path.expanduser('~/Library/Fonts')
def font(style, size): return ImageFont.truetype(os.path.join(FONTS, f'FoundersGrotesk-{style}.otf'), size)
VF = 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1'

def text_layer(lines, y, style='Bold', size=72, fill=(255, 255, 255), halo=150, gap=1.15, align='center'):
    W, H = 1080, 1920; f = font(style, size)
    def lay(col, off=0):
        L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
        for i, ln in enumerate(lines): d.text((W / 2, y + size * 0.78 + i * size * gap + off), ln, font=f, fill=col, anchor='ms')   # common baseline -> even line spacing
        return L
    out = Image.alpha_composite(lay((0, 0, 0, halo)).filter(ImageFilter.GaussianBlur(12)), lay((0, 0, 0, 170), 2).filter(ImageFilter.GaussianBlur(2)))
    return Image.alpha_composite(out, lay(fill + (255,)))

def rotated_word(word, x, y, size=150, fill=(255, 255, 255), angle=90, style='Bold'):
    """one big word turned sideways (Upside Down trend), placed with its centre at (x, y)"""
    f = font(style, size); d0 = ImageDraw.Draw(Image.new('RGBA', (10, 10))); l, t, r, b = d0.textbbox((0, 0), word, font=f)
    w, h = r - l + 40, b - t + 40; L = Image.new('RGBA', (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    sh = Image.new('RGBA', (w, h), (0, 0, 0, 0)); ImageDraw.Draw(sh).text((20 - l, 22 - t), word, font=f, fill=(0, 0, 0, 160))
    d.text((20 - l, 20 - t), word, font=f, fill=fill + (255,)); L = Image.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)), L)
    L = L.rotate(angle, expand=True, resample=Image.BICUBIC); out = Image.new('RGBA', (1080, 1920), (0, 0, 0, 0))
    out.alpha_composite(L, (int(x - L.width / 2), int(y - L.height / 2))); return out

def build(shots, cuts, audio, out, tmp, overlays=None, audio_ss=0.0, fade=0.3):
    """shots: list of (src, start_s); cuts: boundaries incl. 0 and end; overlays: list (per shot) of PIL RGBA or None."""
    os.makedirs(tmp, exist_ok=True); parts = []
    for i, shot in enumerate(shots):
        src, st = shot[0], shot[1]; pre = shot[2] + ',' if len(shot) > 2 and shot[2] else ''; post = ',' + shot[3] if len(shot) > 3 and shot[3] else ''
        nfr = round(cuts[i + 1] * 30) - round(cuts[i] * 30); p = os.path.join(tmp, f'p_{i:02d}.mp4')
        ov = overlays[i] if overlays else None
        if ov is not None:
            op = os.path.join(tmp, f'o_{i:02d}.png'); ov.save(op)
            cmd = ['ffmpeg', '-v', 'error', '-y', '-ss', f'{st:.3f}', '-i', src, '-i', op, '-frames:v', str(nfr), '-an',
                   '-filter_complex', f'[0:v]{pre}{VF}{post}[b];[b][1:v]overlay=0:0', '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-pix_fmt', 'yuv420p', p]
        else:
            cmd = ['ffmpeg', '-v', 'error', '-y', '-ss', f'{st:.3f}', '-i', src, '-frames:v', str(nfr), '-an', '-vf', pre + VF + post,
                   '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-pix_fmt', 'yuv420p', p]
        subprocess.run(cmd, check=True); parts.append(p)
    lst = os.path.join(tmp, 'list.txt'); open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
    cat = os.path.join(tmp, 'cat.mp4'); subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', cat], check=True)
    total = round(cuts[-1] * 30) / 30
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', cat, '-ss', f'{audio_ss:.3f}', '-t', f'{total:.3f}', '-i', audio,
                    '-filter_complex', f'[1:a]afade=t=out:st={max(0, total - fade):.3f}:d={fade},loudnorm=I=-14:TP=-1:LRA=11[a]',
                    '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k', '-ar', '44100', '-shortest', '-movflags', '+faststart', out], check=True)
    return out

def sheet(shots, cuts, tmp, overlays=None, cols=10):
    os.makedirs(tmp, exist_ok=True); ims = []
    for i, shot in enumerate(shots):
        src, st = shot[0], shot[1]; pre = shot[2] + ',' if len(shot) > 2 and shot[2] else ''; post = ',' + shot[3] if len(shot) > 3 and shot[3] else ''
        mid = st + (cuts[i + 1] - cuts[i]) / 2; p = os.path.join(tmp, f's_{i:02d}.png')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{mid:.3f}', '-i', src, '-frames:v', '1', '-vf', pre + VF + post, p], check=True)
        im = Image.open(p).convert('RGBA')
        if overlays and overlays[i] is not None: im = Image.alpha_composite(im, overlays[i])
        ims.append(im.convert('RGB').resize((180, 320)))
    rows = (len(ims) + cols - 1) // cols; o = Image.new('RGB', (180 * cols, 320 * rows), 'white')
    for i, im in enumerate(ims): o.paste(im, ((i % cols) * 180, (i // cols) * 320))
    p = os.path.join(tmp, 'sheet.jpg'); o.save(p, quality=82); return p
