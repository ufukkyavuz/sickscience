---
name: reference-motion-tools
description: "~/motion-tools: mgaudio (code-synthesized music + SFX at -14 LUFS), saas-motion-kit transition atlas / breakdown.py, Opus 5.5 video prompt library; venv ~/motion-tools/.venv"
metadata:
  node_type: memory
  type: reference
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-09T14:29:21.332Z
---

The user asked for these to be installed (2026-10-09). Use them in video work.

- `~/motion-tools/mg-styles-15/lib/audio/mgaudio`: synthesized music beds and SFX, deterministic, exports at -14 LUFS / -1.2 dBTP.
  - Recipes: lofi, ambient (flavor='product'), pop, future_bass, explainer, ...
  - SFX: whoosh / pop / impact / ui / sparkle / text_hit.
  - Usage: `~/motion-tools/.venv/bin/python` with `sys.path.insert(0, '~/motion-tools/mg-styles-15/lib/audio')`, then `recipes.lofi(duration=, drop=, outro=)`, `m.sfx(sfx.whoosh(...), at=t)`, `m.export(path)`.
  - The VCSL CC0 samples were rebuilt locally with tools/build_samples.py, because the repo ships only a partial set.
  - `rubric.md` is a harsh "jury" review prompt for a critique pass.
- `~/motion-tools/saas-motion-kit`: creative/transition-atlas.md (24 transitions), variety-rules.md, tone-matrix.md, and `tools/breakdown.py` (splits a reference video into shots, rhythm and a contact sheet; credit references, borrow grammar only).
- `~/motion-tools/awesome-opus5-5-videos`: 513 prompts (prompts/, data/videos.json).
- **Not installed** (blocked by the auto-mode classifier as untrusted code):
  - `npm install` in mg-styles-15 (puppeteer renderer);
  - symlinking the saas-motion-video skill into ~/.claude/skills;
  - `npx skills add heygen-com/hyperframes`.

  The user must approve these explicitly. Our PIL seek(t) pipeline doesn't need them.

Related: [[reference-claude-setup-kit]]

**Transcription:** `mlx-whisper` is installed in `~/motion-tools/.venv` (2026-10-09). Use it for word timestamps (model `mlx-community/whisper-large-v3-turbo`); session scratchpad venvs get wiped between sessions.

**2026-10-21:** `~/motion-tools/ext-x-2026-10-21/` holds 7 reference repos of Opus code-rendered video work (prompts, mg-styles-15 sources, p5.brush character kit). Its README summarises them along with the "motion studio" article: brief, style guide, shot list as states, seekable frames, contact-sheet critic fixing the top 3 defects, gates. The lemo-opuscar plugin is not installed; the user installs it via /plugin.
