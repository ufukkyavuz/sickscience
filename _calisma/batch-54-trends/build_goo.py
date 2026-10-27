"""Trend 15 — 'Goo Goo Muck' (The Cramps, Halloween/Wednesday). Ref reel instagram.com/reel/Dd9PK0aAY4a. Ours: the launch-night lab after dark —
purple-graded cuts every 2 beats (143 BPM), one line on top. Real footage only."""
import os, sys
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends'))
from trendkit import build, sheet, text_layer
H = os.path.dirname(os.path.abspath(__file__))
D = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma/batch-53-launch-montage")
EV = os.path.join(D, 'src-event-reel-revised.mp4'); SONIA = os.path.join(D, 'src-sonia-video-cut.mp4')
G = 'eq=brightness=-0.10:contrast=1.30:saturation=0.70,colorbalance=rs=0.04:bs=0.14:rm=0.02:bm=0.10,vignette=PI/4.2'
SC = 'crop=810:1440:(iw-810)/2:0'
CUTS = [0, 0.53, 1.37, 2.18, 2.97, 3.90, 4.81, 5.64, 6.50, 7.36, 8.20, 9.03, 9.85, 10.70, 11.54, 12.40, 13.0]
SHOTS = [(EV, 3.75, None, G), (EV, 27.4, None, G), (EV, 10.2, None, G), (EV, 0.2, None, G), (SONIA, 12.0, SC, G), (EV, 32.2, None, G),
         (EV, 18.2, None, G), (EV, 19.2, None, G), (EV, 28.4, None, G), (SONIA, 16.5, SC, G), (EV, 33.2, None, G), (EV, 37.2, None, G),
         (EV, 11.2, None, G), (SONIA, 23.0, SC, G), (EV, 41.2, None, G), (EV, 4.6, None, G)]
OV = [text_layer(['POV: you stayed in the lab', 'after midnight'], 330, style='Medium', size=56)] * len(SHOTS)
if __name__ == '__main__':
    if '--sheet' in sys.argv: print(sheet(SHOTS, CUTS, os.path.join(H, 'tmp'), OV, cols=8)); sys.exit()
    print(build(SHOTS, CUTS, os.path.join(H, 'ref.webm'), os.path.join(H, 'SickScience – Lab after midnight (Goo Goo Muck) – 9x16.mp4'), os.path.join(H, 'tmp'), OV, fade=0.4))
