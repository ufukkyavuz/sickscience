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
