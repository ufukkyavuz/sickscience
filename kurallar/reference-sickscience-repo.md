---
name: reference-sickscience-repo
description: Project repo is github.com/ufukkyavuz/sickscience (branch claude/agency-rules-and-knowledge); the Drive SickScience folder itself is its working copy
metadata:
  type: reference
---
Since 2026-10-12, `Drive'ım/SickScience` is a git working copy of `https://github.com/ufukkyavuz/sickscience`.
- Default branch: `claude/agency-rules-and-knowledge` (there is no main).
- `.gitignore` is a whitelist: only md, py, js, html and txt files; images, videos and PDFs stay on Drive.

**How to push:**
1. `rsync -a --delete <memory dir>/ kurallar/`
2. Update `sessions/SickScience-YYYY-MM.md`.
3. `git add -A && git commit && git push`.
4. Run `Drive'ım/_claude-setup/sync.sh push` as well; that is the kit for the global setup.

`~/claude-setup` (`ufukkyavuz/claude-setup`) is the separate global-setup repo, not the project repo.

Related: [[reference-claude-setup-kit]] [[feedback-delivery-folders]]
