# Batch-92: PowerCycle boyut düzeltmesi (2026-11-02)
Müşteri (Merve): "yeşil olan şişe 60 ml, mor olan 30, bazı görsellerde boyutlar aynı gözüküyor."
Kök neden: Products/sets PNG'lerinde tüm kapsüller 1398 px, PC mordan dar. ss-set-vault ve ss-set-award-duo elementleri bu oranı üretime taşıdı. Gerçek oran (14 cm / 12 cm, S_0684 ile doğrulandı): PC = SS × 1.17 boy.
Ölçüm (yeşil/mor boy): B07 1.01, Vault O1 0.90, Award O2 0.98, B09 ~1.0. Düzeltme sonrası kapak ölçümü: B07 1.17, Vault 1.12, O2 1.16.
Yöntem: tools/bottle_grow.py şişeyi kendi pikselleriyle tabanından büyütür. O2'de el üste geri kondu. B09 tellerin arkasında olduğu için yeniden üretildi (ayrı elementlerle: ss-shapeshift, ss-dropoff, ss-powercycle).
Yedek: Products/sets/ss-set-vault.orig.png, ss-set-award-duo.orig.png.

## Sonuç (2026-11-02)
Figma Kasım: B07 Story/Feed, B09 Story/Feed, Halloween Vault (3 format), Award Duo (3 format), B01 Story/Feed küçük set görseli düzeltildi. B07 Feed, B09 Feed, Award Square Figma Expand 1:1 ile yeniden üretildi. Eski görseller _calisma/batch-89-kasim-foto2 ve batch-87-halloween-indirim içinde duruyor.
Ekim sayfasına dokunulmadı (kullanıcı düzeltmeleri kuralı). Aynı set elementinden gelen adaylar: Bundle 01 vault, Bundle 03 award, Meta BigSet Vault/AwardDuo, SayIDo AwardDuo, SS17 CD v2 Speech bubble, SS20 Receipt Vault, SS20v2 VS price, SS21 Code digits, SS21 Diagram labels, C2 Award review, B69 VAULT KIT. Higgsfield set elementleri eski görselle duruyor.

## B08 geri alındı (2026-11-02)
Kullanıcı: "bunu buna çevirelim, diğeri çok karmaşık". Beyaz kaide sahnesi (batch-89/B08.png) kaldırıldı, sade gri zeminli çanta + kapsül görseli geri geldi (fomo.jpg, _calisma/batch-92-pc-boyut/B08_sade.jpg). Feed birebir; Story Figma Expand 9:16 (ilk Expand'de alt tarafta ton çizgisi vardı, ikinci deneme temiz). Metin siyah, Story'de fiyat + CTA başlığın altında, satır ortalı.
