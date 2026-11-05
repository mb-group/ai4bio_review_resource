const fs = require('fs');
const html = fs.readFileSync('resource.html', 'utf-8');
const m = html.match(/<script>([\s\S]*)<\/script>/);
const src = m[1];
const cut = src.indexOf('};', src.indexOf('const ELP = {')) + 2;
const snippet = src.slice(0, cut);
const sandbox = `
${snippet}
module.exports = {REFS, GLOSS, DATA, TASKS, ELS, EL_ORDER, M, VERD, CLS, CLS_CAT, EV, ROUTES, DESC, ELP};
`;
fs.writeFileSync('/tmp/or_extract.js', sandbox);
const data = require('/tmp/or_extract.js');
fs.mkdirSync('build/data', {recursive:true});
for (const [k,v] of Object.entries(data)) {
  fs.writeFileSync(`build/data/or_${k}.json`, JSON.stringify(v, null, 1));
  const n = Array.isArray(v) ? v.length : Object.keys(v).length;
  console.log(k, n);
}
