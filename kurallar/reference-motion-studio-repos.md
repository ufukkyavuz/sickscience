---
name: reference-motion-studio-repos
description: 2026-11-09 installed the Dumble "2.5D motion studio" repos — Blender MCP, earshot MCP, claymation/painted/kinetic/remotion skills; where they live
metadata:
  type: reference
---

Source: the X article by Dumble, "How to build a 2.5D motion studio with Opus 5.5" (2026-10-27). The format is flat 2D cut-out characters on planes inside lit 3D Blender sets, with the hero prop always in 3D.

The repos are cloned in `~/motion-tools/repos/`. Skills are symlinked into `~/.claude/skills`.
- **MCP `blender`:** run with `uvx mcp-for-blender`, user scope. The addon `blender_mcp` is enabled in Blender 5.2. Blender must be open for it to work: N panel → "MCP for Blender" → Start.
- **MCP `earshot`:** installed as `~/.local/bin/earshot mcp` (uv tool). It lets the agent listen to audio and pick SFX. Its CLAP/AST models are cached in `~/.cache/earshot`.
- **Skills:**
  - blender-claymation
  - painted-animation, kinetic-reel
  - remotion-*, 13 skills
  - earshot, real-sound
  - gsap-frameworks, gsap-react, gsap-scrolltrigger, gsap-utils
- **Projects:**
  - ClaudeAnimationBase (p5.brush): npm install done.
  - awesome-claude-video-skills: a list, nothing to install.
- **Whisper:** use `mlx_whisper` in `~/motion-tools/.venv`. openai-whisper is not installed.

Related: [[reference-motion-tools]], [[feedback-video-studio-gates]].
