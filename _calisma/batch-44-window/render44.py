"""Batch 44 — "window / curtain" ad (ShapeShift + PowerCycle), ≤20 s.
A push-in to the lit window (Veo, first/last frame) -> B they notice the camera and close the curtains (Veo)
-> C the curtains part and both peek out with their products (Kling 3.0, first = B's last frame, last = w4_peek_v3)
-> logo + URL over C's final hold. Cuts are seamless because each clip starts on the previous clip's last frame.
usage: ~/motion-tools/.venv/bin/python render44.py  -> out/w44.mp4"""
import os, sys, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import recipes, sfx

HERE = os.path.dirname(os.path.abspath(__file__)); SS = os.path.abspath(os.path.join(HERE, '..', '..'))
CL = os.path.join(HERE, 'clips'); OUT = os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
FD = os.path.expanduser('~/Library/Fonts/'); FM = FD + 'FoundersGrotesk-Medium.otf'
LOGO = os.path.join(SS, '_calisma', 'video-01-bcrf', 'assets', 'logo.png')      # black "Sick" + magenta "Science"
W, H, FPS = 1080, 1920, 30
# (clip, in, out, speed)
SEG = [('a_pushin_veo', 0.0, 8.0, 1.7), ('b_curtain_veo', 0.0, 8.0, 1.25), ('c_peek_kling', 0.0, 8.0, 1.0)]
CARD = 2.4                                    # logo + URL over the last CARD seconds

def card_png(path):
    """transparent 1080x1920 overlay: logo + URL in the upper safe band, over the warm curtain"""
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    lg = Image.open(LOGO).convert('RGBA'); lw = 440; lg = lg.resize((lw, round(lg.height * lw / lg.width)), Image.LANCZOS)
    im.alpha_composite(lg, ((W - lw) // 2, 282))
    f = ImageFont.truetype(FM, 38); t = 'SickScienceLabs.com'; tw = d.textlength(t, font=f)
    d.text(((W - tw) / 2, 282 + lg.height + 18), t, font=f, fill=(24, 18, 22, 255))
    im.save(path)

def main():
    tmp = tempfile.mkdtemp(prefix='w44_'); durs = []
    ins, fc, vl, al = [], [], [], []
    for i, (n, a, b, sp) in enumerate(SEG):
        ins += ['-i', os.path.join(CL, n + '.mp4')]; durs.append((b - a) / sp)
        fc.append(f'[{i}:v]trim={a}:{b},setpts=(PTS-STARTPTS)/{sp},crop=iw-8:ih-4:4:2,scale={W}:{H}:force_original_aspect_ratio=increase,'
                  f'crop={W}:{H},fps={FPS},setsar=1[v{i}]')
        fc.append(f'[{i}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,atempo={sp},aresample=48000[a{i}]')
        vl.append(f'[v{i}]'); al.append(f'[a{i}]')
    total = sum(durs); card = os.path.join(tmp, 'card.png'); card_png(card)
    ins += ['-loop', '1', '-t', f'{total:.3f}', '-i', card]; k = len(SEG)
    fc.append(''.join(f'{v}{a}' for v, a in zip(vl, al)) + f'concat=n={k}:v=1:a=1[vc][ac]')
    t0 = total - CARD
    fc.append(f'[{k}:v]format=rgba,fade=t=in:st={t0 + 0.2:.3f}:d=0.4:alpha=1[cd]')
    fc.append('[vc][cd]overlay=0:0:format=auto[vo]')
    # music bed: playful lo-fi, lift when the curtains snap shut, soft outro under the card
    cut1, cut2 = durs[0], durs[0] + durs[1]
    m = recipes.lofi(duration=round(total, 3), drop=cut1, outro=t0, keys='rhodes', flavor='chill')
    m.sfx(sfx.whoosh(dur=.45, kind='swish', seed=1), at=cut2 - 0.9, gain=-6)
    m.sfx(sfx.pop('soft'), at=t0 + 0.2, gain=-6)
    bed = os.path.join(tmp, 'bed.wav'); m.export(bed); ins += ['-i', bed]
    fc.append(f'[ac]volume=-2dB[amb];[{k + 1}:a]volume=-9dB[mus];[amb][mus]amix=inputs=2:duration=first:normalize=0,'
              'loudnorm=I=-14:TP=-1.5:LRA=11[ao]')
    out = os.path.join(OUT, 'w44.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', ';'.join(fc), '-map', '[vo]', '-map', '[ao]',
                    '-t', f'{total:.3f}', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-c:a', 'aac', '-b:a', '192k', out], check=True)
    print('->', out, round(total, 2), 's')

if __name__ == '__main__':
    main()
