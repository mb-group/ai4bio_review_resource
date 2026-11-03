#!/usr/bin/env python3
"""
Consolidates content_plan/rehome.md (terms, examples, technique-only entries)
with the review-sourced model data already extracted from mock-up/online_resource.html
(build/data/or_*.json) into one site-data.js consumed by concepts.html, models.html,
techniques.html, and scrollytelling.html.

Per content_plan/00_overview.md principle 6: "Content is data, not HTML."
"""
import json, re, os

D = "build/data"
terms = json.load(open(f"{D}/terms.json"))
examples = json.load(open(f"{D}/examples.json"))
technique_only = json.load(open(f"{D}/technique_only.json"))
or_M = json.load(open(f"{D}/or_M.json"))
or_EV = json.load(open(f"{D}/or_EV.json"))
or_REFS = json.load(open(f"{D}/or_REFS.json"))
or_ELS = json.load(open(f"{D}/or_ELS.json"))
or_DATA = json.load(open(f"{D}/or_DATA.json"))
or_TASKS = json.load(open(f"{D}/or_TASKS.json"))
or_CLS = json.load(open(f"{D}/or_CLS.json"))

# ---------- normalize design_element spelling to underscore form ----------
DE_MAP = {"training scheme":"training_scheme","post-analysis":"post_analysis",
          "data":"data","architecture":"architecture","evaluation":"evaluation"}
for e in examples.values():
    if e["design_element"]:
        e["design_element"] = DE_MAP.get(e["design_element"], e["design_element"])
for t in terms.values():
    if t.get("group"):
        g = t["group"].strip().lower().replace(" ", "_").replace("-", "_")
        t["design_element"] = {"data_and_tokenization":"data","training_scheme":"training_scheme",
                                "architecture":"architecture","evaluation":"evaluation",
                                "post_analysis":"post_analysis","agent_components":"agent_components"}.get(g, None)
    else:
        t["design_element"] = None
for t in technique_only.values():
    g = (t.get("group") or "").strip().lower().replace(" ", "_").replace("-", "_")
    t["design_element"] = {"data_and_tokenization":"data","training_scheme":"training_scheme",
                            "architecture":"architecture","evaluation":"evaluation",
                            "post_analysis":"post_analysis","agent_components":"agent_components"}.get(g, None)

# ---------- id mapping: online_resource short ids -> canonical rehome.md slugs ----------
ID_MAP = {
 "nt":"nucleotide-transformer","dnabert2":"dnabert-2","hyena":"hyenadna","evo2":"evo-2",
 "gpnmsa":"gpn-msa","rnafm":"rna-fm","codont":"codontransformer","af2":"alphafold","af3":"alphafold",
 "esmfold":"esm2",
}
def cid(short): return ID_MAP.get(short, short)

DATA_KEY = {d["k"]: d["n"] for d in or_DATA}
DATA_TYPE = {d["k"]: {"dna":"DNA","rna":"RNA","prot":"protein","sc":"single-cell","sp":"bulk-spatial","mo":"multi-omics"}[d["k"]] for d in or_DATA}
TASK_KEY = {t["k"]: {"rep":"representation","pred":"prediction","gen":"generation"}[t["k"]] for t in or_TASKS}

EL_FIELDS = ["data","architecture","training_scheme","evaluation","post_analysis"]
EL_FROM_OR = {"data":"data","architecture":"arch","training_scheme":"train","evaluation":"evalu","post_analysis":"post"}

TASK_SPECIFIC_IDS = {"alphafold","alphafold-multimer","alphagenome","enformer","borzoi","scooby",
                      "chrombpnet","eve","alphamissense","popeve","cellot","gears","state"}

MODELS = {}

def merge_model(short):
    m = next(x for x in or_M if x["id"] == short)
    canon = cid(short)
    existing = MODELS.get(canon)
    name = m["n"]
    if short == "af3": name = "AlphaFold 3"
    if short == "af2": name = "AlphaFold 2"
    if canon == "alphafold" and short in ("af2","af3"):
        name = "AlphaFold"
    entry = existing or {
        "id": canon, "name": name, "aliases": [], "type": "task_specific" if canon in TASK_SPECIFIC_IDS else "foundation_model",
        "data_types": [], "tasks": [], "description": m["one"],
        "about": m.get("about", ""), "configuration": {k: {"text": None, "source": None, "ref_text": None} for k in EL_FIELDS},
        "refs": [], "related_models": [], "phase": 1,
    }
    dt = DATA_TYPE.get(m["d"]); tk = TASK_KEY.get(m["t"])
    if dt and dt not in entry["data_types"]: entry["data_types"].append(dt)
    if tk and tk not in entry["tasks"]: entry["tasks"].append(tk)
    for r in m.get("r", []):
        if r not in entry["refs"]: entry["refs"].append(r)
    for f in EL_FIELDS:
        orf = EL_FROM_OR[f]
        txt = m.get("el", {}).get(orf)
        if txt and not entry["configuration"][f]["text"]:
            entry["configuration"][f] = {"text": txt, "source": "from_review", "ref_text": None}
    if short in ("af3","esmfold") and m.get("about"):
        entry["about"] = (entry["about"] + " " + m["about"]).strip()
    entry["_stop"] = entry.get("_stop", []) + [
        {"text": s[0], "refs": s[1], "design_element": {"data":"data","arch":"architecture","train":"training_scheme",
         "evalu":"evaluation","post":"post_analysis","agent":"agent_components"}.get(s[2], s[2])}
        for s in m.get("stop", [])
    ]
    MODELS[canon] = entry

for m in or_M:
    merge_model(m["id"])

# attach extended (original-paper) configuration text from ELP, where review's own `el` is thin
or_ELP = json.load(open(f"{D}/or_ELP.json"))
for short, elp in or_ELP.items():
    canon = cid(short)
    if canon not in MODELS: continue
    for f in EL_FIELDS:
        orf = EL_FROM_OR[f]
        txt = elp.get(orf)
        if txt:
            cfg = MODELS[canon]["configuration"][f]
            if cfg["text"] is None:
                MODELS[canon]["configuration"][f] = {"text": txt, "source": "from_references", "ref_text": None}
            elif not cfg.get("ref_text"):
                cfg["ref_text"] = txt
    if not MODELS[canon].get("about"):
        pass

for f_list in MODELS.values():
    for f in EL_FIELDS:
        if f_list["configuration"][f]["text"] is None:
            f_list["configuration"][f] = {"text": None, "source": "not_covered", "ref_text": None}

# ---------- lightweight Phase 2/3 entries, built only from rehome.md examples ----------
ALL_MODEL_IDS = set()
for e in examples.values():
    ALL_MODEL_IDS.update(e["models"])

AGENT_IDS = {"biomni","virtual-biotech","paper2agent","virtual-lab","ai-co-scientist","robin","geneagent","rbio1"}
MLLM_IDS = {"chatnt","cellwhisperer","bioreason","bioreason-pro"}
RESOURCE_IDS = {"uniref","uniprot","pdb","proteingym","casp","cagi","bixbench","kipoi","rosetta","cz-cellxgene-discover"}

DISPLAY_NAME = {
 "biomni":"Biomni","virtual-biotech":"Virtual Biotech","paper2agent":"Paper2Agent","virtual-lab":"Virtual Lab",
 "ai-co-scientist":"AI co-scientist","robin":"Robin","geneagent":"GeneAgent","rbio1":"rbio1",
 "chatnt":"ChatNT","cellwhisperer":"CellWhisperer","bioreason":"BioReason","bioreason-pro":"BioReason-Pro",
 "uniref":"UniRef","uniprot":"UniProt","pdb":"Protein Data Bank (PDB)","proteingym":"ProteinGym","casp":"CASP",
 "cagi":"CAGI","bixbench":"BixBench","kipoi":"Kipoi","rosetta":"Rosetta","cz-cellxgene-discover":"CZ CELLxGENE Discover",
 "scbert":"scBERT","chrombpnet":"ChromBPNet","alphafold-multimer":"AlphaFold-Multimer","progen2":"ProGen2",
}

for mid in sorted(ALL_MODEL_IDS):
    if mid in MODELS: continue
    name = DISPLAY_NAME.get(mid, mid.replace("-", " ").title())
    typ = "agent" if mid in AGENT_IDS else "multimodal_llm" if mid in MLLM_IDS else "resource" if mid in RESOURCE_IDS else \
          "task_specific" if mid in ("alphafold-multimer","chrombpnet") else "foundation_model"
    MODELS[mid] = {
        "id": mid, "name": name, "aliases": [], "type": typ, "data_types": [], "tasks": [],
        "description": None, "about": None,
        "configuration": {k: {"text": None, "source": "not_covered", "ref_text": None} for k in EL_FIELDS},
        "refs": [], "related_models": [], "phase": 2 if typ in ("agent","multimodal_llm") else 3, "_stop": [],
    }

# ProGen2 gets a real one-liner, split out of ProGen's "about" text (both are review-sourced facts)
if "progen2" in MODELS and "progen" in MODELS:
    MODELS["progen2"]["description"] = "Scales ProGen's autoregressive, family-conditioned sequence generation to billions of parameters."
    MODELS["progen2"]["data_types"] = ["protein"]; MODELS["progen2"]["tasks"] = ["generation"]
    MODELS["progen2"]["related_models"] = ["progen"]
    MODELS["progen"]["related_models"] = list(set(MODELS["progen"]["related_models"] + ["progen2"]))

# ---------- derive each example's originating review claim/section (for "See the evidence") ----------
for exid, e in examples.items():
    origin_claim = e.get("source_claim") or re.sub(r'e\d+$', '', exid)
    m = re.match(r'^([0-9]+(?:\.[0-9]+){0,2})', origin_claim)
    e["origin_claim"] = origin_claim
    e["origin_section"] = m.group(1) if m else None

# ---------- inline-link model names inside example prose (computed once, server-side, so it's robust) ----------
ALIASES = {}
for mid, m in MODELS.items():
    ALIASES[mid] = [m["name"]] if m["name"] else []
ALIASES.update({
 "alphafold": ["AlphaFold2","AlphaFold-2","AlphaFold 2","AlphaFold3","AlphaFold-3","AlphaFold 3","AlphaFold"],
 "alphafold-multimer": ["AlphaFold-Multimer","AlphaFold Multimer"],
 "esm2": ["ESMFold","ESM-2","ESM2"],
 "progen2": ["ProGen2","ProGen-2"],
 "progen": ["ProGen"],
 "dnabert-2": ["DNABERT-2","DNABERT2"],
 "nucleotide-transformer": ["Nucleotide Transformer"],
 "hyenadna": ["HyenaDNA"],
 "evo-2": ["Evo 2","Evo-2","Evo2"],
 "evo": ["Evo"],
 "gpn-msa": ["GPN-MSA"],
 "rna-fm": ["RNA-FM"],
 "codontransformer": ["CodonTransformer"],
 "cz-cellxgene-discover": ["CZ CELLxGENE Discover","CELLxGENE"],
 "chrombpnet": ["ChromBPNet"],
 "cellwhisperer": ["CellWhisperer"],
 "bioreason-pro": ["BioReason-Pro"],
 "bioreason": ["BioReason"],
 "chatnt": ["ChatNT"],
 "virtual-lab": ["Virtual Lab"],
 "virtual-biotech": ["Virtual Biotech"],
 "paper2agent": ["Paper2Agent"],
 "ai-co-scientist": ["AI co-scientist"],
 "geneagent": ["GeneAgent"],
 "biomni": ["Biomni"],
 "robin": ["Robin"],
 "rbio1": ["rbio1"],
 "pdb": ["Protein Data Bank","PDB"],
})
for exid, e in examples.items():
    text = e["text"]
    pairs = []  # (alias, mid)
    for mid in e["models"]:
        for alias in ALIASES.get(mid, []):
            pairs.append((alias, mid))
    pairs.sort(key=lambda p: -len(p[0]))
    if pairs:
        pattern = re.compile(r'\b(' + '|'.join(re.escape(a) for a, _ in pairs) + r')\b')
        alias_to_mid = {a: mid for a, mid in pairs}  # longest wins ties naturally via pattern order
        def _sub(m):
            a = m.group(1)
            mid = alias_to_mid.get(a)
            return f'<a class="mref" href="models.html#model-{mid}">{a}</a>' if mid else a
        text = pattern.sub(_sub, text)
    e["text_html"] = text

# ---------- compute "mentioned_in" (examples) and auto "what it has shown / where it stops" ----------
for mid, m in MODELS.items():
    ex_ids = [eid for eid, e in examples.items() if mid in e["models"]]
    m["mentioned_in"] = ex_ids
    m["shown"] = [eid for eid in ex_ids if examples[eid]["direction"] == "success"]
    m["stops_examples"] = [eid for eid in ex_ids if examples[eid]["direction"] == "limitation"]

# dedupe model config dict: drop internal helper keys not needed by front end except _stop (rename)
for m in MODELS.values():
    m["stop_findings"] = m.pop("_stop", [])

# ---------- "used_by" per technique (both-kind terms + technique-only) from examples' models ----------
for tid, t in terms.items():
    used = set()
    for eid in t["examples"]:
        used.update(examples[eid]["models"])
    t["used_by"] = sorted(used)
for tid, t in technique_only.items():
    pass  # already has used_by from the markdown table

# ---------- section ordering (as encountered in the review) ----------
SECTION_ORDER = ["Abstract","1","2.1","2.1.1","2.1.2","2.2","2.2.1","2.2.2","3","4","4.1","4.3","5.2","5.3","6.2","6.3"]
SECTION_TITLE = {
 "Abstract":"Abstract", "1":"1 · Introduction", "2.1":"2.1 · What is a foundation model",
 "2.1.1":"2.1.1 · Key concepts (the language analogy)", "2.1.2":"2.1.2 · Five design elements",
 "2.2":"2.2 · A tour of the foundation models", "2.2.1":"2.2.1 · Inputs: biological data types",
 "2.2.2":"2.2.2 · Outputs: tasks", "3":"3 · Where a model enters an agent",
 "4":"4 · Knowledge boundaries revealed by studies", "4.1":"4.1 · How the five elements define the boundary",
 "4.3":"4.3 · Where foundation model knowledge stops", "5.2":"5.2 · Betting on one general-purpose model",
 "5.3":"5.3 · Where the field stands developmentally", "6.2":"6.2 · Making boundaries explicit",
 "6.3":"6.3 · Community as infrastructure",
}

HOME_BEAT = {
 "biological-foundation-model":"A-01","agentic-system":"A-01","knowledge-boundary":"A-01",
 "knowledge-extraction":"1-01","compression-vs-composability":"1-04","llm":"1-04",
 "self-supervised-learning":"2.1-01","probing":"2.1-01","fine-tuning":"2.1-01","zero-shot-prediction":"2.1-01","supervised-learning":"2.1-01",
 "vocabulary":"2.1.1-01","token":"2.1.1-01","grammar":"2.1.1-01","corpus":"2.1.1-01","embedding":"2.1.1-01",
 "regulatory-dna":"2.1.1-01","tf-binding-motif":"2.1.1-01","sparse-autoencoder":"2.1.1-01",
 "five-design-elements":"2.1.2-01","generalization":"2.1.2-01","transformer":"2.1.2-01","inductive-bias":"2.1.2-01",
 "masked-language-modeling":"2.1.2-01","autoregressive-modeling":"2.1.2-01","contrastive-learning":"2.1.2-01",
 "intrinsic-vs-downstream-evaluation":"2.1.2-01","transfer-learning":"2.1.2-01","in-silico-perturbation":"2.1.2-01",
 "interpretability-analysis":"2.1.2-01",
 "inputs-vs-outputs":"2.2-01","representation-model":"2.2-01","predictive-model":"2.2-01","generative-model":"2.2-01",
 "bulk-rna-seq":"2.2-01","spatial-transcriptomics":"2.2-01","graph-neural-network":"2.2-01","perturbation-model":"2.2-01",
 "reasoning-model":"3-01","hallucination":"3-01","rag":"3-01","function-calling":"3-01","mcp":"3-01","skill-files":"3-01",
 "agent-harness":"3-01","multi-agent-system":"3-01","tool-route":"3-05","text-route":"3-05","encoder-route":"3-05",
 "verifier-route":"3-05","reinforcement-learning":"3-07",
 "decipherment-questions":"4-01","orchestration-boundary":"4-01",
 "cnn":"4.1-01","correlation-vs-causation":"4.1-01","simple-baselines":"4.3-01","four-layers":"4.3-08",
 "sampling-bias":None,"circular-annotation":None,"systematic-variation":None,
 "scaling-laws":"5.2-01","stages-of-biological-science":"5.3-01","adaptive-radiation":"5.3-01",
 "boundary-statement":"6.2-01","self-driving-lab":"6.2-03","shared-literacy":"6.3-01","model-registry":"6.3-01",
}
for tid, t in terms.items():
    t["home_beat"] = HOME_BEAT.get(tid)

# ---------- data-type group intros for the Models catalog (content_plan/03_models_page.md §"Group introductions") ----------
GROUP_INTRO = {
 "DNA": "DNA: how to define a token.",
 "RNA": "RNA: models read sequence and fold structure; non-coding RNA models need not capture mRNA function.",
 "single-cell": "Single-cell: representing expression levels; fixed gene vocabulary.",
 "bulk-spatial": "Bulk and spatial: bulk trades resolution for clinical linkage; spatial adds neighborhood.",
 "protein": "Protein: the vocabulary is settled, so innovation moves to other design elements.",
 "multi-omics": "Multi-omics: no shared vocabulary; models take different routes to align modalities.",
}

# ---------- write output ----------
out = {
    "TERMS": terms, "EXAMPLES": examples, "TECHNIQUE_ONLY": technique_only,
    "MODELS": MODELS, "REFS": or_REFS,
    "EL_LABELS": {
        "data": or_ELS["data"]["n"], "architecture": or_ELS["arch"]["n"], "training_scheme": or_ELS["train"]["n"],
        "evaluation": or_ELS["evalu"]["n"], "post_analysis": or_ELS["post"]["n"],
        "agent_components": "Agent components",
    },
    "SECTION_ORDER": SECTION_ORDER, "SECTION_TITLE": SECTION_TITLE, "GROUP_INTRO": GROUP_INTRO,
}
os.makedirs("build/data", exist_ok=True)
with open("site-data.js", "w", encoding="utf-8") as f:
    f.write("/* generated by build/generate_data.py from content_plan/rehome.md + mock-up/online_resource.html — do not hand-edit */\n")
    for k, v in out.items():
        f.write(f"const {k} = {json.dumps(v, ensure_ascii=False)};\n")

print("terms", len(terms), "examples", len(examples), "technique_only", len(technique_only), "models", len(MODELS), "refs", len(or_REFS))
print("model phases:", {p: sum(1 for m in MODELS.values() if m["phase"]==p) for p in (1,2,3)})
