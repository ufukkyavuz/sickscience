---
name: feedback-reference-image-attach
description: "Attach the pin itself as an image reference in Higgsfield, and read light shape, tone and depth planes before writing; A/B test 2026-11-03 showed it clearly better"
metadata:
  type: feedback
---

Attach the reference image to the Higgsfield job, not just its description. Before writing, read it for: shape of the light (e.g. R10's gauge grows thin to thick), exact tones, depth planes (blurred glass in FRONT of the product, sharp product, soft glass behind), reflection and real 3D perspective.

**Why:** user, 2026-11-03: "Referansların da düzgün okunmamış… aynı tonları yakalamaya çalış… derinlik algısı… üç boyutluluk algısı yok". An A/B test of 8 scenes on the same text: the attached pin matched tone and composition far better in 7 of 8; only the R10 light gauge taper came out better without it.

**How to apply:**
- Prompt adds an IMAGE REFERENCE paragraph: authority for light, grade, glass, depth, composition; takes nothing else (no products, brand names, text).
- Ratio follows the reference (3:4 used), not 9:16; other formats by Figma Expand.
- Real packaging exists: silver iridescent carton, photo `_calisma/batch-95-bf-ref-test/refs/box_shapeshift.jpg`, New Image S_0285–0317. Attach it when a box is in the scene. Never invent a black box. With the box photo alone the model drew a hexagon box; box + pin gave the true carton.
- The hero in the reference pulls our tube large, so measure PC/SS and tube/PC after every run. Prompt sizes as ratios, see [[feedback-scale-relative-to-scene]].

Composer mechanics: [[reference-higgsfield-composer-refs]].
