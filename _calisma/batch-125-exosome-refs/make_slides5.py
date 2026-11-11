# v5 (2026-11-10): OneSkin reference layouts (V1 = text straight on full-bleed video, V2 = frosted top band + sharp video) with
# Pexels STOCK footage in the same pale/clear scientific look + real clinical scalp micrographs. User: "stok video bul, referanslardaki gibi olsun".
import os, subprocess
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'make_slides3.py')).read()
exec(src[:src.index("INK = (255, 255, 255, 255)\n# ---------------- A:")])
OUT = os.path.join(R, 'out5'); os.makedirs(OUT, exist_ok=True)
ST = os.path.join(R, 'stock')
INK = (18, 18, 22, 255)
def stock(name, clip, ss, crop, layout, ov, grade=''):
    """crop = 'w:h:x:y' window of the source with 4:5 aspect"""
    band = 470
    if layout == 'v2': ov, band = ov
    ovp = os.path.join(OUT, name + '_text.png'); ov.save(ovp)
    base = f'[0:v]crop={crop},scale={W}:{H}:flags=lanczos,fps=30,setsar=1{grade}[v]'
    if layout == 'v2':
        fl = base + f';[v]split[a][b];[b]crop=1080:{band}:0:0,gblur=sigma=30,drawbox=x=0:y=0:w=1080:h={band}:color=white@0.42:t=fill[bd];[a][bd]overlay=0:0[c];[c][1:v]overlay=0:0,format=yuv420p[o]'
    else:
        vp = os.path.join(OUT, name + '_veil.png'); veil().save(vp)
        fl = base + ';[v][2:v]overlay=0:0[vv];[vv][1:v]overlay=0:0,format=yuv420p[o]'
    inputs = ['-ss', str(ss), '-t', '8', '-i', os.path.join(ST, clip), '-loop', '1', '-t', '8', '-i', ovp] + (['-loop', '1', '-t', '8', '-i', vp] if layout == 'v1' else [])
    enc(os.path.join(OUT, name + '.mp4'), fl, inputs)
# vertical sources 1080x1920 -> 1080x1350 window; landscape 1920x1080 -> 864x1080 window
# ---------- A ----------
stock('A1_hook', '16040147.mp4', 0, '1080:1350:0:300', 'v1', text_v1([('x', 'SKIP THE SURFACE'), ('v', 'SPEAK TO THE CELL')],
      'NX35™ is our plant exosome technology: carriers that deliver specific coded messages to cells at a molecular level.'))
stock('A2_small', '34633541.mp4', 0.5, '864:1080:500:0', 'v2', text_v2('Small enough to go where it matters', 'Exosomes are 1/1000th the size of a cell, allowing them to easily navigate and deliver signals where it\'s needed most.'))
stock('A3_plant', '4178359.mp4', 0, '864:1080:500:0', 'v2', text_v2('100% plant-derived and vegan', 'NX35™ is a marvel of biomimetics: the science of mimicking natural functions in our bodies.'))
scalp('A4_micro', 'Scalp 18 - Day 0.jpg', 'Scalp 18 - Day 56.jpg', text_v2('Under the microscope', 'NX35 Growth Technology uses bioengineered plant-derived exosomes to carry active growth signals directly into the hair follicle.', True), 'DAY 0', 'DAY 56')
# ---------- B ----------
stock('B1_hook', '8392769.mp4', 0, '1080:1350:0:520', 'v1', text_v1([(None, 'Exosomes are like text'), (None, 'messages for your cells')], '(hear us out)'))
stock('B2_network', '8145846.mp4', 1, '2160:2700:0:900', 'v2', text_v2('Your Skin\'s Messaging Network', 'A text is tiny, carries a coded message, and lands exactly where it\'s sent. Exosomes work the same way: carriers that deliver specific coded messages to cells.'))
scalp('B3_micro', 'Scalp 12 - Day 0.jpg', 'Scalp 12 - Day 56.jpg', text_v2('Don\'t Forget the Messenger', 'A message with no carrier never arrives. That\'s the job of an exosome: built to navigate and deliver signals where it\'s needed most.'), 'DAY 0', 'DAY 56')
stock('B4_effect', '4178359.mp4', 3, '864:1080:900:0', 'v2', text_v2('The NX35™ Effect', 'Our NX35™ technology targets specific cells and delivers "coded" messages. 100% plant-derived and vegan.', True))
