---
name: reference-atria-ad-library
description: Atria ad library via MCP (search_library_ads) gives recent competitor ads with preview images; faster than Meta Ad Library scraping
metadata:
  node_type: memory
  type: reference
  originSessionId: 41fbfb05-23a6-4296-b459-f7903be566f9
  modified: 2026-11-16T07:36:01.539Z
---

2026-10-30: the Atria MCP (`mcp__28d35031…__search_library_ads`) works for competitor research.
- Filter with `query` (brand), `launched_after`, `theme` (discount, holiday_festival, seasonal), `media_format: image`, `collapse_variants: true`.
- `preview_image_url` is a public cdn.tryatria.com jpeg (600 px). `query` also returns unrelated advertisers, so check `advertiser_name`.
- Offer adaptations need current prices first: `/products.json` plus home page "Save $" lines ([[sickscience-site-copy-snippets]]). Never copy a deadline, "lowest price" or a gift we can't confirm.
- Figma: gradient text fills render flat in screenshots; an IMAGE fill on TEXT gives real chrome and keeps the text editable. Notes: `prompts/batch-80-competitor-offers.md`.
- 2026-11-13 API notes: `search_library_ads` has NO `limit` (use `page_size` ≤20); `industry`/`theme`/`media_format` are arrays; `search_advertisers` takes `keyword` (not `query`). Free-text award queries return noise (wigs, spas); reliable route = `search_advertisers` keyword → `scope: advertiser` + `advertiser_id` + `query`. Awards-series findings (Medicube laurel/"Nº1", StriVectin plain packshots): `prompts/batch-131-awards-series.md`.

Related: [[feedback-reference-concept-and-colour]] [[feedback-show-references-next-to-designs]]
