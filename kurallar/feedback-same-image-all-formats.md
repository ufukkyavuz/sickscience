---
name: feedback-same-image-all-formats
description: "Story, Feed and Square must use the SAME image (crops of one 9:16 master); never generate separate square/feed images"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-08T13:10:55.621Z
---

One 9:16 master per creative; Feed (1080×1350) and Square (1080×1080) are crops of it. Never generate a separate 1:1 or 4:5 image for a format. If a crop collides with text, change the text layout (shorter headline, move logo/tag), not the image.

**Why:** User 2026-10-08: "sana dikeyde farklı diğer boyutlarda farklı görsel kullanma demedim mi? bazılarını düzeltiyorum ama tekrar yapma sakın." They were manually fixing frames where I'd used different images per format.

**How to apply:** Plan the master composition (subject low, generous headroom) so all three crops work; don't touch frames the user is fixing. Related: [[feedback-type-scale-and-no-blur]], [[feedback-check-user-edits-before-rebuild]]
