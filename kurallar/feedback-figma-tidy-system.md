---
name: feedback-figma-tidy-system
description: Figma work must be tidy and rule-based — colour variables, SS text styles (LS 0, LH auto), one copy component per concept with Story/Feed/Square instances, column per concept
metadata:
  type: feedback
---
User, 2026-11-16: "figmada daha derli toplu daha düzenli kurallara uyarak nasıl yaparsın" (asked alongside high-end design trials).

**Why:** hand-placed one-off text and hex colours make series hard to edit and inconsistent.
**How to apply:** bind colours to `SickScience / Color` variables (accent/magenta, neutral/ivory added 2026-11-16); use text styles `SS / Display Light`, `SS / Display Light Italic`, `SS / Body`, `SS / Label` (no custom tracking/leading, see observation 91); build each concept's copy as a component (`HE / Copy / X`, Headline/Sub TEXT props + `Show sub` boolean) and place instances in Story/Feed/Square; per-format tweaks via instance overrides; layers named Photo/Karartma/Copy; one column per concept Story→Feed→Square plus a Bileşenler section. Example page "High-end · Kasım 2026" (2022:14). Full rule in project CLAUDE.md "Figma düzen sistemi".

Related: [[feedback-figma-series-sections]] [[feedback-formats-stacked-one-column]] [[feedback-brand-font-only]] [[feedback-motion-brand-kit]]
