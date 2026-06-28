<!-- LANGS:zh-Hans -->
> Simplified Chinese. [English](../README.md)

# Content Flywheel — SEO 与 GEO 内容技能

**一套面向 AI agent 的开放式内容生产方法论。** 研究一个主题，用最强的推理模型规划它，撰写初稿，去除 AI 味，运行一道 GEO/SEO 质量关卡，裂变为社群内容，发布，并将分析数据反馈到下一个循环——作为一个可复用的技能，适用于 Claude Code、Cursor、Codex CLI、Gemini CLI，以及任何能加载 Markdown 技能的 agent。

> 在经典 SEO 之上，为 **Generative Engine Optimization (GEO)** 而构建——让 AI 搜索引擎（ChatGPT、Perplexity、Google AI Overviews）真正愿意引用的内容。

🌐 **语言：** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## 飞轮

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| 阶段 | 发生了什么 | 最契合的 agent 角色 |
|-------|--------------|---------------------|
| **1. 研究** | 趋势、SERP 意图、竞品空缺、受众需求 | 一个研究/接地（grounding）模型 |
| **2a. 规划** | 大纲（H2/H3）、论点、内链规划、CTA、结构化数据规划 | **最强的推理模型** |
| **2b. 撰写** | 按规划写出完整正文 | 一个快速的撰写模型 |
| **2c. 去 AI 味** | 剔除填充内容、套话、"AI 痕迹" | 一个快速的编辑模型 |
| **2d. 质量关卡** | 依据 **CORE-EEAT** + **GEO** 规则给初稿打分；列出差距 | 一个审查模型 |
| **3–4. 裂变** | 拆分为各平台文案（FB/IG/Threads/X/LinkedIn）+ 轮播图 | 一个排版/文案模型 |
| **5. 技术 SEO** | Schema/JSON-LD、Core Web Vitals（INP/LCP/CLS） | 一个技术模型 |
| **6. 发布** | 发布文章 + 安排社群排程 | 自动化 |
| **7. 反馈** | 分析数据 → 调整内容支柱权重 + 发布节奏 | 推理模型 |

一个 **trust score（信任分）** 决定每次运行的自主程度——从"每一步都暂停等待人工审核"一直到"完全自动化"——并根据你对输出的修改幅度而上升或下降。

---

## GEO/SEO 框架

输出的质量来自框架，而非凭感觉。参见 [`frameworks/`](../frameworks/)：

- **[GEO techniques](../frameworks/geo-techniques.md)** —— 定义优化（术语先行，25–50 词，可作为独立答案被引用）、可引用陈述（统计数据/事实/对比）、权威信号、Q&A 结构，以及事实密度，让生成式引擎愿意引用你。
- **[SEO writing checklist](../frameworks/seo-writing-checklist.md)** —— 关键词布局、搜索意图匹配、可读性、内部/外部链接，以及精选摘要（featured snippet）定位。
- **[CORE-EEAT dimensions](../frameworks/core-eeat-dimensions.md)** —— 一道 Experience / Expertise / Authoritativeness / Trustworthiness 的发布关卡（外加全面性、原创性、可读性、证据）。

---

## 安装（作为 agent 技能）

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

或者直接把 `SKILL.md` + `frameworks/` + `schemas/` 复制到你的 agent 技能目录。每个文件都是零依赖的 Markdown/YAML——没有任何锁定。

1. 复制 `schemas/brand.example.yaml` → `brand.yaml`，填入你的品牌语气、受众、作者（用于 E-E-A-T）以及 URL 结构。
2. 把你的 agent 指向 `SKILL.md`，针对某个主题运行飞轮。
3. 这些框架会被自动注入到规划与撰写步骤中。

---

## 想让我们帮你做好？

这个仓库是 **开放的方法论**。如果你更想要一个 **自动化、托管的 API**——审计、GEO/SEO 内容，以及在边缘注入优化后 meta 的自动修复，零配置——请前往 **[1wayseo.com](https://1wayseo.com)**。

---

## 致谢与许可

- **CORE-EEAT** 内容质量框架和 **CITE** 域名信任框架改编自 [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills)（Apache-2.0）。感谢。
- 采用 **Apache-2.0** 许可——参见 [LICENSE](../LICENSE)。

欢迎贡献。请开 issue 或 PR。
