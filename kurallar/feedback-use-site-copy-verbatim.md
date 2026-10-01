---
name: feedback-use-site-copy-verbatim
description: "SickScience creatives must use the product page's own ingredients/benefits/stats verbatim — never add, drop or write own descriptions"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 43d77aec-642b-4770-8d35-b961af17ba24
  modified: 2026-10-01T16:23:09.629Z
---

For any product fact on a creative (key ingredients, benefits, result percentages, usage), copy the wording from the live product page (`sicksciencelabs.com/products/<handle>` HTML; products.json body lacks these sections). Do not pick extra items from the full INCI list, do not invent per-ingredient descriptions, do not reword stats.

**Why:** user (2026-10-01) caught invented labels (Peptides, Bromelain, "for a firmer, de-puffed look") and said the brand already wrote everything on the site.

**How to apply:** fetch the PDP before writing copy; if the site gives no description for an item, show the name only. Site wording overrides my own softening rules. Related: [[sickscience-client]], [[feedback-no-template-typography]].
