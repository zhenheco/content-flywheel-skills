<!-- LANGS:vi -->
> Vietnamese. [English](../README.md)

# Content Flywheel — Kỹ năng nội dung SEO & GEO

**Một phương pháp sản xuất nội dung mã nguồn mở dành cho các AI agent.** Nghiên cứu một chủ đề, lập kế hoạch bằng mô hình suy luận mạnh nhất, soạn thảo, loại bỏ dấu vết AI, chạy cổng kiểm soát chất lượng GEO/SEO, phân nhánh ra mạng xã hội, xuất bản, và đưa dữ liệu phân tích trở lại chu kỳ tiếp theo — dưới dạng một kỹ năng tái sử dụng cho Claude Code, Cursor, Codex CLI, Gemini CLI, và bất kỳ agent nào có thể nạp các kỹ năng định dạng Markdown.

> Được xây dựng cho **Generative Engine Optimization (GEO)** — nội dung mà các công cụ tìm kiếm AI (ChatGPT, Perplexity, Google AI Overviews) thực sự trích dẫn — trên nền tảng SEO cổ điển.

🌐 **Ngôn ngữ:** [English](../README.md) · [繁體中文](README.zh-Hant.md) · [简体中文](README.zh-Hans.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Español](README.es.md) · [Português](README.pt.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Italiano](README.it.md) · [Русский](README.ru.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [Bahasa Indonesia](README.id.md) · [Tiếng Việt](README.vi.md) · [ไทย](README.th.md) · [Türkçe](README.tr.md) · [Nederlands](README.nl.md)

---

## Bánh đà (The Flywheel)

```
  ┌─────────────────────────────────────────────────────────┐
  │                                                         ↓
Research → Plan → Draft → De-AI → GEO/SEO Quality Gate → Publish → Feedback
  ↑                                                                   │
  └───────────────────  analytics tune the next cycle  ───────────────┘
```

| Giai đoạn | Diễn biến | Vai trò agent phù hợp nhất |
|-------|--------------|---------------------|
| **1. Nghiên cứu** | Xu hướng, ý định SERP, khoảng trống của đối thủ, nhu cầu khán giả | một mô hình nghiên cứu/định cơ sở |
| **2a. Lập kế hoạch** | Dàn ý (H2/H3), luận điểm, kế hoạch liên kết nội bộ, CTA, kế hoạch dữ liệu có cấu trúc | **mô hình suy luận mạnh nhất** |
| **2b. Soạn thảo** | Toàn bộ văn xuôi viết theo kế hoạch | một mô hình soạn thảo nhanh |
| **2c. Loại bỏ dấu vết AI** | Loại bỏ từ thừa, cách diễn đạt chung chung, "dấu hiệu AI" | một mô hình biên tập nhanh |
| **2d. Cổng kiểm soát chất lượng** | Chấm điểm bản nháp theo quy tắc **CORE-EEAT** + **GEO**; liệt kê các thiếu sót | một mô hình đánh giá |
| **3–4. Phân nhánh** | Tách thành nội dung cho từng nền tảng (FB/IG/Threads/X/LinkedIn) + carousel | một mô hình bố cục/nội dung |
| **5. SEO kỹ thuật** | Schema/JSON-LD, Core Web Vitals (INP/LCP/CLS) | một mô hình kỹ thuật |
| **6. Xuất bản** | Xuất bản bài viết + lên lịch mạng xã hội | tự động hóa |
| **7. Phản hồi** | Phân tích dữ liệu → điều chỉnh trọng số trụ cột nội dung + tần suất | mô hình suy luận |

Một **điểm tin cậy** (trust score) quyết định mức độ tự chủ của mỗi lần chạy — từ "tạm dừng để con người xem xét ở mọi bước" đến "hoàn toàn tự động" — và tăng hoặc giảm dựa trên mức độ bạn chỉnh sửa kết quả đầu ra.

---

## Các khung GEO/SEO

Chất lượng đầu ra đến từ các khung phương pháp, không phải từ cảm tính. Xem [`frameworks/`](../frameworks/):

- **[Kỹ thuật GEO](../frameworks/geo-techniques.md)** — tối ưu hóa định nghĩa (đặt thuật ngữ lên đầu, 25–50 từ, có thể trích dẫn như một câu trả lời độc lập), các phát biểu có thể trích dẫn (số liệu thống kê/dữ kiện/so sánh), tín hiệu uy tín, cấu trúc Hỏi & Đáp, và mật độ dữ kiện để các generative engine trích dẫn bạn.
- **[Danh sách kiểm tra viết SEO](../frameworks/seo-writing-checklist.md)** — đặt từ khóa, khớp ý định tìm kiếm, độ dễ đọc, liên kết nội bộ/bên ngoài, và nhắm tới featured snippet.
- **[Các chiều CORE-EEAT](../frameworks/core-eeat-dimensions.md)** — một cổng xuất bản theo Experience / Expertise / Authoritativeness / Trustworthiness (cộng thêm tính toàn diện, tính nguyên bản, độ dễ đọc, bằng chứng).

---

## Cài đặt (như một kỹ năng agent)

```bash
# Claude Code (plugin marketplace)
/plugin marketplace add zhenheco/content-flywheel-skills

# skills.sh / generic Agent Skills hosts
npx skills add zhenheco/content-flywheel-skills
```

Hoặc chỉ cần sao chép `SKILL.md` + `frameworks/` + `schemas/` vào thư mục kỹ năng của agent. Mọi tệp đều là Markdown/YAML không phụ thuộc — không bị khóa nhà cung cấp.

1. Sao chép `schemas/brand.example.yaml` → `brand.yaml`, điền giọng điệu thương hiệu, khán giả, tác giả (cho E-E-A-T), và cấu trúc URL của bạn.
2. Trỏ agent của bạn vào `SKILL.md` và chạy bánh đà cho một chủ đề.
3. Các khung phương pháp được đưa vào các bước lập kế hoạch và soạn thảo một cách tự động.

---

## Muốn được làm hộ?

Kho lưu trữ này là **phương pháp mã nguồn mở**. Nếu bạn muốn có một **API được lưu trữ, tự động** — kiểm toán, nội dung GEO/SEO, và tự động sửa lỗi để chèn meta đã được tối ưu ngay tại edge, không cần thiết lập — hãy truy cập **[1wayseo.com](https://1wayseo.com)**.

---

## Ghi nhận & Giấy phép

- Các khung chất lượng nội dung **CORE-EEAT** và độ tin cậy miền **CITE** được điều chỉnh từ [aaron-he-zhu/seo-geo-claude-skills](https://github.com/aaron-he-zhu/seo-geo-claude-skills) (Apache-2.0). Xin cảm ơn.
- Được cấp phép theo **Apache-2.0** — xem [LICENSE](../LICENSE).

Hoan nghênh đóng góp. Hãy mở một issue hoặc PR.
