---
name: feedback-remove-background-in-figma
description: "Cut out images with Figma's own Remove background, never by code"
metadata:
  type: feedback
---

User, 2026-11-01, batch-85f: "Arkaplan silme işini de figmada halletsen daha iyi olur düzgün siliyo."

**Why:** code cut-outs (thresholds, masks, inpainting) leave halos and patches. A PIL inpaint on the gel type left a purple triangle and a pale block; Figma exposure filters washed the gel out instead of clearing the grey.

**How to apply:**
- Place the uncut image in Figma and run Remove background on the layer (selection toolbar, More menu; desktop app, see [[figma-yetenekler]]).
- No PIL masks, flood fills or inpainting for cut-outs. Need a different image? Regenerate it, don't retouch it by code.
- If the Figma app isn't accessible from here, leave the layers ready and name them for the user. On 2026-11-01 computer-use access to Figma was denied; don't re-request it in the same task or route around it through a browser.

Related: [[feedback-expand-in-figma]]
