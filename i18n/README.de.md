<!-- LANGS:de -->
> German. [English](../README.md)

# Content Flywheel — SEO- & GEO-Content-Skills

**Eine offene Content-Produktionsmethodik für KI-Agenten.** Recherchiere ein Thema, plane es mit dem stärksten Reasoning-Modell, verfasse einen Entwurf, entferne den KI-Charakter, durchlaufe ein GEO/SEO-Qualitäts-Gate, verteile den Inhalt auf Social Media, veröffentliche ihn und speise die Analysedaten in den nächsten Zyklus zurück — als wiederverwendbarer Skill für Claude Code, Cursor, Codex CLI, Gemini CLI und jeden Agenten, der Markdown-Skills lädt.

> Entwickelt für **Generative Engine Optimization (GEO)** — Inhalte, die KI-Suchmaschinen (ChatGPT, Perplexity, Google AI Overviews) tatsächlich zitieren — aufbauend auf klassischem SEO.

🌐 **Sprachen:** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## Das Flywheel

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| Phase | Was passiert | Am besten geeignete Agentenrolle |
|-------|--------------|---------------------|
| **1. Recherche** | Trends, SERP-Intent, Wettbewerbslücken, Bedürfnisse der Zielgruppe | ein Recherche-/Grounding-Modell |
| **2a. Planung** | Gliederung (H2/H3), These, internes Verlinkungskonzept, CTA, Plan für strukturierte Daten | das **stärkste Reasoning-Modell** |
| **2b. Entwurf** | Vollständiger Fließtext, geschrieben nach Plan | ein schnelles Entwurfsmodell |
| **2c. De-AI** | Füllwörter, generische Formulierungen und „KI-Verräter" entfernen | ein schnelles Lektoratsmodell |
| **2d. Qualitäts-Gate** | Den Entwurf anhand der **CORE-EEAT**- + **GEO**-Regeln bewerten; Lücken auflisten | ein Review-Modell |
| **3–4. Fan-out** | Aufteilen in plattformspezifische Texte (FB/IG/Threads/X/LinkedIn) + Karussells | ein Layout-/Text-Modell |
| **5. Technisches SEO** | Schema/JSON-LD, Core Web Vitals (INP/LCP/CLS) | ein technisches Modell |
| **6. Veröffentlichung** | Artikel veröffentlichen + Social Media planen | Automatisierung |
| **7. Feedback** | Analysedaten → Gewichtung der Content-Säulen + Veröffentlichungstakt abstimmen | das Reasoning-Modell |

Ein **Trust Score** entscheidet, wie autonom jeder Durchlauf ist — von „bei jedem Schritt für die menschliche Überprüfung pausieren" bis hin zu „vollständig automatisiert" — und steigt oder sinkt je nachdem, wie stark du die Ausgabe bearbeitest.

---

## GEO/SEO-Frameworks

Die Qualität der Ausgabe entsteht durch Frameworks, nicht durch Bauchgefühl. Siehe [`frameworks/`](../frameworks/):

- **[GEO-Techniken](../frameworks/geo-techniques.md)** — Definitionsoptimierung (Begriff zuerst, 25–50 Wörter, als eigenständige Antwort zitierbar), zitierfähige Aussagen (Statistiken/Fakten/Vergleiche), Autoritätssignale, Q&A-Struktur und faktische Dichte, damit generative Engines dich zitieren.
- **[SEO-Schreib-Checkliste](../frameworks/seo-writing-checklist.md)** — Keyword-Platzierung, Übereinstimmung mit der Suchintention, Lesbarkeit, interne/externe Verlinkung und Targeting von Featured Snippets.
- **[CORE-EEAT-Dimensionen](../frameworks/core-eeat-dimensions.md)** — ein Veröffentlichungs-Gate für Experience / Expertise / Authoritativeness / Trustworthiness (plus Vollständigkeit, Originalität, Lesbarkeit, Belege).

---

## Installation (als Agenten-Skill)

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

Oder kopiere einfach `SKILL.md` + `frameworks/` + `schemas/` in das Skills-Verzeichnis deines Agenten. Jede Datei ist abhängigkeitsfreies Markdown/YAML — kein Lock-in.

1. Kopiere `schemas/brand.example.yaml` → `brand.yaml` und trage deine Markenstimme, Zielgruppe, Autoren (für E-E-A-T) und URL-Struktur ein.
2. Verweise deinen Agenten auf `SKILL.md` und lasse das Flywheel für ein Thema laufen.
3. Die Frameworks werden automatisch in die Planungs- und Entwurfsschritte eingespeist.

---

## Soll es für dich erledigt werden?

Dieses Repo ist die **offene Methodik**. Wenn du lieber eine **automatisierte, gehostete API** hättest — Audits, GEO/SEO-Content und Auto-Fix, der optimierte Meta-Daten am Edge einfügt, ganz ohne Setup — dann geh zu **[1wayseo.com](https://1wayseo.com)**.

---

## Danksagungen & Lizenz

- Die Frameworks **CORE-EEAT** für Content-Qualität und **CITE** für Domain-Trust sind adaptiert von [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0). Vielen Dank.
- Lizenziert unter **Apache-2.0** — siehe [LICENSE](../LICENSE).

Beiträge sind willkommen. Eröffne ein Issue oder einen PR.
