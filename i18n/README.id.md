<!-- LANGS:id -->
> Indonesian. [English](../README.md)

# Content Flywheel — Skill Konten SEO & GEO

**Sebuah metodologi produksi konten terbuka untuk agen AI.** Riset sebuah topik, rencanakan dengan model penalaran terkuat, susun draf, hilangkan kesan AI, jalankan gerbang mutu GEO/SEO, sebarkan ke media sosial, terbitkan, dan umpankan analitik kembali ke siklus berikutnya — sebagai skill yang dapat digunakan ulang untuk Claude Code, Cursor, Codex CLI, Gemini CLI, dan agen apa pun yang memuat skill Markdown.

> Dibangun untuk **Generative Engine Optimization (GEO)** — konten yang benar-benar dikutip oleh mesin pencari AI (ChatGPT, Perplexity, Google AI Overviews) — di atas SEO klasik.

🌐 **Bahasa:** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## Roda Gila (Flywheel)

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| Fase | Apa yang terjadi | Peran agen paling cocok |
|-------|--------------|---------------------|
| **1. Riset** | Tren, intensi SERP, celah pesaing, kebutuhan audiens | sebuah model riset/grounding |
| **2a. Rencana** | Kerangka (H2/H3), tesis, rencana tautan internal, CTA, rencana data terstruktur | **model penalaran terkuat** |
| **2b. Draf** | Prosa lengkap ditulis sesuai rencana | sebuah model penyusunan draf yang cepat |
| **2c. De-AI** | Buang pengganjal, frasa generik, "ciri AI" | sebuah model penyuntingan yang cepat |
| **2d. Gerbang mutu** | Nilai draf terhadap aturan **CORE-EEAT** + **GEO**; daftar celahnya | sebuah model peninjau |
| **3–4. Penyebaran** | Pecah menjadi salinan per platform (FB/IG/Threads/X/LinkedIn) + carousel | sebuah model tata letak/salinan |
| **5. SEO Teknis** | Schema/JSON-LD, Core Web Vitals (INP/LCP/CLS) | sebuah model teknis |
| **6. Terbit** | Terbitkan artikel + jadwalkan media sosial | otomasi |
| **7. Umpan balik** | Analitik → setel bobot pilar konten + irama | model penalaran |

Sebuah **skor kepercayaan** menentukan seberapa otonom setiap proses dijalankan — dari "berhenti untuk tinjauan manusia di setiap langkah" hingga "sepenuhnya otomatis" — dan naik atau turun berdasarkan seberapa banyak Anda menyunting keluarannya.

---

## Kerangka Kerja GEO/SEO

Kualitas keluaran berasal dari kerangka kerja, bukan dari perasaan. Lihat [`frameworks/`](../frameworks/):

- **[Teknik GEO](../frameworks/geo-techniques.md)** — optimasi definisi (istilah dulu, 25–50 kata, dapat dikutip sebagai jawaban berdiri sendiri), pernyataan yang dapat dikutip (statistik/fakta/perbandingan), sinyal otoritas, struktur Tanya Jawab, dan kepadatan faktual agar mesin generatif mengutip Anda.
- **[Daftar periksa penulisan SEO](../frameworks/seo-writing-checklist.md)** — penempatan kata kunci, kecocokan intensi pencarian, keterbacaan, penautan internal/eksternal, dan penargetan cuplikan unggulan (featured snippet).
- **[Dimensi CORE-EEAT](../frameworks/core-eeat-dimensions.md)** — gerbang penerbitan Experience / Expertise / Authoritativeness / Trustworthiness (ditambah kelengkapan, orisinalitas, keterbacaan, bukti).

---

## Pasang (sebagai skill agen)

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

Atau cukup salin `SKILL.md` + `frameworks/` + `schemas/` ke direktori skill agen Anda. Setiap berkas adalah Markdown/YAML tanpa dependensi — tanpa keterikatan vendor.

1. Salin `schemas/brand.example.yaml` → `brand.yaml`, isi dengan suara merek, audiens, penulis (untuk E-E-A-T), dan struktur URL Anda.
2. Arahkan agen Anda ke `SKILL.md` dan jalankan flywheel untuk sebuah topik.
3. Kerangka kerja disuntikkan ke langkah perencanaan dan penyusunan draf secara otomatis.

---

## Ingin dikerjakan untuk Anda?

Repo ini adalah **metodologi terbuka**. Jika Anda lebih memilih **API terkelola dan ter-hosting** — audit, konten GEO/SEO, dan perbaikan otomatis yang menyuntikkan meta teroptimasi di edge, tanpa penyiapan — kunjungi **[1wayseo.com](https://1wayseo.com)**.

---

## Kredit & Lisensi

- Kerangka kerja mutu konten **CORE-EEAT** dan kepercayaan domain **CITE** diadaptasi dari [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0). Terima kasih.
- Dilisensikan di bawah **Apache-2.0** — lihat [LICENSE](../LICENSE).

Kontribusi dipersilakan. Buka issue atau PR.
