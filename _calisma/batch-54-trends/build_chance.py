"""Trend 2 — 'Take that chance' (Gwen Stefani, What You Waiting For?). Ref reel instagram.com/reel/Dd1hHprhvP1 (982K views):
a life journey in clips, the lyric appearing word by word. Ours: the founders' journey — lab -> Merve's own ShapeShift challenge ->
launch night -> both on stage -> Ulta -> the two founders under 'what you waiting for?'. Word times from whisper on the reference audio."""
import os, sys
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends'))
from trendkit import build, sheet, text_layer
H = os.path.dirname(os.path.abspath(__file__))
D = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma")
EV = os.path.join(D, 'batch-53-launch-montage/src-event-reel-revised.mp4')
MERVE = os.path.join(D, 'batch-45-14day/raw/IMG_2162.MOV')   # raw take, no overlays
ULTA = os.path.expanduser('~/sickscience-work/batch-53/ulta/src/SickScience UGC-visit.mov')
CUTS = [0, 1.4, 3.6, 4.26, 4.92, 5.57, 6.24, 6.88, 7.94, 8.52, 9.4, 10.34, 11.18, 14.4]
SHOTS = [(EV, 3.75),     # 'Shhh Lab In Use' — take that chance
         (MERVE, 6.3),   # Merve starting her own ShapeShift challenge — cause you might grow
         (EV, 3.2),      # lab coats ready
         (EV, 19.2),     # ShapeShift on the stand
         (EV, 34.2),     # Welcome to The Lab
         (EV, 22.2),     # Polen on stage
         (EV, 24.2),     # Merve on stage
         (EV, 12.2),     # guests in the lab
         (ULTA, 17.6),   # Ulta, NYC — what you waiting
         (ULTA, 20.0),   # walking in
         (ULTA, 25.6),   # the SickScience fixture
         (ULTA, 28.0),   # on the shelf
         (EV, 8.6)]      # Merve + Polen — what you waiting for?
def words(ws): return text_layer(ws, 300, style='Medium', size=84, gap=1.03)
OV = [words(['take', 'that', 'chance']),
      words(['cause', 'you', 'might', 'grow']),
      None, None, None, None, None, None,
      words(['what', 'you', 'waiting']), words(['what', 'you', 'waiting']), words(['what', 'you', 'waiting']), words(['what', 'you', 'waiting']),
      words(['what', 'you', 'waiting', 'for?'])]
if __name__ == '__main__':
    if '--sheet' in sys.argv: print(sheet(SHOTS, CUTS, os.path.join(H, 'tmp'), OV, cols=13)); sys.exit()
    print(build(SHOTS, CUTS, os.path.join(H, 'ref.webm'), os.path.join(H, 'SickScience – Take that chance – 9x16.mp4'), os.path.join(H, 'tmp'), OV, fade=0.5))
