<!-- LANGS:fr -->
> French. [English](../README.md)

# Content Flywheel — Compétences de contenu SEO et GEO

**Une méthodologie ouverte de production de contenu pour les agents IA.** Recherchez un sujet, planifiez-le avec le modèle de raisonnement le plus puissant, rédigez-le, dé-IA-isez-le, faites-le passer par un contrôle qualité GEO/SEO, déployez-le sur les réseaux sociaux, publiez-le, puis réinjectez les données analytiques dans le cycle suivant — le tout sous la forme d'une compétence réutilisable pour Claude Code, Cursor, Codex CLI, Gemini CLI, et tout agent capable de charger des compétences en Markdown.

> Conçu pour la **Generative Engine Optimization (GEO)** — du contenu que les moteurs de recherche IA (ChatGPT, Perplexity, Google AI Overviews) citent réellement — par-dessus le SEO classique.

🌐 **Langues :** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## Le volant d'inertie

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| Phase | Ce qui se passe | Rôle d'agent le mieux adapté |
|-------|--------------|---------------------|
| **1. Recherche** | Tendances, intention SERP, lacunes des concurrents, besoins de l'audience | un modèle de recherche/ancrage |
| **2a. Planification** | Plan (H2/H3), thèse, plan de maillage interne, CTA, plan de données structurées | le **modèle de raisonnement le plus puissant** |
| **2b. Rédaction** | Texte complet écrit selon le plan | un modèle de rédaction rapide |
| **2c. Dé-IA-isation** | Suppression du remplissage, des tournures génériques, des « marqueurs d'IA » | un modèle d'édition rapide |
| **2d. Contrôle qualité** | Notation du brouillon selon les règles **CORE-EEAT** + **GEO** ; liste des lacunes | un modèle de relecture |
| **3–4. Déploiement** | Découpage en textes par plateforme (FB/IG/Threads/X/LinkedIn) + carrousels | un modèle de mise en page/rédaction |
| **5. SEO technique** | Schema/JSON-LD, Core Web Vitals (INP/LCP/CLS) | un modèle technique |
| **6. Publication** | Publication de l'article + planification des réseaux sociaux | automatisation |
| **7. Retour d'information** | Données analytiques → ajustement des pondérations de piliers de contenu + cadence | le modèle de raisonnement |

Un **score de confiance** détermine le degré d'autonomie de chaque exécution — de « pause pour relecture humaine à chaque étape » jusqu'à « entièrement automatisé » — et augmente ou diminue selon l'ampleur de vos retouches sur le résultat.

---

## Cadres GEO/SEO

La qualité du résultat provient de cadres méthodiques, pas de l'intuition. Voir [`frameworks/`](../frameworks/) :

- **[Techniques GEO](../frameworks/geo-techniques.md)** — optimisation des définitions (terme en premier, 25 à 50 mots, citable comme réponse autonome), affirmations citables (statistiques/faits/comparaisons), signaux d'autorité, structure questions-réponses, et densité factuelle pour que les moteurs génératifs vous citent.
- **[Liste de contrôle de rédaction SEO](../frameworks/seo-writing-checklist.md)** — placement des mots-clés, correspondance avec l'intention de recherche, lisibilité, maillage interne/externe, et ciblage des extraits optimisés (featured snippets).
- **[Dimensions CORE-EEAT](../frameworks/core-eeat-dimensions.md)** — une porte de publication Expérience / Expertise / Autorité / Fiabilité (E-E-A-T) (plus exhaustivité, originalité, lisibilité, preuves).

---

## Installation (en tant que compétence d'agent)

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

Ou copiez simplement `SKILL.md` + `frameworks/` + `schemas/` dans le répertoire des compétences de votre agent. Chaque fichier est du Markdown/YAML sans aucune dépendance — pas d'enfermement propriétaire.

1. Copiez `schemas/brand.example.yaml` → `brand.yaml`, et renseignez la voix de votre marque, votre audience, vos auteurs (pour l'E-E-A-T) et la structure de vos URL.
2. Pointez votre agent vers `SKILL.md` et lancez le volant d'inertie pour un sujet.
3. Les cadres sont injectés automatiquement dans les étapes de planification et de rédaction.

---

## Vous préférez qu'on le fasse pour vous ?

Ce dépôt est la **méthodologie ouverte**. Si vous préférez disposer d'une **API hébergée et automatisée** — audits, contenu GEO/SEO et correction automatique qui injecte des balises meta optimisées en périphérie (edge), sans configuration — rendez-vous sur **[1wayseo.com](https://1wayseo.com)**.

---

## Crédits et licence

- Les cadres de qualité de contenu **CORE-EEAT** et de confiance de domaine **CITE** sont adaptés de [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0). Merci.
- Sous licence **Apache-2.0** — voir [LICENSE](../LICENSE).

Les contributions sont les bienvenues. Ouvrez une issue ou une PR.
