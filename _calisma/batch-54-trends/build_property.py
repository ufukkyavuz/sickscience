"""Trend 12 — 'This is private property' (viral confrontation audio). Ref reel instagram.com/reel/DeAZVPuyFvM.
Ours: one take at Ulta — the creator guards his ShapeShift, then his friend grabs one. Caption carries the joke (no lip-sync needed)."""
import os, sys
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends'))
from trendkit import build, sheet, text_layer
H = os.path.dirname(os.path.abspath(__file__))
U = os.path.expanduser('~/sickscience-work/batch-53/ulta/src/SickScience UGC-visit.mov')
CUTS = [0, 13.2]
SHOTS = [(U, 32.0)]
OV = [text_layer(['when my roommate asks', 'to “borrow” my ShapeShift'], 330, style='Medium', size=60)]
if __name__ == '__main__':
    if '--sheet' in sys.argv: print(sheet(SHOTS, CUTS, os.path.join(H, 'tmp'), OV, cols=1)); sys.exit()
    print(build(SHOTS, CUTS, os.path.join(H, 'ref.webm'), os.path.join(H, 'SickScience – This is private property – 9x16.mp4'), os.path.join(H, 'tmp'), OV, fade=0.3))
