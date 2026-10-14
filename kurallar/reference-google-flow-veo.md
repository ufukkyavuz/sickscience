---
name: reference-google-flow-veo
description: How to make Veo 3.1 talking clips in Google Flow (user's Flow credits) and get them into the edit — upload, agent chat, approve, download
metadata:
  type: reference
---

On 2026-10-13 the user said to use their Google Flow credits for Veo videos instead of Higgsfield credits.
- Flow project: `flow.google.com/project/9d3b1d8b-d9b1-4f4b-8f43-8677fb4f0f44`.
- Account tier: Veo 3.1 Fast only, fixed at 8 s, 20 Flow credits per clip.

**Upload:**
- There is no file input.
- In page JS, `fetch` the still from its public Higgsfield cloudfront rawUrl, wrap it in a `File`, and dispatch `dragenter/dragover/drop` with a `DataTransfer` on the canvas.
- Give each file a clear name.

**Generate:**
- Type into the right-side agent chat (find "Ne oluşturmak istiyorsunuz?").
- Name the uploaded file and write: "Veo 3.1 Fast, 9:16, 8 s, exact first frame…", then the spoken line in quotes.
- Send with the "Oluşturmaya başla" button; Enter only adds a newline.
- The agent asks "20 kredi… başlatmamı ister misiniz?". Click the LAST `[role=radio]` "Onayla", not "Her zaman onayla".
- Under heavy load a job can fail ("Başarısız"); just resubmit.

**Download:**
- The user gave permanent OK on 2026-10-13: "var izinlerin zaten".
- Open the video, click "Medyayı indir", choose 720p "Orijinal boyut".
- Then MOVE the file from ~/Downloads into `_calisma/.../clips/`. Never leave copies in Downloads.
- A direct fetch of flow-content.google is blocked by CORS.

**Quality:** Veo native voices pronounce "exosomes", "NX35" and "gel-serum" correctly, verified with blind whisper. Cut off trailing ad-libs such as "Hmm" or a repeated word.

Related: [[feedback-voice-pronunciation-workflow]], [[reference-higgsfield-unlim-mcp]]
