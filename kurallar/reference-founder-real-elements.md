---
name: reference-founder-real-elements
description: "Founder likeness pipeline from the Website ufo-character method: portrait candidates first, user picks, then sheet, then element, then style; 3D toon elements are no face source"
metadata:
  type: reference
---

User, 2026-11-03: real-human versions first, then convert to each style ("normal insan halleri bize hep lazım olacak"). Then: "website tarafında öğrenmiştik referans ve sahne nasıl oluşturulmalı".

Method (Website memory `project_ufo_character_video.md`, `reference_higgsfield_image_playbook.md`):
1. Face first: close portrait only, 3:4, 5 real photos (3 front, 1 side, 1 close) + concrete face description. Nothing else in the prompt. Piling outfit and panels on loses the face.
2. User picks a candidate. No sheet before that.
3. Sheet with the approved portrait as reference: close face + front + back full body, plain grey, face covered by a white oval on full-body panels so video models don't drift.
4. Element from the sheet (`image_job` id, no credits).
5. Style version from the approved face, same order.
6. Location and props are separate plates. Show the scene still; no video before approval.

Sheet format is fixed, copy Website `sheet_E.png` (user, 2026-11-03: "gri arkaplanda yüz yakın çekim boy ön arka"): 16:9, three panels on matte mid-grey, big close face, front full body with white oval over the face, back full body. Never invent another layout. Prompt: `__tri` in the transcript, six real photos attached (five face, one full body).

Status 2026-11-03: `_calisma/batch-96-bf-film-v2/sheets3/` (merve_A, polen_A, polen_B) await the user's pick, no element made yet; face crops in `refs/faces/` (m1–m5, p1–p5). Elements `ss-founder-merve-real` (32f6f60e) and `ss-founder-polen-real` (717e60ac) were made too early from unapproved sheets: REJECTED ("yine benzemedi"), do not use. Old 3D elements have the wrong hair.

Current look: Merve long platinum blonde waves with darker roots, heavy lids, fuller lower face; Polen very long jet-black waves.

Related: [[feedback-our-characters-founders]], [[feedback-identify-people-carefully]]


Approved base 2026-11-03: Merve = face panel of `sheets3/merve_A.png` + body panels of `merve_slim_2.png`, joined in code without regenerating (`sheets3/merve_onayli.png`). Polen A is my pick, not confirmed by the user.

Reel style (user: "fırça dokusu"): style prompt comes first, likeness inside it. Few brush-pen lines that swell and taper, flat porcelain skin, one peach wash on lids, one-line nose, hair as painted masses, gouache texture, watercolour wash with paper grain (`__fs2`). Converting a whole sheet at once loses the face: convert the close face first. Queue dropped 2 of 4 again: keep to 2 in queue.


Matching a reference style (2026-11-03): describing it failed three times. What worked at once: give the reference frame itself as the first image and edit it (`__swap`: "keep this frame exactly, only the woman changes") with the approved face crop as second image. Results `_calisma/batch-96-bf-film-v2/swap/`. Frames carry the IG mute icon; capture without it. The reel is an artist's work: flag before paid use.


Correction, same day: a pure `__swap` copied the reel's scene and was rejected ("senaryomuz böyle değildi"). New scenes from text came out comic-book clean, and repainting them added only speckle. Best so far: `__tf` transforms a high-res reel frame (zoom scale 1, 671×1198, not 403 px) into OUR scene, changing place, people and objects while the frame's paint survives. Products must look the same in every frame. Files `story/yeni_cati.png`, `yeni_lab.png`.


Working recipe 2026-11-03, BF film (`_calisma/batch-96-bf-film-v2/film/ss/`): user dropped to ShapeShift only. First make ONE hand-painted product reference by replacing the reel's own product in its frame (`film/ss_boyali.png`), then in every frame attach Polen, Merve, painted product, reel frame as base, in that order, and transform. Reference ratio over 1:2.5 is silently dropped. Multi-file uploads can land in any order: upload one by one and check the chips. Follow the reel's beats: wide, object close-up, mid, low close-up, eye through clouds, empty city, landing, final.


Story continuity (user, 2026-11-03: "Uçtu da mı çatıya çakılıyor?"): beautiful frames can still break the story. Before generating, write cause and effect frame by frame and check size, place and how each person got there; never copy a reference beat that does not fit our story. Build later frames from the previous approved frame so room and building stay the same. Result `film/v2/son/kare_1..8.png`.
