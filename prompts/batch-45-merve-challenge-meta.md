# Batch 45 — Dr. Merve ShapeShift challenge, Meta cut (2026-10-14)
Source: client edit `14daychallenge.mp4` (Drive, fevziberk.kurt) + raws (Drive folder 1qfudyRQGyXaNaoFYnhFvVj-s9_KVJKaJ, merve@sicksciencelabs.com). Local: `_calisma/batch-45-14day/`.
- Raw camera dates: IMG_2162/2164 = 2 Apr (Day 0) · IMG_2417 = 8 Apr (Day 6) · IMG_2458 = 8 Apr · IMG_2602 = 13 Apr (Day 11) · IMG_2638 = 14 Apr (Day 12) · IMG_8738 = 24 Jul (~16 weeks).
- Client edit labelled the 24 Jul profile "DAY 14" and used it as the "After" → misleading. Day 0 vs Day 12 shows no visible jaw change (posture/light differ). User chose: honest 12-day founder diary, no before/after claim.
- Cut (`render45.py`, 19.95 s, −14.5 LUFS): hook VO "Not another peptide. It's an exosome." over product-to-camera → Merve on camera "I'm Dr. Merve, co-founder of SickScience Labs. Today I'm starting my ShapeShift challenge." → VO "Plant-derived exosomes help signal skin for a firmer, more sculpted-looking jawline." over application (Day 0, Day 11) → profile diary Day 0/6/11/12 → logo + SickScienceLabs.com. Lines with "14 days" and "Day 1, Day 14, look at that difference" dropped.
- VO isolated from the client edit's music with demucs (htdemucs two-stem). Captions Founders Grotesk Bold 84 at y≈1080; day chips magenta #A921C0 at y=300 (safe band).
- Delivered: `Video/2026-10 Ekim/01 UGC/ShapeShift – Dr. Merve challenge (Meta) – 9x16.mp4`.

## v2 (2026-10-14) — same-angle jump cuts + held before/after (user: "nereden nereye geldiğini göstersek… aynı açıdan… stop motion / jump cut… sonunda belli etsek")
- `align45.py`: profile stills d0 (IMG_2164 48.0 s), d6 (IMG_2417 29.9 s, mirrored), d11 (IMG_2602 22.5 s), d12 (IMG_2638 38.0 s), 16 weeks (IMG_8738 6.0 s, mirrored); similarity transform locks ear + nose tip to the same two points → `align/*_full.png` (1080×1920) and `*_half.png` (540 split halves).
- `render45b.py` (19.95 s, −14.0 LUFS): split hook DAY 0 | 16 WEEKS + "Not another peptide. It's an exosome." → Merve intro → mechanism VO over application → 5 jump cuts × 0.5 s (DAY 0/6/11/12/16 WEEKS) → held split + "Look at that difference." → logo strip above the heads (jaw stays visible).
- After frame labelled "16 WEEKS" (true date 24 Jul), never "Day 14". Meta may still flag body before/after — brand to approve.
- Delivered over the v1 file: `Video/2026-10 Ekim/01 UGC/ShapeShift – Dr. Merve challenge (Meta) – 9x16.mp4`.

## v3 — three hook variants (2026-10-14; user: "daha hooklu daha satın almaya yönlendiren birkaç varyant… week değil 14 günde etkisini gösteriyo… chiplerin pillerin butonların içindeki yazılar ortalı olmuyo")
- User confirms the result is at 14 days → client day labels used: DAY 0 (IMG_2164), 3 (2417), 5 (2458), 8 (2602), 10 (2638), 14 (8738; file creation date reads 24 Jul — flagged once, user decided).
- `render45v.py v1|v2|v3` (frame compositor): A = split hook DAY 0 | DAY 14 → founder intro → mechanism → 6 jump cuts × 0.4 s → held split + logo (19.95 s); B = wipe-line before/after hook with big DAY 0 / DAY 14 → jump cuts under the mechanism VO → split + "Look at that difference." → product to camera + "ShapeShift · $64 · SickScienceLabs.com" (13.35 s); C = "I TESTED MY OWN SERUM FOR 14 DAYS" over Merve's intro → countdown jump cuts → wipe → split + price (17.4 s).
- Pills: text centred with anchor='mm' on the pill centre (was top-anchored → off-centre). Captions on split/wipe frames moved above the heads (y≈480) so the jaw stays clear.
- Delivered: `Video/2026-10 Ekim/01 UGC/ShapeShift – 14 günlük challenge – A/B/C … – 9x16.mp4`; the 16-weeks version moved to `out/superseded_16weeks_meta.mp4`.
