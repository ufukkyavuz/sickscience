---
name: reference-higgsfield-composer-refs
description: "Higgsfield composer working flow 2026-11-03: image refs by file_upload, mention first, prompt loading, one-job limit, focus traps"
metadata:
  type: reference
---

- Two contenteditables exist; the first is a hidden Cinema Studio one. Use the one with width > 100.
- Upload references with `file_upload` to the composer `image/*` file input. The chip stays after submit; hover it, then click the X at its top right. Screen coordinates shift between 719 and 753 viewport height, so a wrong click opens an asset preview.
- Type mentions FIRST on an empty prompt, then insert the text. A mention typed after long text can make Return submit the job with only that one element.
- After any JS wait, focus is lost: click the field before cmd+a, or cmd+a selects the page.
- Scrolling collapses the composer to a one-line bar; set scrollTop 0 and click the bar.
- Unlimited processes one job at a time but holds a short queue: 2 to 3 sends in a row are fine (user, 2026-11-03: don't trickle one by one). A fifth in the queue was dropped with a "1 unlimited generation at a time" toast. Unlimited may switch itself off: check `[role=switch][aria-label="Unlimited mode"]` before sending, the button then reads GENERATE with a credit number.
- Large prompts: a hidden file input + `file_upload` of a JSON loads them into the page; `fetch` to localhost is blocked.
- Cancel opens a Close/Confirm dialog; click Confirm or the job stays. Chips need a 1 s hover or some are skipped: check the chip row before every send.
- 2026-11-07: raising the image count above 1/4 with "+" switches Unlimited OFF without a toast. The button then shows a credit number (2/4 → "GENERATE 4"), and one send cost 4 credits. Keep the count at 1/4 and re-read the switch after every settings click, immediately before sending.

**2026-11-10:**
- **Blank project page:** `higgsfield.ai/generate/@residential_walrus_super/sickscience` sometimes renders blank. Use `higgsfield.ai/ai/image?model=nano-banana-pro` instead. It has the same composer, the same mentions and an Unlimited switch.
- **Reference images on that page:** click the References button, then `file_upload` to the file input. Select the uploaded thumbnail, then press Escape.
- **Products drawn too big:** Nano Banana draws set products large. Two prompt lines get them small:
  - "WIDE studio shot taken from far away … tops at 50% / bases at 72% of the frame height".
  - "LABELS ARE CRITICAL: SickScience once on the cap, name once on the silver half".
- **Opening clips with exact first and last frames:** use MCP `generate_video` with `seedance_2_5`, `start_image` + `end_image`. 5 s at 1080p costs 80 credits. The user asked for Seedance on 2026-11-10.
