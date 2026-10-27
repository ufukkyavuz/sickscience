"""Trend 5 — 'Vibin' (Wxoda). Ref reel instagram.com/reel/DdZSu50upPn: walking/vlog clips cut on the bar, one reflective sentence stacked down the middle
for the whole reel (pale cream). Ours: the real Ulta NYC walk-in; 'and finally you found a serum made by actual scientists' (founders are PhD scientists)."""
import os, sys
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends'))
from trendkit import build, sheet, text_layer
H = os.path.dirname(os.path.abspath(__file__))
ULTA = os.path.expanduser('~/sickscience-work/batch-53/ulta/src/SickScience UGC-visit.mov')
CUTS = [0, 1.88, 3.62, 5.22, 6.90, 8.61, 9.54]      # every 4 beats (~143 BPM)
SHOTS = [(ULTA, 11.6), (ULTA, 15.6), (ULTA, 17.4), (ULTA, 19.6), (ULTA, 23.4), (ULTA, 25.8)]
TXT = text_layer(['&', 'finally', 'you', 'found', 'a', 'serum', 'made', 'by', 'actual', 'scientists'], 330, style='Medium', size=76, fill=(246, 236, 196), gap=1.02)
OV = [TXT] * len(SHOTS)
if __name__ == '__main__':
    if '--sheet' in sys.argv: print(sheet(SHOTS, CUTS, os.path.join(H, 'tmp'), OV, cols=6)); sys.exit()
    print(build(SHOTS, CUTS, os.path.join(H, 'ref.webm'), os.path.join(H, 'SickScience – Vibin (made by scientists) – 9x16.mp4'), os.path.join(H, 'tmp'), OV, fade=0.4))
