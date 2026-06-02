<!-- LANGS:pt -->
> Portuguese. [English](../README.md)

# Content Flywheel — Skills de Conteúdo para SEO e GEO

**Uma metodologia aberta de produção de conteúdo para agentes de IA.** Pesquise um tema, planeje-o com o modelo de raciocínio mais forte, redija-o, remova as marcas de IA, execute um portão de qualidade GEO/SEO, distribua-o para as redes sociais, publique e realimente as análises no ciclo seguinte — tudo como uma skill reutilizável para Claude Code, Cursor, Codex CLI, Gemini CLI e qualquer agente que carregue skills em Markdown.

> Concebido para **Generative Engine Optimization (GEO)** — conteúdo que os motores de busca com IA (ChatGPT, Perplexity, Google AI Overviews) realmente citam — sobre a base do SEO clássico.

🌐 **Idiomas:** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## O Volante (Flywheel)

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| Fase | O que acontece | Papel ideal do agente |
|-------|--------------|---------------------|
| **1. Pesquisa** | Tendências, intenção da SERP, lacunas dos concorrentes, necessidades do público | um modelo de pesquisa/fundamentação |
| **2a. Planejamento** | Estrutura (H2/H3), tese, plano de links internos, CTA, plano de dados estruturados | o **modelo de raciocínio mais forte** |
| **2b. Redação** | Texto completo escrito segundo o plano | um modelo de redação rápido |
| **2c. De-AI** | Remover enchimento, frases genéricas, "marcas de IA" | um modelo de edição rápido |
| **2d. Portão de qualidade** | Avaliar o rascunho segundo as regras **CORE-EEAT** + **GEO**; listar lacunas | um modelo de revisão |
| **3–4. Distribuição** | Dividir em textos por plataforma (FB/IG/Threads/X/LinkedIn) + carrosséis | um modelo de layout/texto |
| **5. SEO técnico** | Schema/JSON-LD, Core Web Vitals (INP/LCP/CLS) | um modelo técnico |
| **6. Publicação** | Publicar artigo + agendar redes sociais | automação |
| **7. Feedback** | Análises → ajustar pesos dos pilares de conteúdo + cadência | o modelo de raciocínio |

Uma **pontuação de confiança** decide o grau de autonomia de cada execução — desde "pausar para revisão humana em cada passo" até "totalmente automatizado" — e sobe ou desce conforme o quanto você edita o resultado.

---

## Frameworks de GEO/SEO

A qualidade do resultado vem de frameworks, não de intuição. Veja [`frameworks/`](frameworks/):

- **[Técnicas de GEO](frameworks/geo-techniques.md)** — otimização de definições (termo primeiro, 25–50 palavras, citáveis como resposta autônoma), afirmações citáveis (estatísticas/fatos/comparações), sinais de autoridade, estrutura de perguntas e respostas e densidade factual para que os motores generativos o citem.
- **[Checklist de redação SEO](frameworks/seo-writing-checklist.md)** — posicionamento de palavras-chave, correspondência com a intenção de busca, legibilidade, links internos/externos e foco em featured snippets.
- **[Dimensões CORE-EEAT](frameworks/core-eeat-dimensions.md)** — um portão de publicação de Experiência / Especialização / Autoridade / Confiabilidade (E-E-A-T) (além de abrangência, originalidade, legibilidade e evidências).

---

## Instalação (como uma skill de agente)

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

Ou simplesmente copie `SKILL.md` + `frameworks/` + `schemas/` para o diretório de skills do seu agente. Cada arquivo é Markdown/YAML sem dependências — sem aprisionamento (lock-in).

1. Copie `schemas/brand.example.yaml` → `brand.yaml`, preencha a voz da sua marca, o público, os autores (para E-E-A-T) e a estrutura de URLs.
2. Aponte seu agente para `SKILL.md` e execute o volante para um tema.
3. Os frameworks são injetados automaticamente nas etapas de planejamento e redação.

---

## Quer que façam por você?

Este repositório é a **metodologia aberta**. Se você preferir uma **API automatizada e hospedada** — auditorias, conteúdo GEO/SEO e correção automática que injeta meta tags otimizadas na edge, sem configuração — acesse **[1wayseo.com](https://1wayseo.com)**.

---

## Créditos e Licença

- Os frameworks de qualidade de conteúdo **CORE-EEAT** e de confiança de domínio **CITE** são adaptados de [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0). Obrigado.
- Licenciado sob **Apache-2.0** — veja [LICENSE](LICENSE).

Contribuições são bem-vindas. Abra uma issue ou PR.
