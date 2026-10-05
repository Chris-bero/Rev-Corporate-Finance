# FIN211 — Corporate Finance Learning Platform
**Prepared by / إعداد: 领袖 - EBRA**
### منصة تعلّم المالية الإدارية (FIN211) + لوحة المعلم + نسخ الطباعة

Bilingual (English/Arabic) educational platform built entirely from the course lecture
materials (Lectures 1–13). No frameworks, no build step, no internet required —
every file opens directly in a browser.

منصة تعليمية ثنائية اللغة مبنية بالكامل من محاضرات المقرر (١–١٣). بدون أطر عمل وبدون
خطوة بناء وبدون إنترنت — كل ملف يُفتح مباشرة في المتصفح.

---

## 📁 Contents / المحتويات

| Path | What it is / ما هو |
|---|---|
| `website/index.html` | **Student platform** — 9 chapters / 17 lessons, 50 formulas, 18 concepts, 59+ glossary terms, abbreviations page, embedded cheat sheet, review center, global search (EN/AR), dark mode, name-only sign-in with progress & visit tracking. · موقع الطلاب الكامل |
| `website/teacher.html` | **Teacher dashboard** (PIN-protected, default `211`) — students, visits, progress %, per-lesson completion bars, per-student detail, CSV export. · لوحة المعلم |
| `website/google_apps_script.gs` | Backend for Google Sheets (Apps Script). Stores names, visits, progress. · خلفية جوجل شيت |
| `website/fin211-cheatsheet.html` | Standalone cheat sheet (same copy embedded inside the student site). · الورقة المختصرة المستقلة |
| `prints/FIN211_Cheat_Sheet_A4.pdf` / `.docx` | Printable cheat sheet, A4, chapter-per-page, no split tables/formulas. · ورقة المختصرات للطباعة |
| `prints/FIN211_Formulas_Abbrev_Definitions_A4.pdf` / `.docx` | Numbered reference: **F01–F50** formulas, **A01–A57** abbreviations, **D01–D69** definitions (bilingual). · المرجع المرقّم |
| `prints/FIN211_Course_Book_A4.pdf` / `.docx` | Course study book: cover, TOC with page numbers, and the full core explanation of all 17 lessons (bilingual, with worked examples). · كتاب الشرح الدراسي الكامل |
| `tools/` | Generators (`make_copies.py`, `make_reference.py`, `make_book.py`, `dump_full.js`, data JSONs) to regenerate all print files after any content change. · مولّدات نسخ الطباعة |

---

## 🚀 Quick start / التشغيل السريع

**Students / الطلاب:** open `website/index.html` → enter your name (no password) → learn.
Progress, bookmarks and visits are saved to the course Google Sheet when online,
or locally on the device when offline (indicator ☁ / ⚠ / 🖥).
افتح `index.html` ← أدخل اسمك (بدون كلمة مرور) ← تعلّم. يُحفظ تقدمك في جوجل شيت عند
توفر الإنترنت ومحليًا على الجهاز بدونه.

**Teacher / المعلم:** open `website/teacher.html` → PIN **211** (change it in the file:
`var TEACHER_PIN = "211";`). Full statistics + CSV export.
افتح `teacher.html` ← الرمز **211** (غيّره من السطر `TEACHER_PIN`).

**Google Sheets backend / خلفية جوجل شيت:**
1. New Google Sheet → *Extensions → Apps Script* → paste `google_apps_script.gs` → Save.
2. *Deploy → New deployment → Web app* → Execute as: **Me** · Who has access: **Anyone** → Deploy.
3. Copy the `/exec` URL. It is already pre-configured in `index.html`
   (`DEFAULT_SCRIPT_URL`); to change it, edit that constant.
   انسخ رابط `/exec` وهو مضبوط مسبقًا داخل `index.html` في الثابت `DEFAULT_SCRIPT_URL`.

**Printing / الطباعة:** all print files are A4 with chapter-per-page breaks;
tables, formulas and callouts never split across pages.
كل ملفات الطباعة A4 بقواعد فصول/صفحات نظيفة لا تقطع جدولًا أو معادلة.

---

## 🔁 Regenerating print files / إعادة توليد نسخ الطباعة

```bash
# after editing website content:
node -e '/* dump DATA from website/index.html to tools/data.json (see repo history) */'
python3 tools/make_copies.py       # cheat sheet PDF + DOCX
python3 tools/make_reference.py    # numbered formulas/abbreviations/definitions PDF + DOCX
```

---

## 📝 Notes / ملاحظات
- No passwords anywhere: students are identified by name only (as requested).
  لا كلمات مرور: الطلاب يُعرَّفون بالاسم فقط.
- The teacher PIN gates the dashboard on the device only; the Sheets endpoint
  itself follows the deployment's Google access settings.
- Academic source of truth = the lecture slides; slide misprints are corrected
  with explicit transparency notes inside the lessons.
