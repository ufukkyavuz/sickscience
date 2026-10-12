---
name: feedback-product-text-white-and-network-spelling
description: "All text printed on SickScience products must render pure WHITE; product name is spelled \"NetWork\" (capital W)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-03T07:43:42.433Z
---

Every word printed on the products in generated images must be pure WHITE (cap and silver half), never black or grey. The product name is "NetWork" with a capital N and a capital W, not "Network". (User, 2026-10-03.)

**Why:** the generations kept rendering the lower-label text black. The client's open-pump PNG and the first Higgsfield elements said "Network", so every NetWork image carried the wrong spelling.

**How to apply:**
- Write the white-text sentence into every prompt, and add black or grey letters to the negatives.
- Reject outputs with dark letters.
- Use the corrected `-v2` NetWork elements, never the old ss-network / ss-open-network / ss-set-glp1.
- When the user reports a label error, check the source PNGs and the Higgsfield element images first; that is where it propagates from.

Related: [[sickscience-product-dimensions]], [[feedback-photographic-prompt-format]].
