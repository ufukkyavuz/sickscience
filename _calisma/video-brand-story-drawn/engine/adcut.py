# <=20 s ad cut: same film, cut on VO word times. Video + bed/SFX cut at the same film times, VO re-laid, ducked, -14 LUFS.
import json, os, subprocess
R = os.path.dirname(os.path.abspath(__file__))
tl = json.load(open(os.path.join(R, 'timeline.json')))
LT = tl['LINE_T']
# (line, start, end) in VO-file seconds; start may be negative = film lead-in before the line
SEGS = [('01_P', -0.1, 4.22), ('02_M', 0.0, 1.45), ('06_M', -0.35, 4.42), ('07_P', 0.0, 1.58),
        ('08_M', 0.0, 3.08), ('10_M', 3.22, 5.22), ('11_P', 1.12, 3.75)]
tot = sum(b - a for _, a, b in SEGS)
print('total', round(tot, 2))
assert tot <= 20.0
vf, af, vo, inputs = [], [], [], ['-i', os.path.join(R, 'video_noaudio.mp4'), '-i', os.path.join(R, 'bed.wav')]
t = 0.0
for i, (k, a, b) in enumerate(SEGS):
    fa, fb = LT[k] + a, LT[k] + b
    vf.append(f'[0:v]trim={fa:.3f}:{fb:.3f},setpts=PTS-STARTPTS[v{i}]')
    af.append(f'[1:a]atrim={fa:.3f}:{fb:.3f},asetpts=PTS-STARTPTS,afade=t=in:d=0.03,afade=t=out:st={fb-fa-0.04:.3f}:d=0.04[b{i}]')
    inputs += ['-i', os.path.join(R, 'vo', k + '.mp3')]
    va, vb = max(0.0, a), b
    delay = int((t + (va - a)) * 1000)
    vo.append(f'[{i + 2}:a]aresample=48000,atrim={va:.3f}:{vb:.3f},asetpts=PTS-STARTPTS,afade=t=out:st={vb-va-0.03:.3f}:d=0.03,adelay={delay}|{delay},apad[o{i}]')
    t += b - a
n = len(SEGS)
fc = ';'.join(vf + af + vo)
fc += ';' + ''.join(f'[v{i}]' for i in range(n)) + f'concat=n={n}:v=1:a=0[vout]'
fc += ';' + ''.join(f'[b{i}]' for i in range(n)) + f'concat=n={n}:v=0:a=1,aresample=48000[bed]'
fc += ';' + ''.join(f'[o{i}]' for i in range(n)) + f'amix=inputs={n}:normalize=0:duration=longest,atrim=0:{tot:.3f},loudnorm=I=-16:TP=-2:LRA=7[vo]'
fc += ';[vo]asplit[vo1][vo2];[bed][vo2]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[bd];[bd][vo1]amix=inputs=2:normalize=0:duration=first,afade=t=out:st=' + f'{tot-0.6:.3f}' + ':d=0.6,loudnorm=I=-14:TP=-1.2:LRA=9[aout]'
out = os.path.join(R, 'ad_20s.mp4')
cmd = ['ffmpeg', '-y', '-loglevel', 'error'] + inputs + ['-filter_complex', fc, '-map', '[vout]', '-map', '[aout]',
       '-c:v', 'libx264', '-crf', '17', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', out]
subprocess.run(cmd, check=True)
print('ok', out)
