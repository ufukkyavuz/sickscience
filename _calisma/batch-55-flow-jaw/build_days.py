"""ShapeShift day-by-day (copy of TikTok @itsedonna 'Plump under eyes in a week?' flow + its sound 'Two steps ahead').
Ref flow: hook 0-3 · result tease 3-4.4 · Before 4.4-6.1 · daily application with Day labels 6.1-15.8 · result 15.8-18.4 · product 18.4-end.
Ours ends at 20.0 s (≤20 s rule). AI footage (Veo + Higgsfield edit) -> 'Simulated results.' small at the bottom (house rule)."""
import os, sys, subprocess
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends'))
from trendkit import text_layer, font
from PIL import Image, ImageDraw
H = os.path.dirname(os.path.abspath(__file__)); C = os.path.expanduser('~/sickscience-work/flow-jaw/clips'); T = os.path.join(H, 'tmp'); os.makedirs(T, exist_ok=True)
STILL = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma/batch-47-characters/w_ss_leila.png")
BEFORE = os.path.join(H, 'before.png')
LOGO = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma/video-01-bcrf/assets/logo.png")
HOOK, APPLY = os.path.join(C, 'jaw_hook.mp4'), os.path.join(C, 'jaw_apply.mp4')
VF = 'scale=1080:1920:flags=lanczos,fps=30,setsar=1'
CUTS = [0, 3.04, 4.45, 6.11, 7.50, 8.89, 10.28, 11.67, 13.06, 14.45, 15.84, 18.37, 20.0]
# (kind, src, start, label)
D = os.path.join(H, 'days')
# each day = its own Higgsfield still (different day, outfit, light), jaw a touch more defined each time; handheld drift so it feels filmed
SHOTS = [('clip', HOOK, 0.0, None), ('clip', HOOK, 5.4, None), ('still', BEFORE, 0, 'Before'),
         ('day', os.path.join(D, 'd01.png'), 0, 'Day 1'), ('day', os.path.join(D, 'd03.png'), 1, 'Day 3'), ('day', os.path.join(D, 'd05.png'), 2, 'Day 5'),
         ('day', os.path.join(D, 'd07.png'), 3, 'Day 7'), ('day', os.path.join(D, 'd09.png'), 4, 'Day 9'), ('day', os.path.join(D, 'd11.png'), 5, 'Day 11'),
         ('day', os.path.join(D, 'd14.png'), 6, 'Day 14'), ('clip', HOOK, 5.2, '2 weeks later'), ('product', STILL, 0, None)]
def sim():
    L = Image.new('RGBA', (1080, 1920), (0, 0, 0, 0)); d = ImageDraw.Draw(L)
    d.text((540, 1890), 'Simulated results.', font=font('Regular', 22), fill=(255, 255, 255, 230), anchor='mb', stroke_width=1, stroke_fill=(60, 50, 50))
    return L
def overlay(i, label):
    o = sim()
    if i == 0: o = Image.alpha_composite(o, text_layer(['sculpted-looking jawline', 'in 2 weeks?'], 330, style='Medium', size=64))
    if label: o = Image.alpha_composite(o, text_layer([label], 1000, style='Medium', size=58))
    if SHOTS[i][0] == 'product':
        o = Image.alpha_composite(text_layer(['ShapeShift'], 372, style='Bold', size=96, fill=(18, 14, 24), halo=0), text_layer(['V-Line Jaw Defining Serum'], 490, style='Regular', size=44, fill=(18, 14, 24), halo=0))
        lg = Image.open(LOGO).convert('RGBA'); lw = 330; lg = lg.resize((lw, round(lg.height * lw / lg.width)), Image.LANCZOS)
        o.alpha_composite(lg, ((1080 - lw) // 2, 288))   # dark logo (Sick black + Science magenta) on the white card, inside the Story safe band
    p = os.path.join(T, f'o{i}.png'); o.save(p); return p
def run(c): subprocess.run(c, check=True)
def still_clip(src, nfr, ov, out, z0=1.0, z1=1.04, crop916=False):
    im = Image.open(src).convert('RGB')
    if crop916:   # extend the white studio backdrop on top (repeat the top row) so the name/claim sit on white, then crop 9:16
        ext = round(im.height * 0.075); big = Image.new('RGB', (im.width, im.height + ext)); big.paste(im.crop((0, 0, im.width, 2)).resize((im.width, ext)), (0, 0)); big.paste(im, (0, ext)); im = big
        if im.height > im.width * 16 / 9: im = im.crop((0, 0, im.width, round(im.width * 16 / 9)))
    im = im.resize((1080, 1920), Image.LANCZOS); sp = os.path.join(T, os.path.basename(out) + '.png'); im.save(sp)
    run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', sp, '-i', ov, '-frames:v', str(nfr), '-filter_complex',
         f"[0:v]scale=2160:3840,zoompan=z='{z0}+{(z1 - z0) / max(1, nfr)}*on':x='iw/2-(iw/zoom/2)':y='ih*0.5-(ih/zoom*0.5)':d=1:s=1080x1920:fps=30[b];[b][1:v]overlay=0:0",
         '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', out])
def day_clip(src, nfr, ov, out, k):
    """handheld feel: slow push-in with a small drift; direction alternates per day"""
    im = Image.open(src).convert('RGB').resize((1080, 1920), Image.LANCZOS); sp = os.path.join(T, os.path.basename(out) + '.png'); im.save(sp)
    dx = 0.03 if k % 2 == 0 else -0.03
    run(['ffmpeg', '-v', 'error', '-y', '-loop', '1', '-i', sp, '-i', ov, '-frames:v', str(nfr), '-filter_complex',
         f"[0:v]scale=2160:3840,zoompan=z='1.04+0.0016*on':x='iw/2-(iw/zoom/2)+iw*{dx}*on/{nfr}+iw*0.004*sin(on/5)':y='ih*0.5-(ih/zoom*0.5)+ih*0.003*cos(on/6)':d=1:s=1080x1920:fps=30[b];[b][1:v]overlay=0:0",
         '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', out])
parts = []
for i, (kind, src, st, label) in enumerate(SHOTS):
    nfr = round(CUTS[i + 1] * 30) - round(CUTS[i] * 30); out = os.path.join(T, f'p{i:02d}.mp4'); ov = overlay(i, label)
    if kind == 'clip':
        run(['ffmpeg', '-v', 'error', '-y', '-ss', str(st), '-i', src, '-i', ov, '-frames:v', str(nfr), '-an', '-filter_complex', f'[0:v]{VF}[b];[b][1:v]overlay=0:0',
             '-c:v', 'libx264', '-crf', '16', '-pix_fmt', 'yuv420p', out])
    elif kind == 'still': still_clip(src, nfr, ov, out, 1.0, 1.05)
    elif kind == 'day': day_clip(src, nfr, ov, out, st)
    else: still_clip(src, nfr, ov, out, 1.0, 1.04, crop916=True)
    parts.append(out)
open(os.path.join(T, 'list.txt'), 'w').write(''.join(f"file '{x}'\n" for x in parts))
cat = os.path.join(T, 'cat.mp4'); run(['ffmpeg', '-v', 'error', '-y', '-f', 'concat', '-safe', '0', '-i', os.path.join(T, 'list.txt'), '-c', 'copy', cat])
out = os.path.join(H, 'SickScience – ShapeShift day by day (Veo) – 9x16.mp4')
run(['ffmpeg', '-v', 'error', '-y', '-i', cat, '-t', '20.0', '-i', os.path.join(H, 'ref.webm'), '-filter_complex', '[1:a]afade=t=out:st=19.4:d=0.6,loudnorm=I=-14:TP=-1:LRA=11[a]',
     '-map', '0:v', '-map', '[a]', '-c:v', 'copy', '-c:a', 'aac', '-b:a', '256k', '-ar', '44100', '-shortest', '-movflags', '+faststart', out])
print('ok', out)
