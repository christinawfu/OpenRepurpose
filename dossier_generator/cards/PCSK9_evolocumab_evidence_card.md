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

An investigation was conducted for the drug-repurposing target **PCSK9**, the drug **evolocumab**, and the disease **hypercholesterolemia** using biomedical database APIs. Below is the structured scientific synthesis.

---

### 1. Target Summary
* **Gene Symbol:** PCSK9 (Proprotein Convertase Subtilisin/Kexin Type 9)
* **Ensembl Identifier:** `ENSG00000169174`
* **Biological Role:** PCSK9 encodes a secreted serine protease that binds to low-density lipoprotein receptors (LDLR) on hepatocytes, promoting LDLR degradation and thereby decreasing hepatic clearance of circulating LDL cholesterol.

---

### 2. Disease Summary
* **Disease Name:** Hypercholesterolemia
* **Canonical Ontologies:**
  * **HPO:** `HP:0003124` (Hypercholesterolemia)
  * **MeSH:** `mesh:D006937`
  * **SNOMED CT:** `SNOMED:13644009`
  * **MONDO / Related Concepts:** Familial Hypercholesterolemia (`MONDO:0005439`), Autosomal Dominant Hypercholesterolemia 3 (`MONDO:0011369`)
* **Clinical Context:** Characterized by elevated circulating total and LDL cholesterol levels, significantly increasing the risk for premature atherosclerosis and cardiovascular diseases.

---

### 3. Drug Summary
* **Drug Name:** Evolocumab (Trade Name: Repatha, Research Code: AMG-145)
* **ChEMBL Identifier:** `CHEMBL2364655`
* **Drug Class & Type:** Fully human monoclonal antibody (IgG2), Parenteral administration
* **ATC Classification:** `C10AX13` (Other lipid-modifying agents)
* **Approval Status:** First approved in 2015; currently at Maximum Clinical Phase 4 (Approved drug).
* **Mechanism of Action:** Direct inhibition of extracellular PCSK9, blocking its interaction with LDLR and preserving hepatic LDLR recycling to lower plasma LDL cholesterol.

---

### 4. Tissue Evidence
* **GTEx RNA Expression (GTEx v8):**
  * **Highest Expression:** **Liver** (Median TPM: **25.55**), aligning with the primary biological site of LDLR regulation and cholesterol homeostasis.
  * **Other Notable Tissues:** Brain Cerebellum / Cerebellar Hemisphere (22.15–23.50 TPM), Lung (6.74 TPM), Esophagus Mucosa (4.94 TPM), Terminal Ileum (2.89 TPM), and Pancreas (2.68 TPM).
* **Human Protein Atlas (HPA):**
  * **Protein Tissue Distribution:** Detected in select tissue subsets ("Group enriched", specificity score: 83).
  * **Observed Protein Detection:** High antibody/protein intensity reported in lung and kidney. Related biological pathway proteins (e.g., LDLR) show strong expression across hepatic, intestinal, and endothelial tissues.

---

### 5. Genetic Evidence
* **ClinVar Records:** Multiple pathogenic and likely pathogenic genetic variant entries for `PCSK9` (e.g., variant IDs `4881694`, `4875483`, `4874269`, `4861692`, `4861691`).
* **Open Targets Genetic Associations:**
  * **Hypercholesterolemia, Autosomal Dominant, 3** (`MONDO_0011369`): Association score = **0.816**
  * **Familial Hypercholesterolemia** (`MONDO_0005439`): Association score = **0.852**
* **Genetic Interpretation:** Gain-of-function variants in *PCSK9* cause severe hypercholesterolemia, whereas loss-of-function variants are associated with low circulating LDL cholesterol and protection against coronary artery disease, establishing a validated human genetic target.

---

### 6. Disease Association Evidence
* **Open Targets Score Profile:**
  * **Familial Hypercholesterolemia:** `0.852`
  * **Hypercholesterolemia (HPO):** `0.820`
  * **Autosomal Dominant Hypercholesterolemia 3:** `0.816`
  * **Cardiovascular Disorder:** `0.724`
  * **Coronary Artery Disorder:** `0.718`
* **Evidence Level:** Direct, high-confidence target-disease association supported by human genetics, clinical trial data, and observational studies.

---

### 7. Safety Evidence (FAERS Signals)
* **Primary Post-Market Adverse Event Reports (openFDA FAERS):**
  * Dyspnoea (120 events)
  * Atrial Fibrillation (101 events)
  * Coronary Artery Disease (100 events)
  * Drug Ineffective (99 events)
  * Muscle Spasms (96 events)
  * Cough (93 events)
  * Nasopharyngitis (89 events)
  * Cardiac Disorder (86 events)
  * Dysphonia (85 events)
  * Chest Discomfort (83 events)
* **Safety Interpretation:** FAERS signals reflect voluntary post-market reporting and **do not establish causality**. The presence of cardiovascular reporting terms (e.g., coronary artery disease, chest discomfort) likely represents baseline disease background in hypercholesterolemic patients (indication bias) rather than drug-induced toxicity.

---

### 8. Potential Mismatches & Nuances
* **Tissue Expression Naming / Detection Nuance:** GTEx demonstrates primary RNA transcript expression in the liver (25.55 TPM) alongside central nervous system tissues (cerebellum), whereas HPA antibody-based protein profiling emphasizes lung and kidney tissue intensity. This represents differences in assay sensitivities, sampling, or protein turnover rates rather than a biological contradiction.
* **Brain Expression:** Elevated RNA expression in cerebellar tissue warrants awareness, though therapeutic monoclonal antibodies (such as evolocumab) do not readily cross the intact blood-brain barrier under normal physiological conditions.

---

### 9. Evidence Gaps
* Standalone OMIM and DisGeNET API endpoints were not directly queried via independent individual tools; genetic relationship aggregation was instead evaluated through Open Targets and ClinVar.
* Functional assessment of neurocognitive or central nervous system effects requires continued clinical safety surveillance due to brain RNA expression.

---

### 10. Integrated Assessment & Synthesis

| Evidence Type | Findings & Strength | Supporting Sources |
| :--- | :--- | :--- |
| **Direct Clinical Evidence** | Approved indication for hypercholesterolemia and cardiovascular risk reduction (Phase 4). | ChEMBL, FDA/EMA labels |
| **Direct Target-Disease Evidence** | Exceptionally high score (0.82–0.85) connecting PCSK9 to familial and primary hypercholesterolemia. | Open Targets |
| **Genetic Evidence** | Robust gain-of-function and loss-of-function human genetic validation in autosomal dominant hypercholesterolemia. | ClinVar, Open Targets |
| **Tissue Evidence** | GTEx confirms primary hepatic RNA expression (25.55 TPM), matching the site of LDLR regulation. | GTEx, HPA |
| **Safety Signals** | Post-market reporting shows nasopharyngitis, muscle spasms, and cardiovascular events (the latter influenced by indication bias). | openFDA FAERS |

**Conclusion:** The biological rationale for evolocumab targeting PCSK9 in hypercholesterolemia is supported by robust, concordant evidence across human genetics, physiological tissue distribution (hepatic localization), biochemical mechanism of action, and regulatory approvals.

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
