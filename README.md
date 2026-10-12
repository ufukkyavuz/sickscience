# SickScience Labs — Ajans çalışma deposu

SickScience Labs için yürüttüğümüz marka, strateji ve reklam işlerinin kuralları ve bilgi tabanı.
Bu depo Google Drive'daki `SickScience` klasörünün **metin kısmının** birebir aynısıdır:
- Klasörün kendisi git deposudur.
- Görseller, videolar ve PDF'ler `.gitignore` ile dışarıda tutulur ve Drive'da kalır.

## Klasörler

| Yol | Ne var | Depoda mı? |
|---|---|---|
| [`CLAUDE.md`](CLAUDE.md) | Üretim ve tasarım kurallarının tamamı: Higgsfield elementleri, prompt formatı, ürün ölçüleri/dokuları, model ve set, tipografi, Meta safe zone, reklam metni, BCRF, Ulta, klasör düzeni. **Yeni kural eskisiyle çelişirse tarihi yeni olan geçerlidir.** | ✓ |
| [`SICKSCIENCE-BRAND-BOOK.md`](SICKSCIENCE-BRAND-BOOK.md) | Ürünler, setler, fiyatlar, iddialar, görsel kimlik, rakipler | ✓ |
| [`AGENCY-RECOMMENDATIONS.md`](AGENCY-RECOMMENDATIONS.md) | Konumlandırma, kampanya takvimi, büyüme kaldıraçları | ✓ |
| [`kurallar/`](kurallar/) | Çalışırken öğrenilen kullanıcı tercihleri (Claude'un proje hafızası, `MEMORY.md` = dizin) | ✓ |
| [`sessions/`](sessions/) | Ay ay oturum özetleri: ne yapıldı, ne beğenildi, ne beğenilmedi | ✓ |
| [`prompts/`](prompts/) | `TEMPLATE-photographic.md` ve her batch'in prompt kayıtları + kararları (batch-01 … batch-40) | ✓ |
| [`tools/`](tools/) | `crop`, `compose`, `label_fix` (bozuk kapsül yazısını düzeltir), `cutout` (ürün keser), `ulta_logo_swap`, Higgsfield yardımcıları | ✓ |
| [`strateji/`](strateji/) | 360° büyüme planı, Higgsfield props listesi | ✓ |
| `_calisma/` | Batch klasörleri, ham klipler, ara görseller | sadece `*.py` render/müzik script'leri |
| `Teslim/<YYYY-MM Ay>/` | Müşteriye giden bitmiş videolar (01 UGC · 02 Basın & Podcast · 03 Animasyon · 04 Ulta) | ✗ (Drive) |
| `Products/`, `Ulta/` | Ürün PNG'leri, ödül logoları, Ulta kılavuzları | ✗ (Drive) |

## En önemli kurallar (özet; tamamı CLAUDE.md'de)

1. **Ürün bilgisi = sitedeki metin, birebir.** Kendi açıklama yazılmaz. Dipnot ve yıldız yok.
2. **Görseller yazısız üretilir.** Metin Figma'da Founders Grotesk ile yazılır: condensed kesim yok, en küçük punto 32 px.
3. **Görsel üretimi:** Higgsfield web arayüzü, Nano Banana Pro, 2K, **Unlimited**, adet 1/4. MCP ile kredi harcanmaz.
   - Sonuçlar MCP `rawUrl` üzerinden doğrudan Figma'ya aktarılır, tarayıcıdan indirilmez.
4. **Prompt'lar** `prompts/TEMPLATE-photographic.md` bölümleriyle yazılır. SCALE bölümünde gerçek cm ölçüleri, INTEGRATION bölümü ve negatif liste zorunlu.
5. **Ürün:**
   - Kapsül ince ve uzun (boy/çap 3.4, PowerCycle 3.1).
   - Ürün üzerindeki tüm yazılar beyaz; yazım "NetWork".
   - İçerik yarı şeffaf jel-serum.
   - Gua sha paslanmaz çelik ve her zaman ayrı element (`@ss-guasha`) olarak verilir.
   - Ürün kameraya yaklaştırılıp büyütülmez.
6. **İnsanlı kareler:**
   - Modeller 20'lerinin sonunda, güzel; cilt gerçekçi.
   - Stüdyoda kurulmuş set (plato banyosu), 35 mm geniş açı.
   - Görselde tam iki kol/el olduğu kontrol edilir.
7. **Formatlar:** Story, Feed ve Square tek bir 9:16 master'dan kırpılır. Formatlar için ayrı görsel üretilmez; kenar dolgusu ya da blur yok.
8. **Organik Instagram:**
   - Beyaz, premium, fotoğrafta görsel metafor.
   - Metin grafik tasarımın parçası olur, fotoğrafın üstüne düz yazı konmaz.
   - İşaretleme her görselde farklı olur.
9. **Video:**
   - En fazla 20 sn. Kling 3.0 ile, kredili; önce onay alınır.
   - Kapanış: stat + logo + SickScienceLabs.com. Yorum ("Comment X") CTA'sı kullanılmaz.
10. **Teslim:** sadece bitmiş videolar `Teslim/<YYYY-MM Ay>/` klasörüne, `Ürün – Konsept – Format.mp4` adıyla konur. Statikleri müşteri Figma'dan kendisi export eder.

## Araçlar

- **Figma:** dosya `PHPZ7XLpEVMcUVVEcNTwmz`. Sayfalar: "02 · Reklam Kreatifleri", "Ekim 2026 İG", "Ekim 2026 · İndirim Statikleri".
- **Higgsfield:** proje `higgsfield.ai/generate/@residential_walrus_super/sickscience`.
- **Render:** `~/motion-tools`, müzik için mgaudio (-14 LUFS).
- **Claude kurulumu:** başka bir Mac'te `Drive'ım/_claude-setup/sync.sh pull` çalıştırılır.
