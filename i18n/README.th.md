<!-- LANGS:th -->
> Thai. [English](../README.md)

# Content Flywheel — ทักษะการผลิตเนื้อหา SEO และ GEO

**ระเบียบวิธีการผลิตเนื้อหาแบบเปิดสำหรับ AI agent** ค้นคว้าหัวข้อ วางแผนด้วยโมเดลที่มีการให้เหตุผลแข็งแกร่งที่สุด ร่างเนื้อหา ลบกลิ่นอาย AI ออก รันด่านตรวจคุณภาพ GEO/SEO กระจายต่อไปยังโซเชียล เผยแพร่ และป้อนข้อมูลเชิงวิเคราะห์กลับเข้าสู่รอบถัดไป — ในรูปแบบทักษะที่นำกลับมาใช้ซ้ำได้สำหรับ Claude Code, Cursor, Codex CLI, Gemini CLI และ agent ใดก็ตามที่โหลดทักษะแบบ Markdown ได้

> สร้างขึ้นเพื่อ **Generative Engine Optimization (GEO)** — เนื้อหาที่เครื่องมือค้นหา AI (ChatGPT, Perplexity, Google AI Overviews) อ้างอิงถึงจริง ๆ — บนพื้นฐานของ SEO แบบดั้งเดิม

🌐 **ภาษา:** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## วงล้อหมุน (The Flywheel)

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| เฟส | สิ่งที่เกิดขึ้น | บทบาท agent ที่เหมาะที่สุด |
|-------|--------------|---------------------|
| **1. Research** | เทรนด์ เจตนาของ SERP ช่องว่างของคู่แข่ง ความต้องการของผู้ชม | โมเดลสำหรับการค้นคว้า/grounding |
| **2a. Plan** | โครงร่าง (H2/H3) ใจความหลัก แผนลิงก์ภายใน CTA แผนข้อมูลแบบมีโครงสร้าง | **โมเดลที่ให้เหตุผลแข็งแกร่งที่สุด** |
| **2b. Draft** | เขียนเนื้อความเต็มตามแผน | โมเดลร่างเนื้อหาที่รวดเร็ว |
| **2c. De-AI** | ตัดคำฟุ่มเฟือย ถ้อยคำดาด ๆ และ "ร่องรอยของ AI" ออก | โมเดลแก้ไขที่รวดเร็ว |
| **2d. Quality gate** | ให้คะแนนร่างตามกฎ **CORE-EEAT** + **GEO** และระบุช่องว่าง | โมเดลสำหรับการตรวจทาน |
| **3–4. Fan-out** | แตกออกเป็นข้อความเฉพาะแพลตฟอร์ม (FB/IG/Threads/X/LinkedIn) + carousel | โมเดลด้านเลย์เอาต์/คัดลอกเนื้อหา |
| **5. Technical SEO** | Schema/JSON-LD, Core Web Vitals (INP/LCP/CLS) | โมเดลด้านเทคนิค |
| **6. Publish** | เผยแพร่บทความ + ตั้งเวลาโพสต์โซเชียล | ระบบอัตโนมัติ |
| **7. Feedback** | ข้อมูลเชิงวิเคราะห์ → ปรับน้ำหนักของเสาหลักเนื้อหา + ความถี่ | โมเดลที่ให้เหตุผล |

**คะแนนความน่าเชื่อถือ (trust score)** เป็นตัวตัดสินว่าแต่ละรอบการทำงานจะเป็นอัตโนมัติมากเพียงใด — ตั้งแต่ "หยุดเพื่อให้มนุษย์ตรวจทานในทุกขั้นตอน" ไปจนถึง "อัตโนมัติเต็มรูปแบบ" — และจะเพิ่มขึ้นหรือลดลงตามปริมาณที่คุณแก้ไขผลลัพธ์

---

## เฟรมเวิร์ก GEO/SEO

คุณภาพของผลลัพธ์มาจากเฟรมเวิร์ก ไม่ใช่จากความรู้สึก ดูได้ที่ [`frameworks/`](../frameworks/):

- **[GEO techniques](../frameworks/geo-techniques.md)** — การปรับแต่งคำนิยาม (ขึ้นต้นด้วยคำศัพท์ ความยาว 25–50 คำ อ้างอิงได้ในฐานะคำตอบที่สมบูรณ์ในตัวเอง) ข้อความที่ยกไปอ้างได้ (สถิติ/ข้อเท็จจริง/การเปรียบเทียบ) สัญญาณความน่าเชื่อถือ โครงสร้างถาม-ตอบ และความหนาแน่นของข้อเท็จจริง เพื่อให้ generative engine อ้างถึงคุณ
- **[SEO writing checklist](../frameworks/seo-writing-checklist.md)** — การวางคีย์เวิร์ด การจับคู่เจตนาของการค้นหา ความอ่านง่าย การลิงก์ภายใน/ภายนอก และการเล็งเป้าหมาย featured snippet
- **[CORE-EEAT dimensions](../frameworks/core-eeat-dimensions.md)** — ด่านเผยแพร่ตามมิติ Experience / Expertise / Authoritativeness / Trustworthiness (รวมถึงความครอบคลุม ความเป็นต้นฉบับ ความอ่านง่าย และหลักฐาน)

---

## การติดตั้ง (ในฐานะทักษะของ agent)

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

หรือเพียงคัดลอก `SKILL.md` + `frameworks/` + `schemas/` เข้าไปยังไดเรกทอรีทักษะของ agent ของคุณ ทุกไฟล์เป็น Markdown/YAML ที่ไม่มี dependency — ไม่มีการล็อกอิน

1. คัดลอก `schemas/brand.example.yaml` → `brand.yaml` แล้วกรอกน้ำเสียงของแบรนด์ ผู้ชม ผู้เขียน (สำหรับ E-E-A-T) และโครงสร้าง URL ของคุณ
2. ชี้ให้ agent ของคุณไปที่ `SKILL.md` แล้วรันวงล้อหมุนสำหรับหัวข้อหนึ่ง ๆ
3. เฟรมเวิร์กจะถูกฉีดเข้าไปในขั้นตอนการวางแผนและการร่างเนื้อหาโดยอัตโนมัติ

---

## อยากให้เราทำให้คุณ?

repo นี้คือ **ระเบียบวิธีแบบเปิด** หากคุณต้องการ **API แบบอัตโนมัติที่โฮสต์ให้พร้อม** — การตรวจสอบ (audit) เนื้อหา GEO/SEO และการแก้ไขอัตโนมัติที่ฉีด meta ที่ปรับแต่งแล้วที่ edge โดยไม่ต้องตั้งค่าใด ๆ — ไปที่ **[1wayseo.com](https://1wayseo.com)**

---

## เครดิตและสัญญาอนุญาต

- เฟรมเวิร์ก **CORE-EEAT** ด้านคุณภาพเนื้อหา และ **CITE** ด้านความน่าเชื่อถือของโดเมน ดัดแปลงมาจาก [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0) ขอบคุณครับ
- อยู่ภายใต้สัญญาอนุญาต **Apache-2.0** — ดูที่ [LICENSE](../LICENSE)

ยินดีรับการมีส่วนร่วม เปิด issue หรือ PR ได้เลย
