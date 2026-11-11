# v10 mix (2026-11-10, user: "müziği hiç sevmedim, bilindik instagram'da kullanılan bir şey koy"):
# "Once In Paris" by Pumpupthemind (Pixabay Content License, https://pixabay.com/music/beats-once-in-paris-168895/)
# + pen / cover SFX from the element schedule + Gemini narration, music ducked under the voice.
# usage: python audio_v10.py OPEN_CLIP_SECONDS NOTEBOOK_SECONDS OUT.wav
import os, subprocess, sys
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import sfx, recipes
R = os.path.dirname(os.path.abspath(__file__))
OFF, NB, OUT = float(sys.argv[1]), float(sys.argv[2]), sys.argv[3]
T = OFF + NB
TRACK = os.environ.get('TRACK') or os.path.join(R, '..', 'music', 'pumpupthemind-once-in-paris-168895.mp3')
import animatic_human as h
m = recipes.ambient(duration=T, music_level=-90.0)                     # SFX only
last = -9
for i, e in enumerate(h.EL):
    if e['kind'] in ('hl', 'fill'):
        m.sfx(sfx.pen('pen', dur=max(0.2, e['dur']), seed=i, level=-32), at=OFF + e['start'], gain=-8)   # v29: no squeaky marker
    elif e['start'] - last > 0.25:
        m.sfx(sfx.pen('pen', dur=max(0.25, min(1.6, e['dur'] * 3)), seed=i, level=-31), at=OFF + e['start'], gain=-7)
        last = e['start']
# v28: replaced by a real page-turn sample (user: "hışır hışır ses çok kötü") # m.sfx(sfx.paper('slide', dur=0.5, seed=3, level=-22), at=0.7, gain=-2)        # v27 Firefly opening: hand meets the cover
# v28: replaced by a real page-turn sample (user: "hışır hışır ses çok kötü") # m.sfx(sfx.paper('rustle', dur=0.8, seed=5, level=-21), at=1.3, gain=-1)       # cover swings over the spine
# v28: replaced by a real page-turn sample (user: "hışır hışır ses çok kötü") # m.sfx(sfx.paper('slide', dur=0.4, seed=7, level=-24), at=2.2, gain=-4)        # cover lands
fx = os.path.join(R, 'sfx_v10.wav'); m.export(fx, lufs=float(os.environ.get('FXLUFS', -30.0)), analyze=False)   # v29: -42 = much quieter writing (user)
L = int((OFF + h.ar.LEAD) * 1000)
fc = (f'[0:a]aresample=48000,asetpts=N/SR/TB,apad,atrim=0:{T},afade=t=in:d=0.4,afade=t=out:st={T - 3}:d=3,loudnorm=I=-25:TP=-2,aresample=48000[mu];'
      f'[1:a]aresample=48000,adelay={L}|{L},apad,atrim=0:{T},loudnorm=I=-16:TP=-2:LRA=9,aresample=48000[vo];[vo]asplit[v1][v2];'
      '[mu][v2]sidechaincompress=threshold=0.02:ratio=6:attack=25:release=450[bd];'
      '[2:a]aresample=48000,lowpass=f=3200,highpass=f=300[fx];[bd][v1][fx]amix=inputs=3:normalize=0:duration=first,loudnorm=I=-14:TP=-1.2:LRA=9[out]')
NOMUSIC = bool(os.environ.get('NOMUSIC'))   # 2026-11-10 user: deliver without music, music is added later
min_ = ['-f', 'lavfi', '-t', str(T), '-i', 'anullsrc=r=48000:cl=stereo'] if NOMUSIC else ['-i', TRACK]
if NOMUSIC: fc = fc.replace(',loudnorm=I=-25:TP=-2,aresample=48000[mu]', '[mu]')
if os.environ.get('STEMS'):   # v32: write stems so the no-music cut keeps exactly the same voice/SFX levels as the music cut
    fc = fc.replace('[bd][v1][fx]amix=inputs=3:normalize=0:duration=first,loudnorm=I=-14:TP=-1.2:LRA=9[out]', '')
    fc = fc.rstrip(';')
    b = OUT.replace('.wav', '')
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *min_, '-i', os.path.join(R, 'vo_v5.wav'), '-i', fx, '-filter_complex', fc,
                    '-map', '[bd]', '-ar', '48000', b + '_music.wav', '-map', '[v1]', '-ar', '48000', b + '_vo.wav', '-map', '[fx]', '-ar', '48000', b + '_fx.wav'], check=True)
else:
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *min_, '-i', os.path.join(R, 'vo_v5.wav'), '-i', fx, '-filter_complex', fc, '-map', '[out]', '-ar', '48000', OUT], check=True)
print('mix ok', OUT, round(T, 2))
