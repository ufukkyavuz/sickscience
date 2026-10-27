# SickScience Labs — Proje Rehberi

Bu klasörde ajans gibi çalışıyoruz: marka bilgisi, öneriler ve görsel üretimi.
- Marka bilgisinin tamamı (ürünler, setler, hediye kartı, fiyatlar, iddialar, görsel kimlik, rakipler): **[SICKSCIENCE-BRAND-BOOK.md](SICKSCIENCE-BRAND-BOOK.md)**. Her işten önce okunur.
- Strateji ve kampanya önerileri: **[AGENCY-RECOMMENDATIONS.md](AGENCY-RECOMMENDATIONS.md)**
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
- **Gua sha = PASLANMAZ ÇELİK** (gümüş metal, ~9 cm, tek çentikli kalp/kanat formu, "SickScience" kazımalı — `Products/png/guassha.png`). Pembe/rose quartz/jade/taş gua sha YOK (kullanıcı, 2026-10-07: "böyle bi guasha yok"). Prompt'a "flat SOLID polished stainless-steel gua sha" yaz; negatife "pink gua sha, rose quartz, jade, stone, translucent, melted shape".
- **DropOff** kapsül değil: **mat kobalt/lacivert tüp**, beyaz dikey yazı.
- Renk kodu her sahnede korunur: mor = ShapeShift, kırmızı = NetWork, yeşil = PowerCycle, kobalt = DropOff. On-the-Go pouch'ları aynı renkte.
- Hedef kitle 35–60 yaş, ama **reklam modelleri genç ve güzel: 20'lerinin sonu** (kullanıcı, 2026-10-01: "30lu yaşlarda yap"; 2026-10-04 güncelleme: "kadınlar genel olarak daha genç ve güzel olsunlar"). Prompt'ta "a strikingly beautiful woman in her late 20s, model-like features" yaz. Cilt gerçekçi kalır (gözenek, doğal doku), plastik/aşırı rötuşlu yüz yok; "mature skin / fine lines" ifadesi kullanılmaz. İnsanlı kareler **stüdyoda kurulmuş set** gibi: ör. plato banyosu — beyaz sıva duvar, heykelsi beyaz taş lavabo, seçilmiş 2–3 obje, kampanya ışığı; emek verilmiş prodüksiyon olduğu belli olur. Ne sıradan ev fotoğrafı ne de düz renk seamless fon (kullanıcı, 2026-10-04: "stüdyo setupı gibi olsun… plato banyosu hesabı beyaz arkaplan, uğraşılmış bir fotoğraf olduğu belli olmalı"). Muayene pozu: kalkık kolun altında, parmak uçları göğsün DIŞ/yan kenarında — göğsün ortasında el (yemin pozu) YOK (kullanıcı: "daha kenardan meme kontrolü gibi olmalı").
- Metin dili **İngilizce (ABD)**. Reklam metninde "permanent", "fat burning/breaking", "cure" gibi ifadeler kullanılmaz (bkz. öneriler A).
- **İnsanlı kareler GENİŞ AÇI çekilir** (kullanıcı, 2026-10-01: "az geniş açıdan yap ki hem kareye hem dikeye sorunsuz olsun"): 35mm, belden yukarı; kafa+ürün kadraj yüksekliğinin ~%25'i, kişi yatayda ortadaki %55'te; yüz ve ürün aynı hizada, kadrajın %48–72'sinde; üst %45 boş fon. Tek 9:16 master hem Story hem Feed hem Square'e kesilmeden oturur.
- **Ürün dokusu = YARI ŞEFFAF JEL-SERUM, tüm ürünlerde** (kullanıcı, 2026-10-05: "ürünlerin içindekiler daha jel serum gibi, ne çok beyaz ne tam şeffaf"). Bu kural 2026-10-01'deki "opak beyaz krem / şeffaf sıvı" dokularının YERİNE geçer.
  - Prompt'a aynen: *"a translucent gel-serum — semi-transparent with a soft milky haze, neither opaque white cream nor water-clear; glossy, smooth, slightly viscous, it holds a soft rounded bead and lets light pass through its edges"*.
  - NetWork'te buna "with a very subtle pearly shimmer" eklenebilir; PowerCycle damlalıktan tek, aynı yarı şeffaf jel-serum damlası (altın renk değil).
  - Negatife: "opaque white cream, thick white lotion, whipped or peaked cream, body butter, water-clear liquid, fully transparent gel, coloured or gold serum".
- **Ürün ölçüleri (kullanıcı, 2026-10-02) — her prompt'un SCALE bölümüne yazılır:**
  - ShapeShift kapsül: 12 cm boy, 3.5 cm çap · NetWork kapsül: 12 cm boy, 3.5 cm çap · PowerCycle kapsül: 14 cm boy, 4.5 cm çap
  - DropOff tüp: ~20 cm boy (şimdilik yaklaşık)
  - Makyaj çantaları / On-the-Go pouch: 21 × 16 cm · Holografik tote: 30 × 40 × 10 cm
  - Referans: yetişkin avuç ~18–19 cm → 12 cm kapsül elin ~2/3'ü. "If in doubt make the products smaller, never bigger."
  - **Kapsül ORANI da korunur** (kullanıcı, 2026-10-05: "ürün doğru değil"): ShapeShift/NetWork boyu çapının 3.4 katı, kapak tam üst yarı. Element tıknaz/geniş çizmeye meyilli → her prompt'a "PROPORTIONS ARE CRITICAL: slim and tall… height 3.4× width… cap = upper half; never stubby, chubby, squat" + negatif "stubby, chubby or wide bottle" yazılır; çıktıda en/boy ölçülüp kontrol edilir. Elde tutulan şişe en sık bozulan durum; mümkünse şişe zeminde dursun. Video (Veo) şişeyi yeniden çizer → bozulursa kadraj dışı bırak, kapanışta gerçek PNG kullan.
  - **Ürünü kameraya yaklaştırıp büyütme hilesi YASAK** (kullanıcı, 2026-10-04: "ürünün boyutlarını aşırı büyük yapıp bozmuşsun, istemediğimiz bir şey"). İnsanlı sahnede ürün kişiyle aynı derinlikte durur ya da elde tutulur; kafası/gövdesi kadar görünen ön plan ürünü yok. Prompt'a "at the same distance from the camera as the model" yaz; "appears as tall as her head", "close to the camera" yazma. Etiket küçük kalıp bozulursa piksel düzeltmesi yapılır, ürün büyütülmez.

## Higgsfield elementleri (2026-10-01, kaynak: müşterinin PNG'leri `Products/png/`)
`@ss-shapeshift` `@ss-network` `@ss-powercycle` `@ss-dropoff` `@ss-guasha` · kapağı açık: `@ss-open-shapeshift` (beyaz pompa) `@ss-open-network` (beyaz pompa) `@ss-open-powercycle` (damlalık).
- Kapsül ölçüleri: SS/NW 12×3.5 cm, PC 14×4.5 cm; DropOff tüpü ~20 cm (kapsülün ~1.6 katı).
- Prompt'ta "@element" kelimesini düz yazma — Higgsfield onu çözülmemiş (kırmızı) mention yapıyor; "element reference" yaz.
- Gönderim: proje `higgsfield.ai/generate/@residential_walrus_super/sickscience`, Image modu, 4:5, 2K, Unlimited. Prompt kayıtları `prompts/`, çıktılar `_calisma/`.
- ⚠ Composer "Nano Banana Pro" gösterse de Unlimited işleri API'de `nano_banana_2` olarak kayıtlı çıktı (batch-01) — kullanıcıya soruldu.
- Kampanya görseli kuralı: çerçeveli/kutu içinde fotoğraf YOK; ya tam sayfa sahne ya PNG. Her görselde ürün hikâyesi + varsa teklif (set indirimi, $75 ücretsiz kargo).

### Set / çanta / hediye elementleri (2026-10-01)
- Setler (gerçek ölçekli şeffaf PNG, `Products/sets/`): `@ss-set-vault` (PC+DO+SS) · `@ss-set-award-duo` (SS+PC) · `@ss-set-body-duo` (DO+SS) · `@ss-set-head-to-toe` (PC+DO) · `@ss-set-sculpted-duo` (SS+gua sha) · `@ss-set-glp1` (NW+SS+gua sha). Prompt'ta "exactly N products, no extra product" yaz.
- On-the-Go (site fotoğrafı, pouch+ürün): `@ss-otg-shapeshift` `@ss-otg-network` `@ss-otg-powercycle` `@ss-otg-dropoff`
- Çantalar: `@ss-pouch-purple` `@ss-pouch-orange` `@ss-pouch-blue` `@ss-pouch-red` `@ss-pouch-green` (21×16 cm pouch) · `@ss-tote` (holografik) · `@ss-white-bag` (stokta yok)
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
Referans = Higgsfield batch-01'in kendi tipografisi (`_calisma/batch-01/`). Şablon görünümlü düzen YASAK: mono "eyebrow" etiketler, metin olarak yazılmış logo, sola yaslı aynı blok her görselde, her yere hap buton.
- Başlık TEK güçlü satır/iki satır, BÜYÜK HARF: geniş sahnelerde Inter Bold ortalı (THE VAULT IS OPEN), editoryal/ölçü sahnelerinde Anton kondanse (SCULPTED IN 2 WEEKS*, SMOOTHER. MEASURED.). Satırı kadraj genişliğine fit et.
- İkinci satır vurgu rengi (ürün rengi / #7300C7), altında tek sade Inter Regular satır (istatistik veya fiyat; fiyat kısmı Bold).
- CTA sadece teklif varsa, tek hap, ortalı; ürünün üstüne binmez.
- Dipnot küçük, ürünün üstüne binmez.
- ⚠ Font: Founders Grotesk OTF'leri `~/Library/Fonts`'a kuruldu (2026-10-01) ama use_figma (uzak eklenti ortamı) yerel fontu GÖRMEZ — sadece Google fontları + ekibe yüklenmiş paylaşımlı fontlar. Metinler DAİMA düzenlenebilir TEXT kalır (vektöre çevirme — kullanıcı reddetti). Founders'a geçiş: kullanıcı Figma'da seçip font değiştirir ya da font Figma takım/organizasyon fontu olarak yüklenince script ile yapılır.
- **CONDENSED / X-CONDENSED KESİMLER KULLANILMAZ** (kullanıcı, 2026-10-05: "fontlarda da condensed kullanmayalım, beğenmedim"). Başlıklar dahil her yerde normal genişlikte Founders Grotesk (Regular/Medium/Semibold/Bold). Bu kural aşağıdaki "Founders Condensed Bold 150", "X-Condensed beyaz dev başlık", "Anton kondanse" gibi eski notların ÖNÜNE geçer; uzun başlık sığmazsa punto küçültülür ya da satır bölünür.
- **SADECE marka fontu: Founders Grotesk** (kullanıcı, 2026-10-03: "marka fontu neyse onu kullanacaksın"). Mono (IBM Plex Mono vb.) veya başka hiçbir font kullanılmaz — referansta farklı font olsa bile Founders Grotesk'in bir kesimiyle karşılanır. **İstisna:** konsepti gereği sahnenin parçası olan el yazısı (post-it, kâğıt not vb.) el yazısı fontuyla (Permanent Marker) yazılır (kullanıcı: "kağıtlıda okay konsepte göre olur").
- ✅ 2026-10-01 güncelleme: Founders Grotesk artık Figma'da yükleniyor (kullanıcı ekledi). Stil adları: "Regular/Medium/Semibold/Bold", "Condensed Bold/Semibold…", "X-Condensed Bold…", "Text Regular…". Tüm yeni metinler Founders Grotesk. Anton/Inter kullanma.
- Katmanları KİLİTLEME (kullanıcı istemiyor). Fotoğraf ayrı "Photo" katmanı, kilitsiz.
- Logo: Figma bileşen seti "Component 1" — koyu zemin `29:218` (White and Pink), açık zemin `29:219` (Black and Pink); Story'lerde ortalı, y=190, 398×54.
- Formatlar: her tasarım Story 1080×1920 + Feed 1080×1350 + Square 1080×1080. Fotoğraf = ayrı "Photo" rect (1080×1935, FILL), frame dolgusu fotoğrafın üst renginden; ürün metne binerse Photo katmanını aşağı kaydır.
- "SS · Bundle Offers" (50:6): 10 indirimli set, eski fiyat üstü çizili + yeni fiyat + "YOU SAVE $X · %Y OFF" rozeti (Founders Grotesk).

## Reklam metni kuralları (2026-10-01, kullanıcı: "saçma ya da markaya uymayan başlıkları değiştir")
- Başlık mantıklı ve görselle tutarlı olmalı (ör. kalın beyaz krem görselinde "not a lotion" denmez; "by day / by 8AM" gibi çelişkiler yok).
- Sadece marka kitabında geçen sayı/iddia/ödül kullanılır. Doğrulanmamış dozaj yazılmaz ("2 pumps", "1 ml" YOK; PowerCycle kullanım sıklığı sitede tutarsız → sıklık yazma).
- Etki iddiaları "-looking" ile yumuşatılır (sculpted-looking, thicker-looking). **Dipnot/yasal not EKLENMEZ** (kullanıcı, 2026-10-03: "*Consumer perception study… her görsele eklemene gerek yok, istemiyorum") — istatistiğe yıldız (*) da konmaz; "See website for offer details" gibi notlar da yok. **Tek istisna:** yapay zekayla üretilmiş önce/sonra görsellerinde frame'in en altına küçük (≈20 px) "Simulated results." yazılır (kullanıcı, 2026-10-03: "simulated resultu en alta küçük yaz").
- Teklif satırı sahnedeki ürünle eşleşir (tek ürün sahnesine duo fiyatı konmaz).
- Beacon Awards logosu (kılavuz: `Products/awards/BeaconAwards-2026-Logo-Guidelines-Winner.pdf`): SADECE resmi mercan+siyah "WINNER" logosu (`Products/awards/Beacon-Awards-2026-Winner-Logo-900px.png`); renk değiştirme/beyazlatma/gölge/kontur/germe YOK; her yanda %25 boşluk; koyu, renkli ya da karışık zeminde logo beyaz "ribbon" kart içinde (üst kenardan sarkan beyaz dikdörtgen); açık zeminde direkt.
- **Ödüller — GÜNCEL (2026-10-05, kaynak: sicksciencelabs.com/pages/home-v2, ürün kartlarındaki `data-awards`; bu liste aşağıdaki 2026-10-02 notunun ÖNÜNE geçer):** ShapeShift = Shop TODAY Mature Beauty Awards 2025 · Cosmopolitan Holy Grail Beauty Awards 2025 · Real Simple Awards 2024 (Best Jawline & Neck Treatment). PowerCycle = Esquire Grooming Awards 2026 · Shop TODAY Hair Awards 2025 · Men’s Health Grooming Awards 2025 · Women’s Health Beauty Awards 2025. DropOff = NewBeauty Awards 2026 · Oprah Beauty O-Wards 2025. NetWork = InStyle Best Beauty Buys 2026 · SheFinds Awards 2026 · Beauty Independent 2026. Site toplamı "14 awards incl. Oprah, InStyle & Esquire". Yayın logoları (Oprah, Esquire vb.) izin/dosya olmadan KULLANILMAZ; ödül adı tipografik rozet olarak yazılır (Beacon hariç, resmi logosu var).
- **Resmi ödül rozetleri (müşteri, 2026-10-17, Drive "SickScience Brand Assets/Awards Badge"):** `Products/awards/badges/` — esquire-grooming-awards-2026 (PC) · mens-health-grooming-awards-2026 (PC) · cosmopolitan-holy-grail-beauty-awards (SS) · real-simple-smart-beauty-awards-2024 (SS) · shop-today-mature-beauty-awards (SS) · oprah-daily-beauty-o-awards (DO). Bu ödüller için tipografik rozet yerine bu resmi rozetler kullanılır; renk/şekil değiştirilmez, ilgili ürünle eşleşir.
- **PR maili kontrolü (2026-10-17):** BOLD PR (Rachel Sachs) yayın haberlerini mailliyor. Başlık başka ürünü anlatıyorsa (ör. Real Simple "Botox in a Bottle… $17" = Eva Naturals, ShapeShift sadece listede) o başlık bizim ürüne MAL EDİLMEZ; makaleyi açıp ürünümüz hakkında ne yazdığını doğrula.
- Ödüller (2026-10-02 doğrulandı, kullanıcı: "ödüller nerden gelmiş kanıtla"): SADECE sitede geçen kullanılır. ShapeShift = "2024 REAL SIMPLE Award Winner - Best Jawline & Neck Treatment" (PDP açıklaması) ✅ · PowerCycle = yalnızca "Award Winner" etiketi (detay yok) · NetWork = **2026 Beacon Awards Winner — Product Launch: Skincare** (Beauty Independent, 01.10.2026: "SickScience Labs took skincare honors for its concentrated serum NetWork"; 130+ aday, 25 uzman jüri; resmi Beacon logosu müşteriden geldi, `Products/awards/`) · DropOff = ödül YOK. Oprah Daily ve Men's Health sitede yok → KULLANMA. Rozet tasarımı sade (ince çerçeveli metin), dolgu renkli/sarı daire rozet yok.
- Başlık 2 satırı geçmez; satır kırılımı elle (\n) verilir, sığmazsa punto küçültülür.

## Kullanıcının Figma düzeltmeleri — BOZMA (2026-10-01)
- Kullanıcı mevcut kreatifleri elle düzeltiyor: format başına ayrı görsel/kırpma (Photo rect'i büyütüp kaydırıyor, Square/Feed'de farklı imageHash), dipnotları alta alıyordu (eski işler; yeni işlerde dipnot yok).
- Var olan frame'lerde Photo boyutu/konumu/dolgusu, metin ve dipnot konumu kullanıcı istemedikçe DEĞİŞTİRİLMEZ; toplu "normalize" script'i çalıştırılmaz. Yeni iş yeni frame'lerde yapılır.

## Ürün içerik serisi başlık stili (kullanıcı, 2026-10-01 — kaynak: Figma 80:58)
- Başlık yok; üstte ürün adı + açıklama. Story: "ShapeShift" Founders Condensed Bold 150 (x138,y272) + sağında magenta (#A921C0) hap "$64" (Medium 34, ls 10%, pad 28/12, r200) + alt satır y417: "30 ML" ve "V-Line Jaw Defining Serum" Regular 40. Feed ×0.8, Square ×0.64 ortalanır.
- Çizgi (rule), "30 ML / $64" iki uçlu spec satırı gibi "çizgili saçma şeyler" YOK.
- Ingredient anlatımı: (1) ürün siluetinde şeffaf kapsül içinde katmanlı bileşenler + yan etiketler, (2) The Ordinary tarzı büyük yakın plan + solda başlık/ince çizgi/açıklama listesi. Referanslar kullanıcı tarafından verildi.

## Ürün bilgisi = SİTEDEKİ METİN, birebir (kullanıcı, 2026-10-01: "niye kafana göre bişeyler ekliyon… adamlar websitesine bütün bilgileri yazmış")
- Ingredients, benefits, istatistik cümleleri, kullanım talimatı ürün sayfasından (`/products/<handle>` HTML'i — products.json'da yok) AYNEN alınır. Ekleme/çıkarma, kendi açıklamanı yazma, INCI listesinden seçme YOK.
- ShapeShift (site): Ingredients = NX35™ Sculpt Technology (Pineapple Exosomes) · Butyrospermum Parkii (Shea) Butter · Caffeine · Niacinamide (Vitamin B3) · Sodium Hyaluronate · Ceramides (bileşen başına açıklama yok). Key Benefits = "Supports the look of a contoured, sculpted neck and jawline" · "Helps visibly tighten and firm the neck" · "Softens, smooths and hydrates". Real Results = 92% saw a more sculpted jawline · 94% saw smoother tech-neck lines · 98% saw firmer, tighter neck skin · 90% noticed improved skin definition ("Chisel Your Jawline in 2 Weeks"). Texture: Gel-Serum. How to use: 1–2 pumps, upward, twice daily.
- **Süre: reklamlarda "2 weeks" DEĞİL "4 weeks" yazılır** (müşteri, 2026-10-21; PDP "2 Weeks" dese bile).
- Bu kural yukarıdaki "-looking ile yumuşat / dozaj yazma" kuralının önüne geçer: sitede yazıyorsa sitedeki ifade kullanılır.

## PR / basın kreatifleri (kullanıcı, 2026-10-01)
- Amaç bilinirlik: haberin paylaşıldığını anlat (gerçek ekran görüntüsünden yırtık kâğıt kupürleri + editör kartı + gerçek before/after kupürleri). Sayfanın birebir kopyası "native editoryal" görseller daha önce perform etmedi (Drive: "Ad that looks like editorial").
- Arka plan AÇIK, ferah, bilimsel (gün ışığında beyaz lab tezgâhı). Koyu/dramatik zemin + gazete kupürü = "cinayet haberi" etkisi → kullanma. Açık zeminde logo 29:219 (Black and Pink), yazılar koyu.
- CNN Underscored ile anlaşma var: logo, haber metni ve ekran görüntüsü kullanılabilir.
- **GÜNCEL PR formatı (kullanıcı, 2026-10-17: "papercut tasarımını sevmiyolar… haberleri öne çıkartmak için yaptıkları tarz"):** yırtık kâğıt kupürü YOK. Müşterinin kendi formatı = Drive "SickScience Brand Assets/Awards & Press" (InStyle örneği): tam sayfa karanlık/moody ürün fotoğrafı, üstte beyaz logo (29:218), ortada köşesiz açık gri-beyaz kart (yayın wordmark'ı · makale başlığı BÜYÜK HARF Bold · özet · "Best New …: **Sick Science Ürün**" altı çizili · yazar + tarih), en altta solda "Read More ⊙", sağda "Source : www.yayın.com" beyaz. Örnek uygulama: Figma 883:881 (Esquire, 17.10).
  - **Son karar (2026-10-17, "haber sayfası ekranı gibi olsun… compakt"):** kart değil, mobil haber sayfası ekranı (Bazaar örnekleri gibi): üstte siyah bar (☰ · beyaz yayın wordmark'ı · arama), beyaz sayfada ortalı başlık → ödül satırı (magenta) → kısa editör alıntısı → yazar/tarih, altında tam genişlik makale görseli. Kompakt, boşluk yok. Figma 883:881.
  - Kart **haberi veriyor gibi, özet** okunur (kullanıcı, 2026-10-17; müşterinin Esquire/InStyle/Bazaar örnekleri): yayın logosu → makale başlığı → ödül/kategori satırı büyük (ör. "Best New Scalp Serum", "Best Tone-Evening Serum") → ürün adı → editörün KENDİ sözlerinden kısa alıntı (birebir; kesilen yer "…") → "By Yazar · Published: tarih". Görsel: ürün/lifestyle ya da B/A (Bazaar: Day 0 / Day 56). Alıntıda ürün sayfasında olmayan iddia (ör. "reactivating dormant follicles") seçilmez.

## Fotografik prompt formatı — ZORUNLU (kullanıcı, 2026-10-02: "fotografik görsellerde promptlarını bu şekilde vericen")
Tüm fotografik Higgsfield prompt'ları **[prompts/TEMPLATE-photographic.md](prompts/TEMPLATE-photographic.md)** bölümleriyle ve sırasıyla yazılır: açılış satırı (element) → kimlik koruma paragrafı → PRODUCT ORIENTATION → COMPOSITION AND FRAMING → SCALE (gerçek cm) → LIGHT AND SHADOW → BACKGROUND → PHOTOGRAPHIC FINISH → Negative listesi. Tek paragraflık eski prompt yapısı kullanılmaz. SCALE için ürün cm ölçüleri kullanıcıdan alınacak.

## Meta native kreatif notları (kullanıcı, 2026-10-02)
- Karikatür (2×2 meme) kreatifler onaylı — DOKUNMA.
- Referansı birebir oku: "i am THIS close" = emoji el + parmak arasına küçük yazıyla mesaj. Ürünü gerçek boyutundan küçük gösteren sahne (parmakla tutulan dev hap) YOK.
- Teklif metni paragraf olmaz: ödül = rozet/hap, fiyat = büyük yeni fiyat + üstü çizili eski + SAVE hapı.
- Story'de ürün 270–1250 px safe band içinde ve büyük olmalı.
- Kullanıcıya ara ekran görüntüsü gönderme; işi bitir, son hali tek seferde göster.

## Rakip uyarlamaları (batch-09, 2026-10-02)
- Meta Ad Library (girişsiz) çalışıyor: `facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q="Marka"&search_type=keyword_exact_phrase&media_type=all` (image filtresi girişsiz boş dönüyor). Görselleri sayfada grid overlay ile toplu incele.
- Higgsfield mention'ı JS ile seç (bkz. prompts/batch-09…); ürün boyu yüzdesi tutmuyor → format kırpımları Python kompozitörle yapılır.
- Vücut önce/sonra (DropOff) Meta politikası açısından riskli; yayın öncesi uyar.

## Tipografi ölçeği — ZORUNLU (kullanıcı, 2026-10-03: "yazı boyutlarında ciddi sıkıntılar var… güzel gözükmesini sağla")
Tüm formatlar 1080 px genişlik; telefonda ~1/3 ölçekte görünür. Bu yüzden puntolar Story/Feed/Square'de AYNI kalır (Square'de küçültme yok, gerekirse metin kısaltılır ya da satır bölünür).
- Başlık (display): 120–170 px (Condensed/X-Condensed daha büyük olabilir), en fazla 2–3 satır.
- İkinci başlık / değer satırı: 56–64 px.
- Gövde metni: 40 px, satır başı ~28–32 karakter, satır aralığı %115–120.
- Etiket, çip, CTA, kaynak satırı, mono alt satır: 32 px. **Hiçbir metin 32 px'in altına inmez.**
- Bir frame'de en fazla 3 boyut + CTA; başlık/gövde oranı en fazla ~4 kat.
- Görsel formatlara SADECE kırpma/büyütme ile dağıtılır (`tools/crop.py`); kenar dolgusu, blur, feather, ayna YASAK (kullanıcı: "kenarlarını bulanıklaştırmışsın… bir daha yapma").
- **Story, Feed ve Square AYNI görseli kullanır — formatlar için ayrı görsel ÜRETİLMEZ** (kullanıcı, 2026-10-08: "dikeyde farklı diğer boyutlarda farklı görsel kullanma demedim mi… tekrar yapma sakın"). Tek 9:16 master üretilir; kırpma yetmiyorsa metin yerleşimi değiştirilir (başlık kısaltılır, logo/etiket yeri değişir), yeni görsel üretilmez. Bu, eski "ayrı oranda yeniden üret" notunun yerine geçer.
- Ürün etiketleri: alt yarıdaki yazı da BEYAZ olmalı; siyah çıkmışsa harfler piksel düzeyinde beyaza çevrilir veya yeniden üretilir. Ürün oranı bozulmaz (germe/sıkıştırma yok).
- **ZORUNLU — ürün üzerindeki TÜM yazılar BEYAZ** (kullanıcı, 2026-10-03: "çıktılara kesinlikle ürünlerin üzerindeki yazılar BEYAZ OLMALI"). Her Higgsfield prompt'una yazılır: "every word printed on the products is pure white on the black stripe — on the coloured cap AND on the silver half; never black, grey or dark text"; negatife "black letters, dark or grey text on the product" eklenir. Çıktı kontrolünde siyah/gri harf varsa görsel kabul edilmez (yeniden üret ya da harfleri beyaza çevir).
- **Yazım: "NetWork"** (büyük N, büyük W). Müşterinin açık pompa PNG'si ve ilk elementler "Network" yazıyordu (2026-10-03 düzeltildi: `Products/png/ERH_7483B.png` etiketi ERH_7477C'den aktarıldı, orijinali `Products/png/orig/`; `Products/sets/ss-set-glp1.png` yeniden kuruldu). `@ss-network` ve `@ss-open-network` elementlerinin görseli+açıklaması Higgsfield UI'dan düzeltildi (2026-10-03); `@ss-set-glp1` düzenlenemedi → yerine `@ss-set-glp1-v2` kullan (`-v2` kopyaları da doğru). Beacon A/B (kullanıcının genişlettiği görseller) yeniden üretilmedi, etiket pikselleri düzeltildi (`_calisma/network-fix/beacon*-fixed.png`). Figma'daki NetWork sahneleri `_calisma/network-fix/` görselleriyle, eski kırpımlar korunarak (ürün hizalı CROP) değiştirildi. Prompt'a: "the label reads exactly 'NetWork' with a capital N and a capital W"

- **Ürün sahneye ENTEGRE görünür, photoshop'la konmuş gibi değil** (kullanıcı, 2026-10-04: "ürün çok photoshopla koyulmuş gibi duruyo"). Her fotografik prompt'ta PHOTOGRAPHIC FINISH'ten sonra INTEGRATION bölümü: aynı ışık yönü/yumuşaklık/renk sıcaklığı, kromda ortamın gerçek yansımaları (stüdyo yansıması değil), gerçek temas gölgesi + zeminde hafif yansıma, sahneyle aynı netlik/grain, kontur/hale yok. Negatife: pasted/composited look, cut-out edges, sticker look, halo, product lit differently, floating product. Örnek: `prompts/batch-13-build.py`.

## Ekim 2026 kampanyası — NetWork × BCRF (kullanıcı, 2026-10-03)
- Breast Cancer Awareness Month: Ekim boyunca **SickScienceLabs.com**'daki NetWork satışlarının %20'si The Breast Cancer Research Foundation'a bağışlanıyor (müşteri metni `prompts/batch-11-bcrf.md`).
- Reklamda "on SickScienceLabs.com" ve tam kurum adı korunur; BCRF logosu onay gelmeden kullanılmaz; "cure" ve tıbbi iddia yok.
- **Sahne mantığı tutarlı olmalı** (kullanıcı, 2026-10-04: "xray görüntüsünde kadın kendini muayene edemez… makineye giriyo zaten baktırmak için, akıl var mantık var"): tarama/röntgen/mamografi sahnesinde elle muayene pozu YOK; elle muayene = ev/banyo/set sahnesi. Konsepti üretmeden önce "bu durum gerçekte böyle olur mu" kontrolü yap.

## Ulta Beauty (perakende partneri) — 2026-10-08
- Kaynaklar: `Ulta/Uniquely-Ulta-Brand-Partner-Playbook-Q3-2026.pdf`, `Ulta/FY26-Holiday-BrandSocialContentGuidelines.pdf`, konsept notu `prompts/batch-23-ulta-concepts.md`. Palet: Orange #E35200, holiday Magenta #E90B5A; her görselde/caption'da @ultabeauty + #UltaBeauty; "Only at Ulta Beauty".
- **Ulta logosu = RESMİ logo** (kullanıcı, 2026-10-08: "kafana göre ulta yazmışsın… adamların kendi logosu var"). Tercih: çanta prompt'ta YAZISIZ istenir ("completely plain front panel, no text"), logo `NOCLEAN=1 tools/ulta_logo_swap.py` ile temiz yüzeye basılır. Model yine de yazı çizerse yazı kutusu satır-interpolasyonla doldurulur, kulp orijinalden geri konur, sonra logo basılır (inpaint tek başına kulp kenarında beyaz saçak bırakıyor — kullanıcı 2026-10-08 "logo olan yerler hatalı") (`Ulta/logo/ulta_logo_white.svg|png`, ulta.com header SVG'sinden). Genel kural: partner/perakendeci markası görselde geçiyorsa model çizimi yazı değil, resmi logo.
- Çanta sahnelerinde ürün çantanın YANINDA durur (FOOH dahil: kapsül çantadan çıkmaz). Model ürünü çantaya göre büyük çizmeye çok meyilli; doğru ölçekli görsel bulunca formatlar ondan kırpılır.
- Ulta'da 4 SKU var (gua sha ve setler YOK). Tatil indirimi henüz onaylı değil; Eylül Ulta etkinlikleri %50 → Figma'da %50 fiyatlar "CONFIRM with Ulta" notuyla.
- (2026-10-22 güncelleme: Unlimited artık hesap genelinde aynı anda 1 iş işliyor, diğerleri sırada bekliyor; yine 4 adede kadar sıraya at, ama süreyi buna göre planla.) **Higgsfield Unlimited aynı anda 4 üretim alır — tek tek bekleme YOK** (kullanıcı, 2026-10-19: "niye tek tek üretiyon… tek seferde 4 farklı unlimited üretim yapabiliyon"). Bir seride 4'e kadar prompt'u arka arkaya gönder, bitenlerin yerine yenisini koy. (Eski "tek üretim" notu geçersiz.)

## Müşteri stüdyo çekimleri önce (kullanıcı, 2026-10-23)
- Yeni işlerde önce `SickScience Brand Assets/Images/All Products - New Image` (137 jpg, yerelde) ve `All Products - Old Image` (49 büyük dosya, yalnızca bulutta; gerektikçe indirilir) klasörlerine bakılır; uygun kare varsa Higgsfield'da üretim yapılmaz.
- Dosya aralıklarına göre katalog: memory `reference-client-product-photos.md`.
- Kare sayfası: `~/sickscience-work/client-photos/new_sheet.jpg`.
- **Yön: bilimsel içerikli görseller daha çok kullanılır** (kullanıcı, 2026-10-27). Hem fotoğraf seçerken hem yeni görsel üretirken bu fikir göz önünde tutulur. Örnekler:
  - laboratuvar sehpası S_1133–1143 (Vault üçlüsü)
  - Old Image SS0880 (ShapeShift + ananaslı beher), SS0547
- Bu bir **tercih, kural değil**. "Sadece bu iki klasör" ya da "elde tutulan kare telefon çekimi olmalı" diye bir kural yoktur. Uygun her müşteri fotoğrafı kullanılabilir: UGC, lifestyle, Ulta video kareleri.
- **Ön kamera videolarından alınan kareler aynalı çıkar:** yatay çevrilir, etiket okunarak kontrol edilir.
- **Bir seride her kreatif ayrı fotoğraf kullanır** (kullanıcı, 2026-10-25: "hep aynı fotoğrafı kullanma"). Ürünle alakasız prop olmaz (PowerCycle + balkabağı reddedildi).
- **Yazı hizası referansınkiyle aynıdır** (Prequel referansları = ortalı; kullanıcı, 2026-10-27). Ürüne binmesin diye yazı sağ/sol kolona itilmez; fotoğraf ya da kırpım değiştirilir.
- Site metinlerinin birebir kopyası (About, NX35, DropOff ve NetWork Key Benefits): memory `sickscience-site-copy-snippets.md`.
- Dekupe aracı (Vision): `tools/vision-lift.md`.

## Video üretim kapıları — ZORUNLU (kullanıcı, 2026-10-21: "boktan videolar yapma, adamlar her şeyi anlatmış")
Her videoda sırasıyla şunlar yapılır:
1. Proje klasörüne brief.md (tek cümle mesaj, gerçek asset listesi, kaçınılacaklar)
2. Referanstan style-guide (renk hex, font, tempo, hareket)
3. Shot list (HOOK / PROBLEM / REVEAL / PROOF / CLOSE; her beat için giriş/çıkış durumu ve gerekçe)
4. Önce müzik grid, SFX aynı zaman çizelgesinde
5. Contact sheet + 0.2 sn şeritler
6. En kötü 3 hata bulunur, sadece o bölümler düzeltilip yeniden render edilir
7. Sesli tam izleme, -14 LUFS
Kontrol listesi: `~/lemo-opuscar/DIRECTOR.md` §10–11.
- **Görünüm, ses ve yerleşim (kullanıcı, 2026-10-21):** "daha temiz, beyaz arkaplanlı, bilimsel, çok abartmadan".
  - Ses efekti az: sessiz tik, bir çizgi sesi, bir ding.
  - Ürünler ve SHOP NOW alt %35'e inebilir; sadece kritik metin 270–1250 bandında kalır.
  - Kutu ya da çerçeve içine alma yok, tam arka plan.
  - Geri sayım ilk kareden büyük, 00:59'dan sayar. Kodla animasyon için `lemo-opuscar` skill (kurulu). "Ortada büyük yazı + gradient + her şey fade + sonda logo" kalıbı YASAK.

## Klasör düzeni (kullanıcı, 2026-10-12)
- `Video/<YYYY-MM Ay>/` (2026-10-13 itibarıyla klasör adı `Teslim` → `Video` oldu) = müşterinin gördüğü tek yer, SADECE bitmiş videolar (statikleri müşteri Figma'dan kendisi export ediyor). Alt klasörler: `01 UGC` · `02 Basın & Podcast` · `03 Animasyon` · `04 Ulta`.
- Dosya adı: `Ürün – Konsept – Format.mp4` (ör. `ShapeShift – Soru kutusunu yakma – 9x16.mp4`). Sadece son onaylı versiyon; script, json, ham klip, deneme, prompt KONMAZ.
- Çalışma dosyaları `_calisma/` (eski `output/`): batch klasörleri, render script'leri, klipler. Yeni video bitince final mp4 ilgili ayın `Video/` klasörüne isimlendirilerek kopyalanır.
- **Git (2026-10-12):** this Drive folder is the working copy of `github.com/ufukkyavuz/sickscience` (branch `claude/agency-rules-and-knowledge`). `.gitignore` whitelist: only md/py/js/html/txt; media stays on Drive. `kurallar/` = copy of Claude's project memory, `sessions/` = monthly session summaries.
  - "Pushla" means:
    1. Copy the memory into `kurallar/`.
    2. Update the session summary.
    3. `git add -A && git commit && git push`.
  - Also run `_claude-setup/sync.sh push`.

## Amazon Store (2026-10-19)
- Müşteri mevcut Amazon mağazasından memnun değil (mor balonlu genel AI görünüm). Yeni ana sayfa taslağı: Figma sayfa "06 · Amazon Store" — Hero 3000×600 · Ödüller · 4 ürün kartı 1500×1500 · Kurucular · NX35 · Shop by concern. Görseller `~/sickscience-work/amazon/make_assets.py`.
- **v2 (kullanıcı, 2026-10-20: "daha cam bilim ve beyaz arkaplan temalı")**: renkli karakter fonları bırakıldı → beyaz lab tezgâhı + şeffaf cam ekipman (beher, erlen, petri, pipet) + jel-serum boncukları; kartlar 1:1 ürün sağda/yazı solda, istatistik ürün renginde. Prompt'lar `prompts/batch-56-amazon-glass.py`. Hero 5:1'e dik ürün sığmıyor (Nano Banana zoom-out'u reddediyor) → hero tipografik beyaz, ürün ailesi hemen altında 3000×1273 lab modülünde.
- **v3 (2026-10-20):** NX35 modülü = yazı bandı + tam genişlik lab sahnesi (ananas/turp-salatalık/sarımsak/buğday petri kaplarında, `gen56/nx1`). Shop by concern = 4 dikey kart 750×1500 (üst foto 750×1100, alt beyaz panel yazı). Satışa yönlendiren Amazon ASIN modülleri mock'landı: "Best Sellers" grid (The Line'ın altında) + "Featured product" (ShapeShift, kartların altında); fiyat/puan Amazon'da ASIN'den otomatik dolar, "#1 Best Seller" yazılmaz (Amazon rozeti).
- **Batch-47 karakter serisi (renkli/beyaz) genel işlerde KULLANILMAZ** (kullanıcı, 2026-10-20: o seri belirli bir hedef kitle kampanyası içindi). Modelli görsel gerekirse önce müşterinin orijinalleri: Drive `SickScience Brand Assets/Images/<Ürün>/` (SS `ShapeShift/1.jpg`, NW `NetWork/network-cmnq3cltf…jpeg`, PC `PowerCycle/PowerCycle-cmneo9oyi…jpeg`, DO `DropOff/cgidropoff1.jpg`). NetWork havlulu karede etiket eski "Network" yazımlı → kullanma.
- **v4 (2026-10-20) — Figma dosyası taşındı: `figma.com/design/VS800zq8OqVWN7OlpctFQf/SickScience-Amazon` (node id'ler aynı).** Hero = 5:1 kırpılmış ürünsüz cam/lab arka planı + ortalı yazı (cam kesilebilir, ürün kesilemez). NX35 = açık lila zemin + 3 kart (petri kabında ananas / turp-salatalık / sarımsak-buğday). Konu kartları = "mercek" serisi v2: büyük çerçevesiz cam mercek bedenden uzakta ince şeffaf kolla asılı, kimse tutmuyor, ciltte ışık halkası (kullanıcı: "uzaktan tutulmalı… daha artistik… kendi tutmasın"); v1 (elde saplı büyüteç) reddedildi. Ürün grid başlığı "FIND YOUR FORMULA" (4 ürün varken "Best Sellers" mantıksız). Featured product = solda lab görseli, sağda lila panel + ürün ödül rozetleri. Prompt'lar `prompts/batch-57-amazon-lens.py`.
- **v5 (2026-10-20):** Hero = neredeyse boş lab (solda tek erlen, sağda tek beher, ortası boş). What's inside = 4 kolon, ilk versiyon görselleri (ürünlü lab kareleri) + sitedeki "Key actives" listesi birebir (kullanıcı: "ilk yaptığın en iyisiydi"; flat-lay petri versiyonu reddedildi). Konu kartları = büyüteç efekti (referans: DUMAIN gözlük): çerçevesiz cam, ortada, içi keskin ve büyük, dışı bulanık, beyaz stüdyo. Nano Banana tek karede gerçek optik büyütme ÜRETEMİYOR (içi/dışı aynı ölçek çıkıyor) → v4 stüdyo karesi + `_calisma/amazon-store/lensfx.py` (dış blur, iç 1.5–2.2x zoom, ince cam halka). Glow kartında zoom ≤1.5 (gözenek öne çıkmasın). **Son karar (kullanıcı, 2026-10-20: "son üretilenler daha güzel"):** ~~ham v5 mercek kareleri~~ → **son karar (kullanıcı: "direkt yakın çekim yapalım merceği siktir et"):** mercek YOK; beyaz stüdyo yakın çekimler (çene profili, yanak glow, saç ayrımı, dış bacak) — `prompts/batch-59-closeups.py`.
- Amazon kuralları: hero'da önemli içerik ortadaki 2100 px'te (yanlardan %16 kırpılır, mobilde logo solun %18'ini kapatır → hero metni ortalı); ödül iddiası tarih + kurum + <18 ay (Real Simple 2024 KULLANILMAZ); yüzde/anket iddiaları Amazon PDP'sinde de yazmalı; rakip karşılaştırması yok.
- **v6 (2026-10-20):**
  - **What's inside = "formül" görselleri** (kullanıcı: "formül gibi bilimsel göster… her şeyi anlatma"): ürün renginde kapaklı şeffaf cam kapsül/tüp, içinde gerçek ham bileşen katmanları; Figma'da ince çizgi + nokta ile 4–5 kısa etiket (sitedeki bileşen adları birebir) + altta sadece ürün adı. Kart/liste/paketshot YOK. Prompt'lar `prompts/batch-61-inside-formula.py`.
  - **Featured product** = travertin + lila duvar still life (`prompts/batch-60-amazon-featured.py` B).
  - **Konu kartları:** foto tüm kartı kaplar, alt beyaz gradient üstünde yazı.
  - **v6b (kullanıcı, 2026-10-20: "aşırı karışık… daha premium… kesik görsel sevmiyorum"):**
    - Formül kapsülleri kutulu fotoğraf değil, macOS Vision ile dekupe PNG (`/private/tmp/claude-501/lift/lift.swift`, çıktılar `~/sickscience-work/amazon/gen61/*_trim.png`).
    - Hepsi aynı zemin çizgisinde, yumuşak gölge, açık gradient zemin.
    - Altta sadece ürün adı + NX35 teknolojisi; etiket/çizgi YOK.
    - **Genel kural:** web/Amazon modüllerinde de foto kutusu/kesik kart yerine dekupe ürün veya tam genişlik sahne.
- **v7 (kullanıcı, 2026-10-20: "takke gibi kapağımız var mı… X-ray'de görünümü"):** formül kapsülü (ayrı kapaklı cam şişe) REDDEDİLDİ — ürün formu her zaman gerçek elementten gelir (üst yarı renkli, alt yarı gümüş; DropOff tüp).
  - What's inside = tam genişlik 21:9 sahne: ürünler sağda, solda yazı. A = açık zemin X-ray (ürün silüetleri içinde bileşen gölgeleri); B = see-through (gerçek form camlaşmış, içerikler görünür).
  - Prompt'lar `prompts/batch-62-inside-xray.py` (4 element mention: ss-shapeshift, ss-network-v2, ss-powercycle, ss-dropoff).
  - Koyu X-ray elendi: ölçü çizgisi + "12cm" yazısı çizdi ve arka planda dikiş vardı → SCALE'deki cm'leri model annotasyon olarak çizebilir, X-ray/diyagram prompt'larına "no dimension lines, no numbers" ekle.
  - Composer: mention'ı JS `__pick` ile seçmek yanlış elementi (otg/open) seçti → mention'lar find+ref click ile seçilir, gönderimden önce reference_elements kontrol edilir.
- **v8 (kullanıcı, 2026-10-20: koyu X-ray "daha mantıklı ama daha casual… yazılar olmasın… tam xray"; referans AKANOMA çanta röntgeni):** What's inside = gerçek röntgen dili, ürün üstünde yazı/ölçü YOK.
  - A (910:904) = beyaz zeminde mavi tek renk tote çanta röntgeni: 4 ürün + gözlük, telefon, anahtar, kulaklık, para, çelik gua sha (`prompts/batch-64-xray-bag.py`, mention: ss-tote + 4 ürün).
  - B (2029:11) = koyu film, ürünler masaya gelişigüzel atılmış (`prompts/batch-63-xray-casual.py`).
  - Pouch varyantı 5. kapsül çizdi → elendi.
  - Composer ipucu: mention'lar find+ref click; prompt metni JS `execCommand('insertText')` + shift+Enter KeyboardEvent ile yazılır; gönderimden önce show_generations ile reference_elements kontrol edilir. Composer'a tıklarken koordinatı JS rect'ten hesapla (yanlış tıklama görsel görüntüleyiciyi/"Publish project" penceresini açıyor).

## Basın logoları (kullanıcı, 2026-10-20: "adamların logosunu falan kullan")
- PR/basın kreatiflerinde yayının resmi logosu kullanılır (kullanıcı onayı). Kaynak = yayının kendi site header SVG'si, ör. Oprah Daily `Products/press-logos/oprahdaily-logo{,-black,-white}.svg` (oprahdaily.com header). Logo yeniden çizilmez/yazıyla taklit edilmez.
- Oprah Daily NetWork BCAM kreatifi: Figma PHPZ7XLpEVMcUVVEcNTwmz, "Ekim 2026" sayfası, 941:881.
  - Gerçek makale sayfası UI'ı: siyah header + beyaz logo + pembe SUBSCRIBE; BEAUTY kicker, başlık, editör alıntısı, tarih.
  - Haberdeki ürün kartı birebir: "2" kutusu, "20% OF OCTOBER SALES GOES TO BCRF" pembe etiket, ürün adı, SICKSCIENCELABS.COM butonu.
  - Story'de kart dikey, Feed/Square'de yan yana; görsel `batch-11-bcrf/bc_ribbon_sq.png` (her formatta aynı).
