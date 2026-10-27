---
name: feedback-no-cropped-subjects
description: Never cut the subject off at the frame edge (legs, feet, head) and never let text or gradients cover the image that carries the proof
metadata:
  type: feedback
---

User, 2026-10-16, on the v2 B/A countdowns: "yazılardan vs görsel gözükmüyo daha düzgün yapabilirsin… videoda alttan kesik kalmış bacaklar böyle şeyler istemiyoruz kesik görüntü sevmeyiz".

**Rule:**
- The subject is fully inside the frame with margin. Body shots keep the feet and head in frame.
- Ask for this when generating: "whole subject inside the frame, nothing cut off by the edges", plus a square or 4:5 source that leaves margin.
- Do not crop a tall source so that the body gets cut.
- Text, stickers and dark gradients go on the background next to the image, never over the proof area.

**Why:** a cut body looks cheap. Text that covers the before/after hides the whole point of the ad.

**How to apply:** layouts put the copy block above or beside the photo, on the photo's own backdrop colour; see `_calisma/batch-48-countdown/render48v3.py`. Check the edges of every frame before delivery.

Related: [[feedback-no-framed-photos-be-creative]], [[feedback-show-the-transformation]]

2026-10-20 (Oprah Daily PR, user furious: "daha yeni dedim ki şunları kesme"): when a layout change (vertical card, narrower slot) forces a crop, NEVER crop the product scene to fit — shrink/re-arrange the container instead (narrower centred card, or side-by-side where vertical cannot fit uncropped) and say so. Check every format screenshot for crop before reporting.
