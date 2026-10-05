const fs = require("fs");
const path = require("path");
const idx = path.join(__dirname, "..", "site", "index.html");
const src = fs.readFileSync(idx, "utf8");
const blocks = [...src.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
global.window = {};
for (let i = 0; i < 5; i++) eval(blocks[i]);
const D = window.DATA;
const out = {
  chapters: D.chapters,
  lessons: D.lessons.map(l => ({ id: l.id, ch: l.ch, mins: l.mins, title: l.title, desc: l.desc, obj: l.obj, blocks: l.blocks, examples: l.examples, mistakes: l.mistakes })),
  formulas: Object.fromEntries(D.formulas.map(f => [f.id, { disp: f.disp, name: f.name }]))
};
fs.writeFileSync(path.join(__dirname, "data_full.json"), JSON.stringify(out));
console.log("data_full.json lessons:", out.lessons.length,
  "| blocks:", out.lessons.reduce((a, l) => a + l.blocks.length, 0),
  "| examples:", out.lessons.reduce((a, l) => a + l.examples.length, 0));
