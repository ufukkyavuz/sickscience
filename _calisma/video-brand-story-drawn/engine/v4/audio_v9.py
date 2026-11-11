# v9 mix (2026-11-10, new music per client: warm lo-fi instead of the explainer bed) for the whole film (opening clip + notebook), pen scratches while writing,
# narration (Brielle, 4 parts) starting after the notebook has opened, ducked bed under the voice.
# usage: python audio_v6.py OPEN_CLIP_SECONDS NOTEBOOK_SECONDS OUT.wav
import json, os, subprocess, sys
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import sfx, recipes
R = os.path.dirname(os.path.abspath(__file__))
OFF, NB, OUT = float(sys.argv[1]), float(sys.argv[2]), sys.argv[3]
T = OFF + NB
import animatic_human as h                                 # element schedule = when the pen actually writes
m = recipes.lofi(duration=T, bpm=92, key='D', mode='major', music_level=-23.0, outro=T - 3.0, flavor='chill', vinyl=False)
for tp in h.ar.PUNCH: m.sfx(sfx.swish(dur=0.18, seed=int(tp * 10), level=-30), at=OFF + tp - 0.1, gain=-9)
last = -9
for i, e in enumerate(h.EL):
    if e['kind'] in ('hl', 'fill'):
        m.sfx(sfx.pen('marker', dur=max(0.2, e['dur']), seed=i, level=-32), at=OFF + e['start'], gain=-6)
    elif e['start'] - last > 0.25:                           # one scratch per pen-down group, not per tiny stroke
        m.sfx(sfx.pen('pen', dur=max(0.25, min(1.6, e['dur'] * 3)), seed=i, level=-31), at=OFF + e['start'], gain=-7)
        last = e['start']
m.sfx(sfx.paper('slide', dur=0.5, seed=3, level=-22), at=1.6, gain=-2)          # hand reaches the cover
m.sfx(sfx.paper('rustle', dur=0.7, seed=5, level=-21), at=2.3, gain=-1)        # cover swings open
m.sfx(sfx.paper('slide', dur=0.4, seed=7, level=-24), at=3.4, gain=-4)          # cover lands
bed = os.path.join(R, 'bed_v9.wav'); m.export(bed, lufs=-26.0, analyze=False)
L = int((OFF + h.ar.LEAD) * 1000)
fc = (f'[1:a]aresample=48000,adelay={L}|{L},apad,atrim=0:{T},loudnorm=I=-16:TP=-2:LRA=9[vo];[vo]asplit[v1][v2];'
      '[0:a][v2]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[bd];'
      '[bd][v1]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.2:LRA=9[out]')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', bed, '-i', os.path.join(R, 'vo_v5.wav'), '-filter_complex', fc, '-map', '[out]', '-ar', '48000', OUT], check=True)
print('mix ok', OUT, round(T, 2))
