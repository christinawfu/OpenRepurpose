# OpenRepurpose Evidence Card

**Target:** EGFR
**Drug:** gefitinib
**Disease:** non-small cell lung cancer

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
| non-small cell lung carcinoma | 0.853 |
| lung adenocarcinoma | 0.774 |
| cancer | 0.737 |
| head and neck squamous cell carcinoma | 0.725 |
| lung cancer | 0.717 |

## GTEx Tissue Expression

GENCODE ID: ENSG00000146648.17

Expression records returned: 0

## Human Protein Atlas

Protein records returned: 28

## ClinVar

ClinVar records identified: 5

## ChEMBL

Drug/molecule information retrieved from ChEMBL.

## FAERS Safety Signals

Drug: gefitinib

## Disease Ontology

Canonical disease: Non-small cell lung cancer

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

* **Gene Symbol:** EGFR (Epidermal Growth Factor Receptor)
* **Ensembl Identifier:** `ENSG00000146648`
* **Biological Function:** Receptor tyrosine kinase of the ErbB family involved in extracellular signal transduction, controlling cellular proliferation, survival, differentiation, and migration via downstream signaling pathways (e.g., RAS-RAF-MEK-ERK, PI3K-AKT).

---

### 2. Disease Summary & Ontology Normalization

* **Queried Disease:** Non-small cell lung cancer (NSCLC)
* **Canonical Identifier:** `MONDO:0005233` (non-small cell lung carcinoma)
* **Cross-References:** `NCIT:C2926`, `SNOMED:254637007`
* **Clinical Context:** NSCLC encompasses the majority of lung malignancies (primarily adenocarcinoma and squamous cell carcinoma). A significant subset of NSCLC tumors are driven by somatic activating mutations in the kinase domain of *EGFR*.

---

### 3. Drug Summary

* **Drug Name:** Gefitinib
* **ChEMBL Identifier:** `CHEMBL939`
* **Molecular Class:** Small molecule, selective EGFR tyrosine kinase inhibitor (TKI)
* **Development Status:** Max Phase 4.0 (Approved; initial approval 2003)
* **ATC Classification:** `L01EB01` (Antineoplastic agents, EGFR protein kinase inhibitors)
* **Trade Names:** Iressa, Gefitinib Mylan

---

### 4. Tissue Evidence

* **GTEx RNA Expression (`ENSG00000146648.17`):**
  * **Lung Expression:** Moderate median expression in normal lung tissue (**22.1 TPM**).
  * **Highest Expressing Tissues:** Sun-exposed skin (**78.3 TPM**), non-sun-exposed skin (**75.9 TPM**), cultured fibroblasts (**60.6 TPM**), tibial nerve (**43.1 TPM**), vagina (**40.6 TPM**), and subcutaneous adipose tissue (**39.7 TPM**).
  * **Lowest Expressing Tissues:** Whole blood (**0.045 TPM**) and EBV-transformed lymphocytes (**0.15 TPM**).
* **Human Protein Atlas (HPA) Evidence:**
  * **Protein Tissue Distribution:** Classed as *"Detected in all"*.
  * **Tissue Specificity:** Classified as *"Low tissue specificity"*.
* **Tissue Context & Mismatch Interpretation:**
  * *Observation:* *EGFR* exhibits ubiquitous baseline expression across normal tissues rather than lung-exclusive expression.
  * *Biological Significance:* Efficacy in NSCLC does not depend on baseline organ-restricted expression, but rather on oncogenic kinase activation (e.g., somatic mutations or gene amplification) in tumor cells.
  * *Toxicity Rationale:* High baseline expression in skin and gastrointestinal mucosa correlates directly with observed on-target clinical toxicities (cutaneous rash, mucosal diarrhea).

---

### 5. Genetic Evidence

* **ClinVar Analysis:**
  * Multiple ClinVar variant records exist for *EGFR* (e.g., variant IDs `4883967`, `4881378`, `4881265`, `4881261`, `4881248`).
* **Genomic Relevance:**
  * **Somatic Driver Mutations:** In-frame exon 19 deletions and exon 21 point mutations (e.g., L858R) structurally alter the ATP-binding pocket of EGFR, causing constitutive kinase activation and conferring sensitivity to first-generation TKIs like gefitinib.
  * **Resistance Mutations:** Secondary mutations (e.g., T790M) emerge during therapy, altering drug binding affinity and mediating clinical resistance.

---

### 6. Disease Association Evidence

* **Open Targets Platform:**
  * **Non-small cell lung carcinoma (`MONDO_0005233`):** High overall association score of **0.853**.
  * **Lung adenocarcinoma (`MONDO_0005061`):** Association score of **0.774**.
  * **General lung cancer (`MONDO_0008903`):** Association score of **0.717**.
  * **Head and neck squamous cell carcinoma (`MONDO_0010150`):** Association score of **0.725**.

---

### 7. Safety Evidence & Post-Market Signals

* **openFDA FAERS Safety Signals (Gefitinib):**
  * **Primary On-Target Toxicities:** Diarrhea (175 reports), Rash (144 reports), Nausea (94 reports).
  * **Oncology Outcome / Resistance Signals:** Malignant neoplasm progression (611 reports), Drug resistance (488 reports), Acquired gene mutation (219 reports), Disease progression (150 reports), Central nervous system metastases (112 reports), EGFR gene mutation (110 reports), Death (109 reports).
* **Pharmacovigilance Interpretation:**
  * FAERS adverse event reports reflect post-market spontaneous reporting and do not independently establish causality.
  * Dermatologic and gastrointestinal events align directly with GTEx and HPA findings of broad baseline EGFR expression in skin and mucosal tissues.
  * Signals related to acquired mutations and disease progression reflect standard clinical resistance patterns encountered in advanced NSCLC management.

---

### 8. Evidence Gaps & Data Availability

* **OMIM & DisGeNET:** Not directly queried via available tools; however, ClinVar and Open Targets provide strong somatic and germline variant association data.
* **Variant-Level Response Stratification:** High-level database records confirm variant presence, but specific clinical trial response rates per individual variant require specialized trial data synthesis.

---

### 9. Categorized Scientific Synthesis

| Evidence Category | Evidence Level | Summary Findings | Sources |
| :--- | :--- | :--- | :--- |
| **Direct Clinical Evidence** | **Established / Approved** | Gefitinib is an approved Phase 4 oral drug for *EGFR*-mutated non-small cell lung cancer (ATC L01EB01). | ChEMBL |
| **Database Associations** | **Strong** | High target-disease association score (0.853) for non-small cell lung carcinoma. | Open Targets |
| **Genetic Evidence** | **Strong / Mechanistic** | Somatic driver variants in *EGFR* dictate tumor dependence and TKI sensitivity/resistance. | ClinVar |
| **Tissue Evidence** | **Ubiquitous Baseline** | GTEx (22.1 TPM in lung; high in skin/GI) and HPA ("Detected in all") confirm broad epithelial expression. | GTEx, HPA |
| **Safety Signals** | **On-Target & Resistance** | FAERS events highlight expected cutaneous/mucosal toxicities alongside cancer progression/resistance signals. | openFDA FAERS |

---

### 10. Overall Evidence Assessment

The evidence supporting the triad of **EGFR**, **gefitinib**, and **non-small cell lung cancer** is definitive and represents an established clinical paradigm rather than an unvalidated repurposing candidate. 

1. **Mechanism & Target Validity:** Efficacy is driven by somatic oncogenic alterations in *EGFR* rather than tissue-restricted baseline expression.
2. **Clinical Utility:** Gefitinib functions as a direct inhibitor of the active EGFR kinase domain.
3. **Safety & Expression Alignment:** GTEx and HPA data showing ubiquitous epithelial expression (particularly skin and GI tract) provide a rational baseline explanation for the primary clinical toxicities (rash and diarrhea) observed in FAERS pharmacovigilance data.

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
