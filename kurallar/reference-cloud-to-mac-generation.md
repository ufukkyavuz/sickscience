---
name: reference-cloud-to-mac-generation
description: "Cloud session cannot touch the Mac/Chrome; Higgsfield Unlimited stills are produced by a Mac session (Remote Control) that the cloud session briefs via send_message. Tested OK 2026-10-12 (E1)."
metadata:
  type: reference
  modified: 2026-10-12
---

**Rule:** A claude.ai cloud session (claude.ai/code container) has NO access to the user's Mac, Chrome or computer use. There is no "+ → Devices" option for it. Never ask the user for that again.

The user got angry on 2026-10-12 after a morning lost to these dead ends:
- MCP credits (8 credits wasted)
- headless Chromium login: password and cookie handling are blocked by the auto-mode classifier
- asking the user to add permission rules

**What works (tested 2026-10-12, E1 = Head-to-Toe tape measure):**
1. The user opens a session on the Mac: Claude Desktop → Code, or `claude remote-control` in the SickScience Drive folder.
2. The cloud session finds it with `mcp__claude-code-remote__list_sessions(mine:true)`. Look for `environment_kind: "bridge"`, connection `connected`.
3. Send the brief with `mcp__claude-code-remote__send_message(session_id=…)`. Make it self-contained:
   - the prompt file path on branch `claude/agency-rules-and-knowledge-b2oyie`, read with `git show origin/<branch>:<path>`, no branch switch in Drive
   - Nano Banana Pro, 9:16, 2K, Unlimited ON
   - pick the @element from the dropdown
   - the checks to make
   - "do not spend credits"
4. The Mac session drives Chrome, generates with Unlimited and can also lay the result out in Figma itself.
5. The Mac session could NOT reply: the cloud session id was not addressable from its message tools. Read its progress instead with `list_events(session_id, kinds:[assistant,result])`, and check Figma with `get_screenshot`.

**User clarifications given to the Mac session (2026-10-12):**
- The black stripe on capsules is NOT required. White, legible text is enough.
- The tape/strap crossing the chrome looks odd because it is a real mirror reflection. That is natural, not a defect.
- Results stay in Higgsfield. No need to save copies to Drive.

Related: [[reference-higgsfield-unlim-mcp]]
