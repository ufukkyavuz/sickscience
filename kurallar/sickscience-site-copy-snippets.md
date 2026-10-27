---
name: sickscience-site-copy-snippets
description: "Verbatim site copy pulled 2026-10-27 (About/R&D, NX35 science page, DropOff & NetWork Key Benefits) + how to fetch the site when curl is rate-limited"
metadata:
  node_type: memory
  type: reference
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-27T18:55:34.380Z
---

Pulled 2026-10-27 from sicksciencelabs.com. Use verbatim (see [[feedback-use-site-copy-verbatim]]).

**Fetching**
- `curl` returns `local_rate_limited`. Use the built-in browser and run JS on a site page instead:
  - `fetch('/products.json?limit=50')` for handles;
  - `fetch('/products/<handle>')` + DOMParser for page text.
- Old handles such as `dropoff-body-sculpting-serum` 404 now.
- Current handles: `shapeshift`, `network`, `powercycle`, `dropoff`, `dropoff-1`, `value-bundle` (Vault), `award-winning-duo`, `head-to-toe-duo`, `sculpted-bundle`, `glp-1-facial-recovery-system`, `*-on-the-go`, `stainless-steel-gua-sha`, `tote-bag`, `sickscience-makeup-bag`, `sickscience-gift-card`.
- About page = `/pages/sickscience-labs`. NX35 page = `/pages/science`.

**About / R&D page (/pages/sickscience-labs)**
- "The New Era of Biotech" · "From Cancer to Skincare" · "Two Friends Hacking Biotech".
- "We are a biotech research company developing various regenerative therapies including cancer treatments, hair growth, skin health, and overall wellness."
- Founder names as written on the site:
  - Polen Koçak-Denizci, PhD: Co-Founder, Genetics and Bioengineering; PhD Biotechnology, Yeditepe; Research Scholar, Health Sciences & Technology, Harvard MIT.
  - Merve Yildirim-Canpolat, PhD: Co-Founder; PhD Biotechnology, Yeditepe.
- "…this dynamic duo delved into research on stem cell production, regenerative medicine, and the application of exosomes in cancer treatment."
- Quote: "With the convergence of bioinformatics, nanotechnology, and computational biology, we can tap into precise cellular behavior and engineer molecular coding techniques to deliver extraordinary results."
- Prices shown 2026-10-27: SS $64 (4.7★, 580 reviews) · NW $74 (4.8★, 40) · PC $64 (4.5★, 127) · DO $52 (4.6★, 68) · Gua sha $24 · Sculpted Duo $79 (was $88) · Body Transformation Duo $98 (was $116).

**NX35 page (/pages/science)**
- "Exosomes are carriers that deliver specific coded messages to cells at a molecular level."
- "Exosomes are incredibly minuscule, allowing them to easily navigate and deliver signals where it's needed most." / "1/1000th the size of a cell".
- "Our NX35 technology is a marvel of biomimetics — the science of mimicking natural functions in our bodies."
- "Our NX35™ technology targets specific cells and delivers 'coded' messages." / "100% plant-derived and vegan."

**DropOff Key Benefits**
- "Expertly formulated with plant exosome technology to support smoother, firmer-looking skin and visibly enhance body contour and definition — while helping improve the appearance of cellulite and stretch marks."
- Tags: Sculpts & Defines · Cellulite Defense · Stretch Mark Correction · Bio-Active Toning · Zero-Residue Finish.

**NetWork Key Benefits**
- "Expertly formulated with plant exosome technology and advanced peptides to visibly improve radiance, refine pores, and support firmer, healthier-looking skin — while strengthening the skin barrier and delivering lasting hydration."
- Bullets: Targets uneven tone, texture and wrinkles · Reduces the appearance of dark circles and skin discoloration · Skin looks brighter, hydrated and feels more nourished · Minimizes the appearance of pores · Strengthens the skin barrier.

**Real customer reviews (verbatim, with name):** `prompts/gercek-yorumlar-2026-10-15.md`.
