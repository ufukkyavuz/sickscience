---
name: feedback-check-layout-full-size
description: Before reporting any Figma layout, inspect it at full size and measure; text on a photographed object follows that object's measured corners
metadata:
  type: feedback
---

User, 2026-11-02: "yerleşimi düzgün yap ya bi kontrol et yaptığın işi yaptıktan sonra". I reported B03 done from a small side-by-side preview, with text at a guessed angle, dividers short of the card edges, a divider into the thumb, and Feed crowded top and bottom.

**Why:** small previews hide alignment faults, and the user then has to find them.

**How to apply:** after every layout change, export each format at 1:1, crop the key area and look before saying it is done. For text on a card, screen or sign in a photo, measure its four corners first, derive centre, size and angle, build the text unrotated, then rotate the group with a transparent bounds rectangle so it pivots on the object's centre. Lines end exactly at the object's edges and stop before anything in front of it. Related: [[feedback-format-adaptations-photo-first]].
