<!-- LANGS:tr -->
> Turkish. [English](../README.md)

# Content Flywheel — SEO ve GEO İçerik Becerileri

**AI ajanları için açık bir içerik üretim metodolojisi.** Bir konu araştırın, en güçlü akıl yürütme modeliyle planlayın, taslağını yazın, yapay zeka izlerini temizleyin, bir GEO/SEO kalite kontrolünden geçirin, sosyal medyaya yayın, yayımlayın ve analizleri bir sonraki döngüye geri besleyin — Claude Code, Cursor, Codex CLI, Gemini CLI ve Markdown becerileri yükleyen herhangi bir ajan için yeniden kullanılabilir bir beceri olarak.

> Klasik SEO'nun üzerine inşa edilmiş **Generative Engine Optimization (GEO)** için tasarlandı — AI arama motorlarının (ChatGPT, Perplexity, Google AI Overviews) gerçekten alıntıladığı içerik.

🌐 **Diller:** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## Flywheel (Atalı Çark)

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| Aşama | Ne olur | En uygun ajan rolü |
|-------|--------------|---------------------|
| **1. Araştırma** | Trendler, SERP amacı, rakip boşlukları, hedef kitle ihtiyaçları | bir araştırma/temellendirme modeli |
| **2a. Plan** | Taslak yapı (H2/H3), tez, dahili bağlantı planı, CTA, yapılandırılmış veri planı | **en güçlü akıl yürütme modeli** |
| **2b. Taslak** | Plana göre yazılmış tam metin | hızlı bir taslak yazma modeli |
| **2c. De-AI** | Dolgu, genel kalıp ifadeler, "yapay zeka izleri" temizlenir | hızlı bir düzenleme modeli |
| **2d. Kalite kontrolü** | Taslağı **CORE-EEAT** + **GEO** kurallarına göre puanla; boşlukları listele | bir inceleme modeli |
| **3–4. Yayma (Fan-out)** | Platform metnine böl (FB/IG/Threads/X/LinkedIn) + döngü görselleri (carousel) | bir düzen/metin modeli |
| **5. Teknik SEO** | Schema/JSON-LD, Core Web Vitals (INP/LCP/CLS) | bir teknik model |
| **6. Yayımlama** | Makaleyi yayımla + sosyal medyayı zamanla | otomasyon |
| **7. Geri Bildirim** | Analizler → içerik sütunu ağırlıklarını + sıklığı ayarla | akıl yürütme modeli |

Bir **güven puanı (trust score)**, her çalıştırmanın ne kadar otonom olduğunu belirler — "her adımda insan incelemesi için duraklat"tan "tamamen otomatik"e kadar — ve çıktıyı ne kadar düzenlediğinize bağlı olarak yükselir veya düşer.

---

## GEO/SEO Çerçeveleri

Çıktının kalitesi sezgilerden değil, çerçevelerden gelir. Bkz. [`frameworks/`](../frameworks/):

- **[GEO teknikleri](../frameworks/geo-techniques.md)** — tanım optimizasyonu (terim önce, 25–50 kelime, bağımsız bir yanıt olarak alıntılanabilir), alıntılanabilir ifadeler (istatistikler/gerçekler/karşılaştırmalar), otorite sinyalleri, Soru-Cevap yapısı ve üretken motorların sizi alıntılaması için olgusal yoğunluk.
- **[SEO yazım kontrol listesi](../frameworks/seo-writing-checklist.md)** — anahtar kelime yerleşimi, arama amacı eşleşmesi, okunabilirlik, dahili/harici bağlantı kurma ve öne çıkan snippet hedefleme.
- **[CORE-EEAT boyutları](../frameworks/core-eeat-dimensions.md)** — bir Experience / Expertise / Authoritativeness / Trustworthiness yayımlama kapısı (ayrıca kapsamlılık, özgünlük, okunabilirlik, kanıt).

---

## Kurulum (bir ajan becerisi olarak)

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

Ya da sadece `SKILL.md` + `frameworks/` + `schemas/` dosyalarını ajanınızın beceriler dizinine kopyalayın. Her dosya bağımlılık içermeyen Markdown/YAML'dir — bağımlılık kilidi (lock-in) yok.

1. `schemas/brand.example.yaml` → `brand.yaml` olarak kopyalayın; marka sesinizi, hedef kitlenizi, yazarlarınızı (E-E-A-T için) ve URL yapınızı doldurun.
2. Ajanınızı `SKILL.md` dosyasına yönlendirin ve bir konu için flywheel'i çalıştırın.
3. Çerçeveler, planlama ve taslak yazma adımlarına otomatik olarak enjekte edilir.

---

## Sizin için yapılmasını mı istiyorsunuz?

Bu depo **açık metodolojidir**. Bunun yerine **otomatik, barındırılan bir API** tercih ediyorsanız — denetimler, GEO/SEO içeriği ve optimize edilmiş meta etiketleri uç noktada (edge) enjekte eden otomatik düzeltme, kurulum gerekmez — şuraya gidin: **[1wayseo.com](https://1wayseo.com)**.

---

## Katkılar ve Lisans

- **CORE-EEAT** içerik kalitesi ve **CITE** alan güveni çerçeveleri, [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0) projesinden uyarlanmıştır. Teşekkürler.
- **Apache-2.0** altında lisanslanmıştır — bkz. [LICENSE](../LICENSE).

Katkılar memnuniyetle karşılanır. Bir issue veya PR açın.
