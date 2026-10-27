"""Trend 8 — 'Taking one for the team' (Twista – Sunshine). Ref reel instagram.com/reel/Ddp64nNzU-Y. Your role in the friend group.
Ours: launch-night friends, landing on the one who always brings the serum (all 4 products, real routine footage)."""
import os, sys
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends'))
from trendkit import build, sheet, text_layer
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
D = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma/batch-53-launch-montage")
EV = os.path.join(D, 'src-event-reel-revised.mp4'); SONIA = os.path.join(D, 'src-sonia-video-cut.mp4')
R = os.path.expanduser('~/sickscience-work/batch-53/ulta/src/448df0ca64f3492182880e3b5a203426.mov')
SC = 'crop=810:1440:(iw-810)/2:0'
CUTS = [0, 1.14, 2.07, 3.00, 4.04, 7.02]
SHOTS = [(EV, 1.2), (SONIA, 2.0, SC), (EV, 12.2), (SONIA, 24.0, SC), (R, 1.6)]
TOP = text_layer(['every friend group has one'], 330, style='Medium', size=60)
END = Image.alpha_composite(TOP, text_layer(['the one who always', 'brings the serum'], 1120, style='Bold', size=72))
OV = [TOP, TOP, TOP, TOP, END]
if __name__ == '__main__':
    if '--sheet' in sys.argv: print(sheet(SHOTS, CUTS, os.path.join(H, 'tmp'), OV, cols=5)); sys.exit()
    print(build(SHOTS, CUTS, os.path.join(H, 'ref.webm'), os.path.join(H, 'SickScience – The friend who brings the serum (Sunshine) – 9x16.mp4'), os.path.join(H, 'tmp'), OV, fade=0.3))
