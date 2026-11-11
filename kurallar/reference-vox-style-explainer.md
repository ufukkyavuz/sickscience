---
name: reference-vox-style-explainer
description: Vox-style object callouts in render2.py - colour-tracked spotlight + hand-drawn arrow + label; educational videos keep all content, only dead gaps trimmed
metadata:
  type: reference
---
2026-11-10, Merve's exosome truck clip: user wanted the toy truck highlighted Vox-style with arrows and labels (EXOSOME, PROTEINS, LIPIDS, OTHER MOLECULES), nothing skipped in the science ("bilimsel anlatımı kafana göre kesme"), only dead gaps removed, so the cut is ~50 s (educational exception to the 20 s rule).
- `render2.py`: `spot()` outlines/dims the colour-tracked object, `pointer()` draws the arrow + label; masks from the UNDIMMED frame; largest connected component; props with fixed keyframes when colour fails (`PINK_KF`).
- Edits keys: `spot`, `ptr` (source-time windows), `srcins` (white diagram beat). Props she drops into the truck are part of the explanation - never cut those pauses.
See [[feedback-colours-must-not-shift]], [[reference-ugc-viral-edit-style]].
