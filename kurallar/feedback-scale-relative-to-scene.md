---
name: feedback-scale-relative-to-scene
description: "Prompt SCALE: state the product's size as a ratio to objects in the same scene, not only in cm"
metadata:
  node_type: memory
  type: feedback
  originSessionId: f44c525d-31ea-4866-a6a2-a898dab8636c
  modified: 2026-11-01T00:03:44.264Z
---

User, 2026-11-01, batch-85: "Ürün boyutlarını o görseldeki herhangi bir şeye oranlayarak verirsen daha doğru sonuçlar elde ederiz."

**Why:** the model ignores absolute cm and drifts to oversized products; a visual comparison inside the frame gives it something to match.

**How to apply:** in every SCALE section add ratios to named scene objects, e.g. "capsule as wide as one objective lens barrel", "capsule height = four-fifths of the skull's height", "as tall as the pumpkin is wide". Keep the cm figures as well; the ratios come from them. Then measure the output as before ([[feedback-measure-product-vs-real]]).

Related: [[sickscience-product-dimensions]], [[reference-nano-banana-product-drawing]]
