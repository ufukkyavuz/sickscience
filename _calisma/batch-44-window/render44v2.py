"""Batch 44 v2 — single ShapeShift "caught at the window" ad, cut like the reference (Beypazarı reel), ≤20 s.
A one continuous drone glide into the lit window (Kling 3.0 first/last) -> B locked-off window: she applies the
gel-serum, notices the camera, holds the stare (slowed to half speed), stands, pulls the curtains shut (Veo 3.1 Fast)
-> she holds the curtains shut, peeking through the gap (last half-second at 1/4 speed) under logo + URL.
usage: ~/motion-tools/.venv/bin/python render44v2.py  -> out/w44v2.mp4"""
import os, sys, subprocess, tempfile
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import recipes, sfx

HERE = os.path.dirname(os.path.abspath(__file__)); SS = os.path.abspath(os.path.join(HERE, '..', '..'))
CL = os.path.join(HERE, 'clips'); OUT = os.path.join(HERE, 'out'); os.makedirs(OUT, exist_ok=True)
FM = os.path.expanduser('~/Library/Fonts/FoundersGrotesk-Medium.otf')
LOGO = os.path.join(SS, '_calisma', 'video-01-bcrf', 'assets', 'logo.png')      # black "Sick" + magenta "Science"
W, H, FPS = 1080, 1920, 30
# (clip, in, out, speed) — the stare (2.3–3.1 s of B) runs at half speed so the "caught" beat lands
SEG = [('v2_a_pushin_kling', 0.0, 5.04, 1.15),
       ('v2_b_caught_veo', 0.0, 2.3, 1.0), ('v2_b_caught_veo', 2.3, 3.1, 0.5), ('v2_b_caught_veo', 3.1, 6.25, 1.0), ('v2_b_caught_veo', 6.25, 6.75, 0.25)]
HOLD = 0.0                                   # extra hold on the closed curtains for the card
CARD = 2.4                                   # card fades in this many seconds before the end

def tempo(sp):
    """atempo only takes 0.5–100 per stage, so chain halves for slower speeds"""
    st = []
    while sp < 0.5: st.append('atempo=0.5'); sp /= 0.5
    return ','.join(st + [f'atempo={sp}'])

def card_png(path):
    im = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    lg = Image.open(LOGO).convert('RGBA'); lw = 500; lg = lg.resize((lw, round(lg.height * lw / lg.width)), Image.LANCZOS)
    y = 330; im.alpha_composite(lg, ((W - lw) // 2, y))
    f = ImageFont.truetype(FM, 42); t = 'SickScienceLabs.com'; tw = d.textlength(t, font=f)
    d.text(((W - tw) / 2, y + lg.height + 22), t, font=f, fill=(24, 18, 22, 255))
    im.save(path)

def main():
    tmp = tempfile.mkdtemp(prefix='w44v2_'); durs, ins, fc, vl, al = [], [], [], [], []
    for i, (n, a, b, sp) in enumerate(SEG):
        ins += ['-i', os.path.join(CL, n + '.mp4')]; d = (b - a) / sp; last = i == len(SEG) - 1
        durs.append(d + (HOLD if last else 0))
        hold_v = f',tpad=stop_mode=clone:stop_duration={HOLD}' if last and HOLD else ''
        hold_a = f',apad=pad_dur={HOLD}' if last and HOLD else ''
        fc.append(f'[{i}:v]trim={a}:{b},setpts=(PTS-STARTPTS)/{sp},crop=iw-8:ih-4:4:2,scale={W}:{H}:force_original_aspect_ratio=increase,'
                  f'crop={W}:{H},fps={FPS},setsar=1{hold_v}[v{i}]')
        fc.append(f'[{i}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,{tempo(sp)},aresample=48000{hold_a}[a{i}]')
        vl.append(f'[v{i}]'); al.append(f'[a{i}]')
    total = sum(durs); card = os.path.join(tmp, 'card.png'); card_png(card); k = len(SEG)
    ins += ['-loop', '1', '-t', f'{total:.3f}', '-i', card]
    fc.append(''.join(f'{v}{a}' for v, a in zip(vl, al)) + f'concat=n={k}:v=1:a=1[vc][ac]')
    t0 = total - CARD
    fc.append(f'[{k}:v]format=rgba,fade=t=in:st={t0:.3f}:d=0.4:alpha=1[cd]')
    fc.append('[vc][cd]overlay=0:0:format=auto[vo]')
    cut1 = durs[0]; stare = cut1 + durs[1]
    m = recipes.lofi(duration=round(total, 3), drop=cut1, outro=t0, keys='rhodes', flavor='chill')
    m.sfx(sfx.pop('soft'), at=stare, gain=-8)                  # tiny accent when she looks into the lens
    m.sfx(sfx.whoosh(dur=.45, kind='swish', seed=2), at=t0 - 1.2, gain=-7)
    bed = os.path.join(tmp, 'bed.wav'); m.export(bed); ins += ['-i', bed]
    fc.append(f'[ac]volume=-1dB[amb];[{k + 1}:a]volume=-10dB[mus];[amb][mus]amix=inputs=2:duration=first:normalize=0,'
              'loudnorm=I=-14:TP=-1.5:LRA=11[ao]')
    out = os.path.join(OUT, 'w44v2.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *ins, '-filter_complex', ';'.join(fc), '-map', '[vo]', '-map', '[ao]',
                    '-t', f'{total:.3f}', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', '-c:a', 'aac', '-b:a', '192k', out], check=True)
    print('->', out, round(total, 2), 's')

if __name__ == '__main__':
    main()
