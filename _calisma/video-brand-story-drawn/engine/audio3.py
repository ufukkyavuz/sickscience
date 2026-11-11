# Music bed + SFX (mgaudio), then VO mix with ducking (ffmpeg). -14 LUFS.
import json, os, subprocess, sys
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
import mgaudio as mg
from mgaudio import sfx, recipes

ROOT = os.path.dirname(os.path.abspath(__file__))
TLF = sys.argv[1] if len(sys.argv) > 1 else 'timeline.json'
tl = json.load(open(os.path.join(ROOT, TLF)))
T = tl['TOTAL']
# soft solo piano, quieter during the "mom" beat
m = recipes.ambient(duration=T, flavor='piano', key='D', mode='major', prog='Imaj9 vi9 IVmaj9 V6/9', music_level=-24.0, outro=T - 4.0)
seed = 1
for kind, t0, dur in tl['sfx']:
    seed += 1
    if kind == 'pen':
        m.sfx(sfx.pen('pen', dur=max(0.3, dur), seed=seed, level=-30), at=t0, gain=-6)
    elif kind == 'tape':
        m.sfx(sfx.tape_rip(0.35, seed=seed, level=-28), at=max(0, t0 - 0.12), gain=-6)
    elif kind == 'whoosh':
        m.sfx(sfx.whoosh(0.5, kind='swoosh', seed=seed, level=-24), at=t0, gain=-4)
    elif kind == 'paper':
        m.sfx(sfx.paper('rustle', dur=0.6, seed=seed, level=-24), at=t0, gain=-3)
m.sfx(sfx.ding('E6', 'bell', 1.4, level=-26), at=tl['END_T'] + 0.6, gain=-6)
bed = os.path.join(ROOT, 'bed3.wav' if TLF != 'timeline.json' else 'bed.wav')
m.export(bed, lufs=-26.0, analyze=False)

# VO track
vo_in, flt = [], []
for i, (k, t0) in enumerate(sorted(tl['LINE_T'].items(), key=lambda x: x[1])):
    vo_in += ['-i', os.path.join(ROOT, 'vo', k + '.mp3')]
    flt.append(f'[{i + 1}:a]aresample=48000,adelay={int(t0 * 1000)}|{int(t0 * 1000)},apad[v{i}]')
n = len(tl['LINE_T'])
mixv = ''.join(f'[v{i}]' for i in range(n)) + f'amix=inputs={n}:normalize=0:duration=longest,atrim=0:{T},loudnorm=I=-16:TP=-2:LRA=7[vo]'
fc = ';'.join(flt) + ';' + mixv + ';[vo]asplit[vo1][vo2];[0:a][vo2]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[bd];[bd][vo1]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.2:LRA=9[out]'
cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-i', bed] + vo_in + ['-filter_complex', fc, '-map', '[out]', '-ar', '48000', os.path.join(ROOT, 'mix3.wav' if TLF != 'timeline.json' else 'mix.wav')]
subprocess.run(cmd, check=True)
print('mix ok')
