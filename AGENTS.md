# Agent Guidance

## Scope

This repository is a dependency-free Markdown/YAML skill package for the
Content Flywheel SEO/GEO workflow. Keep changes portable across agent hosts:
Claude Code, Cursor, Codex CLI, Gemini CLI, and generic Markdown skill loaders.

## Boundaries

- Do not add runtime dependencies unless the skill package genuinely needs
  them; prefer standard-library validation and plain Markdown/YAML assets.
- Do not commit brand-specific `brand.yaml`, analytics credentials, customer
  data, generated article drafts, or publishing ledgers.
- Example schemas must stay placeholders. Use variable names and fake domains,
  never raw API keys, analytics IDs, passwords, or private URLs.
- Localized README files should stay aligned with the English README's install
  and framework references.

## Verification

Run the package validator before claiming a change is complete:

```bash
npm test
npm run check
```

`npm run check` validates required skill files, local Markdown links, localized
README shape, and example schema top-level keys without external services.

## Review Log

Continue audit/remediation notes in `docs/review-log.md`. The cross-project
central run is tracked in `/Volumes/500G/Claude Code Projects/Codex Code Review/security-reviews/2026-06-27-active-30d`.
