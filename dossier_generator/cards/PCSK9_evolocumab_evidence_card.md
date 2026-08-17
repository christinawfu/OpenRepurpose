# OpenRepurpose Evidence Card

**Target:** PCSK9
**Drug:** evolocumab
**Disease:** hypercholesterolemia

## Evidence Sources

| Source | Status |
|---|---|
| ensembl | success |
| opentargets | success |
| gtex | success |
| hpa | success |
| clinvar | success |
| chembl | success |
| faers | success |
| ontology | success |
| disgenet | error |
| omim | error |

## Open Targets Disease Associations

| Disease | Score |
|---|---:|
| familial hypercholesterolemia | 0.852 |
| Hypercholesterolemia | 0.820 |
| hypercholesterolemia, autosomal dominant, 3 | 0.816 |
| cardiovascular disorder | 0.724 |
| coronary artery disorder | 0.718 |

## GTEx Tissue Expression

GENCODE ID: ENSG00000169174.10

Expression records returned: 0

## Human Protein Atlas

Protein records returned: 3

## ClinVar

ClinVar records identified: 5

## ChEMBL

Drug/molecule information retrieved from ChEMBL.

## FAERS Safety Signals

Drug: evolocumab

## Disease Ontology

Canonical disease: Hypercholesterolemia

Canonical ID: HP:0003124

## Integrated Evidence Assessment

**Evidence availability:** Insufficient

**Sources successfully retrieved:** 0 / 0 (0%)

### Tissue Evidence

Neither GTEx nor Human Protein Atlas returned usable tissue evidence.

### Genetic Evidence

No dedicated disease-genetics source returned usable evidence.

### Rare-Disease Relevance

Insufficient dedicated rare-disease evidence was retrieved.

### Evidence Gaps

- **RNA tissue expression** (gtex): missing
- **protein tissue expression** (hpa): missing
- **target-disease association** (opentargets): missing
- **clinical genetic variation** (clinvar): missing
- **drug information** (chembl): missing
- **post-market safety** (faers): missing
- **disease ontology** (ontology): missing
- **disease-gene aggregation** (disgenet): missing
- **Mendelian disease genetics** (omim): missing

**Scientific caution:** This assessment describes evidence availability and does not establish clinical efficacy, causality, or therapeutic suitability.

## Integrated Verdict

The current evidence retrieval indicates **insufficient evidence availability** across the connected biomedical databases.

This is an evidence-availability assessment rather than a prediction of clinical efficacy.

## Gemini Evidence Synthesis

### Biomedical Evidence Synthesis: PCSK9 – Evolocumab – Hypercholesterolemia

---

### 1. Target Summary
* **Gene Symbol:** PCSK9 (*Proprotein convertase subtilisin/kexin type 9*)
* **Ensembl ID:** `ENSG00000169174`
* **Synonyms:** `FH3`, `HCHOLA3`, `NARC-1`
* **Molecular Function & Class:** Serine protease / hydrolase; categorized as a secreted plasma protein and an FDA-approved drug target involved in lipid, sterol, and cholesterol metabolism.
* **Biological Role:** PCSK9 binds to the low-density lipoprotein receptor (LDLR) and promotes its degradation, regulating plasma low-density lipoprotein cholesterol (LDL-C) levels.

---

### 2. Disease Summary
* **Disease Name:** Hypercholesterolemia
* **Canonical Ontology Identifiers:**
  * `HP:0003124` (Hypercholesterolemia)
  * `MONDO:0011369` (Hypercholesterolemia, autosomal dominant, 3 / PCSK9-related familial hypercholesterolemia)
  * `MONDO:0005439` (Familial hypercholesterolemia)
* **Clinical Context:** Characterized by elevated levels of circulating cholesterol (specifically LDL-C), leading to accelerated atherosclerosis and increased risk of cardiovascular and coronary artery disease.

---

### 3. Drug Summary
* **Drug Name:** Evolocumab (Brand Name: *Repatha*, Research Code: `AMG-145`)
* **ChEMBL Identifier:** `CHEMBL2364655`
* **Drug Type & Mechanism:** Fully human IgG2 monoclonal antibody targeting secreted PCSK9.
* **ATC Classification:** `C10AX13`
* **Approval Status:** First approved in 2015; Max Clinical Phase 4.0 (FDA and EMA approved for parenteral/subcutaneous administration).

---

### 4. Tissue & Protein Evidence
* **Human Protein Atlas (HPA):**
  * Protein-level evidence confirms PCSK9 presence as a secreted plasma protein.
  * Co-listed with key metabolic interactors such as LDLR (*Low density lipoprotein receptor*, `ENSG00000130164`), which mediates hepatic uptake of LDL particles.
* **GTEx Expression Data:**
  * *Tool Status:* The GTEx expression lookup returned no structured tissue expression results for the query.
  * *Interpretation:* This reflects an evidence retrieval gap in the queried endpoint rather than biological absence of tissue expression.

---

### 5. Genetic Evidence
* **ClinVar Records:** 5 representative variant entries retrieved (`4875483`, `4874269`, `4861692`, `4861691`, `4861690`).
* **Mendelian Disease Mapping:** MONDO ontology explicitly links mutations in *PCSK9* to autosomal dominant hypercholesterolemia type 3 (`MONDO:0011369`).
* **Genetic Support Level:** High direct genetic evidence; gain-of-function variants in *PCSK9* cause severe hypercholesterolemia, whereas loss-of-function variants lead to low LDL-C levels and protection against coronary disease.

---

### 6. Disease Association Evidence
* **Open Targets Database Scores:**
  * Familial Hypercholesterolemia (`MONDO_0005439`): **0.852**
  * Hypercholesterolemia (`HP_0003124`): **0.820**
  * Hypercholesterolemia, Autosomal Dominant, 3 (`MONDO_0011369`): **0.816**
  * Cardiovascular Disorder (`MONDO_0004995`): **0.724**
  * Coronary Artery Disorder (`MONDO_0005010`): **0.718**

---

### 7. Post-Market Safety Signals
* **openFDA FAERS Reports:**
  * Sample retrieved: 3 safety report entries in patients co-treated with evolocumab, ezetimibe, and atorvastatin for hyperlipidemia.
  * **Reported Adverse Events:** Angina pectoris, ventricular extrasystoles, and back pain.
  * **Safety Interpretation:** FAERS signals represent spontaneous post-marketing safety reports in complex clinical settings (often with underlying severe cardiovascular disease) and do not demonstrate direct drug causality.

---

### 8. Evidence Classification

| Category | Retrieved Evidence Items |
| :--- | :--- |
| **Direct Evidence** | Evolocumab is a Phase 4 approved monoclonal antibody directly binding PCSK9 to lower serum cholesterol in hypercholesterolemia. |
| **Indirect Evidence** | Open Targets scores connecting PCSK9 to downstream ischemic endpoints (e.g., coronary artery disorder, overall cardiovascular disease). |
| **Database Associations** | High Open Targets association scores ($\ge 0.81$) across hypercholesterolemia ontology terms. |
| **Genetic Evidence** | ClinVar variant listings and MONDO identifier `MONDO:0011369` establishing causal Mendelian linkage between *PCSK9* and hypercholesterolemia. |
| **Tissue Evidence** | HPA protein-level confirmation of secreted plasma protein status interacting with hepatic LDLR; GTEx query was uninformative. |
| **Safety Signals** | FAERS cases reporting back pain and cardiovascular symptoms (angina, extrasystoles) in polymedicated patients; require cautious contextual interpretation. |

---

### 9. Evidence Gaps & Potential Mismatches
* **GTEx Data Gap:** GTEx tissue RNA expression data were not successfully retrieved via the tool response, requiring reliance on HPA and existing literature for tissue distribution (primarily liver/plasma).
* **Confounding Safety Signals:** Cardiovascular events reported in FAERS reflect the baseline risks of hypercholesterolemic patient populations receiving combination therapy (e.g., statins, ezetimibe) rather than mechanistically unpredicted toxicities.

---

### 10. Integrated Assessment & Synthesis

The biomedical evidence strongly supports the link between **PCSK9**, **evolocumab**, and **hypercholesterolemia**. 

1. **Target-Disease Validity:** Strong direct genetic evidence (Mendelian autosomal dominant hypercholesterolemia type 3, ClinVar records) and high database association scores ($>0.81$) validate PCSK9 as a primary regulator of systemic LDL cholesterol.
2. **Drug Mechanism:** Evolocumab is an approved (Phase 4) biotherapeutic antibody that neutralizes extracellular PCSK9, preventing LDLR degradation and promoting LDL clearance.
3. **Safety & Tolerability:** Post-marketing safety reports reflect expected clinical comorbidities of high-risk hypercholesterolemic populations without unmasking unexpected targeted biological contradictions.
4. **Overall Verdict:** The available evidence confirms an established, robust, and validated target-drug-disease relationship supported by human genetics, molecular pharmacology, and clinical authorization.
