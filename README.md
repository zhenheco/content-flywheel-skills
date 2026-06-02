<!-- LANGS:en -->
# Content Flywheel — SEO & GEO Content Skills

**An open content-production methodology for AI agents.** Research a topic, plan it with the strongest reasoning model, draft it, de-AI it, run a GEO/SEO quality gate, fan it out to social, publish, and feed analytics back into the next cycle — as a reusable skill for Claude Code, Cursor, Codex CLI, Gemini CLI, and any agent that loads Markdown skills.

> Built for **Generative Engine Optimization (GEO)** — content that AI search engines (ChatGPT, Perplexity, Google AI Overviews) actually cite — on top of classic SEO.

🌐 **Languages:** [English](README.md) · [繁體中文](i18n/README.zh-Hant.md) · [简体中文](i18n/README.zh-Hans.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Español](i18n/README.es.md) · [Português](i18n/README.pt.md) · [Français](i18n/README.fr.md) · [Deutsch](i18n/README.de.md) · [Italiano](i18n/README.it.md) · [Русский](i18n/README.ru.md) · [العربية](i18n/README.ar.md) · [हिन्दी](i18n/README.hi.md) · [Bahasa Indonesia](i18n/README.id.md) · [Tiếng Việt](i18n/README.vi.md) · [ไทย](i18n/README.th.md) · [Türkçe](i18n/README.tr.md) · [Nederlands](i18n/README.nl.md)

---

## The Flywheel

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| Phase | What happens | Best-fit agent role |
|-------|--------------|---------------------|
| **1. Research** | Trends, SERP intent, competitor gaps, audience needs | a research/grounding model |
| **2a. Plan** | Outline (H2/H3), thesis, internal-link plan, CTA, structured-data plan | the **strongest reasoning model** |
| **2b. Draft** | Full prose written to the plan | a fast drafting model |
| **2c. De-AI** | Strip filler, generic phrasing, "AI tells" | a fast editing model |
| **2d. Quality gate** | Score the draft against **CORE-EEAT** + **GEO** rules; list gaps | a review model |
| **3–4. Fan-out** | Split to platform copy (FB/IG/Threads/X/LinkedIn) + carousels | a layout/copy model |
| **5. Technical SEO** | Schema/JSON-LD, Core Web Vitals (INP/LCP/CLS) | a technical model |
| **6. Publish** | Publish article + schedule social | automation |
| **7. Feedback** | Analytics → tune content-pillar weights + cadence | the reasoning model |

A **trust score** decides how autonomous each run is — from "pause for human review at every step" up to "fully automated" — and rises or falls based on how much you edit the output.

---

## GEO/SEO Frameworks

The quality of the output comes from frameworks, not vibes. See [`frameworks/`](frameworks/):

- **[GEO techniques](frameworks/geo-techniques.md)** — definition optimization (term-first, 25–50 words, citable as a standalone answer), quotable statements (stats/facts/comparisons), authority signals, Q&A structure, and factual density so generative engines quote you.
- **[SEO writing checklist](frameworks/seo-writing-checklist.md)** — keyword placement, search-intent match, readability, internal/external linking, and featured-snippet targeting.
- **[CORE-EEAT dimensions](frameworks/core-eeat-dimensions.md)** — an Experience / Expertise / Authoritativeness / Trustworthiness publish gate (plus comprehensiveness, originality, readability, evidence).

---

## Install (as an agent skill)

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

Or just copy `SKILL.md` + `frameworks/` + `schemas/` into your agent's skills directory. Every file is zero-dependency Markdown/YAML — no lock-in.

1. Copy `schemas/brand.example.yaml` → `brand.yaml`, fill in your brand voice, audience, authors (for E-E-A-T), and URL structure.
2. Point your agent at `SKILL.md` and run the flywheel for a topic.
3. The frameworks are injected into the planning and drafting steps automatically.

---

## Want it done for you?

This repo is the **open methodology**. If you'd rather have an **automated, hosted API** — audits, GEO/SEO content, and auto-fix that injects optimized meta at the edge, no setup — go to **[1wayseo.com](https://1wayseo.com)**.

---

## Credits & License

- The **CORE-EEAT** content-quality and **CITE** domain-trust frameworks are adapted from [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0). Thank you.
- Licensed under **Apache-2.0** — see [LICENSE](LICENSE).

Contributions welcome. Open an issue or PR.
