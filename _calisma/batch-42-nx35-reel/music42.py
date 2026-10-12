"""Music bed + SFX for batch 42 (mgaudio), -14 LUFS. No voice: the bed carries the reel.
usage: ~/motion-tools/.venv/bin/python music42.py  -> out/u42_nx35.mp4"""
import os, sys, json, subprocess
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import recipes, sfx
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'out')
cues = json.load(open(os.path.join(OUT, 'u42_nx35_cues.json'))); d, end = round(cues['duration'], 3), cues['end']
m = recipes.future_bass(duration=d, drop=2.8, outro=max(end, d - 0.6))
for k, (t, kind) in enumerate(cues['sfx']):
    if kind == 'whoosh': m.sfx(sfx.whoosh(dur=.45, kind='swish', seed=k), at=t, gain=-3)
    elif kind == 'pop': m.sfx(sfx.pop('soft'), at=t, gain=-7)
    elif kind == 'thump': m.sfx(sfx.impact(kind='soft'), at=t, gain=-2)
bed = os.path.join(OUT, '_bed.wav'); m.export(bed)
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(OUT, 'u42_nx35_voice.mp4'), '-i', bed, '-filter_complex',
                '[1:a]aresample=48000,loudnorm=I=-14:TP=-1.5:LRA=11[a]', '-map', '0:v', '-map', '[a]',
                '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', os.path.join(OUT, 'u42_nx35.mp4')], check=True)
os.remove(bed); print('->', os.path.join(OUT, 'u42_nx35.mp4'))
