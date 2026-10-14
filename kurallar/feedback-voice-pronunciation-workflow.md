---
name: feedback-voice-pronunciation-workflow
description: "Spoken lines with brand or science terms — voice in ElevenLabs, lip-sync with Wan 2.7 audio reference; never retry Kling's own voice"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-13T10:46:00.569Z
---

On 2026-10-13, Kling 3.0's native voice mispronounced "exosomes" in two paid takes, and the user's two manual tries failed too. The user was angry: "boşuna ne düşürüyon kredileri".

**Rule:**
- Any spoken line that contains a term Kling may mangle is voiced in ElevenLabs. Terms include exosomes, NX35, ShapeShift and ingredient names.
- Voice options: the eleven_v3 voice "Founder lisa" `iOI1VnXusP7XCIaXVIgU` was used for Merve. ElevenLabs costs are tiny and come from the user's own quota.
- Lip-sync step:
  1. Upload the voice file to Higgsfield (media_upload).
  2. Animate the scene still with **Wan 2.7** (`wan2_7`, 1080p, 5 s, 12.5 credits). Pass the still as `start_image` and the voice file as `audio_references`.
- The user approved the result: "nice düzgün çıktı".
- Seedance 2.0 at full quality costs 45 credits; avoid it.

**Why:** Kling reads hard words its own way, and a phonetic spelling in the prompt did not fix it. Each retry burns credits.

**How to apply:**
- Check pronunciation BLIND: two whisper sizes, no initial_prompt. A hint biases the check (see observation 0035).
- Never pay for a Kling retry hoping the pronunciation changes.
- Give each character one fixed ElevenLabs voice so they sound the same across episodes.

Related: [[feedback-video-max-20s]], [[reference-higgsfield-unlim-mcp]]
