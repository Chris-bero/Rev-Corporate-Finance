# -*- coding: utf-8 -*-
"""Build the printable Course Study Book (core explanations of all lessons) — A4 PDF + Word."""
import io, os, re, json
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(io.open(os.path.join(HERE, 'data_full.json'), encoding='utf-8'))
OUT_PDF = os.path.join(HERE, '..', 'site', 'FIN211_Course_Book_A4.pdf')
OUT_DOCX = os.path.join(HERE, '..', 'site', 'FIN211_Course_Book.docx')
CH = {c['id']: c for c in DATA['chapters']}
FM = DATA['formulas']

SUPSUP = {'2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹', '0': '⁰', '1': '¹', 'n': 'ⁿ'}
def _strip(t): return re.sub(r'<[^>]+>', '', t)
def lin(html):
    s = html
    s = re.sub(r'<sub>(.*?)</sub>', lambda m: _strip(m.group(1)), s, flags=re.S)
    s = re.sub(r'<sup>(.*?)</sup>', lambda m: SUPSUP.get(_strip(m.group(1)), '^' + _strip(m.group(1))), s, flags=re.S)
    def fr(m):
        top, bot = _strip(m.group(1)).strip(), _strip(m.group(2)).strip()
        wt = '(' + top + ')' if re.search(r'[ ±×÷,;]', top) else top
        wb = '(' + bot + ')' if re.search(r'[ ±×÷,;]', bot) else bot
        return wt + ' / ' + wb
    s = re.sub(r'<span class="fr"><span class="top">(.*?)</span><span class="bot">(.*?)</span></span>', fr, s, flags=re.S)
    s = s.replace('<br>', '  ·  ')
    s = re.sub(r'<[^>]+>', '', s)
    s = (s.replace('&gt;', '>').replace('&lt;', '<').replace('&amp;', '&').replace('&nbsp;', ' '))
    return re.sub(r'\s+', ' ', s).strip()

CO_LABEL = {
 'simple': ('In Simple Terms', 'ببساطة'),
 'note': ('Important note', 'ملاحظة مهمة'),
 'warn': ('Careful', 'انتبه'),
 'remember': ('Remember', 'تذكّر'),
}

CSS = """
@page { size: A4; margin: 14mm 12mm 16mm;
  @bottom-center { content: counter(page) " / " counter(pages); font-size:9px; color:#5c6b84; font-family:Tahoma,Arial,sans-serif; } }
@page cover { @bottom-center { content: none; } }
body{font:11.5px/1.6 "Segoe UI",Tahoma,Arial,sans-serif;color:#16233a}
.cover{page:cover;page-break-after:always;height:264mm;display:flex;flex-direction:column;justify-content:center;text-align:center;background:#0e2a47;color:#fff;border-radius:10px;padding:26mm 16mm}
.cover .k{font-size:12px;letter-spacing:3px;text-transform:uppercase;color:#8fc1ff;margin:0 0 10px}
.cover h1{font-size:38px;margin:0 0 6px;color:#fff;border:0;padding:0}
.cover h2{font-size:16px;color:#cfe0f2;border:0;padding:0;margin:0;font-weight:600;page-break-before:auto}
.cover .ar{direction:rtl;font-size:16px;color:#e0b050;font-weight:700;margin:10px 0 0}
.cover .stats{margin:14px 0 0;font-size:12.5px;color:#cfe0f2}
.cover .rule{width:60mm;height:2px;background:#e0b050;margin:12px auto}
.toc{page-break-after:always}
.toc h2{page-break-before:auto}
a.tl{display:block;text-decoration:none;color:#16233a;font-size:12.5px;margin:4px 0}
a.tl::after{content:leader('.') target-counter(attr(href), page);color:#5c6b84}
a.tl.sub{margin-inline-start:12px;font-size:11.5px;color:#33415a}
a.tl b{color:#0f4c81}
h2.ch{font-size:17px;color:#0f4c81;border-bottom:2px solid #dfe6f0;padding-bottom:5px;margin:0 0 4px;page-break-before:always;page-break-after:avoid}
h2.ch .arh{color:#b8860b;font-size:14px}
.chd{color:#5c6b84;font-size:11.5px;margin:4px 0 12px}
h3.le{font-size:14.5px;color:#0e2a47;margin:16px 0 2px;page-break-after:avoid}
h3.le .no{color:#1663c7}
.le-meta{font-size:10.5px;color:#5c6b84;margin:0 0 6px}
h4.bh{font-size:12.5px;color:#1663c7;margin:10px 0 3px;page-break-after:avoid}
h4.bh .arh{color:#b8860b}
p{margin:4px 0}
p.ar,.ar{direction:rtl;text-align:right;color:#33415a}
.co{border-radius:8px;padding:7px 11px;margin:7px 0;page-break-inside:avoid;font-size:11px}
.co .ct{font-weight:800;font-size:10.5px;text-transform:uppercase;letter-spacing:.5px;display:block;margin-bottom:2px}
.co-simple{background:#e5f5ec;border:1px solid #bfe3cf}.co-simple .ct{color:#1a7f4b}
.co-note{background:#e8f0fb;border:1px solid #cfdcec}.co-note .ct{color:#1663c7}
.co-warn{background:#fdecea;border:1px solid #f2c7c3}.co-warn .ct{color:#b3261e}
.f{font-family:Georgia,"Times New Roman",serif;font-size:12.5px;margin:4px 0;background:#eef3f9;border-inline-start:3px solid #1663c7;border-radius:6px;padding:5px 9px;page-break-inside:avoid}
.fr{display:inline-block;vertical-align:middle;text-align:center;margin:0 3px}
.fr .top{display:block;border-bottom:1.2px solid #16233a;padding:0 4px 1px}
.fr .bot{display:block;padding:1px 4px 0}
.ex{border:1px solid #dfe6f0;border-radius:8px;margin:8px 0;page-break-inside:avoid}
.ex .exh{background:#fdf6e3;color:#8a6d1a;font-weight:700;font-size:11.5px;padding:6px 10px;border-bottom:1px solid #dfe6f0}
.ex .exb{padding:7px 11px;font-size:11px}
.ex .lb{color:#1663c7;font-weight:800}
.ex .ans{background:#e5f5ec;color:#1a7f4b;font-weight:800;border-radius:6px;padding:3px 9px;display:inline-block;margin:3px 0}
table{border-collapse:collapse;width:100%;font-size:10px;margin:6px 0}
th,td{border:1px solid #dfe6f0;padding:4px 6px;text-align:start;vertical-align:top}
th{background:#eef3f9;color:#0f4c81;font-size:9.5px;text-transform:uppercase}
tr{page-break-inside:avoid}
ul{margin:4px 0;padding-inline-start:18px}
li{margin:2px 0}
p,li{orphans:3;widows:3}
"""

def co_html(typ, c):
    en, ar = CO_LABEL.get(typ, ('Note', 'ملاحظة'))
    return '<div class="co co-%s"><span class="ct">%s · %s</span>%s<p class="ar">%s</p></div>' % (
        typ, en, ar, c['en'], c['ar'])

def tbl_html(tb):
    h = '<table><tr>' + ''.join('<th>%s<br><span class="ar">%s</span></th>' % (escape(x['en']), escape(x['ar'])) for x in tb['h']) + '</tr>'
    for r in tb['r']:
        h += '<tr>' + ''.join('<td>%s<br><span class="ar">%s</span></td>' % (escape(c['en']), escape(c['ar'])) for c in r) + '</tr>'
    return h + '</table>'

def ex_html(x):
    h = '<div class="ex"><div class="exh">Worked Example · مثال محلول — %s · %s</div><div class="exb">' % (escape(x['ti']['en']), escape(x['ti']['ar']))
    h += '<p><span class="lb">Given · المعطيات:</span> ' + ' '.join(x['g'][0:1][0]['en'] for _ in []) + '</p>' if False else ''
    h += '<p><span class="lb">Given · المعطيات:</span> ' + ' '.join(g['en'] for g in x['g']) + '</p>'
    h += '<p class="ar"><span class="lb">المعطيات:</span> ' + ' '.join(g['ar'] for g in x['g']) + '</p>'
    h += '<p><span class="lb">Required · المطلوب:</span> %s</p><p class="ar"><span class="lb">المطلوب:</span> %s</p>' % (x['rq']['en'], x['rq']['ar'])
    if x.get('f') and x['f'] in FM:
        h += '<div class="f">%s</div>' % FM[x['f']]['disp']
    h += '<p><span class="lb">Calculation · الحساب:</span></p><ul>' + ''.join('<li>%s<p class="ar" style="margin:0">%s</p></li>' % (st['en'], st['ar']) for st in x['st']) + '</ul>'
    h += '<p class="ans">Final Answer · الإجابة: %s · %s</p>' % (x['an']['en'], x['an']['ar'])
    h += '<p><span class="lb">Interpretation · التفسير:</span> %s</p><p class="ar">%s</p>' % (x['ip']['en'], x['ip']['ar'])
    return h + '</div></div>'

parts = ['<html><head><meta charset="utf-8"><style>%s</style></head><body>' % CSS]
nex = sum(len(l['examples']) for l in DATA['lessons'])
parts.append('<div class="cover"><p class="k">FIN211 · Course Study Book</p><h1>Corporate Finance</h1><h2>The Core Explanation of Every Lesson — bilingual EN/AR</h2><div class="rule"></div><p class="ar">المالية الإدارية — الشرح الأساسي لكل درس — باللغتين</p><p class="stats">%d Chapters · %d Lessons · %d Worked Examples<br>%d فصل · %d درس · %d مثالًا محلولًا</p><p class="stats" style="margin-top:22px;font-size:11px;opacity:.85">Built from the course lecture materials (Lectures 1–13) · مبني من محاضرات المقرر (١–١٣)</p><p class="stats" style="margin-top:12px;color:#e0b050;font-weight:700">Prepared by 领袖 - EBRA · إعداد</p></div>' % (
    len(DATA['chapters']), len(DATA['lessons']), nex, len(DATA['chapters']), len(DATA['lessons']), nex))
parts.append('<div class="toc"><h2 class="ch" style="page-break-before:auto">Contents — الفهرس</h2>')
for c in DATA['chapters']:
    parts.append('<a class="tl" href="#ch%s"><b>%d · %s · %s</b></a>' % (c['id'], c['num'], escape(c['title']['en']), escape(c['title']['ar'])))
    for l in [x for x in DATA['lessons'] if x['ch'] == c['id']]:
        parts.append('<a class="tl sub" href="#le%s">%s · %s</a>' % (l['id'], escape(l['title']['en']), escape(l['title']['ar'])))
parts.append('</div>')

for c in DATA['chapters']:
    parts.append('<h2 class="ch" id="ch%s">%d · %s <span class="arh">· %s</span></h2>' % (c['id'], c['num'], escape(c['title']['en']), escape(c['title']['ar'])))
    parts.append('<p class="chd">%s · %s</p>' % (escape(c['desc']['en']), escape(c['desc']['ar'])))
    for l in [x for x in DATA['lessons'] if x['ch'] == c['id']]:
        parts.append('<h3 class="le" id="le%s"><span class="no">Lesson %s</span> — %s · <span style="color:#b8860b">%s</span></h3>' % (l['id'], l['id'][1:], escape(l['title']['en']), escape(l['title']['ar'])))
        parts.append('<p class="le-meta">%s · %d min · %d min</p>' % (escape(l['desc']['en']), l['mins'], l['mins']))
        parts.append('<h4 class="bh">Learning Objectives · <span class="arh">أهداف التعلم</span></h4><ul>' + ''.join('<li>%s</li>' % escape(o) for o in l['obj']['en']) + '</ul><ul class="ar">' + ''.join('<li>%s</li>' % escape(o) for o in l['obj']['ar']) + '</ul>')
        for b in l['blocks']:
            if 'co' in b:
                parts.append(co_html(b['co'], b['c']))
            else:
                parts.append('<h4 class="bh">%s · <span class="arh">%s</span></h4>' % (escape(b['h']['en']), escape(b['h']['ar'])))
                for pg in b['p']:
                    parts.append('<p>%s</p><p class="ar">%s</p>' % (pg['en'], pg['ar']))
                if b.get('tb'):
                    parts.append(tbl_html(b['tb']))
        if l.get('examples'):
            for x in l['examples']:
                parts.append(ex_html(x))
        if l.get('mistakes'):
            parts.append('<div class="co co-warn"><span class="ct">Common mistakes · أخطاء شائعة</span><ul>' + ''.join('<li>%s</li>' % escape(m['en']) for m in l['mistakes']) + '</ul><ul class="ar">' + ''.join('<li>%s</li>' % escape(m['ar']) for m in l['mistakes']) + '</ul></div>')
parts.append('</body></html>')
html = '\n'.join(parts)
io.open(os.path.join(HERE, '_book.html'), 'w', encoding='utf-8').write(html)
from weasyprint import HTML
HTML(string=html).write_pdf(OUT_PDF)
print('PDF written:', OUT_PDF)

# ============================ DOCX ============================
from docx import Document
from docx.shared import Mm, Pt, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Mm(210), Mm(297)
sec.left_margin = sec.right_margin = Mm(15)
sec.top_margin = sec.bottom_margin = Mm(14)
def bidi(p):
    pPr = p._p.get_or_add_pPr(); b = OxmlElement('w:bidi'); pPr.append(b); return p
def _field(par, code):
    r = par.add_run()
    f1 = OxmlElement('w:fldChar'); f1.set(qn('w:fldCharType'), 'begin')
    it = OxmlElement('w:instrText'); it.set(qn('xml:space'), 'preserve'); it.text = code
    f2 = OxmlElement('w:fldChar'); f2.set(qn('w:fldCharType'), 'end')
    r._r.append(f1); r._r.append(it); r._r.append(f2)
fp = sec.footer.paragraphs[0]; fp.alignment = 1
_field(fp, 'PAGE'); fp.add_run(' / '); _field(fp, 'NUMPAGES')

cov = doc.add_heading('Corporate Finance', 0); cov.alignment = 1
p = doc.add_paragraph('FIN211 · Course Study Book — The Core Explanation of Every Lesson'); p.alignment = 1; p.runs[0].bold = True
p = bidi(doc.add_paragraph('المالية الإدارية — الشرح الأساسي لكل درس — باللغتين')); p.alignment = 1
p = doc.add_paragraph('%d Chapters · %d Lessons · %d Worked Examples — bilingual EN/AR' % (len(DATA['chapters']), len(DATA['lessons']), nex)); p.alignment = 1; p.runs[0].italic = True
pc = doc.add_paragraph('Prepared by 领袖 - EBRA · إعداد'); pc.alignment = 1; pc.runs[0].bold = True
doc.add_page_break()
toc_h = doc.add_heading('Contents — الفهرس', 1)
for c in DATA['chapters']:
    doc.add_paragraph('%d · %s · %s' % (c['num'], c['title']['en'], c['title']['ar']), style='List Number')
    for l in [x for x in DATA['lessons'] if x['ch'] == c['id']]:
        pp = doc.add_paragraph('%s · %s' % (l['title']['en'], l['title']['ar']))
        pp.paragraph_format.left_indent = Mm(8); pp.runs[0].font.size = Pt(10)
p = doc.add_paragraph('(Page numbers: see the PDF edition, or update fields in Word with F9.)'); p.runs[0].italic = True; p.runs[0].font.size = Pt(9)

for c in DATA['chapters']:
    h = doc.add_heading('%d · %s · %s' % (c['num'], c['title']['en'], c['title']['ar']), 1)
    h.paragraph_format.page_break_before = True
    pd = doc.add_paragraph(c['desc']['en']); bidi(doc.add_paragraph(c['desc']['ar'])).runs[0].font.color.rgb = RGBColor(0x5c, 0x6b, 0x84)
    for l in [x for x in DATA['lessons'] if x['ch'] == c['id']]:
        hl = doc.add_heading('Lesson %s — %s · %s' % (l['id'][1:], l['title']['en'], l['title']['ar']), 2)
        hl.paragraph_format.keep_with_next = True
        ho = doc.add_paragraph('Learning Objectives · أهداف التعلم'); ho.runs[0].bold = True; ho.runs[0].font.color.rgb = RGBColor(0x16, 0x63, 0xc7); ho.paragraph_format.keep_with_next = True
        for o in l['obj']['en']: doc.add_paragraph(o, style='List Bullet')
        for o in l['obj']['ar']: bidi(doc.add_paragraph(o, style='List Bullet'))
        for b in l['blocks']:
            if 'co' in b:
                en, ar = CO_LABEL.get(b['co'], ('Note', 'ملاحظة'))
                pc = doc.add_paragraph(); r = pc.add_run(en + ' · ' + ar + ': '); r.bold = True
                r.font.color.rgb = RGBColor(0x1a, 0x7f, 0x4b) if b['co'] == 'simple' else RGBColor(0x16, 0x63, 0xc7)
                pc.add_run(b['c']['en'])
                bidi(doc.add_paragraph(b['c']['ar']))
            else:
                hb = doc.add_paragraph(); r = hb.add_run(b['h']['en'] + ' · '); r.bold = True; r.font.color.rgb = RGBColor(0x16, 0x63, 0xc7)
                r2 = hb.add_run(b['h']['ar']); r2.bold = True; r2.font.color.rgb = RGBColor(0xb8, 0x86, 0x0b)
                hb.paragraph_format.keep_with_next = True
                for pg in b['p']:
                    doc.add_paragraph(pg['en']); bidi(doc.add_paragraph(pg['ar']))
                if b.get('tb'):
                    tb = b['tb']; t = doc.add_table(rows=1, cols=len(tb['h'])); t.style = 'Table Grid'
                    hr = t.rows[0]; hr.cant_split = True
                    trPr = hr._tr.get_or_add_trPr(); th = OxmlElement('w:tblHeader'); trPr.append(th)
                    for i, x in enumerate(tb['h']): hr.cells[i].text = x['en'] + ' / ' + x['ar']
                    for rr in tb['r']:
                        row = t.add_row(); row.cant_split = True
                        for i, cc in enumerate(rr): row.cells[i].text = cc['en'] + ' / ' + cc['ar']
                    doc.add_paragraph('')
        for x in l.get('examples', []):
            pe = doc.add_paragraph(); r = pe.add_run('Worked Example · مثال محلول — %s · %s' % (x['ti']['en'], x['ti']['ar'])); r.bold = True; r.font.color.rgb = RGBColor(0x8a, 0x6d, 0x1a)
            pe.paragraph_format.keep_with_next = True
            for lab, key in [('Given · المعطيات', 'g'), ('Required · المطلوب', 'rq')]:
                pp = doc.add_paragraph(); r = pp.add_run(lab + ': '); r.bold = True
                val = x[key]
                pp.add_run(' '.join(v['en'] for v in val) if key == 'g' else val['en'])
                pp2 = bidi(doc.add_paragraph()); r = pp2.add_run(lab.split(' ·')[0] + ': ' if False else ''); 
                pp2.add_run(' '.join(v['ar'] for v in val) if key == 'g' else val['ar'])
            if x.get('f') and x['f'] in FM:
                pf = doc.add_paragraph(lin(FM[x['f']]['disp'])); pf.paragraph_format.left_indent = Mm(5)
                for rn in pf.runs: rn.font.name = 'Cambria'
            pc = doc.add_paragraph(); r = pc.add_run('Calculation · الحساب:'); r.bold = True
            for st in x['st']:
                doc.add_paragraph(st['en'], style='List Bullet'); bidi(doc.add_paragraph(st['ar'], style='List Bullet'))
            pa = doc.add_paragraph(); r = pa.add_run('Final Answer · الإجابة: %s · %s' % (x['an']['en'], x['an']['ar'])); r.bold = True; r.font.color.rgb = RGBColor(0x1a, 0x7f, 0x4b)
            pi = doc.add_paragraph(); r = pi.add_run('Interpretation · التفسير: '); r.bold = True; pi.add_run(x['ip']['en'])
            bidi(doc.add_paragraph(x['ip']['ar']))
        if l.get('mistakes'):
            pm = doc.add_paragraph(); r = pm.add_run('Common mistakes · أخطاء شائعة'); r.bold = True; r.font.color.rgb = RGBColor(0xb3, 0x26, 0x1e)
            for m in l['mistakes']:
                doc.add_paragraph(m['en'], style='List Bullet'); bidi(doc.add_paragraph(m['ar'], style='List Bullet'))
doc.save(OUT_DOCX)
print('DOCX written:', OUT_DOCX)
