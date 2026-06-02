<!-- LANGS:ja -->
> Japanese. [English](../README.md)

# Content Flywheel — SEO & GEO コンテンツスキル

**AI エージェントのためのオープンなコンテンツ制作方法論。** トピックをリサーチし、最も強力な推論モデルでプランニングし、ドラフトを書き、AI 臭さを除去し、GEO/SEO の品質ゲートを通し、ソーシャルへ展開し、公開し、アナリティクスを次のサイクルへフィードバックする — Claude Code、Cursor、Codex CLI、Gemini CLI、そして Markdown スキルを読み込めるあらゆるエージェントで再利用できるスキルとして。

> 古典的な SEO の上に、**Generative Engine Optimization (GEO)** — AI 検索エンジン（ChatGPT、Perplexity、Google AI Overviews）が実際に引用するコンテンツ — のために構築されています。

🌐 **言語:** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## フライホイール

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| フェーズ | 何が起こるか | 最適なエージェントの役割 |
|-------|--------------|---------------------|
| **1. Research** | トレンド、SERP の意図、競合のギャップ、オーディエンスのニーズ | リサーチ／グラウンディング向けモデル |
| **2a. Plan** | アウトライン（H2/H3）、論旨、内部リンク計画、CTA、構造化データ計画 | **最も強力な推論モデル** |
| **2b. Draft** | 計画に沿って書かれた本文全体 | 高速なドラフト用モデル |
| **2c. De-AI** | 埋め草、ありきたりな言い回し、「AI らしさ」を削ぎ落とす | 高速な編集用モデル |
| **2d. Quality gate** | **CORE-EEAT** ＋ **GEO** ルールに照らしてドラフトを採点し、ギャップを列挙する | レビュー用モデル |
| **3–4. Fan-out** | プラットフォーム別コピー（FB/IG/Threads/X/LinkedIn）＋カルーセルへ分割 | レイアウト／コピー用モデル |
| **5. Technical SEO** | スキーマ／JSON-LD、Core Web Vitals（INP/LCP/CLS） | テクニカル向けモデル |
| **6. Publish** | 記事の公開＋ソーシャルのスケジュール設定 | 自動化 |
| **7. Feedback** | アナリティクス → コンテンツピラーの重み付け＋頻度を調整 | 推論モデル |

**信頼スコア**が各実行の自律度を決めます — 「あらゆるステップで人間のレビューのために一時停止する」から「完全自動化」まで — そして出力をどれだけ編集するかに応じて上下します。

---

## GEO/SEO フレームワーク

出力の品質は、雰囲気ではなくフレームワークから生まれます。[`frameworks/`](frameworks/) を参照してください。

- **[GEO techniques](frameworks/geo-techniques.md)** — 定義の最適化（用語を先頭に、25〜50 語、単独の回答として引用可能）、引用に値する記述（統計／事実／比較）、権威性のシグナル、Q&A 構造、そして生成エンジンがあなたを引用するための事実密度。
- **[SEO writing checklist](frameworks/seo-writing-checklist.md)** — キーワードの配置、検索意図との一致、可読性、内部／外部リンク、強調スニペットのターゲティング。
- **[CORE-EEAT dimensions](frameworks/core-eeat-dimensions.md)** — Experience / Expertise / Authoritativeness / Trustworthiness の公開ゲート（加えて網羅性、独自性、可読性、エビデンス）。

---

## インストール（エージェントスキルとして）

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

あるいは、`SKILL.md` ＋ `frameworks/` ＋ `schemas/` をエージェントのスキルディレクトリにコピーするだけでも構いません。すべてのファイルは依存関係ゼロの Markdown/YAML で、ロックインはありません。

1. `schemas/brand.example.yaml` → `brand.yaml` をコピーし、ブランドボイス、オーディエンス、著者（E-E-A-T のため）、URL 構造を記入します。
2. エージェントを `SKILL.md` に向け、トピックに対してフライホイールを実行します。
3. フレームワークはプランニングとドラフトのステップに自動的に注入されます。

---

## 代わりにやってほしいですか？

このリポジトリは**オープンな方法論**です。むしろ**自動化されたホスト型 API** — 監査、GEO/SEO コンテンツ、そして最適化されたメタをエッジで注入する自動修正、セットアップ不要 — が欲しい場合は、**[1wayseo.com](https://1wayseo.com)** へどうぞ。

---

## クレジット＆ライセンス

- **CORE-EEAT** コンテンツ品質フレームワークと **CITE** ドメイン信頼性フレームワークは、[aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills)（Apache-2.0）を基に改変しています。ありがとうございます。
- **Apache-2.0** の下でライセンスされています — [LICENSE](LICENSE) を参照してください。

コントリビューション歓迎です。issue または PR を開いてください。
