<!-- LANGS:hi -->
> Hindi. [English](../README.md)

# Content Flywheel — SEO और GEO कंटेंट स्किल्स

**AI एजेंट्स के लिए एक ओपन कंटेंट-प्रोडक्शन पद्धति।** किसी विषय पर शोध करें, उसे सबसे सशक्त रीज़निंग मॉडल के साथ प्लान करें, उसका ड्राफ़्ट बनाएं, उसे de-AI करें, एक GEO/SEO क्वालिटी गेट चलाएं, उसे सोशल पर फ़ैन-आउट करें, प्रकाशित करें, और एनालिटिक्स को अगले चक्र में वापस फ़ीड करें — Claude Code, Cursor, Codex CLI, Gemini CLI, और किसी भी ऐसे एजेंट के लिए एक पुन: प्रयोज्य स्किल के रूप में जो Markdown स्किल्स लोड करता है।

> **Generative Engine Optimization (GEO)** के लिए बनाया गया — ऐसा कंटेंट जिसे AI सर्च इंजन (ChatGPT, Perplexity, Google AI Overviews) वास्तव में cite करते हैं — क्लासिक SEO के ऊपर।

🌐 **भाषाएं:** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## द फ्लाईव्हील

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| चरण | क्या होता है | सबसे उपयुक्त एजेंट भूमिका |
|-------|--------------|---------------------|
| **1. Research** | ट्रेंड्स, SERP इंटेंट, प्रतिस्पर्धी अंतराल, ऑडियंस की ज़रूरतें | एक research/grounding मॉडल |
| **2a. Plan** | आउटलाइन (H2/H3), थीसिस, इंटरनल-लिंक प्लान, CTA, स्ट्रक्चर्ड-डेटा प्लान | **सबसे सशक्त रीज़निंग मॉडल** |
| **2b. Draft** | प्लान के अनुसार लिखा गया पूरा गद्य | एक तेज़ ड्राफ़्टिंग मॉडल |
| **2c. De-AI** | फ़िलर, सामान्य वाक्यांश, "AI tells" को हटाना | एक तेज़ एडिटिंग मॉडल |
| **2d. Quality gate** | ड्राफ़्ट को **CORE-EEAT** + **GEO** नियमों के विरुद्ध स्कोर करें; अंतराल सूचीबद्ध करें | एक रिव्यू मॉडल |
| **3–4. Fan-out** | प्लेटफ़ॉर्म कॉपी (FB/IG/Threads/X/LinkedIn) + carousels में विभाजित करें | एक लेआउट/कॉपी मॉडल |
| **5. Technical SEO** | Schema/JSON-LD, Core Web Vitals (INP/LCP/CLS) | एक टेक्निकल मॉडल |
| **6. Publish** | लेख प्रकाशित करें + सोशल शेड्यूल करें | ऑटोमेशन |
| **7. Feedback** | एनालिटिक्स → कंटेंट-पिलर वेट + कैडेंस ट्यून करें | रीज़निंग मॉडल |

एक **trust score** तय करता है कि प्रत्येक रन कितना स्वायत्त है — "हर चरण पर मानव समीक्षा के लिए रुकें" से लेकर "पूरी तरह स्वचालित" तक — और यह इस आधार पर बढ़ता या घटता है कि आप आउटपुट को कितना एडिट करते हैं।

---

## GEO/SEO फ़्रेमवर्क

आउटपुट की गुणवत्ता फ़्रेमवर्क से आती है, vibes से नहीं। देखें [`frameworks/`](../frameworks/):

- **[GEO techniques](../frameworks/geo-techniques.md)** — definition optimization (term-first, 25–50 शब्द, एक स्वतंत्र उत्तर के रूप में citable), quotable statements (स्टैट्स/तथ्य/तुलनाएं), authority signals, Q&A संरचना, और factual density ताकि generative engines आपको quote करें।
- **[SEO writing checklist](../frameworks/seo-writing-checklist.md)** — कीवर्ड प्लेसमेंट, search-intent मैच, पठनीयता, internal/external linking, और featured-snippet टार्गेटिंग।
- **[CORE-EEAT dimensions](../frameworks/core-eeat-dimensions.md)** — एक Experience / Expertise / Authoritativeness / Trustworthiness publish gate (साथ ही comprehensiveness, originality, readability, evidence)।

---

## इंस्टॉल करें (एक एजेंट स्किल के रूप में)

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

या बस `SKILL.md` + `frameworks/` + `schemas/` को अपने एजेंट की skills directory में कॉपी करें। हर फ़ाइल zero-dependency Markdown/YAML है — कोई lock-in नहीं।

1. `schemas/brand.example.yaml` → `brand.yaml` कॉपी करें, अपनी brand voice, ऑडियंस, लेखक (E-E-A-T के लिए), और URL संरचना भरें।
2. अपने एजेंट को `SKILL.md` की ओर इंगित करें और किसी विषय के लिए फ्लाईव्हील चलाएं।
3. फ़्रेमवर्क स्वचालित रूप से planning और drafting चरणों में inject हो जाते हैं।

---

## चाहते हैं कि यह आपके लिए हो जाए?

यह repo **ओपन पद्धति** है। यदि आप इसके बजाय एक **automated, hosted API** चाहते हैं — audits, GEO/SEO कंटेंट, और auto-fix जो optimized meta को edge पर inject करता है, बिना किसी setup के — तो जाएं **[1wayseo.com](https://1wayseo.com)** पर।

---

## क्रेडिट्स और लाइसेंस

- **CORE-EEAT** content-quality और **CITE** domain-trust फ़्रेमवर्क [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0) से अनुकूलित हैं। धन्यवाद।
- **Apache-2.0** के तहत लाइसेंस प्राप्त — देखें [LICENSE](../LICENSE)।

योगदान का स्वागत है। एक issue या PR खोलें।
