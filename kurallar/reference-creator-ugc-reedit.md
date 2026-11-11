---
name: reference-creator-ugc-reedit
description: "Creator UGC re-edit pipeline (2026-10-28): hook-first reorder of the creator's own sentences into ≤20 s variants; wa-1028/render.py"
metadata:
  type: reference
---
2026-10-28: the user sent two creator ShapeShift videos and asked for "hook sıralaması" variants, 4–5 from each. "Hook sıralaması" = the beat order HOOK → PRODUCT → PROOF → CLOSE ([[feedback-video-studio-gates]]). Each variant opens on a different strong moment of the creator's own speech.

- **Script:** `~/sickscience-work/video-projects/wa-1028/render.py`.
  - Segments are source time ranges, cut at word gaps (faster-whisper; pass an np array, because the av build rejects file input).
  - Video `VLIM` holds a frame so that unwanted visuals (the fat-cell animation) never show.
  - Hook text sits at y 300 for 2 s, in the blocks / slam / sticker styles.
  - The creator's audio runs through a ducked bed; the master is −14 LUFS.
- **Burned-in captions:** a creator video that already has captions gets no extra captions, only the hook and the end card.
- **Raw video:** a creator video without captions gets word captions at y 1250. Captions drop to y 1730 while the B/A photos are on screen, and a "DAY 1 / DAY 27" pill sits under each single photo.
- **Claims:** never use a creator's fat lines ("lipid droplets / fat cells / dissolve fat") or "clinical results".
- **End card:** on a face close-up the logo is lost on hair and chin, so cut to a product-in-hand frame for the end card.

Related: [[reference-voiced-ugc-pipeline]] [[feedback-video-max-20s]] [[feedback-show-the-transformation]]

**No zoom on burned-in captions (user, 2026-10-28: "altyazı ekranla birlikte büyüyüp küçülmemeli").** On a source that already has burned captions, use no push-in/zoom of any kind, because the captions would scale with the frame. Only overlays that we draw ourselves may sit on a zoomed frame.
