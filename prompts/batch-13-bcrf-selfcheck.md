# Batch 13 — NetWork × BCRF · kendi kendine muayene konseptleri (2026-10-04)

Müşteri isteği: "meme muayenesi gibi daha anlaşılır görselle bir tane". Kullanıcı 4 konseptin hepsini onayladı.

| Kod | Konsept | Görsel | Başlık |
|---|---|---|---|
| ck_mirror | Rutine bir adım ekle | 30'larında kadın, pembe spor sütyeni, ayna karşısında muayene pozu; ürün duvar rafında | ADD ONE STEP TO YOUR ROUTINE. |
| ck_fog | Duş camında buğu | Buğulu camda parmakla çizilmiş daire + tik; ürün mermer pervazda. "MONTHLY SELF-CHECK" Figma'da el yazısıyla (sahne içi yazı) | THE MOST IMPORTANT STEP ISN'T IN A BOTTLE. |
| ck_phone | Telefon hatırlatıcısı | Lavaboda dik duran telefon (ekran boş), yanında NetWork + kurdele; kilit ekranı bildirimi Figma'da çizilir | SET THE REMINDER. WE'LL HANDLE THE GLOW. |
| ck_hand | Know your normal | Üstten flat lay: pembe örgü kazak, düz parmak uçları kazağın göğüs kısmında, kurdele, yatık NetWork | KNOW YOUR NORMAL. |

Ortak alt satır: "This October, 20% of NetWork sales on SickScienceLabs.com go to The Breast Cancer Research Foundation."

Kurallar: çıplaklık yok, kişisel sağlık durumunu ima eden "you/your breasts" dili yok, muayene talimatı/tıbbi iddia yok, BCRF logosu yok, "Know Your Lemons" metaforu yok.

Prompt'lar: `batch-13-build.py` → `batch-13.json`. Çıktılar: `output/batch-13-bcrf-selfcheck/`.

## Sonuç (2026-10-04)
- Figma: "SS · NetWork × BCRF — Self-check concepts (batch-13)" (332:201). 4 konsept × Story/Feed/Square.
- Kullanıcı geri bildirimi "ürün photoshopla konmuş gibi" → prompt'lara INTEGRATION bölümü eklendi (v2); tüm görseller v2/v3 ile yeniden üretildi.
- Görseller: Mirror m5 (Story+Feed kırpım) / m5_sq · Fog fog (Story+Feed kırpım) / fog_sq3 · Phone phone (Story+Feed kırpım) / phone_sq2 · Hand hand2 (Story+Square kırpım) / hand2_45.
- Kilit ekranı (8:14 + "REMINDERS · now / Monthly self-check / Today") Figma'da çizildi; Square'de kart telefonun yanında. Buğu yazısı Permanent Marker (sahne içi).
- Öğrenilen: insanlı sahnede model kafayı hep yukarı koyuyor; "tall room, high ceiling, she stands far back, knees-up, wall above her head fills the upper half" + 24mm işe yaradı (m5). Kare/4:5'te model nesneleri yukarı taşıyor → Feed çoğunlukla 9:16 master'dan kırpıldı; Square'de bağış satırı alta alındı.
- Square'de ilk üretimde bağış satırı ürüne binmesin diye frame'in altına (zemin üstü) taşındı.
