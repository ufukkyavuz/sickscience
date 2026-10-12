---
name: feedback-no-pasted-product-in-video
description: "Never cut-and-paste the product PNG into scenes or end cards; generate the product inside the photo (nano banana + real PNG as reference), then animate"
metadata:
  type: feedback
---

Product beats built by pasting the real PNG onto a generated empty tabletop (shadow, reflection and spring drop-in drawn in code) still look obviously composited. This applies to video stages and to end-card packshots.

**Why:** User 2026-10-09: "Ürünleri sonradan yerleştirme güzel durmuyor… kesip koyduğun çok belli oluyor, direk görsel üretip öyle koyabilirsin illa koyacaksan".

**How to apply:**
- Generate the product photo with nano_banana_2_1, passing the real ERH PNG as `image_references`. Specify lettering, proportions, real lighting, reflections and contact shadow in the prompt. Then animate with a Kling std silent slow push, or a light code push.
- End cards: use a generated packshot photo with empty upper space, and add only the logos and type in code.

This overrides the older "compositing OK for standing products" note in [[feedback-measure-product-vs-real]]. Related: [[feedback-product-integration-not-pasted]].
