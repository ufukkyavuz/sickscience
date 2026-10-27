---
name: feedback-show-the-transformation
description: "Results videos: show the start and end (aligned same-angle jump cuts, held before/after); flag date doubts once then follow the user; centre pill text with anchor mm"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-14T20:46:27.738Z
---

On 2026-10-14 the user rejected a "12-day diary" cut of Dr. Merve's ShapeShift challenge. That cut skimmed past the days and never showed a before/after. The user wanted me to think like an ad person:

> "Day Zero'dan… 14 gün sonraki halini… before after vermeden hızlıca geçmek sence mantıklı mı?… hep aynı açıdan… stop motion ya da jump cut… sonunda nereden nereye geldiğini belli etsek"

**Rule:**
1. In any results or challenge video, the product's proof is the transformation.
2. Open with the result if possible: a split hook.
3. Show the progression from the same angle, aligned so that only the result area changes. `align45.py` does this by locking the ear and nose tip to the same two points and mirroring left-facing shots.
4. Use fast 0.5 s jump cuts with big day labels.
5. End on a held before/after.

**Elapsed time:** check the capture dates (`com.apple.quicktime.creationdate`). If they disagree with the claimed timeframe, flag it once, in one line. Then follow the user's decision; they know the shoot.
- Example: the "Day 14" clip of Dr. Merve's challenge read 24 Jul. The user confirmed "14 günde etkisini gösteriyo" (it shows the effect in 14 days), so it is labelled DAY 14.
- Never silently drop the before/after over a date doubt.

**Why:** a diary without a visible payoff does not sell. The user expects ad judgement, not only rule-safety. They are frustrated when a safe choice removes the persuasive core.

**How to apply:**
- Before editing, pick the strongest real before and after frames. Check their capture dates (`com.apple.quicktime.creationdate`).
- Build the aligned sequence and caption the real time span.
- Put the logo where it does not cover the result area.

**Pills, chips and buttons:** centre the text with PIL `anchor='mm'` on the pill centre, and size the pill from `textbbox(..., anchor='mm')`. Top-anchored text sits off-centre (user: "chiplerin pillerin butonların içindeki yazılar da ortalı olmuyo").

**End cards on video:** logo + URL plain, straight on the footage. No dark band/plate under them and no glow/halo (user, 2026-10-15: plate "çingene işi duruyo"; glow "glow atma… dümdüz koy"). On light walls use the original black + magenta logo with dark text.

Related: [[feedback-ba-must-match-person]], [[feedback-video-max-20s]], [[feedback-no-footnotes]]
