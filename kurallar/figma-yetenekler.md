# Figma MCP — yetenek haritası (2026-10-12, canlı test edildi)

Dosya: `PHPZ7XLpEVMcUVVEcNTwmz` · Hesap: Ufuk Yavuz · Planlar: "Projects" (pro, Full seat, `team::1246029916185874651`), "UFO" (starter, View seat). Figma AI açık.

## Dosyanın durumu
- Sayfalar: `7:3` Ekim 2026 (24 üst düzey frame/section, ~1500 frame, ~3350 text, 553 instance) · `7:7` 99 · Assets (ürün PNG frame'leri, logolar, `Component 1` logo seti 29:223, CTA bileşeni 21:7).
- Değişkenler: `SickScience / Color` (12 renk; signal/01–04 ürün renkleri, neutral/*, accent/chrome, accent/clinical).
- Text style: sadece `SS Ads / CTA`, **Inter Semi Bold 28**. Founders kuralına aykırı, 32 px altında. Paint/effect style yok.
- Fontlar: Founders Grotesk'in tüm kesimleri yükleniyor (Regular…Bold, Text *, Condensed *, X-Condensed *; Condensed kullanılmaz). Permanent Marker da var.

## Çalışan araçlar
| Araç | Ne işe yarar | Not |
|---|---|---|
| `use_figma` | Plugin API ile JS: frame, text, auto-layout, grid layout, component/variant, variable, style, maske, boolean, vektör, text-on-path, export | Ana araç. Kod en fazla 50k karakter. Sayfa başına tek `setCurrentPageAsync`. `figma.notify` ve `createImageAsync` yok. |
| `get_screenshot` / `node.screenshot()` | Görsel kontrol | `maxDimension` ile detay |
| `get_metadata` | XML ağaç: id, boyut, konum | Sayfa listesi için nodeId'siz |
| `download_assets` | Node render'ı PNG/JPG/SVG/PDF (scale ≤4) + kaynak görseller | Toplu export'u buradan almak mümkün |
| `upload_assets` | PNG/JPG/WebP/GIF/SVG'yi dosyaya yükler, istenen node'a fill olarak basar (60 adet/çağrı) | Bulutta Drive medyası yok; Mac'te yerel dosyalarla çalışır |
| `export_video` | Figma Motion timeline'ını MP4'e render eder | Üst düzey frame verilir, iş kuyruğa girer ve jobId ile sorgulanır |
| Motion API | Keyframe (translate, rotate, scale, opacity, width/height, renk, efekt), hazır stiller: **TextStagger**, Position, Scale, Rotation, Size, Opacity, Path | Test edildi, açık. Statikleri animasyonlu Story'ye çevirmek için kullanılabilir. |
| Efektler | GLASS, NOISE (blendMode anahtarı yok), TEXTURE, progressive LAYER_BLUR, drop/inner shadow | Test edildi |
| Shader | Kullanıcının kendi shader'ları uygulanabiliyor: `figma.listAvailableShaders()` → `importShaderById(id)` → `fills/effects = [{type:'SHADER', id}]` | Figma'nın hazır shader'ları (Halftone, Bloom, Mesh gradient…) plugin runtime'da **listelenmiyor**. Kullanmak için `create_shader` ile kendi kopyamızı yazmak gerekiyor. Mevcut kendi shader'larımız: Color invert, Balloon glossy, Wave fill. |
| `create_shader` / `update_shader` | WGSL ile özel efekt/dolgu (ör. krom yansıma, holografik tote parıltısı, grain) | Hesap kütüphanesine kaydolur |
| `create_generative_plugin` | Arayüzlü, tekrar kullanılabilir plugin | Mevcut: "Resize to social sizes" (`15eaab35…`) |
| `search_design_system`, `get_libraries` | Kütüphane bileşen/variable arama | Kütüphane yok, hepsi yerel |
| `generate_image` (Figma AI) | Metinden görsel; modeller gemini-3.1-flash(-lite)-image, gpt-image-2.5 | **Ücretli (Figma AI kredisi)**. Ürün doğruluğu için uygun değil, element referansı yok. |
| Weave (`weave_find_model`/`run_model`) | Nano Banana Pro edit (14 referans görsel, 4K, 9:16), Veo vb. | **Ücretli (~11 kredi/görsel)**, her çalıştırma için kullanıcı onayı gerekir. Higgsfield Unlimited kuralı geçerli olduğu için varsayılan olarak kullanılmaz. |
| `generate_diagram` | FigJam akış/gantt şeması | Kampanya takvimi için kullanılabilir |

## SickScience için pratik kullanım
1. **Format üretimi:** Story master → Feed 4:5 + Square, aynı Photo ile, CROP imageTransform. Script veya plugin ile yapılır; kurallara göre ayrı görsel üretilmez.
2. **Toplu kopya/fiyat değişimi:** `query('TEXT[name*=price]')`. BFCM'de fiyatlar tek script'le güncellenir; mevcut düzeltilmiş frame'lerin konumuna dokunulmaz.
3. **Animasyonlu statik:** TextStagger ile başlık girişi + ürün scale-in, `export_video` ile 6–8 sn MP4. Kısa Story/Reels varyantı üretmenin ucuz yolu.
4. **Design system temizliği:** Founders text style'ları kurulur (Display 120–170 / Sub 56–64 / Body 40 / Label 32). Renk variable'ları bağlanır, CTA bileşeni Founders'a çekilir.
5. **Kalite denetimi script'i:** 32 px altı metin, Founders dışı font, "Network" yazımı, safe zone ihlali (Story'de y<270 veya y>1250 metin) için otomatik rapor.
6. **Özel shader:** krom/holografik parıltı, film grain. Sadece Figma'da çizilen grafiklerde kullanılır, ürün fotoğrafına uygulanmaz.

## 2026-10-25 güncellemesi — INO'da test edildi, burada da geçerli
Kaynak (tam not): INO memory `reference_figma_new_features.md` ve `feedback_figma_plugin_api_gotchas.md`. Yol: `~/Library/CloudStorage/GoogleDrive-ufukkyavuz51@gmail.com/Drive'ım/INO Claude Ads/claude/memory/`. Kullanıcıya tekrar anlattırma; önce oraya bak.

**Expand image (Figma AI, AI kredisi harcar)**
- Plugin API'de ve MCP'de yok. Masaüstü uygulamasında computer-use ile yapılır (`com.figma.Desktop`):
  1. Layers panelinde görsel katmanını seç.
  2. Görselin üstündeki araç çubuğunda **More** → **Expand**.
  3. Oran menüsünden Portrait 9:16 ya da 4:5 / 1:1 seç, ✓ ile onayla.
- Sade/seamless fonu ~20 sn'de genişletir, ürünlere dokunmaz.
- Asıl kullanımı dikey görseli 1:1 ve 4:5'e yanlara genişletmek (Higgsfield zoom-out yerine). Ürün kenarlarını yine de kontrol et.
- Ürün çok yukarıda kalırsa: fotoğrafı 9:16 içinde %70, alta yaslı CROP fill yap, sonra Expand ile boşluğu doldur.
- Masaüstü görünümü `use_figma` ile değişmez; Pages listesinden gezinilir.

**Shader**
- Sadece dosyadaki ya da kullanıcının KENDİ shader'ları uygulanabiliyor. Figma'nın hazır shader'ları id ile gelmiyor: kaynağı `get_shader includeSource` ile okunur, `create_shader` ile kopyası yazılır (`team::1246029916185874651`).
- Kendi shader'larımız (INO'da yapıldı, hesap kütüphanesinde): **INO Glint** (`4591c82d-bd2c-4d02-bb04-930ee7e8f32f`) — parlak alanlarda çapraz ışık süpürmesi. Sade ayar: intensity 0.55, threshold 0.62, width 0.07, softness 0.95; daha güçlüsü yüzü patlatıyor. Krom kapsül parıltısı için aday. Ayrıca INO Smear (`dacb992e…`) ve INO Pixel stretch (`b6fc3d3e…`; metinde işe yaramıyor).
- Uygulama: `node.effects=[{type:'SHADER',id,visible:true,properties:{<propertyDefinitionId>:value}}]`. Anahtarlar tanım id'si, isim değil.

**Motion — çalışanlar**
- Hazır stiller: TextStagger, Position, Scale, Rotation, Size, Opacity, Path. Özel stil: `createCustomAnimationStyle()` + `addAnimationEntryAsync`.
- ⚠ Figma preset'lerinde başlangıç zamanı = `props.delay` (saniye). `timelineOffset` sessizce 0 olarak kaydediliyor. Düzeltme: `n.animationStyles = n.animationStyles.map(s => ({...s, props: {...s.props, delay: T}}))`. Özel stiller `timelineOffset`'i tutar.
- ⚠ 'in' stagger metni offset'ten önce dinlenme halinde gösterir. Sadece 'in' kullan; görünürlüğü katman OPACITY izi (0→1, başta HOLD) ile aç; çıkışları OPACITY + TRANSLATION keyframe ile yap.
- Geçişler:
  - Wipe: kırpan frame WIDTH 1→1080.
  - Iris: 2200² frame, radius 1100, SCALE_XY 0.001→1.
  - Panel morph: CORNER_RADIUS + SCALE_XY.
- Kamera: sahneler yan yana "world" frame'de; TRANSLATION_X + LAYER_BLUR RADIUS sıçraması ile hareket bulanıklığı.
- Path draw: SVG stroke → VECTOR'da PATH_TRIM_END 0→1. Çizilen halka ya da fiyat üstü çizgisi için.
- Mask reveal: clipsContent frame içinde metin, TRANSLATION_Y. Harf içinde foto: mask text + foto TRANSLATION_Y.
- STACK_SPACING keyframe ile harf aralığı daraltma.
- Logo renk dönüşü: `manualKeyframeTracks.fills` ile.
- Efekt keyframe'i: `{type:'INDEXED_ITEM', collection:'effects', index, field:'RADIUS'}` ya da shader için `propertyId`; üst düzey frame'de değil, ÇOCUK katmanda.
- Efektler: progressive blur, NOISE MONOTONE (blendMode verme), GLASS.
- Yok: 3D z-rotation, Lottie export, wiggle/expression. Video fill API ile konamaz, masaüstünden sürüklenir.
- Ses: frame'e masaüstünden eklenir (sağ panel Audio +, computer-use); plugin API ekleyemez.

**Export**
- MCP `export_video` TextStagger'ı ve shader'ları RENDER ETMİYOR.
- Masaüstü Export → Animated → MP4 hepsini render ediyor. Akış:
  1. Frame'i kanvastaki başlık etiketine tıklayarak seç; kanvasta Tab da üst frame'i seçer.
  2. Sağ panelde "Export <frame>".
  3. Video Export sekmesinde Download.
- Metin girişlerini 20 fps kare çıkararak doğrula.

**Plugin API tuzakları**
- Auto-layout çocuğunda `.x/.y` sessizce yok sayılır; sırayı `insertChild` ile değiştir.
- `upload_assets` + `nodeId` bazen success döner ama fill değişmez. Hash'i geri okuyarak doğrula; olmazsa nodeId'siz yükle, hash'i ata, geçici node'u sil.
- Düzenlemeden hemen sonra screenshot eski render dönebilir; `use_figma` ile özelliği okuyarak doğrula.
