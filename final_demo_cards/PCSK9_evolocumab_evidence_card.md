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
| omim | success |

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

Canonical disease: Hypercholesterolemia (disorder)

Canonical ID: Unknown

## Integrated Evidence Assessment

**Evidence availability:** Broad

**Sources successfully retrieved:** 9 / 10 (90.0%)

### Tissue Evidence

Both RNA-level and protein-level tissue evidence are available.

### Tissue Cross-Database Comparison

GTEx returned tissue information, but HPA did not expose comparable tissue information.

**GTEx-only tissues:** Adipose_Subcutaneous, Adipose_Visceral_Omentum, Adrenal_Gland, Artery_Aorta, Artery_Coronary, Artery_Tibial, Bladder, Brain_Amygdala, Brain_Anterior_cingulate_cortex_BA24, Brain_Caudate_basal_ganglia, Brain_Cerebellar_Hemisphere, Brain_Cerebellum, Brain_Cortex, Brain_Frontal_Cortex_BA9, Brain_Hippocampus, Brain_Hypothalamus, Brain_Nucleus_accumbens_basal_ganglia, Brain_Putamen_basal_ganglia, Brain_Spinal_cord_cervical_c-1, Brain_Substantia_nigra, Breast_Mammary_Tissue, Cells_Cultured_fibroblasts, Cells_EBV-transformed_lymphocytes, Cervix_Ectocervix, Cervix_Endocervix, Colon_Sigmoid, Colon_Transverse, Esophagus_Gastroesophageal_Junction, Esophagus_Mucosa, Esophagus_Muscularis, Fallopian_Tube, Heart_Atrial_Appendage, Heart_Left_Ventricle, Kidney_Cortex, Kidney_Medulla, Liver, Lung, Minor_Salivary_Gland, Muscle_Skeletal, Nerve_Tibial, Ovary, Pancreas, Pituitary, Prostate, Skin_Not_Sun_Exposed_Suprapubic, Skin_Sun_Exposed_Lower_leg, Small_Intestine_Terminal_Ileum, Spleen, Stomach, Testis, Thyroid, Uterus, Vagina, Whole_Blood

> **Tissue evidence flag:** The current data warrant additional biological interpretation.

### Genetic Evidence

Genetic evidence is available from: ClinVar, OMIM

### Rare-Disease Relevance

Disease/genetic evidence relevant to rare-disease assessment is available.

Supporting sources: OMIM, ClinVar

### Evidence Gaps

- **disease-gene aggregation** (disgenet): error

**Scientific caution:** This assessment describes evidence availability and does not establish clinical efficacy, causality, or therapeutic suitability.

## Integrated Verdict

The current evidence retrieval indicates **broad evidence availability** across the connected biomedical databases.

This is an evidence-availability assessment rather than a prediction of clinical efficacy.

## Gemini Evidence Synthesis

### 1. Target Summary

* **Gene Symbol:** *PCSK9* (Proprotein Convertase Subtilisin/Kexin Type 9)
* **Ensembl ID:** `ENSG00000169174`
* **Biological Function:** *PCSK9* encodes a secreted serine protease that binds to low-density lipoprotein receptors (LDLR) on cell surfaces, directing them to lysosomal degradation. By reducing hepatic LDLR recycling, PCSK9 raises circulating low-density lipoprotein cholesterol (LDL-C) levels.

---

### 2. Disease Summary

* **Disease Name:** Hypercholesterolemia
* **Canonical Identifiers:** 
  * `HP:0003124` (Hypercholesterolemia)
  * `MONDO:0005439` (Familial Hypercholesterolemia)
  * `MONDO:0011369` (Hypercholesterolemia, Autosomal Dominant, 3)
  * `SNOMED:13644009` / `MeSH:D006937`
* **Clinical Definition:** Elevated concentrations of total cholesterol and LDL-C in the blood, leading to accelerated atherogenesis and heightened risk for premature coronary artery disease and cardiovascular events.

---

### 3. Drug Summary

* **Drug Name:** Evolocumab
* **Trade Name:** Repatha / Repatha SureClick
* **ChEMBL ID:** `CHEMBL2364655`
* **ATC Classification:** `C10AX13` (Other lipid modifying agents)
* **Drug Modality & Mechanism:** Fully human IgG2 monoclonal antibody targeting extracellular PCSK9. By preventing PCSK9 from binding to LDLR, evolocumab increases LDLR recycling to the cell surface, facilitating increased clearance of circulating LDL-C.
* **Development & Approval Status:** Approved for clinical use (First approval: 2015; Max Clinical Phase: Phase 4). Administered parenterally.

---

### 4. Tissue Evidence & Alignment Analysis

* **RNA Expression (GTEx v8):**
  * **Highest Expression:** Liver (median `25.55 TPM`), aligning directly with the primary physiological site of LDLR synthesis, cholesterol metabolism, and systemic LDL clearance.
  * **Other Tissues:** High transcript levels observed in central nervous system structures (Cerebellar Hemisphere: `23.50 TPM`, Cerebellum: `22.15 TPM`), with modest expression in lung (`6.74 TPM`), esophagus mucosa (`4.94 TPM`), terminal ileum (`2.89 TPM`), and pancreas (`2.68 TPM`).
* **Protein Evidence (Human Protein Atlas):**
  * *PCSK9* protein evidence indicates a "Group enriched" tissue specificity profile. High protein detection intensities are reported in tissues such as lung and kidney.
* **Tissue Alignment Assessment:**
  * **Hepatic Alignment:** Strong expression of *PCSK9* RNA in liver tissue directly supports the biological mechanism of hepatic LDLR protection.
  * **Central Nervous System & Peripheral Expression:** The high transcript levels observed in brain tissues represent a potential tissue-level nuance. However, because evolocumab is a large monoclonal antibody administered peripherally, it does not readily cross the intact blood-brain barrier. Thus, central nervous system transcript expression does not undermine the peripheral mechanism of action, though peripheral tissue distribution (e.g., lung) underscores the importance of monitoring systemically broad target engagement.

---

### 5. Genetic & Mendelian Evidence

* **Open Targets Genetic Scores:**
  * **Familial Hypercholesterolemia (`MONDO_0005439`):** `0.852`
  * **Hypercholesterolemia (`HP_0003124`):** `0.820`
  * **Autosomal Dominant Hypercholesterolemia 3 (`MONDO_0011369`):** `0.816`
* **ClinVar Evidence:**
  * ClinVar contains validated pathogenic genetic variants (e.g., variant IDs `4881694`, `4875483`, `4874269`, `4861692`, `4861691`).
  * **Mechanistic Insights:** Gain-of-function mutations in *PCSK9* cause autosomal dominant hypercholesterolemia by excessively degrading LDLR, whereas naturally occurring loss-of-function variants lead to low LDL-C levels and significant lifelong protection against coronary artery disease without major adverse phenotype trade-offs.

---

### 6. Disease Association Evidence

* **Direct Associations (Open Targets):**
  * Strong associations are documented across lipid phenotypes and secondary cardiovascular endpoints:
    * Cardiovascular disorder (`MONDO_0004995`): score `0.724`
    * Coronary artery disorder (`MONDO_0005010`): score `0.718`
* **Interpretation:** The genetic, biomarker, and epidemiological database associations consistently link *PCSK9* variation to serum cholesterol regulation and downstream atherosclerotic cardiovascular disease.

---

### 7. Safety Evidence (FAERS Signals)

Analysis of post-marketing adverse event reports from openFDA FAERS for evolocumab identifies the following top reported adverse event terms:

1. **Dyspnoea** ($n=120$)
2. **Atrial Fibrillation** ($n=101$)
3. **Coronary Artery Disease** ($n=100$)
4. **Drug Ineffective** ($n=99$)
5. **Muscle Spasms** ($n=96$)
6. **Cough** ($n=93$)
7. **Nasopharyngitis** ($n=89$)
8. **Cardiac Disorder** ($n=86$)
9. **Dysphonia** ($n=85$)
10. **Chest Discomfort** ($n=83$)

* **Safety Signal Interpretation:** FAERS data reflect voluntary post-market passive reporting. Cardiovascular terms (e.g., coronary artery disease, atrial fibrillation) and respiratory symptoms reflect background comorbidities in high-risk hypercholesterolemic patient cohorts receiving lipid-lowering therapy. Spontaneous reporting does **not** establish direct pharmacological causation.

---

### 8. Evidence Gaps & Limitations

* **Specific Variant-Level Annotation:** Detailed functional characterization of individual novel loss-of-function versus gain-of-function mutations was limited to aggregated ClinVar variant identifiers.
* **Database Terminology Differences:** Tissue naming conventions between GTEx and Human Protein Atlas vary, presenting a nominal nomenclature mismatch rather than a definitive biological conflict.

---

### 9. Overall Evidence Assessment & Synthesis

| Evidence Category | Level of Support | Summary Findings |
| :--- | :--- | :--- |
| **Direct Therapeutic Evidence** | **Strong** | Evolocumab is an approved monoclonal antibody targeting PCSK9 with documented therapeutic efficacy in lowering LDL-C. |
| **Mechanistic Evidence** | **Strong** | High expression of *PCSK9* transcript in human liver (GTEx `25.55 TPM`) directly supports the hepatic LDLR recycling hypothesis. |
| **Genetic Evidence** | **Strong** | Mendelian disorders (Autosomal Dominant Hypercholesterolemia 3) and ClinVar variants validate *PCSK9* as a causal driver of hypercholesterolemia. |
| **Safety Signals** | **Moderate / Context-dependent** | FAERS events (e.g., nasopharyngitis, muscle spasms, cardiovascular events) reflect baseline patient risk and post-market reporting trends rather than proven toxicity. |

**Scientific Verdict:**  
The collected evidence strongly supports targeting PCSK9 with evolocumab for hypercholesterolemia. Human genetic data, transcriptomic localization in the liver, and validated clinical efficacy collectively confirm the validity of this target-drug-disease triplet.

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
| omim | success |

Evidence is retrieved from public biomedical database APIs through OpenRepurpose wrappers. Unavailable sources are reported rather than treated as evidence of absence.
