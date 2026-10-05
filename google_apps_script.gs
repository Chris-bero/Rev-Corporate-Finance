/**
 * FIN211 Student Tracker — Google Apps Script backend
 * ----------------------------------------------------
 * Setup (one-time, ~2 minutes):
 *  1) Create a new Google Sheet (empty is fine).
 *  2) Menu: Extensions → Apps Script → delete any starter code → paste this whole file → Save.
 *  3) Deploy → New deployment → gear icon → "Web app".
 *       - Description: FIN211 tracker
 *       - Execute as: Me
 *       - Who has access: Anyone
 *     → Deploy → authorize → copy the "Web app URL" (ends with /exec).
 *  4) Open the website sign-in screen → ⚙ Google Sheets sync → paste the URL → Save.
 *
 * The sheet auto-creates a tab named "Students" with columns:
 *   name | created | lastVisit | visits | done | marks | last
 * No passwords are stored — students are identified by name only.
 */

var SHEET_NAME = 'Students';

function getSheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName(SHEET_NAME);
  if (!sh) {
    sh = ss.insertSheet(SHEET_NAME);
    sh.appendRow(['name', 'created', 'lastVisit', 'visits', 'done', 'marks', 'last']);
    sh.getRange(1, 1, 1, 7).setFontWeight('bold');
  }
  return sh;
}

function today_() {
  return Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'yyyy-MM-dd');
}

function json_(obj) {
  return ContentService
    .createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

function fmtDate_(v) {
  if (v instanceof Date) return Utilities.formatDate(v, Session.getScriptTimeZone(), 'yyyy-MM-dd');
  return String(v || '');
}

function readAll_() {
  var sh = getSheet_();
  var v = sh.getDataRange().getValues();
  if (v.length) v.shift(); // header
  return v.filter(function (r) { return String(r[0]).trim() !== ''; }).map(function (r) {
    return {
      name: String(r[0]),
      created: fmtDate_(r[1]),
      lastVisit: fmtDate_(r[2]),
      visits: Number(r[3]) || 0,
      done: String(r[4] || '{}'),
      marks: String(r[5] || '{}'),
      last: String(r[6] || '')
    };
  });
}

/* data rows start at sheet row 2 (row 1 = header) */
function writeRow_(sh, dataRowIndex, stu) {
  sh.getRange(dataRowIndex, 1, 1, 7).setValues([[
    stu.name, stu.created, stu.lastVisit, stu.visits, stu.done, stu.marks, stu.last
  ]]);
}

function findIndex_(rows, name) {
  var key = String(name).trim().toLowerCase();
  for (var i = 0; i < rows.length; i++) {
    if (String(rows[i].name).trim().toLowerCase() === key) return i;
  }
  return -1;
}

/* GET ?action=list  |  GET ?action=get&name=... */
function doGet(e) {
  e = e || { parameter: {} };   // safe when pressing Run inside the editor
  var action = e.parameter.action;
  try {
    if (action === 'list') {
      return json_({ ok: true, students: readAll_() });
    }
    if (action === 'get') {
      var i = findIndex_(readAll_(), e.parameter.name);
      return json_({ ok: true, student: i === -1 ? null : readAll_()[i] });
    }
    return json_({ ok: false, error: 'unknown action' });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  }
}

/* POST body (text/plain): {action:'enter'|'save', name, done?, marks?, last?} */
function doPost(e) {
  e = e || { postData: { contents: "{}" } };   // safe when pressing Run inside the editor
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var b = JSON.parse(e.postData.contents);
    var sh = getSheet_();
    var rows = readAll_();

    if (b.action === 'enter') {
      var name = String(b.name || '').trim();
      if (name.length < 2) return json_({ ok: false, error: 'bad name' });
      var i = findIndex_(rows, name);
      var stu;
      if (i === -1) {
        stu = { name: name, created: today_(), lastVisit: today_(), visits: 1, done: '{}', marks: '{}', last: '' };
        sh.appendRow([stu.name, stu.created, stu.lastVisit, stu.visits, stu.done, stu.marks, stu.last]);
      } else {
        stu = rows[i];
        stu.visits = (Number(stu.visits) || 0) + 1;
        stu.lastVisit = today_();
        writeRow_(sh, i + 2, stu);
      }
      return json_({ ok: true, student: stu });
    }

    if (b.action === 'save') {
      var j = findIndex_(rows, b.name);
      var doneS = JSON.stringify(b.done || {});
      var marksS = JSON.stringify(b.marks || {});
      var lastS = String(b.last || '');
      if (j === -1) {
        sh.appendRow([String(b.name).trim(), today_(), today_(), 1, doneS, marksS, lastS]);
        return json_({ ok: true, created: true });
      }
      var s2 = rows[j];
      s2.done = doneS; s2.marks = marksS; s2.last = lastS;
      writeRow_(sh, j + 2, s2);
      return json_({ ok: true });
    }

    return json_({ ok: false, error: 'unknown action' });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}
