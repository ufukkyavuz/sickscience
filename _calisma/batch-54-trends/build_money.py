"""Trend 3 — 'Money can't buy happiness but…' (original audio by eresdigna, 310K reels). Ref reel instagram.com/reel/Ddtvk-sC3De (1M views):
one continuous clip, the sentence stacked one word per line, each word appearing on a beat (~134 BPM).
Footage: client's real Ulta routine clip, the ShapeShift part (bottle to camera -> pump -> jaw -> neck), one take.
Claim wording follows the PDP ('Chisel Your Jawline in 2 Weeks') softened with '-looking'."""
import os, sys
sys.path.insert(0, os.path.expanduser('~/sickscience-work/trends'))
from trendkit import build, sheet, text_layer
H = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.expanduser('~/sickscience-work/batch-53/ulta/src/448df0ca64f3492182880e3b5a203426.mov')
T0 = 10.75                                 # take ends at 17.05 s, before the DropOff tube enters (17.2 s)
WORDS = ['money', "can’t", 'buy', 'happiness', 'but', 'it', 'can', 'buy', 'a', 'sculpted-looking', 'jawline']
BEATS = [0.10, 0.54, 0.96, 1.41, 1.86, 2.30, 2.75, 3.23, 3.68, 4.13, 4.58]   # word k appears on beat k
CUTS = [0] + BEATS + [6.3]
SHOTS = [(SRC, T0 + c) for c in CUTS[:-1]]
if __name__ == '__main__':
    ovs = [None] + [text_layer(WORDS[:k + 1], 286, style='Medium', size=84, gap=1.03) for k in range(len(WORDS))]
    if '--sheet' in sys.argv: print(sheet(SHOTS, CUTS, os.path.join(H, 'tmp'), ovs, cols=12)); sys.exit()
    print(build(SHOTS, CUTS, os.path.join(H, 'ref.webm'), os.path.join(H, 'SickScience – Money can’t buy happiness – 9x16.mp4'), os.path.join(H, 'tmp'), ovs, fade=0.25))
