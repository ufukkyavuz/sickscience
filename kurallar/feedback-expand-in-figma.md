---
name: feedback-expand-in-figma
description: "Extend/expand images only with Figma's own Expand, never by code (row repeat, pads, canvas stretching)"
metadata:
  type: feedback
---
User, 2026-10-30: "expandları figmada yapacaksın bundan sonra kendin yapma bozuyosun".

**Why:** on the competitor offer series I extended images in PIL by repeating the last row (C1 `W1c.jpg`, C2 `W2d.jpg`) and painted over the bench band (C5 `W5c.jpg`). That leaves streaks and seams, and I then hid them with white fade rectangles.

**How to apply:** when an image must be taller or wider than its frame, use Figma's Expand (desktop app, More menu; see [[figma-yetenekler]]). No PIL padding, row repeating, mirrored edges or fade rectangles to hide a seam. If Expand can't be reached from here, ask the user to run it or say so; don't fall back to code.

Related: [[feedback-type-scale-and-no-blur]], [[feedback-same-image-all-formats]]
