---
name: reference-voiced-ugc-pipeline
description: "Silent UGC → voiced fast cuts: ElevenLabs Brielle VO + render2.py (gap tightening, word captions, slam hooks, push-ins, ducked bed)"
metadata:
  type: reference
---
2026-10-20, ShapeShift "lilac" UGC (user: "seslendirme yapalım… daha hızlı akıcı… 4-5 varyant, büyük hooklu").
- VO: ElevenLabs MCP `creative_generate_speech`, eleven_v3, voice **Brielle** `6u6JbqKdaQy89ENzLSju` (natural Gen-Z). generations_count=1. About 2 ¢ per line. Download from `creative_get_flow_run_status` → `content_url`.
- Pipeline: `~/sickscience-work/video-projects/lilac-1020/render2.py`.
  - Whisper word timestamps; gaps >0.35 s tightened to 0.2 s.
  - Shots start on word onsets, 0.6–1.2 s rhythm, push-in each shot, a 1.22× ease-in plus white flash on shot 1.
  - Hook slams word by word. Hook styles: blocks / slam / sticker.
  - Captions: 1–3 word groups, uppercase Founders Bold 86, active word on a purple block, spring-in, width capped at 980 px.
  - End card is overlaid on the product-in-hand shot.
  - Audio: mgaudio pop bed at -30 LUFS, sidechain-ducked under VO, ending at -16 LUFS.
- Pitfalls:
  - Whisper splits "V-Line" and "92%", so merge the fragment tokens.
  - The clip-library start times must skip the frames where the product is still entering the frame.

Related: [[feedback-voice-pronunciation-workflow]] [[feedback-podcast-cutdown-style]] [[feedback-video-max-20s]]
