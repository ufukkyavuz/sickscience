"""Trend 13 — 'Last Train to London' (fall outfits: same action, quick cuts). Ref reel instagram.com/reel/DatBltLsBgq (3.8M).
Ours: the 4-step routine — each product to camera then applied, every 2 beats (123 BPM). Real routine footage (client's Ulta UGC)."""
import os, sys
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends'))
from trendkit import build, sheet, text_layer
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
R = os.path.expanduser('~/sickscience-work/batch-53/ulta/src/448df0ca64f3492182880e3b5a203426.mov')
CUTS = [0, 0.77, 1.76, 2.74, 3.74, 4.71, 5.69, 6.66, 7.64, 8.64, 9.61, 10.08]
SHOTS = [(R, 1.6), (R, 4.0), (R, 8.0), (R, 10.5), (R, 14.6), (R, 17.5), (R, 18.6), (R, 22.5), (R, 24.0), (R, 28.0), (R, 29.05)]
LAB = ['my fall routine', '01  NetWork · face', '01  NetWork · face', '02  ShapeShift · jaw & neck', '02  ShapeShift · jaw & neck',
       '03  DropOff · body', '03  DropOff · body', '04  PowerCycle · scalp', '04  PowerCycle · scalp', 'done.', 'done.']
OV = [text_layer([l], 1160, style='Medium', size=58) for l in LAB]
if __name__ == '__main__':
    if '--sheet' in sys.argv: print(sheet(SHOTS, CUTS, os.path.join(H, 'tmp'), OV, cols=11)); sys.exit()
    print(build(SHOTS, CUTS, os.path.join(H, 'ref.webm'), os.path.join(H, 'SickScience – Fall routine (Last Train to London) – 9x16.mp4'), os.path.join(H, 'tmp'), OV, fade=0.3))
