---
name: reference-claude-setup-kit
description: "Drive/_claude-setup holds memories, skills, global CLAUDE.md, fonts and sync.sh so the user's laptop Claude has the same setup; run push after memory changes"
metadata:
  node_type: memory
  type: reference
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-09T13:30:09.258Z
---

The user works from a Mac mini and a laptop (set up 2026-10-09). `Google Drive/Drive'ım/_claude-setup/sync.sh push|pull` copies Claude memories for SickScience, INO Claude Ads, INO v2, Casadora and Dejavous, plus user skills and agents, the task-observer workspace, global CLAUDE.md (paths rewritten to `__HOME__`), Founders Grotesk/Anton fonts, and a Python venv (`~/.claude-ss-venv`). Secrets in `~/.claude/settings.json` are deliberately excluded.

**How to apply:** after saving new memories or skills, run `bash "<Drive>/_claude-setup/sync.sh" push` so the other machine can pull them. On a machine where `~/OpenMontage/.venv` doesn't exist, use `~/.claude-ss-venv/bin/python` for render scripts. Related: [[sickscience-client]].

- **GitHub push (user, 2026-10-12: "her şeyi pushla, başka bilgisayardan görmem lazım"):** `~/claude-setup` is the private repo `ufukkyavuz/claude-setup`. Steps:
  1. Run `sync.sh push`.
  2. `rsync` the Drive kit into `~/claude-setup`, excluding `fonts`.
  3. Copy the project's text files (CLAUDE.md, AGENTS.md, brand book, recommendations, `prompts/*.md`, `tools/*`, `_calisma/**/*.py`) into `projects/SickScience/`.
  4. Commit and push.
  - The raw transcript (~650 MB) is never pushed. Write a readable summary instead: `sessions/SickScience-YYYY-MM.md`.
