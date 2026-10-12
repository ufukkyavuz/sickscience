# Batch 24 — Ulta Holiday 2026, yaratıcı konseptler (2026-10-08)

Talep: "daha yaratıcı şeyler" + FY26 Holiday guideline (Social Best Practices + Promotional Moments) kapsaması.
Figma: "SS · Ulta Holiday 2026 — creative concepts (batch-24)" (573:797); batch-23 temel set: 562:773.

| # | Konsept | Ürün | Guideline karşılığı |
|---|---|---|---|
| 01 | Ornament — kapsül süs olarak ağaçta | NetWork | Gifting / Uniquely Ulta palette |
| 02 | Advent calendar — açık kapıda ürün | PowerCycle | Gift inspiration / discovery |
| 03 | FOOH dev Ulta poşeti + kapsül heykel | ShapeShift | Uniquely Ulta (pembe poşet) |
| 04 | Gift burst — patlayan kutu, %50 teklif | NetWork | Value / holiday offers |
| 05 | Wish list flat lay (el yazısı) | ShapeShift | Gift inspiration / self-gifting |
| 06 | Wrapping table, %50 teklif | DropOff | Last-minute gifting / value |
| 07 | BLACK FRIDAY AT ULTA (FOOH görseli) | ShapeShift | Promotional Moment 11/22–11/28 |
| 08 | CYBER MONDAY — online only at ulta.com (advent) | PowerCycle | Promotional Moment 11/29–11/30 (e-com açığı) |
| 09 | SEE THE GEL — jel-serum doku swatch | ShapeShift | Show, don't tell (texture) |

Batch-23 (562:773): 01 bag/magic starts, 02 bag Early Black Friday, 03 self-gift tag, 04 stocking, 05 cake Early offer, 06 lab, 07 gifts, 08 gifts Big Holiday Beauty Sale.

## Kurallar / düzeltmeler
- Ulta logosu resmi SVG (ulta.com) → `tools/ulta_logo_swap.py`; model "ULTA" yazısı kalmaz (poşetler, FOOH tabelaları).
- Poşet sahnesinde ürün poşetin YANINDA (kullanıcı 2026-10-08), önünde değil.
- Fiyatlar: Eylül Ulta etkinlikleri (Beauty Blowout, 21DOB Beauty Steal) "%50 off Sick Science" → $64→$32, $74→$37, $52→$26; katman adında "CONFIRM holiday terms with Ulta".
- Gua sha Ulta'da yok → ornament tek NetWork ile yeniden üretildi.
- Sayfa içi prompt düzeltmeleri: wishlist_v2/sq2 (ürün kağıt genişliğinin yarısı), ornament_nw_v2/sq2 (tek parça fon, yatay bant yok), advent_sq2 (çatı %40 altında), u23_bag_*_side (ürün poşetin yanında).
- Doku karesi (texture_sq) jel fazla opak çıktı → Feed/Square dikey görselden kırpıldı.
