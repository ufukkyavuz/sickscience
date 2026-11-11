# Batch-116 (2026-11-06): founders film v4, realistic plate. Two-page lab notebook spread, blank grid, white cover,
# scientific props around. All handwriting/drawings are added by code (animatic.py), so the pages stay blank.
import json, os
P = {'NB_spread': [
 "A real editorial still-life photograph, shot straight from above: an open hardcover laboratory notebook lying flat on a clean white lab bench, both pages visible as one wide spread.",
 "THE NOTEBOOK: a large A4 lab notebook with a clean WHITE linen hardcover that shows as a thin white border around the pages. Both pages are completely BLANK with a fine light blue-grey 5 mm grid: no writing, no printed words, no numbers, no header text, no page numbers. A soft gutter shadow runs down the middle where the pages curve gently into the binding.",
 "COMPOSITION AND FRAMING: Vertical 9:16, camera exactly top-down and parallel to the bench, 50mm lens, no perspective tilt. The open spread is landscape, perfectly square to the frame and not rotated, and fills 96% of the frame width; it sits across the middle of the frame, from 30% to 70% of the frame height. Above and below the notebook: clean white bench with a few lab objects.",
 "PROPS (only on the bench above and below the notebook, never on the pages): above the notebook — a small glass beaker with a little translucent milky gel-serum, a row of three clear test tubes in a white rack, a clear Erlenmeyer flask; below the notebook — a glass petri dish with a thin slice of pineapple, a clear plastic pipette, a glass microscope slide, a black fine-liner pen lying parallel to the notebook edge. Objects partly cut by the frame edges, tidy, small next to the notebook.",
 "SCALE: the open spread is 42 cm wide and 30 cm tall; beaker 6 cm wide, test tubes 1.6 cm wide, petri dish 9 cm, pen 14 cm.",
 "LIGHT AND SHADOW: soft even daylight from the upper left, gentle soft shadows from the glassware and the notebook edge onto the bench, clear caustic light under the glass, no hard shadow on the pages, both pages evenly lit edge to edge.",
 "BACKGROUND: matte white lab bench, white-dominant, scientific and airy.",
 "PHOTOGRAPHIC FINISH: ultra photorealistic, indistinguishable from a real photograph, 8K detail, natural neutral colour, visible paper fibre on the pages.",
 "IMPERFECTIONS: a faint wave in the pages near the gutter, a light scuff on a cover corner, a few specks of dust on the bench, a faint water ring under the beaker, gentle film grain, soft vignette.",
 "INTEGRATION: every object lit by the same daylight, real contact shadows, glass shows real reflections of the room, same sharpness and grain everywhere.",
 "KEY COMPOSITION: TOP-DOWN OPEN TWO-PAGE BLANK GRID LAB NOTEBOOK, SQUARE TO THE FRAME, FULL WIDTH, ACROSS THE MIDDLE, WHITE BENCH WITH GLASSWARE ABOVE AND BELOW.",
 "Negative: any writing, letters, words, numbers, logos, labels, printed header, page numbers, handwriting, drawings, stickers, objects on the pages, rotated or tilted notebook, perspective, curled pages lifting up, hands, people, products, coloured cover, black cover, kraft cover, lined paper, dark background, CGI, 3D render, watermark, dimension lines."]}
json.dump({k: {'paras': v} for k, v in P.items()}, open(os.path.join(os.path.dirname(__file__), '..', '_calisma', 'p116.json'), 'w'))
print('ok')
