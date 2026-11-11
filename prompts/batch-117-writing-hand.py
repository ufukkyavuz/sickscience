# Batch-117 (2026-11-07): founders film, real writing hand. Cut out (Vision lift) and moved with the pen tip over the plate.
import json, os
P = {'HAND2': [
 "A real photograph shot exactly straight from above: a young woman's right hand writing with a black ballpoint pen on a blank sheet of plain white paper lying flat on a white bench.",
 "THE HAND: a beautiful slim right hand of a woman in her late 20s, natural short almond nails with a clear nude polish, realistic skin with fine texture and knuckle creases, a white lab coat cuff at the wrist. Relaxed natural writing grip: pen held between thumb and index finger, middle finger under the pen, ring and little finger curled and resting lightly on the paper. Exactly five fingers.",
 "THE PEN: a slim matte black ballpoint pen, 14 cm long, no logo, no text. The ballpoint tip touches the paper; the barrel leans back over the knuckles toward the upper right of the frame.",
 "COMPOSITION AND FRAMING: Vertical 9:16, camera exactly top-down, 35mm lens, wide enough to show the whole forearm. The pen tip touches the paper at 18% from the left and 20% from the top of the frame. The hand is in the upper-left part of the frame; the forearm in a white lab coat sleeve runs diagonally from the wrist down to the lower right corner and leaves the frame only through the bottom-right corner, elbow just outside the frame. The whole sleeve is inside the frame except where it crosses the bottom-right corner. Nothing else in the frame: plain white paper only, no other objects.",
 "SCALE: the pen is 14 cm long and spans about one quarter of the frame width; hand from wrist to fingertip about 17 cm, forearm about 26 cm.",
 "LIGHT AND SHADOW: soft even daylight from the upper left, a soft natural shadow of the hand and the pen falls toward the lower right onto the paper, a small sharp contact shadow under the pen tip.",
 "BACKGROUND: plain matte white paper filling the whole frame, evenly lit.",
 "PHOTOGRAPHIC FINISH: ultra photorealistic, indistinguishable from a real photograph, 8K detail, natural neutral colour.",
 "IMPERFECTIONS: fine skin texture, faint veins on the back of the hand, a tiny scuff on the pen, gentle film grain.",
 "INTEGRATION: hand and pen lit by the same daylight, real contact shadows, same sharpness and grain everywhere.",
 "KEY COMPOSITION: TOP-DOWN RIGHT HAND WRITING WITH A BLACK BALLPOINT ON PLAIN WHITE PAPER, PEN TIP UPPER LEFT, FOREARM DIAGONAL TO THE BOTTOM-RIGHT CORNER.",
 "Negative: writing on the paper, letters, words, numbers, lines, grid, logos, rings, jewellery, watch, tattoos, extra fingers, six fingers, deformed fingers, left hand, two hands, long nails, coloured nail polish, fountain pen, pencil, marker, notebook, objects, dark background, CGI, 3D render, watermark."]}
json.dump({k: {'paras': v} for k, v in P.items()}, open(os.path.join(os.path.dirname(__file__), '..', '_calisma', 'p117b.json'), 'w'))
print('ok')
