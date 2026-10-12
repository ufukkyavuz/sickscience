---
name: feedback-render-memory
description: "Video renders must stream frames (never cache whole clips or all output frames), run as background jobs, at most 2 at once on the 16 GB Mac mini, temp output off Drive"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-09T14:58:14.531Z
---

Rendering 4 variants in parallel with whole-clip frame caches (each 1080×1920 clip ≈1.2 GB of RGB, plus every output frame held until the end ≈4 GB) needed ~50 GB. The 16 GB Mac swapped, froze, and the Claude session died twice.

**Why:** User 2026-10-09: "kitleniyo bu konuşmada video yapmaya çalışınca neden olabilir?"

**How to apply:**
- Stream: read clip frames from an ffmpeg pipe on demand (Reader in _calisma/batch-28-video/render29.py), and write output frames straight to the encoder, keeping only a 3-frame buffer for transitions.
- Run renders with `run_in_background`, at most 2 processes at once.
- Write intermediates to a temp dir, then copy the final file to Drive.
- Check peak memory with `/usr/bin/time -l` on the first run of a new renderer.

Related: [[reference-motion-tools]]
