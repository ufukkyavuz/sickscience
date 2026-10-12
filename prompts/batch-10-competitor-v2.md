# Batch 10 — Rakip uyarlamaları v2 (2026-10-03)

Kaynak: Meta Ad Library (US, aktif, gösterime göre sıralı). Bu kez marka kitabındaki doğrudan rakipler: Nutrafol, Vegamour, Medicube, Sol de Janeiro.

## İncelenen kalıplar
| Rakip | Kalıp |
|---|---|
| Nutrafol | "Because you planned to shed weight. Not hair." — avuçta ürün makro, ortalı tek satır (GLP-1 kancası) |
| Nutrafol | "The flashes are hot. The hair thinning is not." — yaşam evresi kelime oyunu, editoryal portre |
| Nutrafol | "SAY 'I DO' TO HEALTHIER HAIR." — ürünler düğün pastası süsü |
| Nutrafol | "We don't just claim it works. We guarantee it." + garanti mührü |
| Vegamour | "your hair called… it's ready to GRO" — retro çevirmeli telefon, model; ürün eski Nokia ekranında |
| Medicube | TikTok "Rating: 10/10" beyaz kutulu yorumlar, mermer tezgâhta ürün (sahte yorum riski → kullanılmadı) |
| Sol de Janeiro | Y2K dijital kamera vizörü içinde selfie + tropik sahne |

## Seçilen konseptler (yazısız master 9:16; metin Figma'da, Founders Grotesk)
- **A · Because you planned** (Nutrafol) — açık avuçta ürün, ürün rengine yakın pastel fon. ×4 ürün.
  - SS: "Because you planned to lose weight. Not your jawline."
  - NW: "… Not your glow."
  - PC: "… Not your hair."
  - DO: "… Not your firm skin."
- **B · Your ___ called** (Vegamour) — 30'larında model, ürün renginde retro telefon ahizesi, masada ürün. SS "your jawline called… it's ready to ShapeShift" · PC "your hair called… it's ready to grow".
- **C · Say I do to the duo** (Nutrafol) — beyaz düğün pastasının üst katında iki ürün = pasta süsü. Award-Winning Duo $108 (reg $128) · Body Transformation Duo $98 (reg $116).

Prompt'lar: `batch-10-build.py` → `batch-10.json` (fotografik şablon bölümleri, beyaz etiket kuralı, cm ölçüleri).

## Sonuç (2026-10-03)
- Figma: "SS · Competitor adaptations v2 — Nutrafol / Vegamour (batch-10)" (282:153), x 25950 y 58003. A ×4 ürün, B ×2 (SS, PC), C ×2 (Award Duo, Body Duo) × Story/Feed/Square = 24 frame. Sağ sütunda referans görseller (Meta Ad Library ekran görüntüsü, `output/batch-10-competitor-v2/refs/`).
- Kullanılan görseller: `hand_*`, `phone_ss4`, `phone_pc4`, `cake_award3`, `cake_body3` (ShapeShift alt etiketi siyah çıktı → siyah şerit + beyaz yazı piksel düzeltmesi; orijinal `cake_body3.orig.png`).

## Öğrenilenler
- Model konum yüzdelerini ~%15–20 yukarı kaydırıyor. "photographed from far away … scene occupying only the LOWER HALF of the frame" + istenen yüzdeleri ~%10 aşağı yazmak işe yarıyor.
- Story'de ürün masada (kadrajın altında) olursa alt %35'e düşer; insanlı sahnede ürün yüz hizasında elde tutulmalı.
- Retro telefon kadranındaki kâğıda model uydurma yazı yazıyor → "paper card in the centre of the dial is completely blank" şart.
- Gümüş yarıda siyah şeritsiz siyah yazı hâlâ çıkabiliyor; her çıktıda alt etiket zoom ile kontrol edilir.
