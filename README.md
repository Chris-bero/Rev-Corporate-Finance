# FIN211 â€” Corporate Finance Learning Platform
**Prepared by / Ø¥Ø¹Ø¯Ø§Ø¯: é¢†è¢– - EBRA**
### Ù…Ù†ØµØ© ØªØ¹Ù„Ù‘Ù… Ø§Ù„Ù…Ø§Ù„ÙŠØ© Ø§Ù„Ø¥Ø¯Ø§Ø±ÙŠØ© (FIN211) + Ù„ÙˆØ­Ø© Ø§Ù„Ù…Ø¹Ù„Ù… + Ù†Ø³Ø® Ø§Ù„Ø·Ø¨Ø§Ø¹Ø©

Bilingual (English/Arabic) educational platform built entirely from the course lecture
materials (Lectures 1â€“13). No frameworks, no build step, no internet required â€”
every file opens directly in a browser.

Ù…Ù†ØµØ© ØªØ¹Ù„ÙŠÙ…ÙŠØ© Ø«Ù†Ø§Ø¦ÙŠØ© Ø§Ù„Ù„ØºØ© Ù…Ø¨Ù†ÙŠØ© Ø¨Ø§Ù„ÙƒØ§Ù…Ù„ Ù…Ù† Ù…Ø­Ø§Ø¶Ø±Ø§Øª Ø§Ù„Ù…Ù‚Ø±Ø± (Ù¡â€“Ù¡Ù£). Ø¨Ø¯ÙˆÙ† Ø£Ø·Ø± Ø¹Ù…Ù„ ÙˆØ¨Ø¯ÙˆÙ†
Ø®Ø·ÙˆØ© Ø¨Ù†Ø§Ø¡ ÙˆØ¨Ø¯ÙˆÙ† Ø¥Ù†ØªØ±Ù†Øª â€” ÙƒÙ„ Ù…Ù„Ù ÙŠÙÙØªØ­ Ù…Ø¨Ø§Ø´Ø±Ø© ÙÙŠ Ø§Ù„Ù…ØªØµÙØ­.

---

## ðŸ“ Contents / Ø§Ù„Ù…Ø­ØªÙˆÙŠØ§Øª

| Path | What it is / Ù…Ø§ Ù‡Ùˆ |
|---|---|
| `index.html` | **Student platform** â€” 9 chapters / 17 lessons, 50 formulas, 18 concepts, 59+ glossary terms, abbreviations page, embedded cheat sheet, review center, global search (EN/AR), dark mode, name-only sign-in with progress & visit tracking. Â· Ù…ÙˆÙ‚Ø¹ Ø§Ù„Ø·Ù„Ø§Ø¨ Ø§Ù„ÙƒØ§Ù…Ù„ |
| `teacher.html` | **Teacher dashboard** (PIN-protected, default `211`) â€” students, visits, progress %, per-lesson completion bars, per-student detail, CSV export. Â· Ù„ÙˆØ­Ø© Ø§Ù„Ù…Ø¹Ù„Ù… |
| `google_apps_script.gs` | Backend for Google Sheets (Apps Script). Stores names, visits, progress. Â· Ø®Ù„ÙÙŠØ© Ø¬ÙˆØ¬Ù„ Ø´ÙŠØª |
| `fin211-cheatsheet.html` | Standalone cheat sheet (same copy embedded inside the student site). Â· Ø§Ù„ÙˆØ±Ù‚Ø© Ø§Ù„Ù…Ø®ØªØµØ±Ø© Ø§Ù„Ù…Ø³ØªÙ‚Ù„Ø© |
| `prints/FIN211_Cheat_Sheet_A4.pdf` / `.docx` | Printable cheat sheet, A4, chapter-per-page, no split tables/formulas. Â· ÙˆØ±Ù‚Ø© Ø§Ù„Ù…Ø®ØªØµØ±Ø§Øª Ù„Ù„Ø·Ø¨Ø§Ø¹Ø© |
| `prints/FIN211_Formulas_Abbrev_Definitions_A4.pdf` / `.docx` | Numbered reference: **F01â€“F50** formulas, **A01â€“A57** abbreviations, **D01â€“D69** definitions (bilingual). Â· Ø§Ù„Ù…Ø±Ø¬Ø¹ Ø§Ù„Ù…Ø±Ù‚Ù‘Ù… |
| `prints/FIN211_Course_Book_A4.pdf` / `.docx` | Course study book: cover, TOC with page numbers, and the full core explanation of all 17 lessons (bilingual, with worked examples). Â· ÙƒØªØ§Ø¨ Ø§Ù„Ø´Ø±Ø­ Ø§Ù„Ø¯Ø±Ø§Ø³ÙŠ Ø§Ù„ÙƒØ§Ù…Ù„ |
| `tools/` | Generators (`make_copies.py`, `make_reference.py`, `make_book.py`, `dump_full.js`, data JSONs) to regenerate all print files after any content change. Â· Ù…ÙˆÙ„Ù‘Ø¯Ø§Øª Ù†Ø³Ø® Ø§Ù„Ø·Ø¨Ø§Ø¹Ø© |

---

## ðŸš€ Quick start / Ø§Ù„ØªØ´ØºÙŠÙ„ Ø§Ù„Ø³Ø±ÙŠØ¹

**Students / Ø§Ù„Ø·Ù„Ø§Ø¨:** open `index.html` â†’ enter your name (no password) â†’ learn.
Progress, bookmarks and visits are saved to the course Google Sheet when online,
or locally on the device when offline (indicator â˜ / âš  / ðŸ–¥).
Ø§ÙØªØ­ `index.html` â† Ø£Ø¯Ø®Ù„ Ø§Ø³Ù…Ùƒ (Ø¨Ø¯ÙˆÙ† ÙƒÙ„Ù…Ø© Ù…Ø±ÙˆØ±) â† ØªØ¹Ù„Ù‘Ù…. ÙŠÙØ­ÙØ¸ ØªÙ‚Ø¯Ù…Ùƒ ÙÙŠ Ø¬ÙˆØ¬Ù„ Ø´ÙŠØª Ø¹Ù†Ø¯
ØªÙˆÙØ± Ø§Ù„Ø¥Ù†ØªØ±Ù†Øª ÙˆÙ…Ø­Ù„ÙŠÙ‹Ø§ Ø¹Ù„Ù‰ Ø§Ù„Ø¬Ù‡Ø§Ø² Ø¨Ø¯ÙˆÙ†Ù‡.

**Teacher / Ø§Ù„Ù…Ø¹Ù„Ù…:** open `teacher.html` â†’ PIN **211** (change it in the file:
`var TEACHER_PIN = "211";`). Full statistics + CSV export.
Ø§ÙØªØ­ `teacher.html` â† Ø§Ù„Ø±Ù…Ø² **211** (ØºÙŠÙ‘Ø±Ù‡ Ù…Ù† Ø§Ù„Ø³Ø·Ø± `TEACHER_PIN`).

**Google Sheets backend / Ø®Ù„ÙÙŠØ© Ø¬ÙˆØ¬Ù„ Ø´ÙŠØª:**
1. New Google Sheet â†’ *Extensions â†’ Apps Script* â†’ paste `google_apps_script.gs` â†’ Save.
2. *Deploy â†’ New deployment â†’ Web app* â†’ Execute as: **Me** Â· Who has access: **Anyone** â†’ Deploy.
3. Copy the `/exec` URL. It is already pre-configured in `index.html`
   (`DEFAULT_SCRIPT_URL`); to change it, edit that constant.
   Ø§Ù†Ø³Ø® Ø±Ø§Ø¨Ø· `/exec` ÙˆÙ‡Ùˆ Ù…Ø¶Ø¨ÙˆØ· Ù…Ø³Ø¨Ù‚Ù‹Ø§ Ø¯Ø§Ø®Ù„ `index.html` ÙÙŠ Ø§Ù„Ø«Ø§Ø¨Øª `DEFAULT_SCRIPT_URL`.

**Printing / Ø§Ù„Ø·Ø¨Ø§Ø¹Ø©:** all print files are A4 with chapter-per-page breaks;
tables, formulas and callouts never split across pages.
ÙƒÙ„ Ù…Ù„ÙØ§Øª Ø§Ù„Ø·Ø¨Ø§Ø¹Ø© A4 Ø¨Ù‚ÙˆØ§Ø¹Ø¯ ÙØµÙˆÙ„/ØµÙØ­Ø§Øª Ù†Ø¸ÙŠÙØ© Ù„Ø§ ØªÙ‚Ø·Ø¹ Ø¬Ø¯ÙˆÙ„Ù‹Ø§ Ø£Ùˆ Ù…Ø¹Ø§Ø¯Ù„Ø©.

---

## ðŸ” Regenerating print files / Ø¥Ø¹Ø§Ø¯Ø© ØªÙˆÙ„ÙŠØ¯ Ù†Ø³Ø® Ø§Ù„Ø·Ø¨Ø§Ø¹Ø©

```bash
# after editing website content:
node -e '/* dump DATA from index.html to tools/data.json (see repo history) */'
python3 tools/make_copies.py       # cheat sheet PDF + DOCX
python3 tools/make_reference.py    # numbered formulas/abbreviations/definitions PDF + DOCX
```

---

## ðŸ“ Notes / Ù…Ù„Ø§Ø­Ø¸Ø§Øª
- No passwords anywhere: students are identified by name only (as requested).
  Ù„Ø§ ÙƒÙ„Ù…Ø§Øª Ù…Ø±ÙˆØ±: Ø§Ù„Ø·Ù„Ø§Ø¨ ÙŠÙØ¹Ø±ÙŽÙ‘ÙÙˆÙ† Ø¨Ø§Ù„Ø§Ø³Ù… ÙÙ‚Ø·.
- The teacher PIN gates the dashboard on the device only; the Sheets endpoint
  itself follows the deployment's Google access settings.
- Academic source of truth = the lecture slides; slide misprints are corrected
  with explicit transparency notes inside the lessons.


