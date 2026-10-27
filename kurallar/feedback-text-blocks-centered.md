---
name: feedback-text-blocks-centered
description: "Colour blocks/pills/cards behind text must be optically centred on the glyphs — compute from textbbox, never fixed offsets"
metadata:
  type: feedback
---
User 2026-10-20 (ShapeShift VO cuts): "yazıların arkasına attığın kareler ortalı olmuyo… bozuyosun sürekli". The rule applies to all future work: videos, Figma, statics.

**Why:** In PIL, a block drawn from a hard-coded y/size offset sits off-centre. Founders Grotesk has a large ascent offset, so the text looked too low or too high inside its purple block. The user had seen this repeatedly.

**How to apply:**
- In PIL, compute `d.textbbox((x, y), text, font)` and draw the block as bbox ± equal padding (e.g. px 16–26, py 14–20).
- For a multi-line card, centre the whole block using the first line's bbox top and the last line's bbox bottom.
- In Figma, use auto-layout with equal top/bottom padding and check the screenshot.
- Before delivery, zoom into one hook frame and one caption frame and check the vertical centring.
- Implemented in `lilac-1020/render2.py` (caption_img, hook_layer).

Related: [[reference-voiced-ugc-pipeline]] [[feedback-podcast-cutdown-style]]

**Figma pills/CTAs (user, 2026-10-21: "butonlara niye üstten 22 alttan 18 verdin?"):** never use asymmetric "optical" padding. Set the text's leadingTrim = 'CAP_HEIGHT' and use equal top/bottom padding (CTA standard: 30/30, 64 sides, Founders Bold 40 → 85 px pill). Then measure the ink gaps on an exported screenshot. Founders Grotesk caps already sit low in the untrimmed box, so 22/18 pushed the text 4 px down.
