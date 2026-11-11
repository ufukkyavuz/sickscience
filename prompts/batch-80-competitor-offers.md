# Batch 80 — Rakip indirim reklamları → bizim teklifler (2026-10-30)

Kaynak: Atria reklam kütüphanesi (Ekim 2026'da başlayan reklamlar). Figma: "Ekim 2026" sayfası, bölüm 1303:1036. Üretim yok, müşteri fotoğrafları + set PNG'leri.

Rakip oranları: Zyren %64 / B2G1, Grüns %55 + hediye, Medicube %41, Cécred %25, StriVectin %25 + hediye, Mustela / Crown Naturale / Drowsy Halloween %20.

| # | Referans | Teklif (site, 30.10) | Görsel |
|---|---|---|---|
| C1 | Cécred krom "25% OFF" | Vault %20, $144 / $180 | S_1140 lab sehpası |
| C2 | Zyren "We're saying goodbye" | Award-Winning Duo $108 / $128 | set PNG |
| C3 | Dr. Melasmin "It's pricey" | Vault $144 / $180 | Old Image SS0547 |
| C4 | StriVectin "25% off" | Subscribe & save %15 | Tezza-0408 (aynalıydı, çevrildi) |
| C5 | Medicube "Save 20% now" | GLP-1 System Save $25, $137 / $162 | set PNG |
| C6 | Grüns "Up to 55% off" | Up to %20 + free shipping (tüm setler $75 üstü) | Vault, Body Duo, Head-to-Toe PNG |

Kullanılmadı: son tarih / "ends at midnight" / "lowest price" (onaylı değil), Black Friday, ücretsiz hediye (sitede hediye ürünleri var, koşulu bilinmiyor).

## v2 (2026-10-30, kullanıcı geri bildirimi) — prompt'lar `prompts/batch-81-offers-white.py`
- C1: Cécred harfleri krom değil, açık beyaz-gri zeminde su damlası. Higgsfield'da "20% OFF" su damlası üretildi, zemin griye desatüre edilip açıldı.
- C2, C3, C5: beyaz lab sahneleri üretildi (Award Duo, Vault buz camı, GLP-1). Referans açıları korundu, zemin beyaz.
- C2: alt yarı etiket gümüşte kayboldu, etiket şeridi gerçek PNG'den (`assets/set_award-duo.png`) yerleştirildi.
- C3: kart gerçek yorumla (Cynthia B., Okendo) yeniden kuruldu, isim + yıldız + harf avatar; uydurma kadın yorumu yazılmadı.
- C4: Story'de yazı bloğu yukarı alındı (y 820–1200), zemin açık tona çekildi.
- C5, C6: zemin beyaz ağırlıklı.

## v3 C6 (2026-10-30, kullanıcı: "daha fazla grünse benzet", "badgeleri falan")
Grüns anatomisi: kırışık kâğıt (Higgsfield, beyazlatıldı, `paperreal.jpg`), dev mor başlık, büyük eğik ürünler (gerçek PNG), tırtıklı sticker'lar (star 22 köşe, kalın stroke), jel lekeleri (MULTIPLY), yuvarlak mühür "Made by two PhD scientists" (site metni). Üst logo yok, logo mühürde.
Tüm seride metinler line height Auto; CTA/rozet/sticker leadingTrim CAP_HEIGHT, CTA padding 30/30, 64.
