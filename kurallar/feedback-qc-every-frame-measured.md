---
name: feedback-qc-every-frame-measured
description: Before delivery every frame is rendered and measured — cut/hidden products and unreadable text are not allowed; the user does not check
metadata:
  type: feedback
---
The user said (2026-11-06): "ben kontrol etmiyorum. kesik bozuk yarısı çıkmayan ürün varsa seni kapatıcam okunmayan yazı varsa da aynı şekilde".

**Why:** the user does not check deliveries. They treat a cut, broken or half-hidden product, or an unreadable text, as grounds to stop working with me.

**How to apply:** after every Figma batch, and before reporting:
- Render every frame with get_screenshot, download them (curl into the scratchpad) and run `scratchpad/qc.py`, or do the same check by hand:
  - measure the contrast between the text colour and its background;
  - flag a large headline at a median below 3, and everything else below 4.5.
- Check the bottom and side edges of every frame in a strip sheet: no product body may touch the frame edge (reflections are fine).
- Check that no product sits behind text, a badge or the seal.
- Fixes that worked:
  - Feed: use the Square's expanded image at 1350×1350.
  - Square: re-expand the image as Portrait 2:3 with a little zoom-out, then place it at width 1080 and y≈-188.
  - Bright background: lower the Photo fill's highlights and exposure.
  - Headline: double dark shadow (radius 40 a.65, plus radius 10 a.9 when an object crosses the text).
  - Logo over a light area: double dark halo.
  - Purple accent on near-black: lighten it to #CD7DF0.
- The magenta "Science" in the logo has low contrast on light backgrounds by nature; measure it every time.
Related: [[feedback-check-layout-full-size]] [[feedback-no-cropped-subjects]]
