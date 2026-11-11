# Founders film v4: the notebook (2026-11-06)

User brief (summary): a notebook/planner with the SickScience logo on the cover. It opens, pages flip, then we stay on a wide two-page spread. A real hand writes with a marker from the top left, synced to the VO piece by piece, and tapes the photos in.

## Brief
- Message: two geneticists turned 17 years of lab work into a beauty brand. "That's sick" → "that's science".
- Real assets: founders photo S_0944, petri crops (gen56/nx1), end card S_0723 (the 4 real products), official logo `Brand Assets/Logos/SickScience Logo Type and Mark White.png`. The logo is composited, never drawn by the model.
- VO: stock ElevenLabs Polen/Merve (vo/01–11), word times in words.json.
- Avoid: a pasted-looking hand (it needs a shadow and lift), CG page curl, the model drawing the logo, dark moody grading (white bench, scientific).

## Style
- White lab bench, soft daylight from the top left, black cloth hardcover with the white foil logo, cream dot-grid pages.
- Ink: navy-black fine marker; yellow highlighter; violet only on the final "Science".
- Camera: locked top-down for the flip; during writing a close (~1.5×) follow of the pen tip; pull back to the full spread at the end.

## Shot list
| # | Beat | In | Out | Why |
|---|---|---|---|---|
| 1 | HOOK cover | closed book, logo, slow push | hand on the cover | brand first, a promise of a story |
| 2 | Open + flip (Veo, first+last frame) | cover lifts, 3–4 pages flip | blank spread, hand leaves | the "opening a diary" moment |
| 3 | Spread wide | empty spread, VO starts | camera pushes to the top-left | sets the canvas |
| 4 | Left page: origin | hand writes "That's sick!", tapes the founders photo, timeline, 14 YEARS, patents | page full | PROBLEM/ORIGIN |
| 5 | Pan to the right page: mechanism | exosomes, drone, FIG prints, THOUSANDS, NX35 | | REVEAL/PROOF |
| 6 | Close | scientist? struck → marketer. / No, that's science. / Sick Science (violet) | hand lifts out | CLOSE |
| 7 | Pull back | full finished spread | | payoff of the whole page |
| 8 | End card | S_0723 + "Science, but never boring." | | |

Plates: Higgsfield Nano Banana Pro Unlimited (cover, spread, hand). Flip: Veo 3.1 Fast in Flow, first frame = cover, last frame = spread.
Render: `~/sickscience-work/brandfilm/render4.py` (per-page homography, ink warped straight to output resolution, hand cut-out follows the pen tip).
