---
name: feedback-show-references-next-to-designs
description: Competitor/reference-based creatives in Figma must have the reference ad image placed beside them
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2ff33643-5f5d-4ccd-9ba5-eae17bd0af91
  modified: 2026-10-03T12:40:12.827Z
---

When creatives are adapted from competitor or reference ads, place the reference image itself next to the designs in Figma. Put it at the end of each row, labelled "REFERENCE · Brand (Meta Ad Library, US)". (User, 2026-10-03: "yaptıklarının yanına referanslarını da koysana".)

**Why:** the user reviews whether the adaptation is faithful to the reference, so they need to compare the two side by side.

**How to apply:**
- Save the reference while researching.
- The Ad Library tool blocks image URLs. Instead, show the single image full-screen and save it with a zoom screenshot (save_to_disk).
- Store it under `_calisma/<batch>/refs/` and upload it into a FIT rectangle beside the row.

Related: [[feedback-no-template-typography]], [[sickscience-client]].

**Adapting a reference = copy its mechanics, not just its layout** (user, 2026-10-21, angry: the SpoiledChild Problem/Solution grid had a before|after pair in every problem card and I put a single image). Before building, list every device in the reference (pairs, arrows, badges, icons, price strike) and reproduce each one. "Diğer referanslar" = the competitor's OTHER live ads in Meta Ad Library: scan the whole advertiser page and adapt many different formats, don't ask which.
