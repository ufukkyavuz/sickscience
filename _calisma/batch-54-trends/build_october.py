"""Trend 16 — 'we fell in love in october' (girl in red). Ref reel instagram.com/reel/Dd6RMmix9Qn (4.3M): soft everyday clip + one white line.
Ours: NetWork during Breast Cancer Awareness Month — exact BCRF wording (full name, 'on SickScienceLabs.com', no medical claims). Cuts on the bar."""
import os, sys
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends'))
from trendkit import build, sheet, text_layer
from PIL import Image
H = os.path.dirname(os.path.abspath(__file__))
R = os.path.expanduser('~/sickscience-work/batch-53/ulta/src/448df0ca64f3492182880e3b5a203426.mov')
ST = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma/batch-53-launch-montage/stories/40.mp4")
CUTS = [0, 1.90, 3.76, 5.60, 7.45, 9.12]
SHOTS = [(R, 3.9), (R, 6.9), (R, 4.7), (R, 8.2), (R, 9.3)]   # event stand sign says "Network" (wrong case) -> not used
L1 = text_layer(['we fell in love in October'], 330, style='Medium', size=64)
L2 = text_layer(['this October, 20% of NetWork sales', 'on SickScienceLabs.com go to', 'The Breast Cancer Research Foundation'], 330, style='Medium', size=46, gap=1.22)
OV = [L1, L1, L2, L2, L2]
if __name__ == '__main__':
    if '--sheet' in sys.argv: print(sheet(SHOTS, CUTS, os.path.join(H, 'tmp'), OV, cols=5)); sys.exit()
    print(build(SHOTS, CUTS, os.path.join(H, 'ref.webm'), os.path.join(H, 'SickScience – We fell in love in October (NetWork x BCRF) – 9x16.mp4'), os.path.join(H, 'tmp'), OV, fade=0.4))
