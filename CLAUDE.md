# SickScience Labs — Proje Rehberi

Bu klasörde ajans gibi çalışıyoruz: marka bilgisi, öneriler ve görsel üretimi.
- Marka bilgisinin tamamı (ürünler, setler, hediye kartı, fiyatlar, iddialar, görsel kimlik, rakipler): **[SICKSCIENCE-BRAND-BOOK.md](docs/SICKSCIENCE-BRAND-BOOK.md)**. Her işten önce okunur.
- Strateji ve kampanya önerileri: **[AGENCY-RECOMMENDATIONS.md](docs/AGENCY-RECOMMENDATIONS.md)**
- Ürün görselleri: `Products/site/` (siteden çekildi, dosya adı = Shopify handle)
- Fiyat veya ürün değişikliği şüphesi varsa siteye bak: `https://sicksciencelabs.com/products.json?limit=250`

## Görsel üretim — INO'dan devralınan kurallar
Teknik prompt kuralları INO projesiyle aynı. Tam kural seti: `../INO Claude Ads/CLAUDE.md` ve `../INO Claude Ads/PERFORMANCE-CREATIVE-WORKFLOW.md`.
- Model **nano_banana_pro**, `"resolution": "2k"`, mod `unlimited` (Higgsfield)
- Her prompt'a eklenir: *"ultra photorealistic, hyperrealistic, indistinguishable from a real photograph, 8K detail"* ve *"all product text must be perfectly legible, sharp, and accurate — no blurry or distorted letters"*
- `@element` varken ürünü **tarif etme**. Sadece "match the @element reference exactly…", ölçek ve konum yazılır.
- Referans görsel paylaşılırsa önce kamera, poz, ürün yerleşimi ve mood analizi yapılır, onaydan sonra üretilir. Referanstaki kişinin yüzü/kimliği kopyalanmaz.
- Referans verilmezse konsepti asistan kendi araştırmasıyla üretir, premium algı bozulmaz.
- Yazı doğruluğu kritikse kamera açısını ürüne dik (ortografik) tut, açılı kadrajda model etiket metnini yeniden çiziyor.

## SickScience'a özel görsel kurallar
- **Kapsül şişe** (ShapeShift mor, NetWork kırmızı, PowerCycle yeşil): üst yarı renkli **metalik krom**, alt yarı **ayna krom gümüş**, uçları yuvarlak hap silüeti, yazılar dikey. Yansımalar fiziksel olarak doğru olmalı, krom mat/plastik gibi görünmemeli.
- **DropOff** kapsül değil: **mat kobalt/lacivert tüp**, beyaz dikey yazı.
- Renk kodu her sahnede korunur: mor = ShapeShift, kırmızı = NetWork, yeşil = PowerCycle, kobalt = DropOff. On-the-Go pouch'ları aynı renkte.
- Hedef kitle 35–60 yaş, ama **reklam modelleri 30'lu yaşlarda** (kullanıcı, 2026-10-01: "modelleri de daha 30lu yaşlarda yap"). Prompt'ta "in her early-to-mid 30s" yaz. Cilt gerçekçi kalır (gözenek, doğal doku), plastik/aşırı rötuşlu yüz yok; "mature skin / fine lines" ifadesi kullanılmaz.
- Metin dili **İngilizce (ABD)**. Reklam metninde "permanent", "fat burning/breaking", "cure" gibi ifadeler kullanılmaz (bkz. öneriler A).
- **İnsanlı kareler GENİŞ AÇI çekilir** (kullanıcı, 2026-10-01: "az geniş açıdan yap ki hem kareye hem dikeye sorunsuz olsun"): 35mm, belden yukarı; kafa+ürün kadraj yüksekliğinin ~%25'i, kişi yatayda ortadaki %55'te; yüz ve ürün aynı hizada, kadrajın %48–72'sinde; üst %45 boş fon. Tek 9:16 master hem Story hem Feed hem Square'e kesilmeden oturur.
- **Ürün dokuları (sitedeki swatch'lardan doğrulandı, 2026-10-01 — kullanıcı: "dropoff şeffaf değil"):** jel/serum sahnesinde bu dokular aynen yazılır, "clear gel" asla kullanılmaz (PowerCycle hariç).
  - DropOff: **opak, saf beyaz, kalın krem-jel**; tepecik yapan, losyon kıvamı.
  - ShapeShift: **opak beyaz, yoğun krem-serum**; kalın, tepecikli swatch.
  - NetWork: **inci gibi ışıltılı opak beyaz krem-serum**; ince sedefli parıltı.
  - PowerCycle: **şeffaf, renksiz, hafif viskoz sıvı serum**; damlalıktan tek damla. Altın renk değil.
- **Ürün ölçüleri henüz doğrulanmadı.** 30 ml kapsül, 60 ml kapsül ve 100 ml tüpün cm ölçüleri kullanıcıdan alınınca buraya yazılacak. INO'daki gibi ölçek hataları burada da beklenir.

## Higgsfield elementleri (2026-10-01, kaynak: müşterinin PNG'leri `Products/png/`)
`@ss-shapeshift` `@ss-network` `@ss-powercycle` `@ss-dropoff` `@ss-guasha` · kapağı açık: `@ss-open-shapeshift` (beyaz pompa) `@ss-open-network` (beyaz pompa) `@ss-open-powercycle` (damlalık).
- Kapsül boyları aynı (30 ml ve 60 ml kapsül aynı silüet); DropOff tüpü kapsülün ~1.3 katı.
- Prompt'ta "@element" kelimesini düz yazma — Higgsfield onu çözülmemiş (kırmızı) mention yapıyor; "element reference" yaz.
- Gönderim: proje `higgsfield.ai/generate/@residential_walrus_super/sickscience`, Image modu, 4:5, 2K, Unlimited. Prompt kayıtları `prompts/`, çıktılar `output/`.
- ⚠ Composer "Nano Banana Pro" gösterse de Unlimited işleri API'de `nano_banana_2` olarak kayıtlı çıktı (batch-01) — kullanıcıya soruldu.
- Kampanya görseli kuralı: çerçeveli/kutu içinde fotoğraf YOK; ya tam sayfa sahne ya PNG. Her görselde ürün hikâyesi + varsa teklif (set indirimi, $75 ücretsiz kargo).

### Set / çanta / hediye elementleri (2026-10-01)
- Setler (gerçek ölçekli şeffaf PNG, `Products/sets/`): `@ss-set-vault` (PC+DO+SS) · `@ss-set-award-duo` (SS+PC) · `@ss-set-body-duo` (DO+SS) · `@ss-set-head-to-toe` (PC+DO) · `@ss-set-sculpted-duo` (SS+gua sha) · `@ss-set-glp1` (NW+SS+gua sha). Prompt'ta "exactly N products, no extra product" yaz.
- On-the-Go (site fotoğrafı, pouch+ürün): `@ss-otg-shapeshift` `@ss-otg-network` `@ss-otg-powercycle` `@ss-otg-dropoff`
- Çantalar: `@ss-pouch-purple` `@ss-pouch-orange` `@ss-pouch-blue` `@ss-pouch-red` `@ss-pouch-green` (~22×15 cm file pouch) · `@ss-tote` (holografik) · `@ss-white-bag` (stokta yok)
- Hediye kartı: `@ss-giftcard`

## Üretim akışı (2026-10-01 kararı): görsel YAZISIZ üretilir, metin Figma'da yazılır
- Higgsfield'da prompt'a hiçbir yazı/headline/fiyat/buton koyma; "no text, no letters, no logos added to the scene" (ürün etiketleri hariç) ekle.
- **Master format 9:16 (1080×1920)** → 4:5 (1080×1350) aynı görselin dikey ortasından kırpılır.
- **Meta safe zone (Stories/Reels 9:16):** üst %14 (0–270 px) ve alt %35 (1250–1920 px) bölgesine metin/logo/CTA konmaz (platform arayüzü kapatır); yanlardan %6 (~65 px) boşluk. Ürün ve metin alanı 270–1250 px bandında kalmalı.
- Kompozisyon kuralı: ürün dikey bandın alt-orta kısmında (≈ %45–65), metin için **%15–42 arası temiz, sade negatif alan** (prompt'a açık copy-space cümlesi yazılır). Alt %35 sakin/az detaylı arka plan devamı olmalı (4:5 kırpımında kesilir).
- Feed 4:5'te logo üstte, CTA altta; 9:16'da ikisi de safe band içinde.

## Figma
- Dosya: https://www.figma.com/design/PHPZ7XLpEVMcUVVEcNTwmz/SickScience — sayfa "02 · Reklam Kreatifleri" (7:3).
- "SS · October · Creative V2" (21:2) = önceki oturumun düz renk + kutulu ürün şablonları (A01–A16 brief'leri ve kopyaları burada; kopya kaynağı olarak kullan, görsel stil olarak kullanma).
- "SS · Creative V3 / Higgsfield scenes" (35:6) = yeni akış: Higgsfield yazısız master tam sayfa arka plan + Inter metin. Story 1080×1920, Feed 1080×1350.
- Feed kırpımı: image fill CROP, imageTransform [[1,0,0],[0,1350/1935,150/1935]] (üstten 150px kaydırma) — ürün kesilmeden üstte metin alanı kalır.
- Font: Founders Grotesk / Neue Haas plugin ortamında YOK → Inter (Black/Bold/Semi Bold) + IBM Plex Mono eyebrow. Logo: "Sick" beyaz/siyah + "Science" #A921C0.
- Story frame'lerinde gizli/kilitli "Meta safe zone guide" katmanı var (aç-kapa ile kontrol).

## Figma tipografi kuralı (kullanıcı, 2026-10-01: "saçma ai slop işlerinden vazgeç")
Referans = Higgsfield batch-01'in kendi tipografisi (`output/batch-01/`). Şablon görünümlü düzen YASAK: mono "eyebrow" etiketler, metin olarak yazılmış logo, sola yaslı aynı blok her görselde, her yere hap buton.
- Başlık TEK güçlü satır/iki satır, BÜYÜK HARF: geniş sahnelerde Inter Bold ortalı (THE VAULT IS OPEN), editoryal/ölçü sahnelerinde Anton kondanse (SCULPTED IN 2 WEEKS*, SMOOTHER. MEASURED.). Satırı kadraj genişliğine fit et.
- İkinci satır vurgu rengi (ürün rengi / #7300C7), altında tek sade Inter Regular satır (istatistik veya fiyat; fiyat kısmı Bold).
- CTA sadece teklif varsa, tek hap, ortalı; ürünün üstüne binmez.
- Dipnot küçük, ürünün üstüne binmez.
- ⚠ Font: Founders Grotesk OTF'leri `~/Library/Fonts`'a kuruldu (2026-10-01) ama use_figma (uzak eklenti ortamı) yerel fontu GÖRMEZ — sadece Google fontları + ekibe yüklenmiş paylaşımlı fontlar. Metinler DAİMA düzenlenebilir TEXT kalır (vektöre çevirme — kullanıcı reddetti). Founders'a geçiş: kullanıcı Figma'da seçip font değiştirir ya da font Figma takım/organizasyon fontu olarak yüklenince script ile yapılır.
- ✅ 2026-10-01 güncelleme: Founders Grotesk artık Figma'da yükleniyor (kullanıcı ekledi). Stil adları: "Regular/Medium/Semibold/Bold", "Condensed Bold/Semibold…", "X-Condensed Bold…", "Text Regular…". Tüm yeni metinler Founders Grotesk. Anton/Inter kullanma.
- Katmanları KİLİTLEME (kullanıcı istemiyor). Fotoğraf ayrı "Photo" katmanı, kilitsiz.
- Logo: Figma bileşen seti "Component 1" — koyu zemin `29:218` (White and Pink), açık zemin `29:219` (Black and Pink); Story'lerde ortalı, y=190, 398×54.
- Formatlar: her tasarım Story 1080×1920 + Feed 1080×1350 + Square 1080×1080. Fotoğraf = ayrı "Photo" rect (1080×1935, FILL), frame dolgusu fotoğrafın üst renginden; ürün metne binerse Photo katmanını aşağı kaydır.
- "SS · Bundle Offers" (50:6): 10 indirimli set, eski fiyat üstü çizili + yeni fiyat + "YOU SAVE $X · %Y OFF" rozeti (Founders Grotesk).

## Reklam metni kuralları (2026-10-01, kullanıcı: "saçma ya da markaya uymayan başlıkları değiştir")
- Başlık mantıklı ve görselle tutarlı olmalı (ör. kalın beyaz krem görselinde "not a lotion" denmez; "by day / by 8AM" gibi çelişkiler yok).
- Sadece marka kitabında geçen sayı/iddia/ödül kullanılır. Doğrulanmamış dozaj yazılmaz ("2 pumps", "1 ml" YOK; PowerCycle kullanım sıklığı sitede tutarsız → sıklık yazma).
- Etki iddiaları "-looking" ile yumuşatılır (sculpted-looking, thicker-looking); istatistikte * + "Clinical evaluation / Consumer perception study. Individual results may vary."
- Teklif satırı sahnedeki ürünle eşleşir (tek ürün sahnesine duo fiyatı konmaz).
- Ödüller (2026-10-02 doğrulandı, kullanıcı: "ödüller nerden gelmiş kanıtla"): SADECE sitede geçen kullanılır. ShapeShift = "2024 REAL SIMPLE Award Winner - Best Jawline & Neck Treatment" (PDP açıklaması) ✅ · PowerCycle = yalnızca "Award Winner" etiketi (detay yok) · DropOff / NetWork = ödül YOK. Oprah Daily ve Men's Health sitede yok → KULLANMA. Rozet tasarımı sade (ince çerçeveli metin), dolgu renkli/sarı daire rozet yok.
- Başlık 2 satırı geçmez; satır kırılımı elle (\n) verilir, sığmazsa punto küçültülür.

## Kullanıcının Figma düzeltmeleri — BOZMA (2026-10-01)
- Kullanıcı mevcut kreatifleri elle düzeltiyor: format başına ayrı görsel/kırpma (Photo rect'i büyütüp kaydırıyor, Square/Feed'de farklı imageHash), dipnotları alta alıyor (Story ~1710, Feed 1310, Square 1044).
- Var olan frame'lerde Photo boyutu/konumu/dolgusu, metin ve dipnot konumu kullanıcı istemedikçe DEĞİŞTİRİLMEZ; toplu "normalize" script'i çalıştırılmaz. Yeni iş yeni frame'lerde yapılır.

## Ürün içerik serisi başlık stili (kullanıcı, 2026-10-01 — kaynak: Figma 80:58)
- Başlık yok; üstte ürün adı + açıklama. Story: "ShapeShift" Founders Condensed Bold 150 (x138,y272) + sağında magenta (#A921C0) hap "$64" (Medium 34, ls 10%, pad 28/12, r200) + alt satır y417: "30 ML" ve "V-Line Jaw Defining Serum" Regular 40. Feed ×0.8, Square ×0.64 ortalanır.
- Çizgi (rule), "30 ML / $64" iki uçlu spec satırı gibi "çizgili saçma şeyler" YOK.
- Ingredient anlatımı: (1) ürün siluetinde şeffaf kapsül içinde katmanlı bileşenler + yan etiketler, (2) The Ordinary tarzı büyük yakın plan + solda başlık/ince çizgi/açıklama listesi. Referanslar kullanıcı tarafından verildi.

## Ürün bilgisi = SİTEDEKİ METİN, birebir (kullanıcı, 2026-10-01: "niye kafana göre bişeyler ekliyon… adamlar websitesine bütün bilgileri yazmış")
- Ingredients, benefits, istatistik cümleleri, kullanım talimatı ürün sayfasından (`/products/<handle>` HTML'i — products.json'da yok) AYNEN alınır. Ekleme/çıkarma, kendi açıklamanı yazma, INCI listesinden seçme YOK.
- ShapeShift (site): Ingredients = NX35™ Sculpt Technology (Pineapple Exosomes) · Butyrospermum Parkii (Shea) Butter · Caffeine · Niacinamide (Vitamin B3) · Sodium Hyaluronate · Ceramides (bileşen başına açıklama yok). Key Benefits = "Supports the look of a contoured, sculpted neck and jawline" · "Helps visibly tighten and firm the neck" · "Softens, smooths and hydrates". Real Results = 92% saw a more sculpted jawline · 94% saw smoother tech-neck lines · 98% saw firmer, tighter neck skin · 90% noticed improved skin definition ("Chisel Your Jawline in 2 Weeks"). Texture: Gel-Serum. How to use: 1–2 pumps, upward, twice daily.
- Bu kural yukarıdaki "-looking ile yumuşat / dozaj yazma" kuralının önüne geçer: sitede yazıyorsa sitedeki ifade kullanılır.

## PR / basın kreatifleri (kullanıcı, 2026-10-01)
- Amaç bilinirlik: haberin paylaşıldığını anlat (gerçek ekran görüntüsünden yırtık kâğıt kupürleri + editör kartı + gerçek before/after kupürleri). Sayfanın birebir kopyası "native editoryal" görseller daha önce perform etmedi (Drive: "Ad that looks like editorial").
- Arka plan AÇIK, ferah, bilimsel (gün ışığında beyaz lab tezgâhı). Koyu/dramatik zemin + gazete kupürü = "cinayet haberi" etkisi → kullanma. Açık zeminde logo 29:219 (Black and Pink), yazılar koyu.
- CNN Underscored ile anlaşma var: logo, haber metni ve ekran görüntüsü kullanılabilir.

## Fotografik prompt formatı — ZORUNLU (kullanıcı, 2026-10-02: "fotografik görsellerde promptlarını bu şekilde vericen")
Tüm fotografik Higgsfield prompt'ları **[prompts/TEMPLATE-photographic.md](prompts/TEMPLATE-photographic.md)** bölümleriyle ve sırasıyla yazılır: açılış satırı (element) → kimlik koruma paragrafı → PRODUCT ORIENTATION → COMPOSITION AND FRAMING → SCALE (gerçek cm) → LIGHT AND SHADOW → BACKGROUND → PHOTOGRAPHIC FINISH → Negative listesi. Tek paragraflık eski prompt yapısı kullanılmaz. SCALE için ürün cm ölçüleri kullanıcıdan alınacak.

## Meta native kreatif notları (kullanıcı, 2026-10-02)
- Karikatür (2×2 meme) kreatifler onaylı — DOKUNMA.
- Referansı birebir oku: "i am THIS close" = emoji el + parmak arasına küçük yazıyla mesaj. Ürünü gerçek boyutundan küçük gösteren sahne (parmakla tutulan dev hap) YOK.
- Teklif metni paragraf olmaz: ödül = rozet/hap, fiyat = büyük yeni fiyat + üstü çizili eski + SAVE hapı.
- Story'de ürün 270–1250 px safe band içinde ve büyük olmalı.
- Kullanıcıya ara ekran görüntüsü gönderme; işi bitir, son hali tek seferde göster.
