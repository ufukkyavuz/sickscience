---
name: feedback-no-black-stripe-on-capsule
description: "Capsule text legibility comes from LIGHTING (a dark card reflection behind the white text), never a drawn stripe; DropOff tube gets nothing"
metadata:
  type: feedback
---

User, 2026-11-05 (final): "her durumda bunların arkasına siyah şerit çekmek zorunda değilsin… ışığı öyle bir ayarlaman lazım ki bu ürünün üzerindeki yazılar okunacak şekilde olmalı. Yani direkt yazıların arkasında siyah şerit var deme." Also: putting a stripe on the matte DropOff tube "bozdun".

History: 11-03 "no stripe, text on chrome" made white text unreadable; my 11-05 fix wrote "black vertical stripe" into prompts, so the model printed stripes on every product including DropOff. Both wrong.

**Why:** the dark band in the client's photos is a photographer's black card reflected in the chrome. It belongs to the light setup, not to the product.

**How to apply:**
- Never describe a stripe/band as part of a product.
- In LIGHT AND SHADOW: "a narrow black card stands opposite each capsule, out of frame, so a soft dark reflection runs down the chrome behind the white lettering and every word reads clearly".
- DropOff (matte cobalt tube): nothing added; negative "stripe or band on the tube". Reject outputs with a stripe on the tube.
- No stripe-removal edits or pixel stripes either way; fix with lighting and regenerate.

Related: [[reference-nano-banana-product-drawing]], [[feedback-product-text-white-and-network-spelling]]
