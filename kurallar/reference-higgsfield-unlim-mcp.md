---
name: reference-higgsfield-unlim-mcp
description: "ALL stills go through the Higgsfield WEB UI with Nano Banana Pro + Unlimited (user, repeatedly, 2026-10-10); never MCP generate_image with credits"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-10T08:54:44.888Z
---

**Rule:** Every still image is made in the Higgsfield web composer (Chrome) with model **Nano Banana Pro**, 2K, **Unlimited**.
- Project: `higgsfield.ai/generate/@residential_walrus_super/sickscience`.
- Never use the MCP `generate_image` / `generate_image_batch` with credits for stills.

The user said this several times and got angry on 2026-10-10: "nano banana 2 pro da unlimited üreteceksin dedik kaç kere".

**Why:** Through the MCP, `models_explore(unlim=true)` reports `unlim.available: false`. Unlimited requests are rejected, so MCP stills always cost credits and use a weaker model (`nano_banana_2_1`). The user's Unlimited allowance only works in the web UI.

**How to apply:**
- Drive the web UI through Claude in Chrome. It accepts one job at a time, so queue the jobs.
- Upload references there, or use the @elements (see CLAUDE.md).
- Download the results into the batch's `stills/` folder.
- Video (Kling) still goes through the MCP with credits.
- **TRAP:** Keep the image count at **1/4**. Raising it to 2 silently switches Unlimited OFF, the button changes to "+N" credits, and a running job cannot be cancelled. This happened on 2026-10-10 and cost 4 credits.
- Before every click on Generate, zoom on the composer bar and check two things: the toggle reads "Unlimited" in green, and the button says UNLIMITED.
- If you need variants, submit the job again at count 1.
- Write every prompt in the sectioned format from `prompts/TEMPLATE-photographic.md`, never as one paragraph.
- The composer adds a `@mention` only when you pick it from the dropdown after typing `@ss-…`.

Related: [[reference-motion-tools]]
- **Results (user, 2026-10-11, angrily):** Never download results through the browser.
  - Get the URLs with MCP `show_generations(type='image', only_completed=false)`; web-UI jobs appear there with `results.rawUrl`.
  - Stream each one straight into Figma: `curl -sL rawUrl | curl -X POST --data-binary @- submitUrl`.
  - Do not fill ~/Downloads or Drive with copies.
- Web UI Unlimited allows **max 4 queued jobs** ("1 unlimited at a time… switch to credits" toast on the 5th).
- Pick @mentions with the keyboard: type the full name, wait 2 s, then Enter (first option) or Down+Enter. Option order is `open-*`, plain, `otg-*`. Clicking a stale ref selects the wrong item.
- Check the chip BEFORE clicking Generate, in a separate step.

**Batch, don't trickle (user, 2026-10-30: "tek tek üretmesene olm sıradan bas geç tek seferde 4 üretim hakkın var").** Before the first submit, list every image the job needs and fill the 4-slot queue straight away, without waiting or doing other work between submits; top up as slots free. One job processes at a time, but the queue takes 4.

**Long prompts (2026-10-30):** a long `computer type` can silently fail to reach the composer, and jobs then go out with only the element chip. Insert with JS `document.execCommand('insertText')`, then confirm the prompt on the first job before filling the queue.

2026-11-02: raising the composer's count above 1/4 silently turns Unlimited OFF and the button becomes credit "Generate +N". Keep 1/4; for variations send the same prompt twice about 45 s apart. Lowering the count does not re-enable it, so check the toggle is green and the button reads UNLIMITED before clicking.
