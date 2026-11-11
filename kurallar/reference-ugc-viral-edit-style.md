---
name: reference-ugc-viral-edit-style
description: UGC viral re-edit pipeline (2026-11-06) — Buzzfy rules + user's Notion caption method (big word behind the head via Vision person mask, waveform-snapped captions)
metadata:
  type: reference
---
2026-11-06: the user asked for 10 viral edits from the client's "All UGC" Drive folder, edited "by Buzzfy", then styled after a Notion guide (Shaan Johari, "How I edited my captions reel with AI").

**Script:** `~/sickscience-work/video-projects/ugc-viral-1106/render.py`.
- Cuts are set in `edits.py` as phrase pairs.
- Sources are read straight from the Drive path in `srcmap.py`. The user does not want copies or bulk downloads. Evict the Drive cache after use with `scratchpad/evict`, which calls `FileManager.evictUbiquitousItem`.
- The person mask comes from `~/sickscience-work/tools/segvid`, a Vision person-segmentation tool that runs on a folder of frames.

**Style rules:**
- Open on the peak line.
- One big key word (Founders Bold, about 85% of the frame width) pops in on the frame it is spoken. It goes behind the head only when the head top is at y ≥ 300 px. Close-up UGC usually has the head at the top of the frame; there the word goes in front at chest height (y ≈ 1000).
- The word never crosses a cut, and it leaves before a contradicting word (BEFORE is gone before "after" is said).
- Captions: Founders Bold 76 px, soft shadow, at most 3–4 words, y 1180. Hide the whole caption group that contains the big word; removing just the word leaves broken lines.
- Word starts snap to the audio onset.
- No added captions on a creator video that already has burned-in captions.

**Other:**
- Billo watermark: remove it by cropping and zooming (crop 932×1655 starting at y 265), not by blurring.
- The user has no objection to TikTok-downloaded creator clips.

Related: [[reference-creator-ugc-reedit]] [[reference-dropbox-ugc]] [[feedback-video-max-20s]]

**Update 2026-11-06 (after user review):**
- **B/A creator clips:** the creator usually says "that was my before" while the AFTER footage is already on screen; the before footage is earlier in the clip. Find it from a contact sheet and open on it under a BEFORE label (video taken from another source time, `vstart`), then show AFTER as she says it.
- **Comedic or high-energy creators** get "fun mode" (`FUN` in `edits.py`): punch-zoom on stressed words, a shake on the punchline, Apple emoji that fly in from the sides at y ≈ 860 (never over the face), and a pop or whoosh on each.
- **"Metal" SFX:** the user wanted the trending metallic clang on 1–2 videos. It is synthesised (`metal_clang`), not downloaded, and placed on the joke word (BS, "universe").
- **Black frames:** freeze on the last good frame (`VHOLD`) when the source cuts through black.

**Round 2 (2026-11-10, Viral UGC 2):** `_calisma/ugc-viral-2/` (render2.py, edits.py, srcmap.py, resolve.py reads `w/NN.json`; run with `~/sickscience-work/venv313/bin/python`, TMPDIR=/private/tmp/claude-501).
- **User steer:** the 1106 hit worked because of the pop-up/before-after, NOT because DropOff; mix products, prefer recognisable people (Today Show clip), explain the product properly, and animate text: word-by-word pop, blur→sharp, slide, spin, drop; big word behind speaker; product chips that slide in.
- **Engine:** `STYLE[k] = cap/big/bpm/key/tick`, `CHIPS` (output-time chip with site-verbatim product name + descriptor), per-seg `lcrop` pan for landscape sources, numeric segs allowed.
- **Lessons:** burned-in-caption sources get no captions (chips + big word only); creator fat-cell lines are cut; Whisper mishears (Shapelift, liposurum, 6 .30am) get fixed via WFIX/merge rules; the → glyph is missing in Founders.
- **Delivered:** `Video/2026-11 Kasım/01 UGC/Viral UGC 2/` (10 files, 11–18 s, -14 LUFS). Sources read in place, then evicted with `scratchpad/evict` (swiftc evictUbiquitousItem).
- **Educational cut (2026-11-10):** Merve's exosome/delivery-truck clip (Drive file shared from merve@genestetix.com, not in the mounted tree → one browser download to `_calisma/ugc-viral-2/src/edu.MOV`). `INSERTS` in edits.py = full-bleed white science diagram beats (`make_insert`), `CHIPS` plain labels with brand-colour dots.

**Round 3 (2026-11-11, Viral UGC 3):** Polen/Ayşim raw shoots from Berk's Drive folders (shared, not mounted) → `_calisma/ugc-viral-3/` (render3.py + specs.py, spec-driven: segs/texts/big/inserts/emoji/punch/sfx/music).
- **Downloads:** one Chrome download per file into `src/`. Big files open a "virus scan" page: open the file viewer → download → click "Yine de indir" in the tab it opens. Programmatic form submits get blocked.
- **iPhone HLG raws:** converted with Apple's tone map (`tools/hlg2sdr.swift`). Berk's exports are darker (his grade), so don't match to them. Check colour: source vs output mean RGB within ~2 levels.
- **Music:** 5 new Pixabay tracks added to the INO pool (CREDITS.txt), one per video.
- **Silent raws:** told with animated step text using site-verbatim how-to (1–2 pumps, upward, twice daily, Gel-Serum).
- **Myth video:** inserts the lab microscopy image as a white card, with a yellow ring drawn on the merged panel and paper-title crops dropping in.
- **Ayşim clip:** avoid the dark gua sha shot (ours is steel).

- 2026-11-11: Polen VO = Higgsfield element "Polen real voice (DropOff sample)" 2cb98bff-9efc-4922-a078-a2f6433c4ef7, cloned from her own recording _calisma/batch-123-polen-dropoff/polen_real_vo_raw.mpeg (user-approved). Old "Polen IG clean" sounded Russian → never use. Before cloning, send the user the source recording to confirm. Myth opening = her silent phone-reading moment (myth_raw 9.7–13.1), not lab b-roll of her standing idle. OneSkin ref (DeP1VsdmHsZ) = single calm shot, white-box name tag top-left, small captions, no flashes.
- 2026-11-11 inserts/cards: thin white border (~9 px), never hugging the frame edge (keep ≥100 px side margin), cards never overlap each other; B/A photos cropped to jaw/neck (no eyes). Big words (MYTH/BEFORE) sit behind the head but high enough that most letters read.
