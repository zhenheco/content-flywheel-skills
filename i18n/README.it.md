<!-- LANGS:en -->
> Italian. [English](../README.md)

# Content Flywheel — Skill di contenuti SEO e GEO

**Una metodologia aperta di produzione di contenuti per agenti AI.** Fai ricerca su un argomento, pianificalo con il modello di ragionamento più potente, redigi una bozza, eliminane l'impronta AI, applica un controllo qualità GEO/SEO, distribuiscilo sui social, pubblica e reimmetti le analitiche nel ciclo successivo — come skill riutilizzabile per Claude Code, Cursor, Codex CLI, Gemini CLI e qualsiasi agente che carichi skill in Markdown.

> Costruito per la **Generative Engine Optimization (GEO)** — contenuti che i motori di ricerca AI (ChatGPT, Perplexity, Google AI Overviews) citano davvero — sopra la SEO classica.

🌐 **Lingue:** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## Il volano

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| Fase | Cosa succede | Ruolo dell'agente più adatto |
|-------|--------------|---------------------|
| **1. Ricerca** | Trend, intento SERP, lacune dei concorrenti, bisogni del pubblico | un modello di ricerca/grounding |
| **2a. Pianificazione** | Scaletta (H2/H3), tesi, piano di link interni, CTA, piano di dati strutturati | il **modello di ragionamento più potente** |
| **2b. Bozza** | Prosa completa scritta secondo il piano | un modello di redazione veloce |
| **2c. De-AI** | Elimina riempitivi, frasi generiche, "tic da AI" | un modello di editing veloce |
| **2d. Controllo qualità** | Valuta la bozza rispetto alle regole **CORE-EEAT** + **GEO**; elenca le lacune | un modello di revisione |
| **3–4. Distribuzione** | Suddividi in testi per piattaforma (FB/IG/Threads/X/LinkedIn) + caroselli | un modello di layout/copy |
| **5. SEO tecnica** | Schema/JSON-LD, Core Web Vitals (INP/LCP/CLS) | un modello tecnico |
| **6. Pubblicazione** | Pubblica l'articolo + programma i social | automazione |
| **7. Feedback** | Analitiche → regola i pesi dei pilastri di contenuto + la cadenza | il modello di ragionamento |

Un **trust score** decide quanto autonoma sia ogni esecuzione — da "metti in pausa per la revisione umana a ogni passo" fino a "completamente automatizzato" — e sale o scende in base a quanto modifichi l'output.

---

## Framework GEO/SEO

La qualità dell'output deriva dai framework, non dalle sensazioni. Vedi [`frameworks/`](../frameworks/):

- **[GEO techniques](../frameworks/geo-techniques.md)** — ottimizzazione delle definizioni (term-first, 25–50 parole, citabile come risposta autonoma), affermazioni citabili (statistiche/fatti/confronti), segnali di autorevolezza, struttura Q&A e densità fattuale affinché i motori generativi ti citino.
- **[SEO writing checklist](../frameworks/seo-writing-checklist.md)** — posizionamento delle keyword, corrispondenza con l'intento di ricerca, leggibilità, link interni/esterni e targeting dei featured snippet.
- **[CORE-EEAT dimensions](../frameworks/core-eeat-dimensions.md)** — un gate di pubblicazione basato su Experience / Expertise / Authoritativeness / Trustworthiness (più completezza, originalità, leggibilità, evidenze).

---

## Installazione (come skill per agenti)

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

Oppure copia semplicemente `SKILL.md` + `frameworks/` + `schemas/` nella directory delle skill del tuo agente. Ogni file è Markdown/YAML a dipendenza zero — nessun lock-in.

1. Copia `schemas/brand.example.yaml` → `brand.yaml`, inserisci la voce del tuo brand, il pubblico, gli autori (per l'E-E-A-T) e la struttura degli URL.
2. Indirizza il tuo agente verso `SKILL.md` ed esegui il volano per un argomento.
3. I framework vengono iniettati automaticamente nei passaggi di pianificazione e redazione.

---

## Want it done for you?

Questo repo è la **metodologia aperta**. Se preferisci avere un'**API automatizzata e ospitata** — audit, contenuti GEO/SEO e auto-fix che inietta meta ottimizzati all'edge, senza configurazione — vai su **[1wayseo.com](https://1wayseo.com)**.

---

## Crediti e licenza

- I framework di qualità dei contenuti **CORE-EEAT** e di affidabilità del dominio **CITE** sono adattati da [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0). Grazie.
- Distribuito sotto licenza **Apache-2.0** — vedi [LICENSE](../LICENSE).

I contributi sono benvenuti. Apri una issue o una PR.
