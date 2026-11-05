#!/usr/bin/env python3
"""Bundle scrollytelling.html + resource.html + techniques.html + data/JS/CSS/figures
into ONE self-contained file: scrollytelling_standalone.html (run from anywhere)."""
import base64, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
rd = lambda p: (ROOT / p).read_text(encoding="utf-8")
safe_script = lambda js: js.replace("</script", "<\\/script")

site_data, gmap, css = rd("site-data.js"), rd("glossary-map.js"), rd("site.css")

# ---- embedded sub-pages (Resource, Techniques) -------------------------------------------
BRIDGE = """<script>
/* standalone bridge: route cross-page links to the parent, accept hash changes from it */
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href]');if(!a)return;
 var h=a.getAttribute('href')||'';
 if(h.indexOf('#/')===0){e.preventDefault();if(location.hash!==h)location.hash=h;return;} /* srcdoc frames resolve '#...' against the parent URL; set the hash directly */
 var m=/^(resource|techniques|scrollytelling)\\.html(#.*)?$/.exec(a.getAttribute('href')||'');if(!m)return;
 e.preventDefault();e.stopPropagation();parent.postMessage({go:m[1],hash:m[2]||''},'*');},true);
addEventListener('message',function(e){var d=e.data;if(d&&typeof d.setHash==='string'&&location.hash!==d.setHash&&d.setHash)location.hash=d.setHash;});
</script>"""

def inline_page(name):
    h = rd(name)
    h = h.replace('<link rel="stylesheet" href="site.css">', "<style>" + css + "</style>")
    h = h.replace('<script src="site-data.js"></script>', "<script>" + safe_script(site_data) + "</script>")
    h = h.replace('<script src="glossary-map.js"></script>', "<script>" + safe_script(gmap) + "</script>")
    assert 'src="site-data.js"' not in h and 'href="site.css"' not in h
    return h.replace("</body>", BRIDGE + "</body>")

pages = {"resource": inline_page("resource.html"), "techniques": inline_page("techniques.html")}
pages_js = json.dumps(pages).replace("</", "<\\/")

# ---- figures -> data URIs -----------------------------------------------------------------
figs = {}
for p in sorted((ROOT / "content_plan/review_content").glob("Figure*_*.png")):
    figs[p.stem] = "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode()

# ---- main page ----------------------------------------------------------------------------
s = rd("scrollytelling.html")
s = s.replace('<script src="site-data.js"></script>', "<script>" + safe_script(site_data) + "</script>")
s = s.replace('<script src="glossary-map.js"></script>', "<script>" + safe_script(gmap) + "</script>")
s = s.replace('<script>\n/* ======================= DATA',
              "<script>const FIGDATA=" + json.dumps(figs) + ";</script>\n<script>\n/* ======================= DATA", 1)
assert "FIGDATA=" in s
s = s.replace('src="${FIGDIR}${f}.png"', 'src="${FIGDATA[f]}"')
assert "FIGDIR}${f}" not in s

OVERLAY_CSS = """
#xov{position:fixed;inset:0;z-index:1000;display:flex;flex-direction:column;background:var(--paper)}
#xov .xbar{display:flex;align-items:center;gap:12px;padding:8px 14px;border-bottom:1px solid var(--rule);background:var(--surface)}
#xov .xbar button{font:600 13px var(--f-display);padding:6px 12px;border:1px solid var(--rule);border-radius:99px;background:var(--paper);color:var(--ink);cursor:pointer}
#xov .xbar button:hover,#xov .xbar button.on{border-color:var(--accent);color:var(--accent)}
#xov .xbar nav{margin-left:auto;display:flex;gap:6px}
#xov .xframes{flex:1;min-height:0;position:relative}
#xov iframe{position:absolute;inset:0;width:100%;height:100%;border:0;background:var(--paper)}
"""
OVERLAY_JS = """
/* ======================= standalone: Resource & Techniques open in-page ======================= */
(function(){
 const PAGES=%s, TITLE={resource:'Resource: landscape, models, evidence, glossary',techniques:'Techniques'};
 const ov=document.createElement('div'); ov.id='xov'; ov.hidden=true;
 ov.innerHTML='<div class="xbar"><button type="button" id="xback">\\u2190 Back to the story</button><span id="xtitle" style="font:500 13px var(--f-display);color:var(--muted)"></span><nav><button type="button" data-p="resource">Resource</button><button type="button" data-p="techniques">Techniques</button></nav></div><div class="xframes"></div>';
 document.body.appendChild(ov);
 const host=ov.querySelector('.xframes'), frames={}; let cur=null;
 function open(name,hash){
  hash=hash||'';
  let fr=frames[name];
  if(!fr){
   const el=document.createElement('iframe'); el.title=TITLE[name]; el.srcdoc=PAGES[name];
   fr=frames[name]={el,loaded:false,pending:hash}; host.appendChild(el);
   el.addEventListener('load',()=>{fr.loaded=true; if(fr.pending) el.contentWindow.postMessage({setHash:fr.pending},'*');});
  } else if(fr.loaded){ el_post(fr,hash); } else fr.pending=hash;
  Object.keys(frames).forEach(k=>frames[k].el.hidden=(k!==name));
  ov.querySelectorAll('.xbar nav button').forEach(b=>b.classList.toggle('on',b.dataset.p===name));
  ov.querySelector('#xtitle').textContent=TITLE[name];
  cur=name; ov.hidden=false; document.documentElement.style.overflow='hidden';
 }
 function el_post(fr,hash){ if(hash) fr.el.contentWindow.postMessage({setHash:hash},'*'); }
 function close(){ ov.hidden=true; cur=null; document.documentElement.style.overflow=''; }
 ov.querySelector('#xback').onclick=close;
 ov.querySelectorAll('.xbar nav button').forEach(b=>b.onclick=()=>open(b.dataset.p,''));
 addEventListener('keydown',e=>{ if(e.key==='Escape'&&cur) close(); });
 addEventListener('message',e=>{ const d=e.data; if(!d||!d.go) return;
  if(d.go==='scrollytelling'){ close(); if(d.hash) location.hash=d.hash; } else open(d.go,d.hash); });
 document.addEventListener('click',e=>{
  const a=e.target.closest&&e.target.closest('a[href]'); if(!a) return;
  const m=/^(resource|techniques)\\.html(#.*)?$/.exec(a.getAttribute('href')||''); if(!m) return;
  e.preventDefault(); open(m[1],m[2]);
 },true);
 window.__xopen=open;
})();
""" % pages_js
s = s.replace("</style>", OVERLAY_CSS + "</style>", 1)
s = s.replace("</script>\n</body>", OVERLAY_JS + "</script>\n</body>")
assert "__xopen" in s
out = ROOT / "scrollytelling_standalone.html"
out.write_text(s, encoding="utf-8")
print(f"wrote {out.name}: {out.stat().st_size/1e6:.2f} MB, {len(figs)} figures, pages={list(pages)}")
