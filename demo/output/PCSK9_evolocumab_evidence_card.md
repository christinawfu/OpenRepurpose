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

### Biomedical Investigation Synthesis: PCSK9 — Evolocumab — Hypercholesterolemia

---

### 1. Target Summary
* **Gene Symbol:** `PCSK9` (Proprotein Convertase Subtilisin/Kexin Type 9)
* **Ensembl Identifier:** `ENSG00000169174`
* **Biological Function:** PCSK9 encodes a secreted serine protease that binds to low-density lipoprotein receptors (LDLR) on the surface of hepatocytes, promoting their intracellular degradation and thereby reducing hepatic clearance of circulating LDL cholesterol.

---

### 2. Disease Summary
* **Disease Name:** Hypercholesterolemia
* **Canonical Identifiers:** 
  * `HP:0003124` (Hypercholesterolemia)
  * `MONDO:0005439` (Familial Hypercholesterolemia)
  * `MONDO:0011369` (Hypercholesterolemia, Autosomal Dominant, 3)
  * `SNOMED:13644009` (Hypercholesterolemia disorder)
* **Clinical Context:** Characterized by abnormally elevated concentrations of circulating total and LDL cholesterol, leading to accelerated atherosclerosis and increased risk of cardiovascular and coronary artery disease.

---

### 3. Drug Summary
* **Drug Name:** Evolocumab (Trade Name: Repatha)
* **ChEMBL Identifier:** `CHEMBL2364655`
* **Molecule Type:** Fully human monoclonal antibody (`-umab`)
* **Mechanism of Action:** Direct binding and neutralization of extracellular PCSK9, preventing PCSK9-mediated LDLR degradation and restoring LDLR recycling to the hepatocyte surface.
* **Development Status:** Approved (Max Phase 4; initial approval 2015)
* **ATC Classification:** `C10AX13` (Other lipid modifying agents)
* **Administration Route:** Parenteral (subcutaneous injection)

---

### 4. Tissue Evidence
* **GTEx (RNA Expression):**
  * **Highest Tissue:** Liver (median expression: **25.55 TPM**), followed by Cerebellar Hemisphere (**23.50 TPM**) and Cerebellum (**22.15 TPM**). Moderate expression is present in Lung (**6.74 TPM**) and Esophagus Mucosa (**4.94 TPM**).
  * **Relevance:** The predominant expression in the liver is highly aligned with the known physiology of hepatic lipoprotein receptor regulation and systemic lipid clearance.
* **Human Protein Atlas (HPA):**
  * Protein tissue distribution is categorized as **"Group enriched"** (specificity score 83).
  * Protein intensity values recorded include Lung (**10,905.9**) and Kidney (**5,642.2**).
* **Tissue Comparison & Limitations:**
  * GTEx confirms robust hepatic transcription. 
  * Because PCSK9 is a secreted circulating proprotein synthesized heavily in the liver, tissue tissue-level protein quantification in HPA may capture local tissue binding or matrix retention (e.g., in lung or kidney vascular beds) rather than intracellular synthesis alone. Differing tissue nomenclature and detection methods across GTEx and HPA reflect distinct assays (RNA-seq vs. antibody/mass spectrometry intensities) and should not be interpreted as a biological contradiction.

---

### 5. Genetic Evidence
* **ClinVar:** 
  * Identified 5 cataloged clinical variant records for `PCSK9` (e.g., variant IDs `4881694`, `4875483`, `4874269`, `4861692`, `4861691`).
* **Mendelian & Population Genetics:**
  * Open Targets links `PCSK9` to **Autosomal Dominant Hypercholesterolemia 3 (HCHOLA3; `MONDO:0011369`)**.
  * Gain-of-function mutations in `PCSK9` lead to hypercholesterolemia via hyper-degradation of LDLR, whereas loss-of-function mutations are known to produce low plasma LDL cholesterol levels and confer protection against coronary heart disease.

---

### 6. Disease Association Evidence
* **Open Targets Database Scores:**
  * Familial hypercholesterolemia (`MONDO:0005439`): **0.852**
  * Hypercholesterolemia (`HP:0003124`): **0.820**
  * Autosomal dominant hypercholesterolemia 3 (`MONDO:0011369`): **0.816**
  * Cardiovascular disorder (`MONDO:0004995`): **0.724**
  * Coronary artery disorder (`MONDO:0005010`): **0.718**
* **Evidence Level:** Strong multi-layered database support spanning genetic associations, functional genomics, and clinical phenotypic links.

---

### 7. Safety Evidence (Post-Market Signals)
* **Source:** openFDA FAERS (Spontaneous Adverse Event Reporting System)
* **Top Reported Adverse Events for Evolocumab:**
  1. Dyspnoea ($n = 120$)
  2. Atrial fibrillation ($n = 101$)
  3. Coronary artery disease ($n = 100$)
  4. Drug ineffective ($n = 99$)
  5. Muscle spasms ($n = 96$)
  6. Cough ($n = 93$)
  7. Nasopharyngitis ($n = 89$)
  8. Cardiac disorder ($n = 86$)
  9. Dysphonia ($n = 85$)
  10. Chest discomfort ($n = 83$)
* **Safety Interpretation:** 
  * Spontaneous FAERS reporting counts reflect post-marketing surveillance submissions and **do not establish clinical causality** or estimate true incidence rates.
  * Reported cardiovascular events (e.g., coronary artery disease, atrial fibrillation) likely reflect underlying baseline risk in the patient population receiving lipid-lowering therapy.
  * Nasopharyngitis and upper respiratory symptoms are recognized potential adverse reactions listed in clinical labeling.

---

### 8. Evidence Gaps
* **OMIM / DisGeNET Specific Breakdown:** Detailed locus-specific penetrance data were not directly queried in this pipeline run.
* **Tissue Protein Kinetics:** Direct quantification of circulating extracellular PCSK9 protein clearance vs. tissue-bound hepatic LDLR degradation rates requires specialized functional assay integration beyond standard static database queries.

---

### 9. Potential Mismatches
* **Tissue Labeling Mismatch:** GTEx identifies the liver as the top RNA-expressing organ, whereas HPA highlights protein intensity in lung and kidney tissues. This difference highlights operational variations in sample preparation and assay types (transcriptional output vs. tissue protein detection) rather than a biological discrepancy, particularly given PCSK9's nature as a secreted protein.

---

### 10. Overall Evidence Assessment

| Evidence Category | Supporting Findings | Assessment / Confidence |
| :--- | :--- | :--- |
| **Direct Clinical Evidence** | FDA approval (2015), Phase 4 status for evolocumab targeting PCSK9 in hypercholesterolemia. | Strong direct clinical validation |
| **Mechanistic Evidence** | Monoclonal antibody binding of circulating PCSK9 prevents LDLR degradation. | Strong direct functional mechanism |
| **Genetic Evidence** | `PCSK9` variants linked to autosomal dominant hypercholesterolemia and ClinVar entries. | Strong Mendelian & human genetic evidence |
| **Tissue Evidence** | GTEx demonstrates high liver RNA expression (**25.55 TPM**), matching hepatic LDLR biology. | Strongly supporting physiological localization |
| **Safety Signals** | FAERS signals note respiratory and cardiovascular reports typical of the target population. | Surveillance signals present; causality unestablished |

**Conclusion:** 
The collected evidence **strongly supports** the therapeutic intervention of evolocumab against PCSK9 for hypercholesterolemia. High hepatic transcript expression, human genetic validation (gain- and loss-of-function phenotypes), and high Open Targets disease association scores consistently align with established clinical efficacy.

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
