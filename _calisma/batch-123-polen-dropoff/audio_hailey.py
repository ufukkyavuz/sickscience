import os, sys, subprocess
sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from mgaudio import recipes
R = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(R, 'render_hailey.py')).read(); g = {'__file__': os.path.join(R, 'render_hailey.py')}
exec(src[:src.index('F = os.path.expanduser')], g)            # VAR, HK, V0, END from the video script
HK, V0, T, VAR = g['HK'], g['V0'], g['END'], g['VAR']
m = recipes.lofi(duration=T, bpm=88, key='F', mode='major', music_level=-22.0, outro=T - 1.5, flavor='chill', vinyl=False)
bed = os.path.join(R, f'bed_{VAR}.wav'); m.export(bed, lufs=-26.0, analyze=False)
H = os.path.join(R, 'ref', 'hailey_full.mp4')
ins, parts = [], []
for k, (a, b, s, _, _) in enumerate(HK):
    ins += ['-i', H]; d = b - a
    parts.append(f'[{k + 1}:a]aresample=48000,atrim={s}:{s + d},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={d - 0.06}:d=0.06[h{k}]')
n = len(HK); vi = n + 1
fc = (';'.join(parts) + ';' + ''.join(f'[h{k}]' for k in range(n)) + f'concat=n={n}:v=0:a=1,loudnorm=I=-16:TP=-2,apad,atrim=0:{T}[hh];'
      f'[{vi}:a]aresample=48000,adelay={int(V0*1000)}|{int(V0*1000)},apad,atrim=0:{T},loudnorm=I=-16:TP=-2[vo];'
      '[hh][vo]amix=inputs=2:normalize=0:duration=first[sp];[sp]asplit[s1][s2];'
      f"[0:a]aresample=48000,volume=enable='lt(t,{HK[-1][1]})':volume=0[bd0];[bd0][s2]sidechaincompress=threshold=0.03:ratio=5:attack=20:release=300[bd];"
      '[bd][s1]amix=inputs=2:normalize=0:duration=first,loudnorm=I=-14:TP=-1.2[o]')
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', bed, *ins, '-i', os.path.join(R, 'vo_polen.wav'), '-filter_complex', fc, '-map', '[o]', '-ac', '2', '-ar', '48000', os.path.join(R, f'mix_{VAR}.wav')], check=True)
print('ok', VAR, T)
