---
name: feedback-price-base-regular-price
description: Campaign discounts are % of the REGULAR price (site compare_at), by date: Early BF sets 25, BF all 30, CM all 40; verify on the site (user, 2026-11-16)
metadata:
  type: feedback
---

Kullanıcı (2026-11-16): fiyat tabanı = normal/ana fiyat (ör. Head-to-Toe $116), üstüne dönemin yüzdesi uygulanır; siteden doğrulanır. Önceki "sitedeki güncel satış fiyatı" yorumu YANLIŞTI. Sitede setler zaten %25'te (Early BF): fiyat = 0.75 × `compare_at_price`.

**Site 2026-11-16 (price / compare_at):** Vault 135/180, Award Duo 96/128, Head-to-Toe 87/116, Body Duo (dropoff-1) 87/116, Sculpted 66/88, GLP-1 121.50/162; tekler normal: SS 64, NW 74, PC 64, DO 52.
**Takvim:** 9–21 Kasım Early BF setlerde %25; 22–28 BF tüm marka %30; 29–30 CM %40 (bkz. CLAUDE.md). Tarih yazılmaz.
**Hesap:** BF/CM fiyatı = normal fiyat × 0.70 / 0.60 (ör. Vault 126 / 108; Head-to-Toe 81.20 / 69.60). Free shipping mührü yalnız sonuç > $75.
**How to apply:** her fiyatlı kreatifte önce `products.json` (tarayıcı JS, curl rate-limit) ile compare_at'i çek; mail PDF'leri de bu tabanı kullanıyor ([[project-friday13-mail-concepts]]).
