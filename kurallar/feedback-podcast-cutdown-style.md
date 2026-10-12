---
name: feedback-podcast-cutdown-style
description: "Podcast/talking cut-downs — cut only at sentence ends, dynamic big word captions, punchy intro; never mid-thought jump cuts"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-09T23:44:55.845Z
---

User feedback on the Gloss Angeles cut-downs (2026-10-10): "Saçma yerlerde jump cut yapmışsın bide altyazı kısmı daha dinamik ve dikkat çekici olabilir giriş sahneleri de aynı şekilde."

**Why:** Cuts in the middle of a thought looked careless. Small caption pills and a calm opening did not stop the scroll.

**How to apply** (implemented in _calisma/batch-32-gloss-angeles/render32.py):
- **Cuts:** Cut only at sentence ends, snapped to the word gap from the whisper timestamps. Use few, longer chunks. Punch-in on a cut only when the camera stays the same.
- **Captions:** 1–3 word groups, centred, uppercase Founders Bold ~76 px. Each group springs in from 0.8× scale. Exactly one active word sits on a brand-purple (#A921C0) block.
- **Intro:** A fast push from 1.25× plus a short white flash and an impact SFX. The headline slams in word by word (1.8× → 1×).
- **Multi-camera 16:9 → 9:16:** Pick the crop per frame by camera, so the speaker stays centred. On podcast footage the headline goes at chest height, not over the faces.

Related: [[feedback-video-max-20s]] [[reference-motion-tools]]

**Later feedback (2026-10-10):**
- The hook must show for ~2–3 s and then leave. A headline that stays on screen means nothing.
- Vary the HOOK style per video (purple blocks / stacked big words / tilted typed sticker / slam). Keep the layout full-bleed and the captions centred, with the active word on a purple block; the user liked that layout and asked to keep it. Vary the endings too.
- When speech says "before and afters", show the brand's SITE before/afters (ShapeShift PDP + sculpted-bundle hi-res, in src/site-ba). They are the clearest. Show each one whole, on a pop-in card over the dimmed footage, labels included. Never use another campaign's B/A.
- Cut the brand's own footage (`~/motion-tools/footage-v3`) in as b-roll that matches the words. Those films end with built-in logo reveals, which work as end cards.
- (2026-10-10) No dark shade bands behind hook or step text. The user called them "saçma"; the text's black stroke is enough.
- Never show a person on screen in silence. If they appear, they speak (a new Kling talking clip), or the shot is replaced with b-roll. The user complained: "Right on your scalp kısmında ses yok".
- Short videos must tell the full story (problem → answer → how to use from the PDP → PDP proof stat → logo, ~15–17 s). A bare 8–9 s hook-and-reveal is too thin.
