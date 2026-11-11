---
name: feedback-colours-must-not-shift
description: From 2026-11-10 every video - source and brand colours must not shift; verify output vs source colour numerically
metadata:
  type: feedback
---
User, 2026-11-10: "renklere dikkat edelim bozulmasınlar, bundan sonra her videoda dikkat edicez."

**Why:** colour shifts (HDR tone-map, wrong matrix, off-brand overlay colours) are visible to the user and have been rejected before ([[feedback-iphone-hdr-tonemap]]).
**How to apply:** ffprobe color_transfer first (HLG/PQ = native pipeline); compare mean RGB of a source frame and the same output frame (within ~2-3 levels, 2026-11-10 edu video: 179/139/131 vs 177/137/129); overlay colours only from brand palette (SS purple 115,0,199 / NW red / PC green / DO cobalt). Educational beats = white full-bleed diagrams in `render2.py make_insert`.
