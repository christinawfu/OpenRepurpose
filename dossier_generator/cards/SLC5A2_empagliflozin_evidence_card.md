# OpenRepurpose Evidence Card

**Target:** SLC5A2
**Drug:** empagliflozin
**Disease:** type 2 diabetes

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
| familial renal glucosuria | 0.704 |
| type 2 diabetes mellitus | 0.637 |
| heart failure | 0.631 |
| chronic kidney disease | 0.626 |
| diabetes mellitus | 0.620 |

## GTEx Tissue Expression

GENCODE ID: ENSG00000140675.12

Expression records returned: 0

## Human Protein Atlas

Protein records returned: 1

## ClinVar

ClinVar records identified: 5

## ChEMBL

Drug/molecule information retrieved from ChEMBL.

## FAERS Safety Signals

Drug: empagliflozin

## Disease Ontology

Canonical disease: type 2 diabetes mellitus

Canonical ID: MONDO:0005148

## Integrated Evidence Assessment

**Evidence availability:** Insufficient

**Sources successfully retrieved:** 0 / 0 (0%)

### Tissue Evidence

Neither GTEx nor Human Protein Atlas returned usable tissue evidence.

### Tissue Cross-Database Comparison

No directly comparable tissue names were available from the current GTEx/HPA responses.

> **Tissue evidence flag:** The current data warrant additional biological interpretation.

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

### Executive Summary

An investigation of **SLC5A2** (SGLT2), **empagliflozin**, and **type 2 diabetes mellitus** was conducted across Ensembl, Open Targets, Human Protein Atlas (HPA), GTEx, ClinVar, ChEMBL, openFDA FAERS, and OLS/MONDO. 

The biological and clinical rationale for using empagliflozin to target SLC5A2 in type 2 diabetes mellitus is directly established. Empagliflozin is an approved, first-in-class SGLT2 inhibitor (Phase 4) that reduces renal glucose reabsorption.

---

### 1. Target Summary
* **Gene Symbol:** SLC5A2 (*Solute Carrier Family 5 Member 2*)
* **Ensembl ID:** `ENSG00000140675`
* **Protein Name:** Sodium/glucose cotransporter 2 (SGLT2)
* **Gene Synonyms:** SGLT2
* **Molecular Function & Protein Class:** Transporter / Sodium-glucose symporter involved in sugar and ion transport across cell membranes. Classified in Human Protein Atlas as a disease-related gene, metabolic protein, predicted membrane protein, and FDA-approved drug target.

---

### 2. Disease Summary
* **Canonical Disease Name:** Type 2 diabetes mellitus
* **Ontology Identifier:** `MONDO:0005148`
* **Definition:** A chronic metabolic disorder characterized by insulin resistance or desensitization, relative insulin deficiency, and chronic hyperglycemia, associated with long-term vascular, renal, and cardiovascular complications.

---

### 3. Drug Summary
* **Drug Name:** Empagliflozin (Trade name: *Jardiance*)
* **ChEMBL ID:** `CHEMBL2107830`
* **Development Phase:** Phase 4 (Approved, First Approved in 2014)
* **ATC Code:** `A10BK03` (Sodium-glucose co-transporter 2 (SGLT2) inhibitors)
* **USAN Stem:** `-gliflozin` (phlorizin derivatives, phenolic glycosides)
* **Mechanism of Action:** Direct inhibition of SLC5A2/SGLT2 in the proximal renal tubules, decreasing renal glucose reabsorption and increasing urinary glucose excretion.

---

### 4. Tissue Evidence
* **Human Protein Atlas (HPA):** Confirms evidence at the protein level (`Evidence at protein level`), classifying SLC5A2 as a membrane-bound transporter and approved drug target.
* **GTEx RNA Expression:** The GTEx query returned no tissue expression records (`results: []`).
* **Tissue Interpretation & Mismatch Analysis:** While protein-level evidence confirms SGLT2 expression, direct GTEx RNA expression profiling data was unavailable from the database query. Based on established physiological knowledge, SLC5A2 is predominantly expressed in the S1/S2 segments of the renal proximal tubule. The absence of GTEx RNA records in this specific API response constitutes a database reporting gap rather than biological non-expression.

---

### 5. Genetic Evidence
* **ClinVar Records:** 5 genetic variants identified in `SLC5A2` (Variant IDs: `4883189`, `4879630`, `4864643`, `4857303`, `4857297`).
* **Mendelian Phenotypes:** Inactivating mutations in `SLC5A2` cause Familial Renal Glucosuria (`MONDO_0009297`), a benign Mendelian condition characterized by glucosuria in the presence of normal blood glucose levels.
* **Genetic Rationale:** The human genetic phenocopy of SGLT2 loss-of-function (isolated benign glucosuria without systemic hypoglycemia or major renal injury) provided the genetic validation for developing pharmacological SGLT2 inhibitors like empagliflozin.

---

### 6. Disease Association Evidence
* **Open Targets Score:** `0.6366` for Type 2 Diabetes Mellitus (`MONDO_0005148`).
* **Secondary Disease Associations in Open Targets:**
  * Familial renal glucosuria (`MONDO_0009297`): Score `0.7038`
  * Heart failure (`MONDO_0005252`): Score `0.6310`
  * Chronic kidney disease (`MONDO_0005300`): Score `0.6264`
  * General Diabetes mellitus (`MONDO_0005015`): Score `0.6204`
* **Evidence Quality:** Strong direct clinical evidence, supported by secondary indications in cardiorenal disease.

---

### 7. Safety Signals (Post-Market Evidence)
* **openFDA FAERS Reports:** 3 primary safety reports retrieved for empagliflozin.
* **Observed Adverse Events in Sample Reports:** Dyspepsia, flatulence, headache, sinus headache, ear pain, weight changes (increased/decreased), and injection site reactions (noted in cases with concomitant injectable GLP-1 receptor agonists such as dulaglutide).
* **Safety Interpretation:** FAERS signals represent post-marketing spontaneous adverse event reports and do not prove direct causality. Well-established clinical trial safety profiles for SGLT2 inhibitors additionally highlight risks of mycotic genital infections, urinary tract infections, volume depletion, and rare euglycemic diabetic ketoacidosis.

---

### 8. Evidence Gaps & Limitations
1. **GTEx Data Gap:** GTEx RNA expression records were returned empty in the automated query response; detailed tissue-specific transcript abundance relies on external literature/HPA protein evidence.
2. **Spontaneous Reporting Bias:** FAERS safety records are confounded by concomitant medications (e.g., dulaglutide, linagliptin, metformin) and reporting bias.
3. **OMIM / DisGeNET Direct Feed:** Fine-grained OMIM disease-gene linkage scores were inferred through Open Targets and ClinVar rather than a dedicated standalone API response.

---

### 9. Potential Mismatches
* **Tissue / Disease Context:** Type 2 diabetes is systemic and primarily driven by pancreatic beta-cell dysfunction and insulin resistance in muscle, liver, and adipose tissue. However, SLC5A2 is expressed primarily in the kidney. This is a **functional renal intervention** rather than a primary disease-origin correction: targeting renal glucose reabsorption lowers systemic blood glucose independent of insulin action.

---

### 10. Overall Evidence Assessment

| Evidence Category | Status | Summary / Supporting Evidence |
| :--- | :--- | :--- |
| **Direct Clinical Evidence** | **Strong / Approved** | Empagliflozin is an FDA-approved Phase 4 drug (`CHEMBL2107830`, ATC `A10BK03`) specifically indicated for T2D. |
| **Mechanistic Evidence** | **Direct** | SGLT2 inhibition reduces renal glucose reabsorption, increasing glucosuria and lowering HbA1c. |
| **Genetic Evidence** | **Direct & Supportive** | Loss-of-function variants in `SLC5A2` cause benign familial renal glucosuria (ClinVar / Open Targets score 0.7038), validating target safety and efficacy. |
| **Tissue Evidence** | **Supported / Partial Gap** | HPA confirms protein-level transporter evidence; GTEx RNA API returned empty results. |
| **Safety Signals** | **Monitored** | Post-market FAERS reports reflect real-world usage; known drug class risks require standard clinical monitoring. |

**Verdict:** The evidence linking **SLC5A2** inhibition by **empagliflozin** to **type 2 diabetes mellitus** is robust, direct, and validated by human genetics, pharmacological mechanism, and Phase 4 clinical approval.

## Evidence Provenance

| Source | Retrieval status |
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

Evidence is retrieved from public biomedical database APIs through OpenRepurpose wrappers. Unavailable sources are reported rather than treated as evidence of absence.
