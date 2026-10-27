"""Trend 4 — 'Upside Down' (Diana Ross). Ref reel instagram.com/reel/DbgAfQMCEHe (1.6M views): sideways phone framing, lyric words huge & rotated
('upside', 'inside', red 'OUT'), hand/flip transitions. Ours does what the lyric says: the shot flips on 'down', the landscape launch clip plays sideways,
OUT pops in brand magenta, the founders spin on 'round and round' and land upright. Real footage: Ulta NYC visit + NetWork launch night."""
import os, sys
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends'))
from trendkit import build, sheet, rotated_word
H = os.path.dirname(os.path.abspath(__file__))
D = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma")
EV = os.path.join(D, 'batch-53-launch-montage/src-event-reel-revised.mp4'); SONIA = os.path.join(D, 'batch-53-launch-montage/src-sonia-video-cut.mp4')
ULTA = os.path.expanduser('~/sickscience-work/batch-53/ulta/src/SickScience UGC-visit.mov')
MAG = (169, 33, 192)
CUTS = [0, 1.1, 2.04, 4.16, 5.38, 6.22, 8.56, 9.70]
SPIN = 'scale=2214:3936,rotate=2*PI*t/2.34:ow=1080:oh=1920'   # one full turn across 'round and round'; zoomed so corners never show
SHOTS = [(ULTA, 50.0),                              # upside  — creator at Ulta, hands to face
         (ULTA, 51.1, 'hflip,vflip'),               # down    — same shot, flipped upside down
         (SONIA, 0.3, 'transpose=1'),               # boy you turned me — launch night, sideways like the trend
         (ULTA, 28.0, 'transpose=2'),               # inside  — the SickScience shelf, sideways
         (ULTA, 40.0, 'hflip,vflip'),               # OUT     — creator laughing, upside down
         (EV, 7.0, None, SPIN),  # round and round — Merve + Polen spin
         (EV, 9.3)]                                 # up      — founders upright
OV = [rotated_word('upside', 170, 960), rotated_word('down', 170, 960, angle=-90), None,
      rotated_word('inside', 170, 960), rotated_word('OUT', 540, 960, size=420, fill=MAG), None, None]
if __name__ == '__main__':
    if '--sheet' in sys.argv: print(sheet(SHOTS, CUTS, os.path.join(H, 'tmp'), OV, cols=7)); sys.exit()
    print(build(SHOTS, CUTS, os.path.join(H, 'ref.webm'), os.path.join(H, 'SickScience – Upside down – 9x16.mp4'), os.path.join(H, 'tmp'), OV, fade=0.3))
