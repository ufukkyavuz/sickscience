---
name: reference-nano-banana-product-drawing
description: "Capsule label anatomy must be spelled out in every prompt (full-height black stripe, white text on it, cap = exact half, rounded bottom); products on counters/tables drift to the foreground and get oversized — prefer in-hand at face depth"
metadata:
  node_type: memory
  type: reference
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-21T08:38:01.348Z
---

Batch-70 (2026-10-21). The user rejected the NetWork dark scene: "ürün yanlış". Even with the element attached, the model drew the text straight on the chrome, left out the black stripe, made the cap short and the bottom flat.

**What fixed it:** the CAP block in `prompts/batch-70-contextual-scenes.py`. It spells out the label anatomy:
- A narrow vertical BLACK stripe runs the full height over both halves.
- Every word is pure white on that stripe, never text directly on the chrome.
- The cap is exactly the upper half.
- The ends are fully rounded top AND bottom; never flat-bottomed.

**Scale drift:** when the product stands on a table or counter, the model puts it at the front edge. It then renders 1.5–2× the face height, which is the banned "bring the product closer" trick. Telling it "beside her elbow" or "8% of the frame" did not help, and neither did a mirror scene.
- What worked: product held in her hand at face depth (K, M).
- Also worked: a no-person still life where the product is the hero.
- Q_pc_gold showed the opposite problem: "pulled back / small" was still ignored and it came back as a close-up. Measure every output before layout.

Related: [[reference-nano-banana-placement]], [[feedback-measure-product-vs-real]], [[sickscience-product-dimensions]]
