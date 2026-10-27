"""Trend 6 — 'My reaction when you tell me how many ___'. Ref reel instagram.com/reel/DeFSyZLJlkP (474K views): fixed line on top,
a growing number at the bottom, the reaction escalating each cut, last one huge. Count = the site's '14 awards'.
Footage: client's real Ulta NYC visit (two creators reacting at the SickScience shelf)."""
import os, sys
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends'))
from trendkit import build, sheet, text_layer
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.expanduser('~/sickscience-work/batch-53/ulta/src/SickScience UGC-visit.mov')
CUTS = [0, 1.667, 4.6, 6.267, 7.867, 8.4, 8.867, 9.4, 10.667]
SHOTS = [(SRC, 35.6), (SRC, 37.4), (SRC, 40.0), (SRC, 41.4), (SRC, 50.0), (SRC, 52.0), (SRC, 54.0), (SRC, 56.2)]
LABELS = ['1 award', '3 awards', '5 awards', '7 awards?', '9 awards?', '11 awards?!', '12?!', '14 AWARDS?!?!']
def ov(k):
    top = text_layer(['my reaction when they tell me how', 'many awards SickScience has won'], 360, style='Medium', size=44, gap=1.18)
    big = k == len(LABELS) - 1
    lab = text_layer([LABELS[k]], 1120, style='Bold', size=112 if big else 68)
    return Image.alpha_composite(top, lab)
if __name__ == '__main__':
    ovs = [ov(k) for k in range(len(SHOTS))]
    if '--sheet' in sys.argv: print(sheet(SHOTS, CUTS, os.path.join(H, 'tmp'), ovs, cols=8)); sys.exit()
    print(build(SHOTS, CUTS, os.path.join(H, 'ref_sfx.wav'), os.path.join(H, 'SickScience – My reaction (14 awards) – 9x16.mp4'), os.path.join(H, 'tmp'), ovs))
