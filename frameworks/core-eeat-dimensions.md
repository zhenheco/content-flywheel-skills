# CORE-EEAT — content quality publish gate

> Score a draft against these dimensions before publishing. Inspired by the CORE-EEAT benchmark from [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0). Use it as the quality gate at phase 2d of the flywheel.

For each dimension, rate the draft and list concrete gaps to fix before publishing.

| Dimension | What "good" looks like |
|-----------|------------------------|
| **Experience** | First-hand use, real examples, screenshots, "we tried X and Y happened" — not generic theory. |
| **Expertise** | Correct, current, technically precise; depth a non-expert could not fake. |
| **Authoritativeness** | Bylined author with credentials; cites primary/authoritative sources; named case studies. |
| **Trustworthiness** | Accurate, transparent about limitations, no unsupported claims, clear sourcing, up-to-date. |
| **Comprehensiveness** | Fully answers the search intent and the obvious follow-up questions; no thin sections. |
| **Originality** | Adds insight, data, or a point of view not already in the top results. |
| **Readability** | Scannable structure, short paragraphs, tables/lists for dense points, plain language. |
| **Evidence** | Every claim that needs proof has a number, source, example, or demonstration. |

**Gate rule:** if any dimension is weak, fix it before publishing. A draft that scores high here is also the draft most likely to be **cited by generative engines** — see [GEO techniques](geo-techniques.md).
