---
name: reference-trend-audio-workflow
description: "How to put a reference reel's trending song into our edit — user supplies the licensed mp3; match the exact section by envelope cross-correlation"
metadata:
  node_type: memory
  type: reference
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-17T11:27:04.232Z
---

When a reference reel uses a trending song and the user wants "aynı ses" (2026-10-17, batch-53, STORM II):
- The user supplies the track (they said the licence is cleared). They suggested mp3juice.sc (YouTube ripper); I don't download from rip sites myself — ask the user to drop the mp3 in Downloads.
- Find the exact section the reference uses: record the reel's audio in Chrome (click page first for a user gesture, `video.captureStream()` + MediaRecorder), compute a 50 Hz RMS envelope in the page, pull it out in ≤190-value chunks (JS output truncates ~1000 chars), then cross-correlate log-envelope + onset with the song locally (librosa in ~/motion-tools/.venv). STORM II → reference starts at 0:21.90.
- Copy the reference's cut times by frame-differencing the reel in a canvas (15 fps sampling), and render each shot with exact frame counts (`-frames:v`) so cuts never drift.
- Verify by correlating the final mux against the reference envelope (peak should be at 0 ms).

Related: [[feedback-video-max-20s]], [[reference-dropbox-ugc]]
