<!-- LANGS:zh-Hant -->
> Traditional Chinese. [English](../README.md)

# Content Flywheel — SEO 與 GEO 內容技能

**一套為 AI 代理打造的開放式內容生產方法論。** 研究一個主題、用最強的推理模型擬定規劃、撰寫初稿、去除 AI 痕跡、通過 GEO/SEO 品質關卡、裂變到社群、發布，並把分析數據回饋到下一個循環——以可重複使用的技能形式，提供給 Claude Code、Cursor、Codex CLI、Gemini CLI，以及任何能載入 Markdown 技能的代理。

> 在傳統 SEO 之上，專為 **Generative Engine Optimization (GEO)** 而打造——讓 AI 搜尋引擎（ChatGPT、Perplexity、Google AI Overviews）真正願意引用的內容。

🌐 **語言：** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## 飛輪

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| 階段 | 發生什麼事 | 最適合的代理角色 |
|-------|--------------|---------------------|
| **1. 研究** | 趨勢、SERP 搜尋意圖、競爭對手缺口、受眾需求 | 研究／接地（grounding）模型 |
| **2a. 規劃** | 大綱（H2/H3）、論點、內部連結規劃、CTA、結構化資料規劃 | **最強的推理模型** |
| **2b. 撰寫初稿** | 依規劃寫出完整內文 | 快速撰稿模型 |
| **2c. 去除 AI 痕跡** | 刪除贅字、空泛措辭、「AI 味」 | 快速編輯模型 |
| **2d. 品質關卡** | 依 **CORE-EEAT** + **GEO** 規則為初稿評分；列出缺口 | 審查模型 |
| **3–4. 裂變** | 拆分為各平台文案（FB/IG/Threads/X/LinkedIn）+ 輪播圖卡 | 排版／文案模型 |
| **5. 技術 SEO** | Schema/JSON-LD、Core Web Vitals (INP/LCP/CLS) | 技術模型 |
| **6. 發布** | 發布文章 + 排程社群貼文 | 自動化 |
| **7. 回饋** | 分析數據 → 調整內容支柱權重 + 發文節奏 | 推理模型 |

一個 **信任分數** 決定每次執行的自主程度——從「每一步都暫停等人工審查」一直到「全自動」——並依你修改輸出的多寡而上升或下降。

---

## GEO/SEO 框架

輸出的品質來自框架，而非感覺。請見 [`frameworks/`](../frameworks/)：

- **[GEO 技巧](../frameworks/geo-techniques.md)** — 定義最佳化（術語優先、25–50 字、可作為獨立答案被引用）、可引述的陳述（統計數據／事實／比較）、權威訊號、Q&A 結構，以及事實密度，讓生成式引擎引用你。
- **[SEO 寫作檢查清單](../frameworks/seo-writing-checklist.md)** — 關鍵字配置、搜尋意圖匹配、可讀性、內部／外部連結，以及精選摘要（featured snippet）鎖定。
- **[CORE-EEAT 維度](../frameworks/core-eeat-dimensions.md)** — 一個由 Experience／Expertise／Authoritativeness／Trustworthiness 構成的發布關卡（外加完整性、原創性、可讀性、佐證）。

---

## 安裝（作為代理技能）

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

或者直接把 `SKILL.md` + `frameworks/` + `schemas/` 複製到你的代理技能目錄。每個檔案都是零相依的 Markdown/YAML——沒有綁定鎖死。

1. 把 `schemas/brand.example.yaml` 複製為 `brand.yaml`，填入你的品牌語氣、受眾、作者（供 E-E-A-T 使用），以及 URL 結構。
2. 讓你的代理指向 `SKILL.md`，並針對某個主題執行飛輪。
3. 這些框架會自動注入到規劃與撰稿步驟中。

---

## 想要我們幫你搞定？

這個 repo 是 **開放方法論**。如果你寧願擁有一個 **自動化、託管的 API**——稽核、GEO/SEO 內容，以及在邊緣注入最佳化 meta 的自動修復，無需任何設定——請前往 **[1wayseo.com](https://1wayseo.com)**。

---

## 致謝與授權

- **CORE-EEAT** 內容品質框架與 **CITE** 網域信任框架改編自 [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills)（Apache-2.0）。謝謝。
- 採用 **Apache-2.0** 授權——請見 [LICENSE](../LICENSE)。

歡迎貢獻。請開 issue 或 PR。
