"""ShapeShift jawline close-up (TikTok 'plump under eyes' format adapted). Veo 3.1 Fast in Flow, first frame = Leila w_ss_leila crop.
No Day labels / no before-after (AI footage). Close on the real studio still (product label as generated + checked). Music: mgaudio ambient/product."""
import os, sys, subprocess
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends')); sys.path.insert(0, os.path.expanduser('~/motion-tools/mg-styles-15/lib/audio'))
from trendkit import text_layer
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__)); C = os.path.join(H, '..', 'clips'); T = os.path.join(H, 'tmp'); os.makedirs(T, exist_ok=True)
STILL = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma/batch-47-characters/w_ss_leila.png")
VF = 'scale=1080:1920:flags=lanczos,fps=30,setsar=1'
SEG = [('jaw_hook', 0.0, 2.6), ('jaw_apply', 3.2, 3.2), ('jaw_hook', 4.6, 3.0), ('jaw_apply', 6.4, 1.6)]
HOOK = text_layer(['sculpted-looking jawline', 'in 2 weeks?'], 330, style='Medium', size=64)
END = Image.alpha_composite(text_layer(['ShapeShift'], 300, style='Bold', size=96, fill=(18, 14, 24), halo=0), text_layer(['V-Line Jaw Defining Serum'], 420, style='Regular', size=44, fill=(18, 14, 24), halo=0))
def run(c): subprocess.run(c, check=True)
parts = []
for i, (n, st, d) in enumerate(SEG):
    p = os.path.join(T, f'p{i}.mp4'); nfr = round(d * 30)
    if i == 0:
        HOOK.save(os.path.join(T, 'hook.png'))
        run(['ffmpeg', '-v', 'error', '-y', '-ss', str(st), '-i', os.path.join(C, n + '.mp4'), '-i', os.path.join(T, 'hook.png'), '-frames:v', str(nfr), '-an',
             '-filter_complex', f'[0:v]{VF}[b];[b][1:v]overlay=0:0', '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', p])
    else:
        run(['ffmpeg', '-v', 'error', '-y', '-ss', str(st), '-i', os.path.join(C, n + '.mp4'), '-frames:v', str(nfr), '-an', '-vf', VF, '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', p])
    parts.append(p)
# closing: real studio still, slow push-in, product name
im = Image.open(STILL).convert('RGB'); im = im.crop((0, 0, im.width, round(im.width * 16 / 9))) if im.height > im.width * 16 / 9 else im
im = im.resize((1080, 1920), Image.LANCZOS); im.save(os.path.join(T, 'still.png')); END.save(os.path.join(T, 'end.png'))
p = os.path.join(T, 'p4.mp4')
run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', os.path.join(T, 'still.png'), '-i', os.path.join(T, 'end.png'), '-frames:v', '78',
     '-filter_complex', "[0:v]scale=2160:3840,zoompan=z='1+0.0008*on':x='iw/2-(iw/zoom/2)':y='ih*0.55-(ih/zoom*0.55)':d=1:s=1080x1920:fps=30[b];[b][1:v]overlay=0:0",
     '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', p]); parts.append(p)
open(os.path.join(T, 'list.txt'), 'w').write(''.join(f"file '{x}'\n" for x in parts))
cat = os.path.join(T, 'cat.mp4'); run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', os.path.join(T, 'list.txt'), '-c', 'copy', cat])
dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', cat]))
import mgaudio as mg
from mgaudio import recipes, sfx
m = recipes.ambient(duration=dur, flavor='product', drop=2.6, outro=dur - 2.6)
m.sfx(sfx.whoosh(dur=.6, kind='soft'), at=2.6, gain=-6); m.sfx(sfx.shimmer_hit(), at=dur - 2.6, gain=-3)
wav = os.path.join(T, 'music.wav'); m.export(wav)
out = os.path.join(H, 'SickScience – ShapeShift jawline close-up (Veo) – 9x16.mp4')
run(['ffmpeg', '-v', 'error', '-y', '-i', cat, '-i', wav, '-map', '0:v', '-map', '1:a', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k', '-shortest', '-movflags', '+faststart', out])
print('ok', out, dur)
