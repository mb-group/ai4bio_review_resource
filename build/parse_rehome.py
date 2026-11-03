import re, json, sys

PATH = "content_plan/rehome.md"
lines = open(PATH, encoding="utf-8").read().split("\n")

HEAD_RE = re.compile(r'^(#{1,4})\s+(.*)$')
CLAIM_RE = re.compile(r'^\*\*([A-Za-z0-9.\-]+)\*\*\s+(.*)$')
TERM_RE = re.compile(r'^-\s+\*\*(.+?)\*\*\s+`([a-z0-9\-]+)`\s*(?:\xc2\xb7|\u00b7|\u30fb|·)?\s*(.*)$')
DEF_RE = re.compile(r'^\s*-\s*\*Definition:\*\s*(.*)$')
EXHDR_RE = re.compile(r'^\s*-\s*\*Examples(?:\s*\(([0-9]+),\s*folded\))?:\*\s*(.*)$')
FINDING_RE = re.compile(r'^\s*-\s*\u25b8\s*\*Finding:\s*(.*)\*\s*$')
EX_RE = re.compile(r'^\s*-\s*`([A-Za-z0-9.\-]+e[0-9]+)`\s*\[([^\]]+)\]\s*(.*)$')
TECH_ONLY_TERM_RE = re.compile(r'^-\s+\*\*(.+?)\*\*\s+`([a-z0-9\-]+)`\s*$')
USEDBY_RE = re.compile(r'^\s*-\s*\*Used by:\*\s*(.*?)\s*(?:\u00b7|·)\s*\*Source in the draft:\*\s*(.*)$')
GROUP_HDR_RE = re.compile(r'^##\s+(.*)$')

terms = {}      # id -> {...}
examples = {}   # id -> {...}
technique_only = {}

section_stack = {1:'', 2:'', 3:''}
current_section = ''
current_claim = None
current_term = None   # term id
current_mode = None    # 'def' | 'ex'
current_finding = None
in_technique_only = False
current_tech_group = None
current_tech_term = None

def split_models(text):
    m = re.search(r'\u00b7\s*models:\s*(.*)$', text)
    models = []
    if m:
        models = [x.strip() for x in m.group(1).split(',') if x.strip()]
        text = text[:m.start()].rstrip()
    return text.strip(), models

for raw in lines:
    line = raw.rstrip('\n')

    if line.strip() == '# Technique-only entries':
        in_technique_only = True
        current_term = None
        continue

    if line.strip() == '# Reconciliation notes':
        break

    hm = HEAD_RE.match(line)
    if hm:
        level = len(hm.group(1))
        title = hm.group(2).strip()
        if in_technique_only:
            if level == 2:
                current_tech_group = title
            current_tech_term = None
            continue
        # section tracking from numbered headings like "## 2. Landscape..." "### 2.1. ..." "#### 2.1.1. ..."
        msec = re.match(r'^([0-9]+(?:\.[0-9]+){0,2})\.?\s', title)
        if msec:
            current_section = msec.group(1)
        elif title.lower().startswith('abstract'):
            current_section = 'Abstract'
        elif title.lower().startswith('conclusion'):
            current_section = '7'
        current_term = None
        current_mode = None
        current_finding = None
        continue

    if in_technique_only:
        tm = TECH_ONLY_TERM_RE.match(line)
        if tm:
            name, tid = tm.group(1), tm.group(2)
            technique_only[tid] = {"id": tid, "name": name, "group": current_tech_group, "def": "", "used_by": [], "source": ""}
            current_tech_term = tid
            continue
        if current_tech_term:
            dm = DEF_RE.match(line)
            if dm:
                technique_only[current_tech_term]["def"] = dm.group(1).strip()
                continue
            um = USEDBY_RE.match(line)
            if um:
                used = [x.strip() for x in um.group(1).split(',') if x.strip() and x.strip() != '(none named in the review)']
                technique_only[current_tech_term]["used_by"] = used
                technique_only[current_tech_term]["source"] = um.group(2).strip()
                continue
        continue

    cm = CLAIM_RE.match(line)
    if cm and not line.lstrip().startswith('-'):
        current_claim = cm.group(1)
        current_term = None
        current_mode = None
        current_finding = None
        continue

    tm = TERM_RE.match(line)
    if tm:
        name, tid, rest = tm.group(1), tm.group(2), tm.group(3)
        kind = 'concept'
        group = None
        evidence_only = False
        if 'both' in rest:
            kind = 'both'
            gmatch = re.search(r'technique group:\s*(.*)$', rest)
            if gmatch: group = gmatch.group(1).strip()
        if 'example_only' in rest:
            evidence_only = True
        terms[tid] = {
            "id": tid, "name": name, "kind": kind, "group": group,
            "evidence_only": evidence_only, "section": current_section,
            "source_claim": current_claim, "def": "", "examples": []
        }
        current_term = tid
        current_mode = None
        current_finding = None
        continue

    if current_term:
        dm = DEF_RE.match(line)
        if dm:
            terms[current_term]["def"] = dm.group(1).strip()
            current_mode = 'def'
            continue
        em = EXHDR_RE.match(line)
        if em:
            current_mode = 'ex'
            current_finding = None
            continue
        fm = FINDING_RE.match(line)
        if fm and current_mode == 'ex':
            current_finding = fm.group(1).strip()
            continue
        xm = EX_RE.match(line)
        if xm and current_mode == 'ex':
            exid, tags, text = xm.group(1), xm.group(2), xm.group(3)
            text, models = split_models(text)
            tagparts = [t.strip() for t in tags.split('\xb7')] if '\xb7' in tags else [t.strip() for t in tags.split('·')]
            direction = tagparts[0] if tagparts else 'illustration'
            design_element = None
            from_claim = None
            landing_claim = None
            for p in tagparts[1:]:
                fm2 = re.match(r'from\s+([A-Za-z0-9.\-]+)\s*\u2192\s*shown with\s+([A-Za-z0-9.\-]+)', p)
                fm3 = re.match(r'from\s+([A-Za-z0-9.\-]+)\s*->\s*shown with\s+([A-Za-z0-9.\-]+)', p)
                fm4 = re.match(r'from\s+([A-Za-z0-9.\-]+).*shown with\s+([A-Za-z0-9.\-]+)', p)
                if fm4:
                    from_claim, landing_claim = fm4.group(1), fm4.group(2)
                elif p not in ('',):
                    design_element = p
            examples[exid] = {
                "id": exid, "term": current_term, "text": text, "models": models,
                "direction": direction, "design_element": design_element,
                "finding": current_finding, "source_claim": from_claim,
                "landing_claim": landing_claim or from_claim
            }
            terms[current_term]["examples"].append(exid)
            continue

print(json.dumps({"terms": len(terms), "examples": len(examples), "technique_only": len(technique_only)}, indent=2))

import os
os.makedirs("build/data", exist_ok=True)
json.dump(terms, open("build/data/terms.json","w"), indent=1, ensure_ascii=False)
json.dump(examples, open("build/data/examples.json","w"), indent=1, ensure_ascii=False)
json.dump(technique_only, open("build/data/technique_only.json","w"), indent=1, ensure_ascii=False)
