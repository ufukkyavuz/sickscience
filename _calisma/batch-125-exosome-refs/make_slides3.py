# v3 (2026-11-10): media = CLIENT's own NX35 exosome animation (Brand Assets/Images/ShapeShift/Animations) + REAL clinical
# scalp micrographs (Brand Assets/Images/PowerCycle/Before After/Hair Before After Clinical Macro Shot). Nothing self-generated.
import os, subprocess
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_slides2.py')).read()
exec(src[:src.index('def render(')])
OUT = os.path.join(R, 'out3'); os.makedirs(OUT, exist_ok=True)
BA = os.path.join(os.path.dirname(ROOT), 'SickScience Brand Assets')
NX = os.path.join(R, 'client', 'NX35_-_Desktop.mp4')
SC = os.path.join(BA, 'Images', 'PowerCycle', 'Before After', 'Hair Before After Clinical Macro Shot')
WHITE = (255, 255, 255, 255)
def enc(out, fl, inputs, extra=()):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', fl, '-map', '[o]', '-t', '8', '-r', '30', '-c:v', 'libx264', '-crf', '14',
                    '-preset', 'slow', '-pix_fmt', 'yuv420p', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-colorspace', 'bt709', '-movflags', '+faststart', out], check=True)
    print(out)
def nx(name, ss, dur, x0, flip, layout, ov, white=False):
    """client animation window [ss, ss+dur] text-free -> boomerang -> 4:5 crop 864x1080 at x0 (1.25x), no AI"""
    band = 470
    if layout == 'v2': ov, band = ov
    ovp = os.path.join(OUT, name + '_text.png'); ov.save(ovp)
    f = 'hflip,' if flip else ''
    base = (f'[0:v]trim=0:{dur},setpts=2.2*(PTS-STARTPTS),minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:vsbmc=1,split[a][b];[b]reverse,setpts=PTS-STARTPTS[r];[a][r]concat=n=2:v=1:a=0,loop=loop=4:size=600:start=0,'
            f'crop=864:1080:{x0}:0,scale={W}:{H}:flags=lanczos,fps=30,setsar=1,{f}format=yuv420p[v]').replace(',,', ',')
    if layout == 'v2':
        fl = base + f';[v]split[a][b];[b]crop=1080:{band}:0:0,gblur=sigma=30,drawbox=x=0:y=0:w=1080:h={band}:color=white@0.80:t=fill[bd];[a][bd]overlay=0:0[c];[c][1:v]overlay=0:0,format=yuv420p[o]'
        enc(os.path.join(OUT, name + '.mp4'), fl, ['-ss', str(ss), '-t', str(dur), '-i', NX, '-loop', '1', '-t', '8', '-i', ovp])
    else:
        fl = base + ';[v][1:v]overlay=0:0,format=yuv420p[o]'
        enc(os.path.join(OUT, name + '.mp4'), fl, ['-ss', str(ss), '-t', str(dur), '-i', NX, '-loop', '1', '-t', '8', '-i', ovp])
def label(txt):
    lay = Image.new('RGBA', (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay); f = font('Semibold', 44)
    sh = Image.new('L', (W, H), 0); ImageDraw.Draw(sh).text((60, H - 130 + 3), txt, font=f, fill=200); lay.paste((0, 0, 0), (0, 0), sh.filter(ImageFilter.GaussianBlur(8)))
    d.text((60, H - 130), txt, font=f, fill=WHITE); return lay
def scalp(name, a, b, ov, la, lb):
    ovp = os.path.join(OUT, name + '_text.png'); ov[0].save(ovp); band = ov[1]
    for k, t in (('a', la), ('b', lb)): label(t).save(os.path.join(OUT, f'{name}_{k}.png'))
    crop = 'crop=1396:1745:464:0,scale=1176:1470,'
    z = "zoompan=z='1+0.07*on/240':x='(iw-1080)/2':y='(ih-1350)/2':d=1:s=1080x1350:fps=30"
    fl = (f'[0:v]{crop}{z},setsar=1[A];[1:v]{crop}{z},setsar=1[B];[A][B]xfade=transition=fade:duration=1.4:offset=3.2[v];'
          f'[v]split[a][b];[b]crop=1080:{band}:0:0,gblur=sigma=30,drawbox=x=0:y=0:w=1080:h={band}:color=white@0.42:t=fill[bd];[a][bd]overlay=0:0[c];[c][2:v]overlay=0:0[d];'
          f"[d][3:v]overlay=0:0:enable='lt(t,3.6)'[e];[e][4:v]overlay=0:0:enable='gte(t,3.6)',format=yuv420p[o]")
    imgs = []
    for f in (a, b): imgs += ['-loop', '1', '-framerate', '30', '-t', '8', '-i', os.path.join(SC, f)]
    enc(os.path.join(OUT, name + '.mp4'), fl, imgs + ['-loop', '1', '-t', '8', '-i', ovp, '-loop', '1', '-t', '8', '-i', os.path.join(OUT, name + '_a.png'), '-loop', '1', '-t', '8', '-i', os.path.join(OUT, name + '_b.png')])

INK = (255, 255, 255, 255)
# ---------------- A: "Your cells talk" ----------------
nx('A1_hook', 8.4, 1.0, 528, False, 'v1', text_v1([('x', 'SKIP THE SURFACE'), ('v', 'SPEAK TO THE CELL')],
   'NX35™ is our plant exosome technology: carriers that deliver specific coded messages to cells at a molecular level.'))
INK = (18, 18, 22, 255)
nx('A2_carriers', 5.1, 0.7, 528, False, 'v2', text_v2('1/1000th the size of a cell', 'Exosomes are incredibly minuscule, allowing them to easily navigate and deliver signals where it\'s needed most.'))
nx('A3_plant', 32.0, 0.5, 528, False, 'v2', text_v2('100% plant-derived and vegan', 'NX35™ is a marvel of biomimetics: the science of mimicking natural functions in our bodies.'))
scalp('A4_micro', 'Scalp 18 - Day 0.jpg', 'Scalp 18 - Day 56.jpg', text_v2('Under the microscope', 'NX35 Growth Technology uses bioengineered plant-derived exosomes to carry active growth signals directly into the hair follicle.', True), 'DAY 0', 'DAY 56')
# ---------------- B: "text messages for your cells" ----------------
INK = (255, 255, 255, 255)
nx('B1_hook', 8.0, 0.9, 300, True, 'v1', text_v1([(None, 'Exosomes are like text'), (None, 'messages for your cells')], '(hear us out)'))
INK = (18, 18, 22, 255)
nx('B2_network', 5.2, 0.6, 300, True, 'v2', text_v2('Your Skin\'s Messaging Network', 'A text is tiny, carries a coded message, and lands exactly where it\'s sent. Exosomes work the same way: carriers that deliver specific coded messages to cells.'))
scalp('B3_micro', 'Scalp 12 - Day 0.jpg', 'Scalp 12 - Day 56.jpg', text_v2('Don\'t Forget the Messenger', 'A message with no carrier never arrives. That\'s the job of an exosome: built to navigate and deliver signals where it\'s needed most.'), 'DAY 0', 'DAY 56')
nx('B4_effect', 35.0, 0.6, 528, False, 'v2', text_v2('The NX35™ Effect', 'Our NX35™ technology targets specific cells and delivers "coded" messages. 100% plant-derived and vegan.', True))
