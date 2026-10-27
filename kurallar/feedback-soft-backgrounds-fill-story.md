---
name: feedback-soft-backgrounds-fill-story
description: "Flat-colour ads - no harsh saturated flat fills; soft clean per-product pastel gradients/shapes, and Story content must fill the frame (no empty bottom third)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-20T22:00:14.343Z
---

User, 2026-10-21, on batch-66 Problem/Solution + award card: "arkaplanlar çok düz ve aşırı tırt renkler, daha tatlı temiz renkler ya da farklı bir arkaplan şekli… ürünlere göre", and Story bottoms were "çok boş".

**Why:** saturated flat purple/green looked cheap; content packed into the 270–1250 band left ~670 px empty at the bottom of the Story.

**How to apply:**
- Use a soft pastel vertical gradient in the product's colour, with a white radial glow behind the product and dark text.
  - Palette in use: SS lilac #F4EDFF→#D9C6FA, NW blush #FFF1EF→#F7D0D2, PC mint #F2FAEA→#D2ECC0, DO periwinkle #EEF2FF→#CBD7F8.
  - The CTA takes the product's accent colour.
- User's fixed Story spacing (Figma 951:882):
  - logo at y 190
  - headers at y 359
  - content from y 481, product top aligned with the card top, ~600 px tall
  - CTA at y ~1308

Related: [[feedback-type-scale-and-no-blur]], [[feedback-check-user-edits-before-rebuild]]
- Update 2026-10-21: the user's 951:882 now has headers y 339, CTA y 1326, and a custom VECTOR contact shadow (node 951:894). The shadow is ~1.17× product width, 11 px tall, product accent colour at 52% opacity, layer blur 14, sitting 9 px above the product base. It "looks more professional" than an ellipse, so clone it for product shadows.
- Same block in Feed: logo 64, headers 213, card 355, CTA 1200. Square: logo 40, headers 150, card 277, name at product base +20, subline +58, CTA ~934.
