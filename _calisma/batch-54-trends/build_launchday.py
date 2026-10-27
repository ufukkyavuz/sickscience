"""Trend 9 — 'Patient Zero' (Taylor Swift) wedding-day-edit format, adapted to the NetWork launch night ('Welcome to The Lab', Feb 2026).
Audio = the hook section used across the trend (ref reel instagram.com/reel/DdtjtW5t9hz). Cuts on every beat (~92 BPM), last shot held with one white line."""
import os, sys
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends'))
from trendkit import build, sheet, text_layer
H = os.path.dirname(os.path.abspath(__file__))
EV = os.path.expanduser("~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/SickScience/_calisma/batch-53-launch-montage/src-event-reel-revised.mp4")
CUTS = [0, 0.7, 1.35, 1.97, 2.65, 3.32, 3.97, 4.62, 5.27, 5.9, 6.57, 7.22, 7.87, 8.54, 9.2, 9.82, 10.4, 11.6]
SHOTS = [(EV, 3.75),  # neon 'Shhh Lab In Use'
         (EV, 3.2),   # lab coats on the rack
         (EV, 19.2),  # ShapeShift capsules on the stand
         (EV, 10.2),  # flask
         (EV, 34.2),  # Welcome to The Lab wall
         (EV, 0.2),   # first guest in goggles
         (EV, 1.2),   # guests in lab coats
         (EV, 22.2),  # Polen on the mic
         (EV, 23.2),  # NX35 screen
         (EV, 24.2),  # Merve on the mic
         (EV, 12.2),  # mixing at the bench
         (EV, 18.2),  # pipette
         (EV, 14.2),  # laughing guest
         (EV, 35.2),  # guest laughing in her lab coat
         (EV, 38.3),  # Merve + Polen on the screen
         (EV, 7.0),   # Merve + Polen
         (EV, 8.6)]   # Merve + Polen, held — closing line
if __name__ == '__main__':
    # story captions so the edit reads like a wedding-day edit: set-up -> doors open -> speeches -> party -> closing line
    STAGES = [(range(0, 4), ['NetWork launch day.', 'Setting up the lab…']),
              (range(4, 7), ['Doors open.']),
              (range(7, 10), ['Our founders take the mic.']),
              (range(10, 15), ['Then the lab came alive.'])]
    ovs = []
    for i in range(len(SHOTS)):
        lines = next((l for r, l in STAGES if i in r), None)
        ovs.append(text_layer(lines, 330, style='Medium', size=60) if lines else None)
    ovs[-2] = text_layer(['The night we opened', 'The Lab.'], 330, style='Medium', size=60)
    ovs[-1] = ovs[-2]
    if '--sheet' in sys.argv: print(sheet(SHOTS, CUTS, os.path.join(H, 'tmp'), ovs, cols=9)); sys.exit()
    print(build(SHOTS, CUTS, os.path.join(H, 'ref.webm'), os.path.join(H, 'SickScience – Launch day (Patient Zero) – 9x16.mp4'), os.path.join(H, 'tmp'), ovs, fade=0.5))
