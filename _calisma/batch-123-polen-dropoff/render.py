# Polen x DropOff nightly routine (2026-11-10): Polen's own clip (front camera, mirrored -> hflip), Brielle VO,
# sentence captions, soft lo-fi bed. Hailey Bieber/TIME hook NOT used (celebrity likeness + third-party footage).
import json, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
R = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(R, 'src_polen_wa.mp4')
W, H, FPS = 1080, 1920, 30
SEG = [(0.0, 8.3, 13.0), (4.7, 13.0, 14.9), (6.6, 17.4, 19.2), (8.4, 23.0, 24.7), (10.1, 62.5, 65.0), (12.6, 67.5, 69.5), (14.6, 88.0, 90.4), (17.0, 96.0, 99.4)]
END = 20.4
F = os.path.expanduser('~/Library/Fonts/FoundersGrotesk')
fb = lambda s: ImageFont.truetype(F + '-Semibold.otf', s); fbb = lambda s: ImageFont.truetype(F + '-Bold.otf', s)
words = json.load(open(os.path.join(R, 'vo_words.json')))
LINES = [(0.0, 1.58, 'My nightly body routine.'), (1.94, 6.42, 'DropOff Body Sculpting Serum,\nmade with plant exosome technology.'),
         (6.88, 8.3, 'I smooth it on,'), (8.4, 12.1, 'then do my lymphatic drainage\nmassage with my sculpting tools.'),
         (12.74, 17.0, 'Smoother, firmer-looking skin\nand a more defined contour.'), (17.5, 20.3, 'Honestly, my favorite\npart of the night.')]
def frames(s0, s1):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(s0), '-t', str(s1 - s0), '-i', SRC, '-vf',
                          f'hflip,scale={W}:{H}:flags=lanczos,fps={FPS}', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)
def caption(im, t):
    d = ImageDraw.Draw(im)
    for a, b, s in LINES:
        if a - 0.05 <= t < b + 0.25:
            f = fb(52); y = 1110
            sh = Image.new('L', im.size, 0); sd = ImageDraw.Draw(sh)
            sd.multiline_text((W / 2, y + 4), s, font=f, fill=200, anchor='ma', align='center', spacing=10)
            im.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(10)))
            d.multiline_text((W / 2, y), s, font=f, fill=(255, 255, 255), anchor='ma', align='center', spacing=10)
    if t < 1.9:                                                     # hook, big, on her dark sweater (face stays clear)
        s = 'LYMPHATIC DRAINAGE,\nTHE AT-HOME WAY'; f = fbb(92)
        sh = Image.new('L', im.size, 0); ImageDraw.Draw(sh).multiline_text((W / 2, 820 + 6), s, font=f, fill=210, anchor='ma', align='center', spacing=6)
        im.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(14)))
        d.multiline_text((W / 2, 820), s, font=f, fill=(255, 255, 255), anchor='ma', align='center', spacing=6)
    return im
out = os.path.join(R, 'video_noaudio.mp4')
p = subprocess.Popen(['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
                      '-c:v', 'libx264', '-crf', '18', '-pix_fmt', 'yuv420p', out], stdin=subprocess.PIPE)
n = 0
for i, (t0, s0, s1) in enumerate(SEG):
    t1 = SEG[i + 1][0] if i + 1 < len(SEG) else END
    fr = frames(s0, s1); need = int(round((t1 - t0) * FPS))
    for k in range(need):
        im = Image.fromarray(fr[min(k, len(fr) - 1)]); t = (n) / FPS
        p.stdin.write(np.asarray(caption(im, t)).tobytes()); n += 1
p.stdin.close(); p.wait(); print('frames', n)
