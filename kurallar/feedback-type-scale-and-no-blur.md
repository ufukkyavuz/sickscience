---
name: feedback-type-scale-and-no-blur
description: "SickScience ads: fixed type scale (min 32px, same across formats) and format variants only by cropping — never blurred/padded edges"
metadata:
  type: feedback
---

Text sizes: headline 120–170, H2 56–64, body 40, labels/chips/CTA 32 minimum; identical across Story/Feed/Square (all 1080 wide). Format variants come only from cropping or zooming the generated image; never pad, mirror, feather or blur edges — regenerate in the needed aspect ratio instead.

**Why:** user (2026-10-03) said the blurred edges looked bad ("bir daha yapma") and that text sizes had serious problems (14–26 px labels next to 150 px headlines).

**How to apply:** run a font-size audit script before showing work; plan layouts so product + text fit the crop; full rule set in project CLAUDE.md "Tipografi ölçeği". Related: [[feedback-photographic-prompt-format]], [[feedback-no-footnotes]].
