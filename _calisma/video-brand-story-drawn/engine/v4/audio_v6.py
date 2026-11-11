# v6 mix: soft piano bed for the whole film (opening clip + notebook), pen scratches while writing,
# narration (Brielle, 4 parts) starting after the notebook has opened, ducked bed under the voice.
# usage: python audio_v6.py OPEN_CLIP_SECONDS NOTEBOOK_SECONDS OUT.wav
import json, os, subprocess, sys
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import sfx, recipes
R = os.path.dirname(os.path.abspath(__file__))
OFF, NB, OUT = float(sys.argv[1]), float(sys.argv[2]), sys.argv[3]
T = OFF + NB
import animatic_human as h                                 # element schedule = when the pen actually writes
m = recipes.ambient(duration=T, flavor='piano', key='D', mode='major', prog='Imaj9 vi9 IVmaj9 V6/9', music_level=-24.0, outro=T - 4.0)
last = -9
for i, e in enumerate(h.EL):
    if e['kind'] in ('hl', 'fill'):
        m.sfx(sfx.pen('marker', dur=max(0.2, e['dur']), seed=i, level=-32), at=OFF + e['start'], gain=-6)
    elif e['start'] - last > 0.25:                           # one scratch per pen-down group, not per tiny stroke
        m.sfx(sfx.pen('pen', dur=max(0.25, min(1.6, e['dur'] * 3)), seed=i, level=-31), at=OFF + e['start'], gain=-7)
        last = e['start']
bed = os.path.join(R, 'bed_v6.wav'); m.export(bed, lufs=-26.0, analyze=False)
L = int((OFF + h.ar.LEAD) * 1000)
fc = (f'[1:a]aresample=48000,adelay={L}|{L},apad,atrim=0:{T},loudnorm=I=-16:TP=-2:LRA=9[vo];[vo]asplit[v1][v2];'
      '[0:a][v2]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[bd];'
      '[bd][v1]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.2:LRA=9[out]')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', bed, '-i', os.path.join(R, 'vo_v5.wav'), '-filter_complex', fc, '-map', '[out]', '-ar', '48000', OUT], check=True)
print('mix ok', OUT, round(T, 2))
