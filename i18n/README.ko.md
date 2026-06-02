<!-- LANGS:ko -->
> Korean. [English](../README.md)

# Content Flywheel — SEO & GEO 콘텐츠 스킬

**AI 에이전트를 위한 오픈 콘텐츠 제작 방법론.** 주제를 리서치하고, 가장 강력한 추론 모델로 기획하고, 초안을 작성하고, AI 티를 제거하고, GEO/SEO 품질 게이트를 실행하고, 소셜로 확산하고, 발행한 뒤, 분석 데이터를 다음 사이클에 다시 반영합니다 — Claude Code, Cursor, Codex CLI, Gemini CLI, 그리고 Markdown 스킬을 로드하는 모든 에이전트를 위한 재사용 가능한 스킬로 제공됩니다.

> 고전적인 SEO 위에 더해, **Generative Engine Optimization (GEO)** — AI 검색 엔진(ChatGPT, Perplexity, Google AI Overviews)이 실제로 인용하는 콘텐츠 — 를 위해 만들어졌습니다.

🌐 **Languages:** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## 플라이휠

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| 단계 | 무슨 일이 일어나는가 | 가장 적합한 에이전트 역할 |
|-------|--------------|---------------------|
| **1. 리서치** | 트렌드, SERP 의도, 경쟁사 공백, 오디언스 니즈 | 리서치/그라운딩 모델 |
| **2a. 기획** | 아웃라인(H2/H3), 논지, 내부 링크 계획, CTA, 구조화 데이터 계획 | **가장 강력한 추론 모델** |
| **2b. 초안 작성** | 계획에 맞춰 전체 본문 작성 | 빠른 초안 작성 모델 |
| **2c. AI 티 제거** | 군더더기, 진부한 표현, "AI 티"를 제거 | 빠른 편집 모델 |
| **2d. 품질 게이트** | 초안을 **CORE-EEAT** + **GEO** 규칙으로 채점하고 공백 목록화 | 리뷰 모델 |
| **3–4. 확산** | 플랫폼 카피(FB/IG/Threads/X/LinkedIn) + 캐러셀로 분할 | 레이아웃/카피 모델 |
| **5. 기술 SEO** | 스키마/JSON-LD, Core Web Vitals (INP/LCP/CLS) | 기술 모델 |
| **6. 발행** | 아티클 발행 + 소셜 예약 | 자동화 |
| **7. 피드백** | 분석 → 콘텐츠 필러 가중치 + 발행 주기 조정 | 추론 모델 |

**신뢰 점수(trust score)** 가 각 실행이 얼마나 자율적으로 진행될지를 결정합니다 — "매 단계마다 사람의 검토를 위해 멈춤"부터 "완전 자동화"까지 — 그리고 결과물을 얼마나 수정하는지에 따라 오르거나 내려갑니다.

---

## GEO/SEO 프레임워크

결과물의 품질은 감(感)이 아니라 프레임워크에서 나옵니다. [`frameworks/`](../frameworks/)를 참고하세요:

- **[GEO 기법](../frameworks/geo-techniques.md)** — 정의 최적화(용어 우선, 25–50 단어, 독립형 답변으로 인용 가능), 인용 가능한 진술(통계/사실/비교), 권위 신호, Q&A 구조, 그리고 생성형 엔진이 당신을 인용하도록 만드는 사실 밀도.
- **[SEO 작성 체크리스트](../frameworks/seo-writing-checklist.md)** — 키워드 배치, 검색 의도 매칭, 가독성, 내부/외부 링크, 그리고 featured snippet 타기팅.
- **[CORE-EEAT 차원](../frameworks/core-eeat-dimensions.md)** — Experience / Expertise / Authoritativeness / Trustworthiness 발행 게이트(여기에 포괄성, 독창성, 가독성, 근거를 더함).

---

## 설치 (에이전트 스킬로)

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

또는 `SKILL.md` + `frameworks/` + `schemas/`를 에이전트의 스킬 디렉터리에 복사하기만 하면 됩니다. 모든 파일은 의존성이 없는 Markdown/YAML이며 — 종속(lock-in)이 없습니다.

1. `schemas/brand.example.yaml` → `brand.yaml`로 복사하고, 브랜드 보이스, 오디언스, 저자(E-E-A-T용), URL 구조를 채워 넣으세요.
2. 에이전트가 `SKILL.md`를 바라보게 하고 어떤 주제로 플라이휠을 실행하세요.
3. 프레임워크는 기획 및 초안 작성 단계에 자동으로 주입됩니다.

---

## 대신 해드릴까요?

이 저장소는 **오픈 방법론**입니다. 만약 **자동화되고 호스팅되는 API** — 감사(audit), GEO/SEO 콘텐츠, 그리고 최적화된 메타를 엣지에서 주입하는 자동 수정, 별도 설정 불필요 — 를 원하신다면 **[1wayseo.com](https://1wayseo.com)**으로 가세요.

---

## 크레딧 및 라이선스

- **CORE-EEAT** 콘텐츠 품질 프레임워크와 **CITE** 도메인 신뢰 프레임워크는 [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0)에서 차용했습니다. 감사합니다.
- **Apache-2.0**로 라이선스됩니다 — [LICENSE](../LICENSE)를 참고하세요.

기여를 환영합니다. 이슈나 PR을 열어주세요.
