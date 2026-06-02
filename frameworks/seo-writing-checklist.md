# SEO Writing Checklist

> Compact checklist for drafting content that is useful, scannable, and ready for a CORE-EEAT review. Adapted from [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0).

## On-page checklist

| Area | Required checks |
|------|-----------------|
| **Keyword placement** | Primary keyword in title, H1, first 100 words, ≥1 H2, conclusion, and meta description; secondary terms in H2/H3; related entities throughout the body. |
| **Search intent** | Content type, angle, depth, and CTA match the dominant SERP intent; mixed-intent pages answer the primary intent first. |
| **Quality** | Comprehensive coverage, original insight or data, actionable takeaways, examples, and expert/source support where claims need evidence. |
| **Readability** | 3–5 sentence paragraphs, varied sentence length, bullets/tables for dense points, bold only for key phrases, and a table of contents for long-form. |
| **Technical** | 2–5 relevant internal links, 2–3 authoritative external links, descriptive image alt text, concise keyword-led URL slug. |
| **Snippet targeting** | Definition answers in 40–60 words, ordered steps for how-to queries, tables for comparisons, concise FAQ answers. |

## Copy-start template

```markdown
# [H1 with Primary Keyword]

**Meta Description:** [150–160 char value proposition with keyword and CTA]

[Hook] [Problem statement] [Promise: what the reader will learn] [Primary keyword used naturally]

## [H2 with Secondary Keyword]
[1–2 sentence setup]
[Useful explanation with evidence, examples, or data]

### [H3 if needed]
- [Actionable point]
- [Actionable point]

## [H2 for next major section]
> **Pro Tip:** [Specific, non-obvious implementation note]

| Comparison point | Option A | Option B |
|------------------|----------|----------|
| [Factor] | [Evidence] | [Evidence] |
```

## Core Web Vitals are part of SEO

Treat Core Web Vitals as a content baseline, not a frontend afterthought:

- **INP ≤ 200ms** — avoid heavy synchronous JS and third-party widgets on first interaction.
- **LCP ≤ 2.5s** — never block the hero image / H1 with JS, animations, or font chains.
- **CLS ≤ 0.1** — reserve dimensions for every image, iframe, and embed.

Ship static content first; lazy-load images (`loading="lazy"`, `decoding="async"`, explicit `width`/`height`); defer all third-party scripts.
