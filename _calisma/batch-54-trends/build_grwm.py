"""Trend 1 — 'Daily GRWM loading' (WINDOWS IN BRAZIL (Sped Up) – VHM4D). Reference reel instagram.com/reel/Dd_FYbfud-m (1.2M views):
3.7 s opening at 0%, then fast cuts with a big centred % counter up to 100%. Footage: client's real Ulta routine clip (creator, 4 products)."""
import os, sys
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends'))
from trendkit import build, sheet, text_layer
H = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.expanduser('~/sickscience-work/batch-53/ulta/src/448df0ca64f3492182880e3b5a203426.mov')
CUTS = [0, 3.808, 4.133, 4.458, 4.807, 5.132, 5.457, 5.782, 6.107, 6.432, 6.757, 7.082, 7.407, 7.732, 8.057, 8.382, 8.707, 9.033, 9.381, 10.681]  # drop at 3.808, then the song's half-beat grid; 100% held on the last bar
SHOTS = [(SRC, 1.5),                       # 0%  holds all four products
         (SRC, 7.0), (SRC, 8.0), (SRC, 9.0),   # NetWork: pump, face
         (SRC, 10.5), (SRC, 12.0),             # ShapeShift to camera, pump
         (SRC, 13.8), (SRC, 15.4),             # jaw, neck
         (SRC, 17.5), (SRC, 18.6), (SRC, 21.0),# DropOff to camera, arm, belly
         (SRC, 22.5), (SRC, 24.0), (SRC, 25.0),# PowerCycle to camera, dropper on scalp
         (SRC, 26.0), (SRC, 27.0),             # scalp massage
         (SRC, 27.6), (SRC, 28.1),             # hair flip
         (SRC, 29.05)]                         # 100% final look
PCT = [0] + list(range(5, 90, 5)) + [100]
if __name__ == '__main__':
    ovs = [text_layer([f'{p}%'], 860, size=96) for p in PCT]
    if '--sheet' in sys.argv: print(sheet(SHOTS, CUTS, os.path.join(H, 'tmp'), ovs)); sys.exit()
    print(build(SHOTS, CUTS, os.path.join(H, 'ref.webm'), os.path.join(H, 'SickScience – GRWM loading – 9x16.mp4'), os.path.join(H, 'tmp'), ovs))
