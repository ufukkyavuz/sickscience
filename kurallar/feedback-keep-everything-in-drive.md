---
name: feedback-keep-everything-in-drive
description: All SickScience project files (sources, assets, plates, render engines) live in the Drive folder, never only on the local disk
metadata:
  type: feedback
---
User 2026-11-08: "ben sana bilgisayara bir şey kaydetme Drive dosyasında tut. Her şeyi demedim mi?" (after I pointed them to ~/sickscience-work/brandfilm/v4/plate/spread_expanded.png).

**Why:** the user edits files themselves and works from Drive on several machines; local-only files are invisible and get lost.

**How to apply:** keep project files under the Drive SickScience folder (_calisma/...). The founders film engine now lives at `_calisma/video-brand-story-drawn/engine/` (old path ~/sickscience-work/brandfilm is a symlink to it). Only throwaway temp frames may go to /tmp. Give the user Drive paths/links, never ~/ paths. This narrows [[feedback-render-memory]] (temp off Drive): temp yes, project files no.
