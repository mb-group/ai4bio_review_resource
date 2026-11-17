#!/usr/bin/env python3
"""Convert the chat-assistant guides in for_download/*.md into branded PDFs
(colored formatting + citation / preprint / website provenance) using
python-markdown + headless Chrome. Run from anywhere."""
import pathlib, subprocess, sys, tempfile

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CITATION = ("Cai, T., Kleist, A., Patel, J., Malinverni, D., Taylor, A. K., Sharan, M., "
            "Umeton, R., &amp; Babu, M. M. (2026). AI for Biologists: The Knowledge Boundaries "
            "of Foundation Models in the Age of Agentic Systems. arXiv:2611.17015. "
            "https://doi.org/10.48550/arXiv.2611.17015")
PREPRINT = "https://arxiv.org/abs/2611.17015"
WEBSITE = "https://mb-group.github.io/ai4bio_review_resource/scrollytelling_standalone.html"

CSS = """
@page{size:A4;margin:18mm 16mm 20mm}
*{box-sizing:border-box}
body{margin:0;color:#13222A;font:14px/1.55 Georgia,'Times New Roman',serif}
.eyebrow{font:700 11px/1.3 'Helvetica Neue',Arial,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#A3266F;margin:0 0 6px}
h1{font:700 26px/1.15 'Helvetica Neue',Arial,sans-serif;letter-spacing:-.02em;margin:0 0 4px;color:#13222A}
h1+h3{font:500 16px/1.35 Georgia,serif;font-style:italic;color:#566870;margin:2px 0 14px;border:0;padding:0}
h2{font:700 19px/1.2 'Helvetica Neue',Arial,sans-serif;letter-spacing:-.01em;color:#A3266F;margin:26px 0 8px;padding:12px 0 6px;border-top:2px solid #A3266F}
h3{font:700 15px/1.3 'Helvetica Neue',Arial,sans-serif;color:#13222A;margin:18px 0 6px;padding-bottom:3px;border-bottom:1px solid #D3DBDC}
h4{font:700 13.5px/1.3 'Helvetica Neue',Arial,sans-serif;color:#566870;margin:14px 0 4px}
p{margin:0 0 9px}
a{color:#A3266F;text-decoration:none;border-bottom:1px dotted #A3266F;word-break:break-all}
strong{font-family:'Helvetica Neue',Arial,sans-serif;font-size:13px}
ul,ol{margin:0 0 10px;padding-left:22px}
li{margin:0 0 4px}
hr{border:0;border-top:1px solid #D3DBDC;margin:18px 0}
blockquote{margin:10px 0;padding:8px 14px;border-left:3px solid #A3266F;background:#F6E3EE;border-radius:0 5px 5px 0;color:#13222A}
blockquote p{margin:0 0 4px}
code{font:12px Menlo,Consolas,monospace;background:#F2F5F4;border:1px solid #E4EAEA;border-radius:3px;padding:1px 4px}
pre{background:#F2F5F4;border:1px solid #D3DBDC;border-left:3px solid #A3266F;border-radius:5px;padding:10px 12px;overflow-wrap:break-word;white-space:pre-wrap}
pre code{background:none;border:0;padding:0}
table{border-collapse:collapse;width:100%;margin:10px 0 14px;font:12.5px/1.45 'Helvetica Neue',Arial,sans-serif;page-break-inside:auto}
th{background:#13222A;color:#fff;text-align:left;padding:6px 9px;font-size:11.5px;letter-spacing:.02em}
td{border:1px solid #D3DBDC;padding:6px 9px;vertical-align:top}
tr:nth-child(even) td{background:#F2F5F4}
tr{page-break-inside:avoid}
h2,h3,h4{page-break-after:avoid}
.prov{margin:14px 0 22px;padding:12px 16px;background:#F6E3EE;border:1px solid #E6B8D4;border-left:4px solid #A3266F;border-radius:6px;font:12px/1.55 'Helvetica Neue',Arial,sans-serif;page-break-inside:avoid}
.prov b{display:block;font-size:11px;letter-spacing:.1em;text-transform:uppercase;color:#A3266F;margin-bottom:5px}
.prov p{margin:0 0 5px}
.prov .lbl{font-weight:700;color:#13222A}
.endnote{margin-top:28px;padding-top:12px;border-top:2px solid #A3266F;font:11.5px/1.55 'Helvetica Neue',Arial,sans-serif;color:#566870;page-break-inside:avoid}
.endnote .lbl{font-weight:700;color:#13222A}
"""

PROV = f"""
<div class="prov">
<b>Where this guide comes from</b>
<p><span class="lbl">Source review:</span> {CITATION}</p>
<p><span class="lbl">Preprint:</span> <a href="{PREPRINT}">{PREPRINT}</a></p>
<p><span class="lbl">Interactive companion website:</span> <a href="{WEBSITE}">{WEBSITE}</a></p>
</div>
"""

ENDNOTE = f"""
<div class="endnote">
<p><span class="lbl">This guide accompanies the review</span> &ldquo;AI for Biologists: The Knowledge
Boundaries of Foundation Models in the Age of Agentic Systems&rdquo; (Cai et al., 2026,
arXiv:2611.17015). Preprint: <a href="{PREPRINT}">{PREPRINT}</a> &middot;
Interactive resource: <a href="{WEBSITE}">{WEBSITE}</a>.
Please keep this notice when sharing.</p>
</div>
"""

GUIDES = [
    ("knowledge_boundary_model_briefing_guide", "Companion guide · Understand a model paper"),
    ("problem_to_model_consultation_guide", "Companion guide · From biological problem to model brief"),
]

def convert(stem, eyebrow):
    src = ROOT / "for_download" / f"{stem}.md"
    out = ROOT / "for_download" / f"{stem}.pdf"
    text = src.read_text(encoding="utf-8")
    # Drop the md's own plain-text source/companion lines; the styled provenance box replaces them.
    lines = [l for l in text.splitlines()
             if not l.startswith("**Source framework:**") and not l.startswith("**Companion resource")]
    body = markdown.markdown("\n".join(lines), extensions=["tables", "fenced_code", "sane_lists"])
    # Styled provenance box goes right under the title block (after the subtitle h3).
    k = body.find("</h3>")
    body = body[:k + 5] + PROV + body[k + 5:] if k != -1 else PROV + body
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body><p class="eyebrow">{eyebrow}</p>{body}{ENDNOTE}</body></html>')
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as f:
        f.write(html)
        tmp = f.name
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={out}", f"file://{tmp}"], check=True, capture_output=True)
    pathlib.Path(tmp).unlink()
    print(f"wrote {out.relative_to(ROOT)}: {out.stat().st_size/1024:.0f} KB")

if __name__ == "__main__":
    for stem, eyebrow in GUIDES:
        convert(stem, eyebrow)
