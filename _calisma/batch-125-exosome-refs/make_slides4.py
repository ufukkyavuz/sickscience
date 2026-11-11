# v4 (2026-11-10): client's OWN portrait NX35 animation (Brand Assets/Images/ShapeShift/Animations/NX35 - Mobile) with its own burned-in copy,
# 4:5 centre crop of the 2:3 master; real clinical scalp micrographs with a text band. Nothing self-generated.
import os, subprocess
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_slides3.py')).read()
exec(src[:src.index("INK = (255, 255, 255, 255)\n# ---------------- A:")])
OUT = os.path.join(R, 'out4'); os.makedirs(OUT, exist_ok=True)
NM = os.path.join(R, 'client', 'NX35_-_Mobile.mp4')
def clip(name, ss, dur):
    out = os.path.join(OUT, name + '.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(ss), '-t', str(dur), '-i', NM, '-vf',
                    f'crop=600:750:0:75,scale={W}:{H}:flags=lanczos,fps=30,setsar=1,format=yuv420p', '-an', '-c:v', 'libx264', '-crf', '12', '-preset', 'slow',
                    '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-movflags', '+faststart', out], check=True); print(out)
INK = (18, 18, 22, 255)
# A
clip('A1_intro', 0, 9); clip('A2_science', 9, 12); clip('A4_more', 34, 7)
scalp('A3_micro', 'Scalp 18 - Day 0.jpg', 'Scalp 18 - Day 56.jpg', text_v2('Under the microscope', 'NX35 Growth Technology uses bioengineered plant-derived exosomes to carry active growth signals directly into the hair follicle.', True), 'DAY 0', 'DAY 56')
# B
clip('B1_messages', 21, 7); clip('B3_what', 28, 6)
scalp('B2_micro', 'Scalp 12 - Day 0.jpg', 'Scalp 12 - Day 56.jpg', text_v2('Don\'t Forget the Messenger', 'A message with no carrier never arrives. That\'s the job of an exosome: built to navigate and deliver signals where it\'s needed most.'), 'DAY 0', 'DAY 56')
