"""Batch 53 (2026-10-17): 'just getting started' montage — real footage only (Ulta NYC visit + NetWork launch 'Welcome to The Lab').
Cuts copied from the reference reel (Saie x Sephora UK, sound GENER8ION/Yung Lean 'STORM II'), so the song can be added in Instagram and lands on the same cuts.
Usage: python build53.py [--sheet]   (sheet = one frame per shot for checking)"""
import os, sys, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__))
ULTA = os.path.expanduser('~/sickscience-work/batch-53/ulta/src/SickScience UGC-visit.mov')
ULTA2 = os.path.expanduser('~/sickscience-work/batch-53/ulta/src/448df0ca64f3492182880e3b5a203426.mov')
EVENT = os.path.join(HERE, 'src-event-reel-revised.mp4')
SONIA = os.path.join(HERE, 'src-sonia-video-cut.mp4')
TMP = os.path.expanduser('~/sickscience-work/batch-53/tmp'); os.makedirs(TMP, exist_ok=True)
CUTS = [0, 0.733, 1.667, 2.333, 3.0, 3.667, 4.333, 5.067, 5.8, 6.467, 7.2, 7.933, 8.6, 9.333, 10.067, 10.733, 11.423, 13.467]  # last = extra founders hold, ends on a song beat (13.468)
# (source, start second) per shot: founders first (user 2026-10-17), then Ulta, then the launch party
SHOTS = [
 (EVENT, 5.0),   # 1 founders Merve (blonde) + Polen (dark hair) at the Welcome wall
 (EVENT, 22.3),  # 2 Polen on the mic
 (EVENT, 24.0),  # 3 Merve on the mic
 (EVENT, 13.2),  # 4 Polen at the lab bench with a flask
 (ULTA, 17.6),   # 5 Ulta sign on the street
 (ULTA, 20.0),   # 6 walking into Ulta
 (ULTA, 25.6),   # 7 SickScience fixture in the aisle
 (ULTA, 28.0),   # 8 shelf close-up
 (ULTA, 33.6),   # 9 creator grabs a product, big grin
 (EVENT, 0.2),   # 10 launch night: lab-coat guest close-up
 (ULTA, 50.0),   # 11 creator hands-to-face at Ulta
 (SONIA, 3.5),   # 12 red dress, drinks in beakers
 (EVENT, 39.0),  # 13 guests with beaker drinks
 (ULTA, 38.0),   # 14 creator dancing in the aisle
 (EVENT, 1.2),   # 15 lab-coat guests laughing at the purple wall
 (ULTA, 54.6),   # 16 together in Ulta
 ('PUSH', 8.05), # 17 closing: Merve + Polen laughing together (end of the Welcome-wall take), slow push-in
 # NOTE: photographer IMG_0099 is NOT Merve (user 2026-10-17) — a blonde guest; never identify founders by hair colour
]
VF = {SONIA: 'crop=810:1440:(iw-810)/2:0,scale=1080:1920', None: 'scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920'}
def vf(src): return VF.get(src, VF[None]) + ',fps=30,setsar=1'

def caption():
    W, H = 1080, 1920; img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    f = ImageFont.truetype(os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Medium.otf'), 50)
    lines = ['Funny thing is, we’re just', 'getting started']; y = 400
    def layer(fill, off=0):
        L = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
        for i, ln in enumerate(lines): d.text((W / 2, y + i * 60 + off), ln, font=f, fill=fill, anchor='mt')
        return L
    glow = layer((0, 0, 0, 150)).filter(ImageFilter.GaussianBlur(12))      # soft halo so white text reads on white walls too
    tight = layer((0, 0, 0, 170), 2).filter(ImageFilter.GaussianBlur(2))
    out = Image.alpha_composite(Image.alpha_composite(glow, tight), layer((255, 255, 255, 255)))
    p = os.path.join(TMP, 'caption.png'); out.save(p); return p

PHOTO = os.path.join(HERE, 'src-founders-IMG_0099.jpg')
_base = None
def photo_base():
    # 1365x2048 photo -> crop 1152 wide around both faces -> 1080x1920; extend the plain white wall on top by 400 px so the caption sits on wall, not faces
    global _base
    if _base is None:
        from PIL import ImageOps
        im = ImageOps.exif_transpose(Image.open(PHOTO)).convert('RGB')
        im = im.crop((144, 0, 1296, 2048)).resize((1080, 1920), Image.LANCZOS)
        top = 400; out = Image.new('RGB', (1080, 1920 + top))
        out.paste(im.crop((0, 0, 1080, 6)).resize((1080, top)), (0, 0)); out.paste(im, (0, top))
        _base = out.crop((0, 0, 1080, 1920))
    return _base
def photo_frame(t):
    b = photo_base(); z = 1.0 + 0.05 * t; w, h = 1080 / z, 1920 / z; cx, cy = 540, 760   # push in toward the faces
    box = (cx - w / 2, cy - h * (760 / 1920), cx + w / 2, cy - h * (760 / 1920) + h)
    return b.resize((1080, 1920), Image.BICUBIC, box=box)

def main(sheet=False):
    parts = []
    for i, (src, st) in enumerate(SHOTS):
        dur = CUTS[i + 1] - CUTS[i]
        if src == 'PUSH':   # event clip with a slow push-in anchored below the caption (heads stay at y~700)
            nfr = round(CUTS[i + 1] * 30) - round(CUTS[i] * 30); p = os.path.join(TMP, f'p_{i:02d}.mp4')
            rd = subprocess.Popen(['ffmpeg', '-v', 'error', '-ss', f'{st:.3f}', '-i', EVENT, '-frames:v', str(nfr), '-vf', vf(EVENT), '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE)
            frames = []
            while True:
                buf = rd.stdout.read(1080 * 1920 * 3)
                if len(buf) < 1080 * 1920 * 3: break
                frames.append(Image.frombytes('RGB', (1080, 1920), buf))
            rd.wait()
            def push(im, t):
                z = 1.0 + 0.14 * t; ax, ay = 540, 700; w, h = 1080 / z, 1920 / z
                return im.resize((1080, 1920), Image.BICUBIC, box=(ax - ax / z, ay - ay / z, ax - ax / z + w, ay - ay / z + h))
            if sheet: p = os.path.join(TMP, f'sh_{i:02d}.jpg'); push(frames[len(frames) // 2], 0.5).resize((216, 384)).save(p); parts.append(p); continue
            pr = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', '1080x1920', '-r', '30', '-i', '-',
                                   '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-pix_fmt', 'yuv420p', p], stdin=subprocess.PIPE)
            for k, im in enumerate(frames): pr.stdin.write(push(im, k / max(1, len(frames) - 1)).tobytes())
            pr.stdin.close(); pr.wait(); parts.append(p); continue
        if sheet:
            p = os.path.join(TMP, f'sh_{i:02d}.jpg'); mid = st + dur / 2
            subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{mid:.3f}', '-i', src, '-frames:v', '1', '-vf', vf(src) + ',scale=216:384', p], check=True); parts.append(p); continue
        p = os.path.join(TMP, f'p_{i:02d}.mp4')
        nfr = round(CUTS[i + 1] * 30) - round(CUTS[i] * 30)          # frame-exact, so cuts never drift off the music
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{st:.3f}', '-i', src, '-frames:v', str(nfr), '-an', '-vf', vf(src),
                        '-c:v', 'libx264', '-crf', '16', '-preset', 'fast', '-pix_fmt', 'yuv420p', p], check=True)
        parts.append(p)
    if sheet:
        ims = [Image.open(p) for p in parts]; o = Image.new('RGB', (216 * 9, 384 * 2))
        for i, im in enumerate(ims): o.paste(im, ((i % 9) * 216, (i // 9) * 384))
        o.save(os.path.join(TMP, 'shots_sheet.jpg'), quality=82); print('sheet ok'); return
    lst = os.path.join(TMP, 'list.txt'); open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
    cat = os.path.join(TMP, 'cat.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', cat], check=True)
    out = os.path.join(HERE, 'SickScience – Just getting started – 9x16.mp4')
    # music: STORM II (GENER8ION & Yung Lean) from 0:21.90 = the same part the reference reel uses (envelope cross-correlation); licence confirmed by the user 2026-10-17
    song = os.path.expanduser('~/sickscience-work/batch-53/audio/storm2.mp3'); total = round(CUTS[-1] * 30) / 30
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', cat, '-i', caption(), '-ss', '21.90', '-t', f'{total:.3f}', '-i', song,
                    '-filter_complex', f'[0:v][1:v]overlay=0:0[v];[2:a]afade=t=out:st={total-0.6:.3f}:d=0.6,loudnorm=I=-14:TP=-1:LRA=11[a]',
                    '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '256k', '-ar', '44100',
                    '-shortest', '-movflags', '+faststart', out], check=True)
    print('ok', out)

if __name__ == '__main__': main('--sheet' in sys.argv)
