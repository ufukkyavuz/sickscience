"""Music bed + SFX for batch 40 (mgaudio), mixed to -14 LUFS. No voice in these cuts: the bed carries them.
usage: ~/motion-tools/.venv/bin/python music40.py v1 [v2 v3]  -> out/u40_<v>.mp4"""
import os, sys, json, subprocess
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import recipes, sfx

HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'out')
BEDS = {
    'v1': lambda d, e: recipes.future_bass(duration=d, drop=1.7, outro=e),        # drop on the burn
    'v2': lambda d, e: recipes.pop(duration=d, drop=0.75, outro=e),               # drop on the catch
    'v3': lambda d, e: recipes.lofi(duration=d, drop=2.0, outro=e, keys='rhodes', flavor='chill'),
}

def bed(v):
    cues = json.load(open(os.path.join(OUT, f'u40_{v}_cues.json'))); d, end = round(cues['duration'], 3), cues['end']
    m = BEDS[v](d, max(end, d - 0.6))
    for k, (t, kind) in enumerate(cues['sfx']):
        if kind == 'whoosh': m.sfx(sfx.whoosh(dur=.45, kind='swish', seed=k), at=t, gain=-3)
        elif kind == 'pop': m.sfx(sfx.pop('soft'), at=t, gain=-6)
        elif kind == 'thump': m.sfx(sfx.impact(kind='soft'), at=t, gain=-2)
        elif kind == 'fire':
            m.sfx(sfx.static(dur=1.4, kind='tv', seed=k), at=t, gain=-16); m.sfx(sfx.paper('rustle', dur=1.2, seed=k), at=t + .1, gain=-8)
        elif kind == 'crumple': m.sfx(sfx.paper('rustle', dur=.6, seed=k), at=t, gain=-4)
    path = os.path.join(OUT, f'_bed_{v}.wav'); m.export(path); return path

def mix(v, bedwav):
    src = os.path.join(OUT, f'u40_{v}_voice.mp4'); out = os.path.join(OUT, f'u40_{v}.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-i', bedwav, '-filter_complex',
                    '[1:a]aresample=48000,loudnorm=I=-14:TP=-1.5:LRA=11[a]', '-map', '0:v', '-map', '[a]',
                    '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', '-shortest', out], check=True)
    os.remove(bedwav); print(v, '->', out)

if __name__ == '__main__':
    for v in sys.argv[1:] or list(BEDS): mix(v, bed(v))
