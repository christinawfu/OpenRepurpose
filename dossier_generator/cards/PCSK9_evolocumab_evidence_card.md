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

## Gemini Evidence Synthesis

# Scientific Evidence Synthesis: PCSK9 / Evolocumab / Hypercholesterolemia

---

### 1. Target Summary
* **Gene Symbol:** PCSK9 (*Proprotein convertase subtilisin/kexin type 9*)
* **Ensembl ID:** `ENSG00000169174`
* **Protein Function & Class:** Serine protease, secreted plasma protein involved in cholesterol, sterol, and lipid metabolism. 
* **Biological Mechanism:** PCSK9 binds to low-density lipoprotein receptors (LDLR) on hepatocytes, promoting their lysosomal degradation and thereby reducing plasma clearance of low-density lipoprotein cholesterol (LDL-C).

---

### 2. Disease Summary
* **Disease Name:** Hypercholesterolemia
* **Ontology Mapping:** 
  * `HP:0003124` (*Hypercholesterolemia*)
  * `MONDO:0005439` (*Familial hypercholesterolemia*)
  * `MONDO:0011369` (*Hypercholesterolemia, autosomal dominant, 3 / HCHOLA3*)
* **Clinical Context:** Characterized by pathologically elevated levels of circulating cholesterol (specifically LDL-C), leading to accelerated atherosclerosis and increased risk of coronary artery disease and cardiovascular events.

---

### 3. Drug Summary
* **Drug Name:** Evolocumab (Trade name: Repatha; ChEMBL ID: `CHEMBL2364655`)
* **Drug Type & Mechanism:** Fully human IgG2 monoclonal antibody targeting PCSK9. It binds selectively to PCSK9, preventing its interaction with LDLR and leading to increased hepatocyte LDLR surface expression and enhanced clearance of plasma LDL-C.
* **Approval Status:** First approved in 2015 (Max Phase 4.0; ATC Class `C10AX13`). Administered via parenteral (subcutaneous) route.

---

### 4. Tissue Evidence
* **Human Protein Atlas (HPA):** Validates PCSK9 as a secreted plasma protein with strong protein-level evidence involved in cholesterol and lipid metabolism, alongside key interacting pathways involving LDLR.
* **GTEx Expression Data:** Query returned no RNA expression data from the GTEx database API endpoint.
* **Tissue Match Analysis:** HPA evidence confirms a clear functional alignment with systemic circulation and hepatic cholesterol clearance via the secreted protein pathway.

---

### 5. Genetic Evidence
* **ClinVar:** Identified multiple clinically annotated genetic variants in `PCSK9` (e.g., ClinVar variant IDs `4875483`, `4874269`, `4861692`).
* **Mendelian Disease Links:** Gain-of-function mutations in `PCSK9` cause autosomal dominant hypercholesterolemia 3 (`MONDO:0011369`), directly increasing plasma LDL-C levels. Conversely, naturally occurring loss-of-function variants in human populations significantly lower LDL-C and confer protection against coronary artery disease without major adverse developmental phenotypes.

---

### 6. Disease Association Evidence
* **Open Targets Score:** Strong target-disease associations across multiple ontologies:
  * Familial Hypercholesterolemia (`MONDO_0005439`): Score **0.852**
  * Hypercholesterolemia (`HP_0003124`): Score **0.820**
  * Autosomal Dominant Hypercholesterolemia 3 (`MONDO_0011369`): Score **0.816**
  * Cardiovascular Disorder (`MONDO_0004995`): Score **0.724**
  * Coronary Artery Disorder (`MONDO_0005010`): Score **0.718**

---

### 7. Safety Evidence
* **FAERS Signals:** Post-market spontaneous reports in patients taking evolocumab (often in combination regimens with statins/ezetimibe) note adverse events including:
  * Angina pectoris
  * Ventricular extrasystoles
  * Back pain
* **Interpretation:** FAERS reports reflect real-world post-market pharmacovigilance surveillance. These reports establish safety signals but do not demonstrate direct drug causality due to potential confounding factors (e.g., underlying cardiovascular disease in high-risk hypercholesterolemic patient populations).

---

### 8. Evidence Gaps
* **Database Gaps:** GTEx RNA expression records were unretrievable/absent via the automated database call during this query, requiring reliance on Human Protein Atlas for expression/protein localization evidence.
* **Variant Heterogeneity:** Detailed functional impact characterization for every individual variant in ClinVar requires dedicated variant-level curation.

---

### 9. Potential Mismatches
* **No Biological or Tissue Mismatch Detected:** Target expression, physiological function, genetic validation, and primary drug indication align across all sources.

---

### 10. Overall Evidence Assessment

| Evidence Category | Evidence Level | Description / Findings |
| :--- | :--- | :--- |
| **Direct Evidence** | Strong / Approved | Evolocumab is an FDA/EMA-approved direct PCSK9 inhibitor specifically indicated for hypercholesterolemia and cardiovascular risk reduction. |
| **Genetic Evidence** | High | Gain-of-function mutations in *PCSK9* cause severe hypercholesterolemia (`MONDO:0011369`), while loss-of-function variants lower LDL-C. |
| **Database Associations**| High | Open Targets score of >0.82 across hypercholesterolemia ontology terms. |
| **Tissue Evidence** | Moderate | HPA confirms protein-level evidence as a secreted plasma protein involved in lipid metabolism; GTEx API returned no records. |
| **Safety Signals** | Monitored | Post-market FAERS reports record cardiovascular events and back pain, typical for a high-risk cardiovascular population, requiring standard clinical surveillance. |

**Synthesis:** The mechanism of evolocumab targeting PCSK9 for hypercholesterolemia represents a benchmark validated target-disease-drug triad supported by direct clinical, pharmacological, and human genetic evidence.
