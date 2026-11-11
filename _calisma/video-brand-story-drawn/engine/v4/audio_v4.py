import json, os, subprocess, sys
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
import mgaudio as mg
from mgaudio import sfx, recipes
R = os.path.dirname(os.path.abspath(__file__))
tl = json.load(open(os.path.join(R, 'anim_timeline.json')))
T = tl['TOTAL']; BT = tl['BT']
m = recipes.ambient(duration=T, flavor='piano', key='D', mode='major', prog='Imaj9 vi9 IVmaj9 V6/9', music_level=-24.0, outro=T - 4.0)
for i, t0 in enumerate(BT[1:-1], 1):
    nxt = BT[i + 1] if i + 1 < len(BT) else T
    dur = max(0.5, min(2.2, (nxt - t0) * 0.75))
    m.sfx(sfx.pen('pen', dur=dur, seed=i, level=-30), at=t0, gain=-6)
m.sfx(sfx.whoosh(0.45, kind='swoosh', seed=3, level=-26), at=BT[1] - 0.45, gain=-6)
m.sfx(sfx.ding('E6', 'bell', 1.4, level=-26), at=tl['EC_T'] + 0.3, gain=-6)
bed = os.path.join(R, 'bed_v4.wav'); m.export(bed, lufs=-26.0, analyze=False)
L = int(tl['LEAD'] * 1000)
fc = (f'[1:a]aresample=48000,adelay={L}|{L},apad,atrim=0:{T},loudnorm=I=-16:TP=-2:LRA=7[vo];[vo]asplit[v1][v2];'
      '[0:a][v2]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[bd];'
      '[bd][v1]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.2:LRA=9[out]')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', bed, '-i', os.path.join(R, 'vo.wav'), '-filter_complex', fc, '-map', '[out]', '-ar', '48000', os.path.join(R, 'mix_v4.wav')], check=True)
print('mix ok')
