---
name: reference-figma-text-invert-mask
description: "Figma text that flips colour across a photo edge: black text below, white copy in a group with a mask shape at index 0; order matters"
metadata:
  node_type: memory
  type: reference
  originSessionId: f44c525d-31ea-4866-a6a2-a898dab8636c
  modified: 2026-11-02T17:09:55.363Z
---

Used on Black Friday BF7 (diagonal) and BF8 (inside capsule), 2026-11-02. Text stays editable and reads across light and dark areas.

**How:** add the dark text, add a white copy on top, draw the mask shape over the bright or dark region, `figma.group([mask, white], frame)`, then `g.insertChild(0, mask)` and `mask.isMask = true`. A mask only clips layers above it, so without `insertChild` the white copy shows everywhere. Applies [[feedback-text-integrated-in-scene]].

Higgsfield composer, same day: keep newlines by inserting each paragraph with `execCommand('insertText')` and dispatching shift+Enter keydown twice; raw `\n` is dropped. The composer can reopen in Video mode (Cinema Studio, paid) with Unlimited off, so check Image, Nano Banana Pro and the Unlimited toggle before Generate.
