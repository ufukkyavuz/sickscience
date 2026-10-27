---
name: feedback-video-model-choice
description: "Realistic video: default to Veo 3.1 in Google Flow; if Flow has no credits, ASK before switching to Higgsfield; never generate when the user only asked a question"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-14T12:36:33.097Z
---

The user set these rules on 2026-10-14, after the window-curtain ad v1 and v2 felt unrealistic.

**Model choice:**
- Default model is **Veo 3.1**, run in **Google Flow**: 20 Flow credits per 8 s, paid from the user's Google plan.
- If the Flow quota is exhausted ("Kullanım sınırınıza ulaştınız"), **ask the user first**. Only then continue on Higgsfield (Veo 3.1 Fast costs 32 credits there).
- User quote: "flowda kredi yoksa bana sorup higgs ile devam edebilirsin o zaman şimdilik veo 3.1 kullan".

**Reference prices (Higgsfield, 8 s, 9:16, checked 2026-10-14):**

| Model | Credits |
|---|---|
| Kling 3.0 | 14 |
| Veo 3.1 Fast | 32 |
| Veo 3.1 Lite | 12 |
| Wan 3.0 | 14 |
| FLUX 3 Video | 44 |
| Seedance 2.5 | 56 (720p) / 128 (1080p) / 24 (480p draft, finalize cost unknown) |

**Questions are not go-aheads:**
- When the user asks a question (which model, what does it cost, how does it work), answer it in text. Do not start production.
- Even a `get_cost` preflight looked like generating to the user and made them angry ("ben sana soru soruyorum adam gibi önce cevap ver ne üretime geçiyon"). Say in words what you are checking. Never propose 480p or a draft as a deliverable; the work is about quality.

**Why:** AI acting realism mattered more than credit savings. The user also wants control over where credits go.

**How to apply:**
- For every new video, use Flow + Veo 3.1 unless it is out of credits.
- Generate 2–3 takes of one well-written prompt rather than fixing a single take in the edit.
- No speed ramps that make AI footage look edited.

Related: [[reference-google-flow-veo]], [[reference-higgsfield-unlim-mcp]], [[feedback-video-max-20s]]
