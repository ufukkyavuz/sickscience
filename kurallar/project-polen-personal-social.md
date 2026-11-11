---
name: project-polen-personal-social
description: Polen wants to become active on her personal social with GRWM-style "final touch" reels (from 2026-10-30); her selfie clips are mirrored and may be silent
metadata:
  type: project
---

On 2026-10-30 Polen said she needs to get active on social media and proposed a get-ready "final touch" reel from Beauty Connect in LA.

**Why:** these are her own account's posts, so they look native: no logo, offer or end card.

**How to apply:**
- Project: `~/sickscience-work/video-projects/polen-1030`; `render2.py` is the live cut, music "Luxury Fashion" by JayStacksBeats (Pixabay Content License).
- Her front-camera clips are mirrored: the SickScience label reads backwards until `hflip`.
- Voice-over: the user asked for a female voice on 2026-10-30, so her reels use ElevenLabs Brielle (not a clone of her voice). When a client asks for VO, deliver it; don't ship a silent version.
- GRWM text: small, sentence case, no boxes, on the pale wall above her head (never over jaw, neck or the white shirt). Opener: big purple GET READY WITH ME on the wall BEHIND her (per-frame `tools/lift` mask), words on the VO; user asked for this on 2026-10-30. Key words (SHAPESHIFT, SNATCHED JAWLINE, READY?) stay big behind her too, above her head so no letter is covered (see [[feedback-text-reads-whole-and-holds]]). Hallway opener: white text in front of her.
- Live cut: `render6.py A|B`, two versions (hoodie opener, hallway opener).
- Clips arrive through WhatsApp at 576x1024; ask for originals if sharpness matters.

**2026-11-10 — Polen's voice (approved: "polenin ses harika"):** Higgsfield voice element "Polen IG clean" (voice_id b9e7773c-2932-49dc-9fdf-43943533e037, voice_type element), cloned from her SOLO 0–24 s in the founders IG post (instagram.com/p/Db8U_cwh-b_ — Merve speaks later, never mix them), music removed with demucs (~/motion-tools/.venv/bin/demucs --two-stems=vocals). Generate with text2speech_v2 variant elevenlabs, one take, lively script ("Okay, …!"). The seed_audio clone from the 5 Nov Adobe-cleaned sample was rejected ("canlı bir ses olmalı, bu çok kötü"); never generate 4 preset voices instead of her own.
