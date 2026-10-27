# Batch 44 — "Caught at the window" (2026-10-14)
Client asked for a video like IG reel https://www.instagram.com/reels/Debdz5uqays/ (Beypazarı "yakaladım" trend, Google Flow).
Reference beat (7–20 s of the reel): night apartment block → one continuous push-in to one lit window → two friends with the product → one notices the camera, walks to the window, closes the curtains → logo over the closed curtain, a face peeks through the gap.

## Our brief (user, 2026-10-14)
- Two women (late 20s, beautiful, model-like), NOT irritated — playful "caught you" instead.
- One uses **ShapeShift** (upward strokes on jaw/neck), the other **PowerCycle** (dropper on scalp parting).
- First they close the curtains, THEN both peek through the gap and show their products to the camera.
- ≤20 s. Photoreal live-action look. Product text white, true scale (SS 12×3.5 cm, PC 14×4.5 cm).

## Shots (stills = Higgsfield Unlimited; video = Google Flow Veo 3.1 Fast, first/last frame)
| # | ~s | Still(s) | Action |
|---|---|---|---|
| 1 | 0–7 | W1 wide night facade (first) → W2 window close (last) | one continuous physical push-in toward the single warm window |
| 2 | 7–12 | W2 | woman with ShapeShift notices the lens, raises an eyebrow, knowing smile, nudges her friend; both get up, walk to the window and pull the curtains closed |
| 3 | 12–17 | W3 closed curtains (first) → W4 both faces peeking through the gap with products (last) | the curtains part a little, two smiling faces peek out, each lifts her product beside her face |
| 4 | 17–19 | W3 still + official logo + SickScienceLabs.com (no plate) | end card |

## Production (2026-10-14) — delivered
- Stills (Higgsfield Unlimited): W1 `48880c40`, W2 `bd03b1bd`, W3 closed-curtain edit `e36ebac9`, W4 peek `dce90cf0` (products 2x too large + stubby → rejected) → guide composite of real PNGs at true scale (face ≈19 cm) + "integrate" edit `a946d998` → label stripe re-laid from the element PNGs at the measured stripe angle (`w4_peek_v3.png`).
- Clips: A push-in W1→W2 (Flow Veo 3.1 Fast, first/last), B notice + close curtains (Flow Veo, first = W2), C peek (Higgsfield Kling 3.0, 14 cr; first = B's real last frame, last = W4 v3) — Flow quota ran out before C.
- Edit `_calisma/batch-44-window/render44.py`: A ×1.7, B ×1.25, C ×1.0, seamless cuts (each clip starts on the previous last frame); logo + SickScienceLabs.com (Founders Medium) over the last 2.4 s at y≈282 on the curtain; lo-fi bed −14 LUFS. 19.1 s.
- Delivered: `Video/2026-10 Ekim/03 Animasyon/ShapeShift + PowerCycle – Perde – 9x16.mp4`.
- Known: ShapeShift capsule in the final hold measures ~2.8:1 (real 3.4:1) — slightly wide.

## v2 — single ShapeShift, exactly like the reference (user, 2026-10-14: "Video çok kötü olmuş referanstaki gibi yapman lazım… yakalanmış gibi gözükmüyolar… direkt referanstaki gibi tekli shapeshift için yap")
Reference beats (Beypazarı, 7–24 s of the reel): one continuous drone shot down the night facade into the single lit window → straight-on, eye-level, tight window shot with the product clearly on the table → one person notices the camera, STARES INTO THE LENS (caught), stands, walks up to the glass so he fills the frame, yanks both curtains shut in one move; camera locked-off → closed curtains, silhouette at the edge, logo.
Why v1 failed: wide distant framing, two women laughing/waving — no "caught" moment, nobody looked into the lens; peek beat felt random.
v2: one woman (late 20s), ShapeShift capsule on the side table, applying gel-serum to the jawline → freezes, looks straight into the lens, slow eyebrow raise + tiny knowing smile (not angry) → stands, walks to the glass, pulls the curtains shut → closed glowing curtains + logo.
- S1 = w1_facade (reuse) · S2 = straight-on window still (Higgsfield Unlimited) · A = facade→S2 push-in (Kling 3.0 first/last, 14 cr) · B = caught + close curtains (Veo 3.1 Fast on Higgsfield, 32 cr; Flow quota exhausted).
### v2 production (2026-10-14) — delivered `Video/2026-10 Ekim/03 Animasyon/ShapeShift – Perde – 9x16.mp4` (13.4 s); v1 moved to `_calisma/batch-44-window/out/v1_rejected_…`
- S2 window: first try with the element = capsule forearm-sized + angled window (rejected) → product-free straight-on scene `c0267538` → real PNG placed at true scale (face ≈19 cm → 9.4 px/cm, capsule 115 px) → integrate edit `36af98be` → label stripe re-laid (`v2_s2_final.png`).
- A push-in: Kling 3.0 first/last (w1_facade → S2), 5 s. B caught: Veo 3.1 Fast on Higgsfield (start = S2), 8 s; eye contact ~2.5 s but brief → 2.3–3.1 s slowed ×0.5; Veo re-opened the curtains after ~6.7 s → cut at the most-closed moment, 6.25–6.75 s at ×0.25 under the card (she holds the curtains, peeking — same as the reference ending).
- Edit `render44v2.py`; credits: Kling 9 + Veo 32 (+ v1 Kling 14).

## v3 — realism pass (2026-10-14; user: "hissiyatlar gerçekçi değil") — delivered, v2 moved to `_calisma/batch-44-window/out/v2_rejected_…`
- Diagnosis: staged "knowing smile", speed ramps, showroom flat + silk pyjamas + locked symmetric camera read as an advert.
- Still: voyeur telephoto from the building across the street (`7c48fe93`; blurred own window frame in the foreground, T-shirt + claw clip, laptop, lived-in flat) → cropped 860 px around the window → real PNG at true scale (face ≈19 cm → 5.8 px/cm before crop) → one edit added curtains + integrated the capsule (`53d97bf3`, back to 2K) → label stripe re-laid (`v3_scene_final.png`).
- Video: Veo 3.1 Fast on Higgsfield (Flow quota empty, user approved), 3 takes × 32 cr; take 1 rejected (sudden zoom/cut at 5 s), take 2 chosen (startle → hand-over-mouth laugh → curtains → capsule up in the gap). Whisper "What the fuck?" on the full clip was a hallucination over quiet audio (three models on the 2.8–5.4 s window: nothing); final mix clean.
- Edit `render44v3.py`: 0–7.1 s at real speed, logo + URL on the right curtain panel (the gap runs the full height), last 1.6 s. 7.1 s.
