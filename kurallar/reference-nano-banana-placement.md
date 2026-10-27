---
name: reference-nano-banana-placement
description: "Nano Banana ignores \"product in lower third / 46-66% of frame\" unless the product is also told to be SMALL with an explicit % height; check Story safe band after every product still"
metadata:
  node_type: memory
  type: reference
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-20T20:33:58.733Z
---

Batch-66 (2026-10-20): PowerCycle gold and DropOff gym stills came back with the product in the bottom 35% of a 9:16 frame (Meta UI zone) twice, even with "lower third" and later "occupies 46% to 66% of the frame height".

What moved it: state the product's height as a share of the frame ("only 18% of the frame height, from 40% to 58%", "pulled back so the bottle is SMALL") plus "everything below 62% is calm empty surface". Writing the floor/surface edge position helps.

**How to apply:** after every 9:16 product still, measure the product's top and bottom against 270–1250 px of 1920 before building the Figma frame. If it sits low, fix the prompt as above; don't extend the frame with fills.

Related: [[feedback-measure-product-vs-real]], [[feedback-same-image-all-formats]]
