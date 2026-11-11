---
name: project-founders-film-next-round
description: "Founders notebook film (v24 delivered 2026-11-08) is on hold; next round = approve final layout first, then regenerate; music must change"
metadata:
  node_type: memory
  type: project
  originSessionId: f44c525d-31ea-4866-a6a2-a898dab8636c
  modified: 2026-11-08T15:18:15.959Z
---

Founders notebook film: v24 delivered 2026-11-08 (Video/2026-11 Kasım/03 Animasyon). On hold until the founders' old photos arrive (2009 photo, mother + balloons, old lab photos).

User's notes for the next round (2026-11-08):
- Content and images will change and the film will be produced again.
- Before regenerating, get the user's OK on a still of the FINAL two-page layout (every print and text in place). Then produce the film from that layout, so nothing shifts or drifts during production or placement.
- Music must change. The user is thinking of a better-known track. Decide together; the user supplies a licensed mp3 (see [[reference-trend-audio-workflow]]).
- The user said "şu an bir şey yapma": do nothing on it until they pick it up again.

**Why:** Each content change so far has moved elements and broken the sync. Locking the layout first avoids redoing the whole film.

**How to apply:** When the film resumes, first send a static layout mock with the new photos and text. Render only after approval. Ask about music before mixing.

Related: [[feedback-brand-film-no-product-list]], [[feedback-frame-problem-fix-camera-not-layout]].

**2026-11-10 v27 delivered:** opening re-generated in Adobe Firefly (Veo 3.1, 1080p, 9:16, 4 s, first+last frame; user asked for Firefly). First frame = closed notebook lying exactly on the right-page footprint of the spread; last frame = the FINISHED spread with drawings and prints (user: "niye yazısız ürettin" — never a blank spread). Only the two desk photos outside the notebook were removed from the start; they now drop in at the end pull-back (animatic_real.add_prints desk=True). Delivered WITHOUT music (user: "müziksiz yapalım, müzik sonradan eklenir") — audio_v10.py NOMUSIC=1. Firefly upload trick: patch HTMLInputElement.prototype.click to catch the file input, move it to document.body, then file_upload.
