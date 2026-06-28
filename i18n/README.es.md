<!-- LANGS:es -->
> Spanish. [English](../README.md)

# Content Flywheel — Skills de contenido SEO y GEO

**Una metodología abierta de producción de contenido para agentes de IA.** Investiga un tema, planifícalo con el modelo de razonamiento más potente, redáctalo, quítale el aire de IA, pásalo por una verificación de calidad GEO/SEO, distribúyelo en redes sociales, publícalo y realimenta la analítica en el siguiente ciclo, todo como una skill reutilizable para Claude Code, Cursor, Codex CLI, Gemini CLI y cualquier agente que cargue skills en Markdown.

> Creado para **Generative Engine Optimization (GEO)** — contenido que los motores de búsqueda con IA (ChatGPT, Perplexity, Google AI Overviews) realmente citan — sobre la base del SEO clásico.

🌐 **Idiomas:** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## El volante (flywheel)

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| Fase | Qué ocurre | Rol de agente más adecuado |
|-------|--------------|---------------------|
| **1. Investigación** | Tendencias, intención en la SERP, brechas frente a la competencia, necesidades de la audiencia | un modelo de investigación/grounding |
| **2a. Planificación** | Esquema (H2/H3), tesis, plan de enlaces internos, CTA, plan de datos estructurados | el **modelo de razonamiento más potente** |
| **2b. Redacción** | Prosa completa escrita según el plan | un modelo de redacción rápido |
| **2c. Quitar el aire de IA** | Eliminar relleno, frases genéricas, "marcas de IA" | un modelo de edición rápido |
| **2d. Verificación de calidad** | Puntuar el borrador frente a las reglas **CORE-EEAT** + **GEO**; listar carencias | un modelo de revisión |
| **3–4. Distribución** | Dividir en copy por plataforma (FB/IG/Threads/X/LinkedIn) + carruseles | un modelo de maquetación/copy |
| **5. SEO técnico** | Schema/JSON-LD, Core Web Vitals (INP/LCP/CLS) | un modelo técnico |
| **6. Publicación** | Publicar el artículo + programar las redes sociales | automatización |
| **7. Realimentación** | Analítica → ajustar los pesos de los pilares de contenido + la cadencia | el modelo de razonamiento |

Una **puntuación de confianza** decide cuán autónoma es cada ejecución — desde "pausar para revisión humana en cada paso" hasta "totalmente automatizado" — y sube o baja según cuánto edites el resultado.

---

## Frameworks GEO/SEO

La calidad del resultado proviene de frameworks, no de la intuición. Consulta [`frameworks/`](../frameworks/):

- **[GEO techniques](../frameworks/geo-techniques.md)** — optimización de definiciones (término primero, 25–50 palabras, citable como respuesta autónoma), afirmaciones citables (estadísticas/hechos/comparaciones), señales de autoridad, estructura de preguntas y respuestas y densidad factual para que los motores generativos te citen.
- **[SEO writing checklist](../frameworks/seo-writing-checklist.md)** — colocación de palabras clave, coincidencia con la intención de búsqueda, legibilidad, enlazado interno/externo y orientación a los fragmentos destacados.
- **[CORE-EEAT dimensions](../frameworks/core-eeat-dimensions.md)** — una puerta de publicación de Experience / Expertise / Authoritativeness / Trustworthiness (más exhaustividad, originalidad, legibilidad y evidencia).

---

## Instalación (como skill de agente)

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

O simplemente copia `SKILL.md` + `frameworks/` + `schemas/` en el directorio de skills de tu agente. Cada archivo es Markdown/YAML sin dependencias, sin ataduras.

1. Copia `schemas/brand.example.yaml` → `brand.yaml`, rellena la voz de tu marca, la audiencia, los autores (para E-E-A-T) y la estructura de URL.
2. Apunta tu agente a `SKILL.md` y ejecuta el flywheel para un tema.
3. Los frameworks se inyectan automáticamente en los pasos de planificación y redacción.

---

## ¿Quieres que lo hagamos por ti?

Este repositorio es la **metodología abierta**. Si prefieres tener una **API alojada y automatizada** — auditorías, contenido GEO/SEO y autocorrección que inyecta meta optimizado en el edge, sin configuración — visita **[1wayseo.com](https://1wayseo.com)**.

---

## Créditos y licencia

- Los frameworks de calidad de contenido **CORE-EEAT** y de confianza de dominio **CITE** están adaptados de [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0). Gracias.
- Licenciado bajo **Apache-2.0** — consulta [LICENSE](../LICENSE).

Las contribuciones son bienvenidas. Abre un issue o un PR.
