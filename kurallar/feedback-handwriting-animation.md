---
name: feedback-handwriting-animation
description: Hand-drawn notebook films — writing/drawing reveals strictly left to right, fast, real stroke-following, steady pen, keep the ink texture
metadata:
  type: feedback
---
For hand-drawn / notebook explainer videos (founders film v4, 2026-11-06), every word and drawing is drawn like a real pen:
- **Strictly left to right**, quickly: "2009" appears 2 → 0 → 0 → 9, never 2, 9, then the middle. Same for drawings.
- Follow the stroke path (skeleton), never box/rectangle wipes or masks ("maskelenerek yapılmış gibi kutu kutu açılıyo" was rejected).
- Steady pen: the pen sprite must not tremble (smooth the tip); but the drawings keep their ballpoint texture (double pass, slight wobble) — the user wanted the pen steady, not the lines clean.
- Fast: ~1700 px of path per second; highlighter swept after the word.
- Camera pans left/right so the whole new element is in frame; never cut text at the left edge.

**Why:** user feedback on animatic v4a–v4d, 2026-11-06 ("soldan sağa doğru açarız… 2,0,0,9 yaparız. Hızlı bir şekilde"; "kalemi titretme"; "dokusunu kaybetmişsin").
**How to apply:** carry these into the realistic version (real notebook plate, hand/pen) as well. Code: ~/sickscience-work/brandfilm/v4/animatic.py (stroke_order). Related: [[feedback-video-studio-gates]].
