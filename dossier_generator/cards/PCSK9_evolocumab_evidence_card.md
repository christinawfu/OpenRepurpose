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

### 1. Target Summary
* **Gene Symbol:** PCSK9 (*Proprotein convertase subtilisin/kexin type 9*)
* **Ensembl ID:** `ENSG00000169174`
* **Gene Synonyms:** `FH3`, `HCHOLA3`, `NARC-1`
* **Molecular & Biological Function:** PCSK9 encodes a secreted serine protease involved in cholesterol, sterol, and lipid metabolism. It binds to the low-density lipoprotein receptor (LDLR) and promotes its intracellular degradation, thereby reducing cellular uptake of circulating LDL cholesterol.
* **Protein Classification:** Secreted/plasma protein, enzyme (protease), FDA-approved drug target.

---

### 2. Disease Summary
* **Disease Name:** Hypercholesterolemia
* **Ontology Mapping:** 
  * Phenotype ID: `HP:0003124` (*Hypercholesterolemia*)
  * Related MONDO Entities: `MONDO_0005439` (*Familial hypercholesterolemia*), `MONDO_0011369` (*Hypercholesterolemia, autosomal dominant, 3 / PCSK9-related*)
* **Pathophysiology Context:** Hypercholesterolemia is characterized by abnormally elevated blood levels of cholesterol, specifically LDL-C, leading to increased risk for atherosclerotic cardiovascular disease and coronary artery disease.

---

### 3. Drug Summary
* **Drug Name:** Evolocumab (Trade Name: *Repatha*, *Repatha SureClick*)
* **ChEMBL Identifier:** `CHEMBL2364655`
* **Molecule Type & Subclass:** Fully human IgG2 monoclonal antibody (`-umab`)
* **ATC Classification:** `C10AX13` (*Lipid modifying agents, other lipid modifying agents*)
* **Development Status:** Phase 4 (Approved worldwide; First approved in 2015)
* **Administration Route:** Parenteral (subcutaneous injection)
* **Mechanism of Action:** Evolocumab binds selectively and with high affinity to extracellular PCSK9, preventing PCSK9 from binding to LDLR. This inhibits PCSK9-mediated LDLR degradation, increasing LDLR recycling back to the hepatocyte cell membrane and enhancing systemic clearance of LDL-C from the bloodstream.

---

### 4. Tissue Evidence
* **Human Protein Atlas (HPA):** Protein and transcript evidence confirm expression as a secreted plasma protein with direct biological roles in cholesterol and lipid metabolism. HPA also documents interacting metabolic receptors, including LDLR (`ENSG00000130164`).
* **GTEx Expression Data:** The GTEx query returned no results for RNA expression profiles in this query run.
* **Tissue Interpretation:** While GTEx RNA quantification was unavailable in the current query, HPA protein annotations establish that PCSK9 functions as a secreted plasma protein acting primarily on hepatic LDL receptor clearance.

---

### 5. Genetic Evidence
* **ClinVar Evidence:** ClinVar contains multiple documented genetic variation records for *PCSK9* (e.g., variant IDs `4881694`, `4875483`, `4874269`, `4861692`, `4861691`).
* **Mendelian Relevance:** Gain-of-function variants in *PCSK9* are established causes of severe autosomal dominant hypercholesterolemia type 3 (`MONDO_0011369`). Conversely, loss-of-function variants lead to low plasma LDL cholesterol levels and lifelong protection against coronary heart disease without adverse health consequences, validating PCSK9 inhibition as a therapeutic strategy.

---

### 6. Disease Association Evidence
* **Open Targets Score:**
  * **Familial hypercholesterolemia (`MONDO_0005439`):** Score = **0.852**
  * **Hypercholesterolemia (`HP_0003124`):** Score = **0.820**
  * **Autosomal dominant hypercholesterolemia 3 (`MONDO_0011369`):** Score = **0.816**
  * **Cardiovascular disorder (`MONDO_0004995`):** Score = **0.724**
  * **Coronary artery disorder (`MONDO_0005010`):** Score = **0.718**
* **Direct vs. Indirect Evidence:**
  * *Direct:* Human human genetics (ClinVar, MONDO) and Phase 4 clinical trial data unequivocally link PCSK9 function directly to plasma LDL-C levels and hypercholesterolemia.
  * *Indirect:* Downstream associations with secondary cardiovascular outcomes (coronary artery disease, cardiovascular disease reduction).

---

### 7. Safety Evidence
* **FAERS Signals:**
  * Post-marketing spontaneous adverse event reports list co-administered regimens (evolocumab with statins/ezetimibe) associated with reported events such as *angina pectoris*, *ventricular extrasystoles*, and *back pain*.
* **Safety Interpretation:** Post-market FAERS reports represent passive, spontaneous safety submissions and do not establish causal drug-adverse event relationships. Clinical trial evaluations confirm evolocumab is well tolerated, with primary adverse events typically limited to injection site reactions and common upper respiratory symptoms.

---

### 8. Evidence Gaps
* **Tissue RNA Baseline:** GTEx database query returned empty results in this session, leaving tissue-specific transcript abundance unquantified within this tool run.
* **Long-term Safety Profiling:** Post-market surveillance captures spontaneous events; long-term observational registries remain essential for tracking rare real-world adverse event profiles across diverse multi-morbid patient cohorts.

---

### 9. Potential Mismatches
* **Database Representation Mismatch:** A missing GTEx transcript record contrasts with protein-level evidence from HPA and ChEMBL approval records. This reflects a query/database availability artifact rather than a true biological mismatch.
* **Tissue Context vs. Secreted Function:** PCSK9 acts extracellularly in the systemic circulation as a secreted protein; local mRNA expression patterns in non-hepatic tissues do not directly dictate systemic target liability or therapeutic efficacy.

---

### 10. Overall Evidence Assessment

| Evidence Category | Status / Evidence Level | Summary Notes |
| :--- | :--- | :--- |
| **Target Identity** | Confirmed (`PCSK9` / `ENSG00000169174`) | Secreted serine protease regulating hepatic LDLR degradation. |
| **Drug Identity** | Approved (`evolocumab` / Phase 4) | Fully human monoclonal antibody targeting extracellular PCSK9. |
| **Disease Alignment** | Strong canonical match (`HP:0003124`) | Direct association across familial and general hypercholesterolemia. |
| **Genetic Evidence** | Robust | Gain-of-function causes hypercholesterolemia; loss-of-function lowers LDL-C. |
| **Tissue Evidence** | Partial (HPA available, GTEx empty) | Confirmed plasma/secreted protein; hepatic LDLR interplay. |
| **Safety Signals** | Monitored (FAERS reports noted) | FAERS adverse signals require clinical contextualization and do not prove causality. |

**Synthesis Verdict:**
The biological, genetic, and clinical evidence strongly supports targeting PCSK9 with evolocumab for hypercholesterolemia. The relationship is backed by human loss-of-function and gain-of-function genetics, high Open Targets association scores (>0.81), and Phase 4 regulatory approvals. Missing GTEx transcript data represents a technical tool retrieval gap rather than biological uncertainty. Overall, the target-drug-disease mechanism is firmly established with a favorable therapeutic rationale.

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
