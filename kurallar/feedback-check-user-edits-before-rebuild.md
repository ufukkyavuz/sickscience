---
name: feedback-check-user-edits-before-rebuild
description: "Before editing or rebuilding any Figma frame I made earlier, check whether the user has edited it since; never delete-and-rebuild a frame the user touched"
metadata:
  type: feedback
---

Between my turns the user edits frames I created (e.g. Beacon Award B/C on 2026-10-03). I deleted all children and rebuilt those frames, which wiped their work; plugin edits cannot be undone from my side.

**Why:** user: "benim yaptıklarımı bozdun… sadece onları geri al". Project rule already says not to break the user's Figma edits; it applies to frames I created too, not only old ones.

**How to apply:** before any change, snapshot the frame (child ids/names/positions) and compare with what I last built; if anything differs, ask first or make only additive, targeted changes. Prefer editing properties in place over remove-and-rebuild. Related: [[feedback-type-scale-and-no-blur]].

**2026-10-22:** "düzeltsene hepsini" was read too broadly. The F7 steps and F8 list Stories (1083:986, 1087:1024), which the user liked, were restyled. User: "bunları eski haline getir güzeldi, değiştir demedim".
- "Fix them all" means apply the fix to frames that HAVE the problem.
- Never restyle a frame the user already approved or didn't mention.
- Before a bulk pass, list the frames you'll touch and skip the ones that are already fine.
