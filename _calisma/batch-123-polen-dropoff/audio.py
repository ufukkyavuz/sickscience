import os, sys, subprocess
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import recipes
R = os.path.dirname(os.path.abspath(__file__)); T = 20.4
m = recipes.lofi(duration=T, bpm=88, key='F', mode='major', music_level=-22.0, outro=T - 1.5, flavor='chill', vinyl=False)
bed = os.path.join(R, 'bed.wav'); m.export(bed, lufs=-26.0, analyze=False)
fc = ('[1:a]aresample=48000,apad,atrim=0:20.4,loudnorm=I=-16:TP=-2[vo];[vo]asplit[v1][v2];'
      '[0:a][v2]sidechaincompress=threshold=0.03:ratio=5:attack=20:release=300[bd];[bd][v1]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.2[o]')
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', bed, '-i', os.path.join(R, 'vo.mp3'), '-filter_complex', fc, '-map', '[o]', '-ar', '48000', os.path.join(R, 'mix.wav')], check=True)
print('ok')
