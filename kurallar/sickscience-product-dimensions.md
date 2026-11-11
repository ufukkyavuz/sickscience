---
name: sickscience-product-dimensions
description: Real SickScience product/bag sizes in cm for the SCALE section of every image prompt
metadata:
  node_type: memory
  type: project
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-11-02T16:40:57.496Z
---

Real dimensions given by the user (2026-10-02), to be written into the SCALE section of every photographic prompt:

- ShapeShift capsule: 12 cm tall, 3.5 cm diameter
- NetWork capsule: 12 cm tall, 3.5 cm diameter
- PowerCycle capsule: 14 cm tall (confirmed again 2026-11-05), 4.5 cm diameter (not re-confirmed)
- DropOff tube: **19 cm tall** (confirmed by the user 2026-11-05: "dropoff 19 amazondaki doğru"). Tube/SS height = 1.58, tube/PC = 1.36
- Makeup bags / On-the-Go pouches: 21 × 16 cm
- Holographic tote bag: 30 × 40 × 10 cm

**Why:** earlier images (UGC selfies, "not a pill" shots) got product scale wrong; the user measured and supplied these so the next images are realistic.

**How to apply:** state each item's cm size plus a hand/face reference (an adult palm is ~18–19 cm long, so a 12 cm capsule is about two-thirds of a hand). Re-ask for the DropOff size before precise close-ups. Related: [[feedback-photographic-prompt-format]], [[sickscience-client]].

**Perspective may enlarge, proportions may not** (user, 2026-11-02, replaces the 2026-10-04 foreground ban): camera play can make the product look large, see [[feedback-lens-and-product-scale]]. Fix garbled labels with a pixel relabel; regenerate if the bottle's own proportions break.

**Verified 2026-10-08** (user asked "sence ürün bu kadar büyük mü… kullanıcı yorumlarına bak"):
- ShapeShift: Amazon.ca B0DVC1LK9S lists 12.5 × 4.3 × 4.3 cm, 130 g. Customer photos (Okendo reviews) show it filling a woman's palm, about three fingers wide. Real h/w is about 2.9, so it is chunkier than the "3.4×" prompt rule.
- DropOff: Amazon.ca B0DVC5NHQ6 lists 19 × 4 × 4 cm, 135 g, 100 ml. Reviews: "wish the bottle was bigger", "needs a much larger size".
- PowerCycle: not on Amazon. It holds 60 ml (2.03 oz on Ulta), twice the SS volume. Studio-PNG proportions (same photographer) suggest about 14–15 cm × 4.5–5 cm, so 14 cm is plausible.
- In customer selfies the capsule held next to the face looks as tall as the face, because it is close to the lens.

**PowerCycle is visibly bigger, always (client Merve, 2026-11-02: "yeşil olan şişe 60 ml, mor olan 30, bazı görsellerde boyutlar aynı gözüküyor"):** target height ratio PC/SS = 1.17, diameter about 1.2 (checked on client shot S_0684). Products/sets PNGs drew every capsule at 1398 px with PC narrower, so ss-set-vault and ss-set-award-duo carried the error into generations. Vault and award PNGs were rebuilt on 2026-11-02 (.orig.png kept), but the Higgsfield elements still hold the old images. In scenes with PC plus SS/NW use the separate elements, write the ratio in SCALE and measure the output. tools/bottle_grow.py enlarges a bottle from its own pixels; details in prompts/batch-92-pc-boyut.md.

**DropOff width (2026-11-03):** the 19 × 4 cm listing is the round end. The crimped flat end is about 6 cm wide, and in client shot S_0314 the tube reads about 3.3:1 at the crimp. Do not call a tube "too wide" from 4.7:1. Check its height against the capsule instead: tube/PowerCycle = 1.43.

**Open question (2026-11-05):** the ShapeShift/NetWork diameter. The rule says 3.5 cm (h/w 3.4); Amazon.ca says 4.3 cm (h/w 2.9). Ask for a ruler measurement before judging a capsule "too wide" or "too thin".

**Measured on the real PNGs (2026-11-06):** the SS/NW capsule silhouette in Products/png (ERH_7470B, 7471B, 7477C, 7480C) is 3.1× as tall as wide, not 3.4 (3.4 comes from the 12 × 3.5 cm figures). When checking generated images, a height/width of ~3.1–3.2 matches the real bottle; reject only below ~3.0. In-hand shots of SS kept coming out at 2.96–3.17; 3.15+ is acceptable.
