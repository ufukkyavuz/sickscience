---
name: reference-atria-ad-library
description: "Atria ad library via MCP (search_library_ads) gives recent competitor ads with preview images; faster than Meta Ad Library scraping"
metadata:
  type: reference
---
2026-10-30: the Atria MCP (`mcp__28d35031…__search_library_ads`) works for competitor research.
- Filter with `query` (brand), `launched_after`, `theme` (discount, holiday_festival, seasonal), `media_format: image`, `collapse_variants: true`.
- `preview_image_url` is a public cdn.tryatria.com jpeg (600 px). `query` also returns unrelated advertisers, so check `advertiser_name`.
- Offer adaptations need current prices first: `/products.json` plus home page "Save $" lines ([[sickscience-site-copy-snippets]]). Never copy a deadline, "lowest price" or a gift we can't confirm.
- Figma: gradient text fills render flat in screenshots; an IMAGE fill on TEXT gives real chrome and keeps the text editable. Notes: `prompts/batch-80-competitor-offers.md`.

Related: [[feedback-reference-concept-and-colour]] [[feedback-show-references-next-to-designs]]
