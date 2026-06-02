<!-- LANGS:nl -->
> Dutch. [English](../README.md)

# Content Flywheel — SEO- & GEO-contentvaardigheden

**Een open contentproductiemethodologie voor AI-agents.** Onderzoek een onderwerp, plan het met het sterkste redeneermodel, schrijf een concept, verwijder de AI-kenmerken, voer een GEO/SEO-kwaliteitspoort uit, verspreid het naar social media, publiceer het en voer de analysegegevens terug in de volgende cyclus — als een herbruikbare vaardigheid voor Claude Code, Cursor, Codex CLI, Gemini CLI en elke agent die Markdown-vaardigheden laadt.

> Gebouwd voor **Generative Engine Optimization (GEO)** — content die AI-zoekmachines (ChatGPT, Perplexity, Google AI Overviews) daadwerkelijk citeren — bovenop klassieke SEO.

🌐 **Talen:** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## Het vliegwiel

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| Fase | Wat er gebeurt | Best passende agentrol |
|-------|--------------|---------------------|
| **1. Onderzoek** | Trends, SERP-intentie, hiaten bij concurrenten, behoeften van het publiek | een onderzoeks-/groundingmodel |
| **2a. Plan** | Overzicht (H2/H3), stelling, plan voor interne links, CTA, plan voor gestructureerde data | het **sterkste redeneermodel** |
| **2b. Concept** | Volledige tekst geschreven volgens het plan | een snel schrijfmodel |
| **2c. De-AI** | Verwijder opvulsel, generieke formuleringen, "AI-kenmerken" | een snel bewerkingsmodel |
| **2d. Kwaliteitspoort** | Beoordeel het concept aan de hand van **CORE-EEAT**- + **GEO**-regels; benoem de hiaten | een reviewmodel |
| **3–4. Verspreiding** | Splits naar platformteksten (FB/IG/Threads/X/LinkedIn) + carrousels | een lay-out-/tekstmodel |
| **5. Technische SEO** | Schema/JSON-LD, Core Web Vitals (INP/LCP/CLS) | een technisch model |
| **6. Publiceren** | Publiceer artikel + plan social media in | automatisering |
| **7. Feedback** | Analyse → stem de gewichten van de contentpijlers + cadans af | het redeneermodel |

Een **vertrouwensscore** bepaalt hoe autonoom elke run is — van "pauzeer bij elke stap voor menselijke beoordeling" tot "volledig geautomatiseerd" — en stijgt of daalt op basis van hoeveel je de output bewerkt.

---

## GEO/SEO-frameworks

De kwaliteit van de output komt voort uit frameworks, niet uit gevoel. Zie [`frameworks/`](frameworks/):

- **[GEO-technieken](frameworks/geo-techniques.md)** — definitie-optimalisatie (term eerst, 25–50 woorden, citeerbaar als een op zichzelf staand antwoord), citeerbare uitspraken (statistieken/feiten/vergelijkingen), autoriteitssignalen, vraag-en-antwoordstructuur en feitelijke dichtheid zodat generatieve engines je citeren.
- **[SEO-schrijfchecklist](frameworks/seo-writing-checklist.md)** — plaatsing van zoekwoorden, afstemming op zoekintentie, leesbaarheid, interne/externe links en het richten op featured snippets.
- **[CORE-EEAT-dimensies](frameworks/core-eeat-dimensions.md)** — een publicatiepoort op basis van Experience / Expertise / Authoritativeness / Trustworthiness (plus volledigheid, originaliteit, leesbaarheid, bewijs).

---

## Installeren (als een agentvaardigheid)

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

Of kopieer gewoon `SKILL.md` + `frameworks/` + `schemas/` naar de skills-map van je agent. Elk bestand is afhankelijkheidsvrije Markdown/YAML — geen vendor lock-in.

1. Kopieer `schemas/brand.example.yaml` → `brand.yaml`, vul je merktoon, publiek, auteurs (voor E-E-A-T) en URL-structuur in.
2. Wijs je agent naar `SKILL.md` en voer het vliegwiel uit voor een onderwerp.
3. De frameworks worden automatisch geïnjecteerd in de plannings- en schrijfstappen.

---

## Wil je het voor je laten doen?

Deze repo is de **open methodologie**. Als je liever een **geautomatiseerde, gehoste API** hebt — audits, GEO/SEO-content en automatische correctie die geoptimaliseerde meta aan de edge injecteert, zonder installatie — ga dan naar **[1wayseo.com](https://1wayseo.com)**.

---

## Dankbetuigingen & licentie

- De **CORE-EEAT**-frameworks voor contentkwaliteit en **CITE**-frameworks voor domeinvertrouwen zijn aangepast van [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0). Bedankt.
- Gelicentieerd onder **Apache-2.0** — zie [LICENSE](LICENSE).

Bijdragen zijn welkom. Open een issue of PR.
