"""Music bed + SFX for the u29 variants with mgaudio (~/motion-tools), then the final mix under the voices.
usage: ~/motion-tools/.venv/bin/python music29.py v1 [v2 ...]
reads out/u32_<v>_cues.json + out/u32_<v>_voice.mp4 -> out/u32_<v>.mp4 (music ducked under speech, -14 LUFS)"""
import os, sys, json, subprocess
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import recipes, sfx

HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, 'out')
# one recipe per variant so the four ads don't sound alike
BEDS = {
    'g1': lambda d, e: recipes.lofi(duration=d, drop=1.0, outro=e, keys='rhodes', flavor='chill'),
    'g2': lambda d, e: recipes.future_bass(duration=d, drop=1.0, outro=e),
    'g4': lambda d, e: recipes.explainer(duration=d, drop=1.0, outro=e),
    'g3': lambda d, e: recipes.ambient(duration=d, drop=1.0, outro=e, flavor='product'),
}

def bed(v):
    cues = json.load(open(os.path.join(OUT, f'u32_{v}_cues.json')))
    d, end = round(cues['duration'], 3), cues['end']
    m = BEDS[v](d, max(end, d - 0.6))           # keep the bed playing under the end card (no silent tail)
    for k, (t, kind) in enumerate(cues['sfx']):
        if kind == 'whoosh': m.sfx(sfx.whoosh(dur=.45, kind='swish', seed=k), at=t, gain=-3)
        elif kind == 'pop': m.sfx(sfx.pop('soft'), at=t, gain=-7)
        elif kind == 'thump': m.sfx(sfx.impact(kind='soft'), at=t, gain=-2)
    path = os.path.join(OUT, f'_bed_{v}.wav'); m.export(path)
    return path

def mix(v, bedwav):
    voice = os.path.join(OUT, f'u32_{v}_voice.mp4'); out = os.path.join(OUT, f'u32_{v}.mp4')
    fc = ('[0:a]aresample=48000,asplit=2[v1][v2];'
          '[1:a]volume=-11dB[b];'
          '[b][v1]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=350:makeup=1[bd];'
          '[v2][bd]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', voice, '-i', bedwav, '-filter_complex', fc,
                    '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '192k', out], check=True)
    os.remove(bedwav); print(v, '->', out)

if __name__ == '__main__':
    for v in sys.argv[1:] or list(BEDS): mix(v, bed(v))
