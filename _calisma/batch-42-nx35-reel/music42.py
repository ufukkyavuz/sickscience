"""Music bed + SFX for batch 42 (mgaudio), -14 LUFS.
usage: ~/motion-tools/.venv/bin/python music42.py [u42_nx35|u42b]
  u42_nx35 = montage (no voice); u42b = UGC hybrid (music ducked under the creators' voices)"""
import os, sys, json, subprocess
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import recipes, sfx
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'out')
v = sys.argv[1] if len(sys.argv) > 1 else 'u42_nx35'
cues = json.load(open(os.path.join(OUT, f'{v}_cues.json'))); d, end = round(cues['duration'], 3), cues['end']
m = (recipes.lofi(duration=d, drop=1.0, outro=max(end, d - 0.6), keys='rhodes', flavor='chill') if v == 'u42b'
     else recipes.future_bass(duration=d, drop=2.8, outro=max(end, d - 0.6)))
for k, (t, kind) in enumerate(cues['sfx']):
    if kind == 'whoosh': m.sfx(sfx.whoosh(dur=.45, kind='swish', seed=k), at=t, gain=-3)
    elif kind == 'pop': m.sfx(sfx.pop('soft'), at=t, gain=-7)
    elif kind == 'thump': m.sfx(sfx.impact(kind='soft'), at=t, gain=-2)
bed = os.path.join(OUT, f'_bed_{v}.wav'); m.export(bed)
src = os.path.join(OUT, f'{v}_voice.mp4'); out = os.path.join(OUT, f'{v}.mp4')
if v == 'u42b':
    fc = ('[0:a]aresample=48000,asplit=2[v1][v2];[1:a]volume=-11dB[b];'
          '[b][v1]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=350:makeup=1[bd];'
          '[v2][bd]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]')
else:
    fc = '[1:a]aresample=48000,loudnorm=I=-14:TP=-1.5:LRA=11[a]'
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-i', bed, '-filter_complex', fc, '-map', '0:v', '-map', '[a]',
                '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', out], check=True)
os.remove(bed); print('->', out)
