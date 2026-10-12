---
name: feedback-check-user-edits-before-rebuild
description: "Before editing or rebuilding any Figma frame I made earlier, check whether the user has edited it since; never delete-and-rebuild a frame the user touched"
metadata:
  type: feedback
---

Between my turns the user edits frames I created (e.g. Beacon Award B/C on 2026-10-03). I deleted all children and rebuilt those frames, which wiped their work; plugin edits cannot be undone from my side.

**Why:** user: "benim yaptıklarımı bozdun… sadece onları geri al". Project rule already says not to break the user's Figma edits; it applies to frames I created too, not only old ones.

**How to apply:** before any change, snapshot the frame (child ids/names/positions) and compare with what I last built; if anything differs, ask first or make only additive, targeted changes. Prefer editing properties in place over remove-and-rebuild. Related: [[feedback-type-scale-and-no-blur]].
