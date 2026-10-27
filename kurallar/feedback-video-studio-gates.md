---
name: feedback-video-studio-gates
description: "Every video follows the motion-studio gates and the lemo-opuscar director/technique guides; no one-shot 'big text + gradient + fade' videos"
metadata:
  type: feedback
---

User, 2026-10-21, angry: "sonra yine bana boktan videolar yapma, adamlar her şeyi anlatmış". This came after sharing rari's "Motion Engineering" article and the lemo-opuscar repos.

**Why:** the user saw one-prompt videos come out generic (centred big text, gradient, everything fades in, logo at the end). They expect the documented studio process, every time.

**How to apply.** For ANY video (ads, UGC edits, animations), before rendering:
1. Write a brief in the project folder:
   - one-sentence takeaway
   - audience
   - duration ≤20 s
   - formats (one master cropped — the SickScience rule wins over "separate compositions")
   - real assets only
   - keep/avoid list
2. Do a reference analysis and write it up as a style guide: palette hex, type, composition, pacing, motion, texture. It teaches grammar; never copy.
3. Write the shot list as states, with entry/exit and a reason for each beat:
   - HOOK 0–2 s
   - PROBLEM
   - REVEAL
   - PROOF
   - CLOSE
4. Build the music/beat grid first and put SFX on the same timeline.
5. Make sheets: a contact sheet of every beat, plus 0.2 s strips of fast transitions.
6. Critic pass on the sheets:
   - name the 3 worst defects (timestamp, evidence, local fix)
   - patch only those sections and re-render them
   - repeat once
7. Final checks:
   - one full-speed viewing with sound
   - −14 LUFS
   - no black frames
   - captions never over the subject
8. Read `~/lemo-opuscar/DIRECTOR.md` §10–11 ("failures we saw most", "before you deliver") as the checklist.

For code-rendered animation, use the `lemo-opuscar` skill (installed in ~/.claude/skills; library in ~/lemo-opuscar). Pick a style whose look fits SickScience premium (glass-product, white-model, swiss-motion, dataviz, microscope). Brand rules still apply: Founders Grotesk, real product PNG/photo, no LemoLab sign-off.

Related: [[feedback-video-max-20s]], [[reference-motion-tools]], [[feedback-no-pasted-product-in-video]]
