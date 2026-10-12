---
name: feedback-measure-product-vs-real
description: "In model images, measure the product (h/w ratio + size vs face) against the real product PNGs and fix whatever is off before delivery"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-08T13:57:40.807Z
---

Every image with a person: measure the product's height/width ratio and its size relative to the face, compare with the real PNGs (Products/png: SS/NW closed h/w ≈3.1, PC closed ≈3.26, PC open ≈2.97, DropOff ≈3.36; SS/NW 12 cm ≈ 0.6× chin-to-hairline, PC 14 cm ≈ 0.7×, DropOff 20 cm ≈ 1× face). If off, fix with tools/bottle_rescale.py using the real PNG, or regenerate.

**Why:** User 2026-10-08: "boyutları da gerçek görsellerle bi karşılaştırırsın ne yanlışsa ona göre düzeltirsin… hep insanlı görsellerde ürünlerde bi orantısızlık oluyo".

**How to apply:** Part of the pre-delivery check together with anatomy ([[feedback-check-anatomy]]); dimensions in [[sickscience-product-dimensions]].

**Hand-held exception (user 2026-10-08: "powercycle kaymış kızın eline oturmuyor"):** pasting the real PNG at a new scale into a gripping hand looks slid/pasted even with fingers restored. For hand-held products, regenerate instead. The pose that holds scale best is the bottle standing upright on an open palm beside the face, with a face yardstick in the SCALE section (PC 14 cm ≈ slightly taller than eyebrows-to-chin). Use compositing only for products standing on a surface.

**Video exception (user 2026-10-09: "Ürünleri öyle açık el tutması saçma… hareketler yapınca düşmesi lazım… mantıklı tutması lazım"):** the open-palm balancing pose reads as absurd once the person moves or talks. In any VIDEO, the person grips the product naturally: fingers around the lower half, thumb on the side, label visible. Give the hand a yardstick in the prompt (12.5 cm capsule ≈ palm base to middle knuckles) and measure the result. Keep the palm pose for stills only.

- Small capsule held in hand (2026-10-11, IG rock-paper grid): the model garbles the small vertical lettering ("StapeShift", "NotWork"). Do not enlarge the product. Fix with `tools/label_fix.py in out <json>`: it erases only the letter pixels with a vertical column fill and redraws white Helvetica Bold, reading bottom to top. Always check the label at FULL resolution; the _min.webp preview hides the errors.
