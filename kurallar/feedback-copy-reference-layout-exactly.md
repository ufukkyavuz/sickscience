---
name: feedback-copy-reference-layout-exactly
description: When adapting a reference ad, copy its layout, element positions and type sizes exactly (measured, as % of frame); no own layouts; no logo on Feed/Square
metadata:
  type: feedback
---
The user said (2026-11-06, OneSkin variants): "referanslardaki yerleşimleri boyutları vs birebir uygula kafana göre bişeyler yapma 1080x1350 ve 1080x1080 lerden logoları kaldır".

**Why:** I had rebuilt OneSkin references with my own type scale (120 px headlines) and my own layout. The user wants the reference's proportions, not a reinterpretation.

**How to apply:**
- Before building, measure every reference element as a % of the creative: text x/y, cap height, line height, image boxes, label strips, gaps. Use a grid overlay on the reference image. Then scale those values to 1080 px.
- Type size follows the reference, even when it is below the 120–170 px headline scale. The 32 px minimum still holds.
- The Feed (1080×1350) and Square (1080×1080) adaptations carry no SickScience logo. Story keeps it only if the reference has room for it.
- Other formats keep the reference's relative layout. Reflow only when the aspect forces it.

Related: [[feedback-reference-concept-and-colour]] [[feedback-type-scale-and-no-blur]]
