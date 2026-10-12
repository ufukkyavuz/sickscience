---
name: sickscience-product-dimensions
description: Real SickScience product/bag sizes in cm for the SCALE section of every image prompt
metadata:
  node_type: memory
  type: project
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-02T14:48:42.060Z
---

Real dimensions given by the user (2026-10-02), to be written into the SCALE section of every photographic prompt:

- ShapeShift capsule: 12 cm tall, 3.5 cm diameter
- NetWork capsule: 12 cm tall, 3.5 cm diameter
- PowerCycle capsule: 14 cm tall, 4.5 cm diameter
- DropOff tube: about 20 cm tall (provisional, "şimdilik")
- Makeup bags / On-the-Go pouches: 21 × 16 cm
- Holographic tote bag: 30 × 40 × 10 cm

**Why:** earlier images (UGC selfies, "not a pill" shots) got product scale wrong; the user measured and supplied these so the next images are realistic.

**How to apply:** state each item's cm size plus a hand/face reference (an adult palm is ~18–19 cm long, so a 12 cm capsule is about two-thirds of a hand) and add "if in doubt make the products smaller". Re-ask for the DropOff size before precise close-ups. Related: [[feedback-photographic-prompt-format]], [[sickscience-client]].

**Never enlarge via foreground placement** (user, 2026-10-04: "ürünün boyutlarını aşırı büyük yapıp bozmuşsun"): in people scenes the product sits at the same depth as the person or in her hand, so it reads at true 12 cm scale. Fix small garbled labels with a pixel relabel, not by enlarging the product.

**Verified 2026-10-08** (user asked "sence ürün bu kadar büyük mü… kullanıcı yorumlarına bak"):
- ShapeShift: Amazon.ca B0DVC1LK9S lists 12.5 × 4.3 × 4.3 cm, 130 g. Customer photos (Okendo reviews) show it filling a woman's palm, about three fingers wide. Real h/w is about 2.9, so it is chunkier than the "3.4×" prompt rule.
- DropOff: Amazon.ca B0DVC5NHQ6 lists 19 × 4 × 4 cm, 135 g, 100 ml. Reviews: "wish the bottle was bigger", "needs a much larger size".
- PowerCycle: not on Amazon. It holds 60 ml (2.03 oz on Ulta), twice the SS volume. Studio-PNG proportions (same photographer) suggest about 14–15 cm × 4.5–5 cm, so 14 cm is plausible.
- In customer selfies the capsule held next to the face looks as tall as the face, because it is close to the lens. In ads keep it at face depth.
