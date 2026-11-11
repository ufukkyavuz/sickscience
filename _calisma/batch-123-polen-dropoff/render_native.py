# Same cut/captions as render.py, but no RGB round trip: segments cut straight from the source YUV (BT.709), captions as an
# RGBA overlay, colour tags kept (2026-11-10, user: "renkleri bozmuştun, düzelt").
import os, subprocess, sys
sys.argv = [sys.argv[0]]
import importlib.util
from PIL import Image
R = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(R, 'render.py')).read(); src = src[:src.index("out = os.path.join(R, 'video_noaudio.mp4')")]
g = {'__file__': os.path.join(R, 'render.py')}; exec(src, g)
SEG, END, FPS, W, H, caption, SRC = g['SEG'], g['END'], g['FPS'], g['W'], g['H'], g['caption'], g['SRC']
ins, fl, labs, total = [], [], [], 0
for i, (t0, s0, s1) in enumerate(SEG):
    t1 = SEG[i + 1][0] if i + 1 < len(SEG) else END
    n = int(round((t1 - t0) * FPS)); total += n
    ins += ['-ss', str(s0), '-t', str(s1 - s0 + 0.5), '-i', SRC]
    fl.append(f'[{i}:v]hflip,scale={W}:{H}:flags=lanczos,fps={FPS},tpad=stop_mode=clone:stop_duration=2,trim=end_frame={n},setpts=PTS-STARTPTS[s{i}]'); labs.append(f'[s{i}]')
k = len(SEG)
fl.append(''.join(labs) + f'concat=n={k}:v=1:a=0[base]'); fl.append(f'[base][{k}:v]overlay=format=yuv420[v]')
cmd = ['ffmpeg', '-v', 'error', '-y', *ins, '-f', 'rawvideo', '-pix_fmt', 'rgba', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-', '-i', os.path.join(R, 'mix.wav'),
       '-filter_complex', ';'.join(fl), '-map', '[v]', '-map', f'{k + 1}:a', '-c:v', 'libx264', '-crf', '17', '-pix_fmt', 'yuv420p',
       '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-c:a', 'aac', '-b:a', '192k', '-frames:v', str(total), '-movflags', '+faststart',
       os.path.join(R, 'polen_dropoff_native.mp4')]
p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
for i in range(total):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); p.stdin.write(caption(im, i / FPS).tobytes())
p.stdin.close(); p.wait(); print('frames', total, p.returncode)
