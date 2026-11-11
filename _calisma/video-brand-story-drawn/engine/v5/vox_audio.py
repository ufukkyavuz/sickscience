# audio for the vox test: playful explainer bed, paper/stamp/tape SFX from events.json, narration part 1 ducking the bed.
import json, os, sys, subprocess
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import sfx, recipes
R = os.path.dirname(os.path.abspath(__file__))
EV = json.load(open(os.path.join(R, 'events.json')))
T = EV['end']; OUT = sys.argv[1]
VO = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma/video-brand-story-drawn/vo_v5/part1.mp3")
m = recipes.explainer(duration=T, key='D', mode='major', music_level=-25.0, outro=T - 2.5)
for i, e in enumerate(EV['events']):
    k, t = e['kind'], e['t']
    if k == 'slide': m.sfx(sfx.paper('slide', dur=0.32, seed=i, level=-24), at=t - 0.08, gain=-4)
    elif k == 'stamp': m.sfx(sfx.stamp(seed=i, level=-18), at=t, gain=-3)
    elif k == 'stamp_small': m.sfx(sfx.sticker_slap(seed=i, level=-22), at=t, gain=-5)
    elif k == 'pop': m.sfx(sfx.pop('cork', pitch=1.1, level=-24), at=t, gain=-6)
    elif k == 'drop': m.sfx(sfx.paper('rustle', dur=0.3, seed=i, level=-24), at=t - 0.1, gain=-4); m.sfx(sfx.sticker_slap(seed=i, level=-24), at=t, gain=-6)
    elif k == 'tape': m.sfx(sfx.tape_rip(dur=0.22, seed=i, level=-26), at=t - 0.05, gain=-6)
    elif k == 'swish': m.sfx(sfx.swish(dur=0.22, seed=i, level=-28), at=t - 0.05, gain=-8)
    elif k == 'marker': m.sfx(sfx.pen('marker', dur=e.get('dur', 0.25), seed=i, level=-26), at=t, gain=-5)
    elif k == 'wipe': m.sfx(sfx.paper('slide', dur=0.55, seed=i, level=-20), at=t - 0.3, gain=-2)
    elif k == 'boing': m.sfx(sfx.boing(pitch=1.3, dur=0.4, level=-28), at=t, gain=-8)
    elif k == 'sparkle': m.sfx(sfx.sparkle(dur=0.7, level=-28, seed=i), at=t, gain=-8)
bed = os.path.join(R, 'vox_bed.wav'); m.export(bed, lufs=-24.0, analyze=False)
L = int(EV['lead'] * 1000)
fc = (f'[1:a]aresample=48000,adelay={L}|{L},apad,atrim=0:{T},loudnorm=I=-16:TP=-2:LRA=9[vo];[vo]asplit[v1][v2];'
      '[0:a][v2]sidechaincompress=threshold=0.03:ratio=4:attack=20:release=300[bd];'
      '[bd][v1]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.2:LRA=9[out]')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', bed, '-i', VO, '-filter_complex', fc, '-map', '[out]', '-ar', '48000', OUT], check=True)
print('mix ok', OUT)
