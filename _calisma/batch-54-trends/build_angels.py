"""Trend 7 — 'Not all angels are in heaven' (original audio by shharlene). Ref reel instagram.com/reel/Dath-4sRHsF (658K views):
one clip, one cream line in the middle: 'not all angels are in heaven / for example I am at work'.
Ours: launch-night guest in goggles + lab coat (Sonia cut, one take) — 'for example I'm in the lab'."""
import os, sys
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends'))
from trendkit import build, sheet, text_layer
H = os.path.dirname(os.path.abspath(__file__))
SONIA = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma/batch-53-launch-montage/src-sonia-video-cut.mp4")
CUTS = [0, 7.6]
SHOTS = [(SONIA, 11.5, 'crop=810:1440:(iw-810)/2:0')]
OV = [text_layer(['not all angels', 'are in heaven', 'for example', 'I’m in the lab'], 1080, style='Medium', size=66, fill=(246, 236, 196), gap=1.12)]
if __name__ == '__main__':
    if '--sheet' in sys.argv: print(sheet(SHOTS, CUTS, os.path.join(H, 'tmp'), OV, cols=1)); sys.exit()
    print(build(SHOTS, CUTS, os.path.join(H, 'ref.webm'), os.path.join(H, 'SickScience – Not all angels – 9x16.mp4'), os.path.join(H, 'tmp'), OV, fade=0.3))
