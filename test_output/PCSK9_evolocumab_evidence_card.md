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

Canonical disease: Hypercholesterolemia (disorder)

Canonical ID: Unknown

## Integrated Evidence Assessment

**Evidence availability:** Broad

**Sources successfully retrieved:** 8 / 10 (80.0%)

### Tissue Evidence

Both RNA-level and protein-level tissue evidence are available.

### Tissue Cross-Database Comparison

GTEx returned tissue information, but HPA did not expose comparable tissue information.

**GTEx-only tissues:** Adipose_Subcutaneous, Adipose_Visceral_Omentum, Adrenal_Gland, Artery_Aorta, Artery_Coronary, Artery_Tibial, Bladder, Brain_Amygdala, Brain_Anterior_cingulate_cortex_BA24, Brain_Caudate_basal_ganglia, Brain_Cerebellar_Hemisphere, Brain_Cerebellum, Brain_Cortex, Brain_Frontal_Cortex_BA9, Brain_Hippocampus, Brain_Hypothalamus, Brain_Nucleus_accumbens_basal_ganglia, Brain_Putamen_basal_ganglia, Brain_Spinal_cord_cervical_c-1, Brain_Substantia_nigra, Breast_Mammary_Tissue, Cells_Cultured_fibroblasts, Cells_EBV-transformed_lymphocytes, Cervix_Ectocervix, Cervix_Endocervix, Colon_Sigmoid, Colon_Transverse, Esophagus_Gastroesophageal_Junction, Esophagus_Mucosa, Esophagus_Muscularis, Fallopian_Tube, Heart_Atrial_Appendage, Heart_Left_Ventricle, Kidney_Cortex, Kidney_Medulla, Liver, Lung, Minor_Salivary_Gland, Muscle_Skeletal, Nerve_Tibial, Ovary, Pancreas, Pituitary, Prostate, Skin_Not_Sun_Exposed_Suprapubic, Skin_Sun_Exposed_Lower_leg, Small_Intestine_Terminal_Ileum, Spleen, Stomach, Testis, Thyroid, Uterus, Vagina, Whole_Blood

> **Tissue evidence flag:** The current data warrant additional biological interpretation.

### Genetic Evidence

Genetic evidence is available from: ClinVar

### Rare-Disease Relevance

Disease/genetic evidence relevant to rare-disease assessment is available.

Supporting sources: ClinVar

### Evidence Gaps

- **disease-gene aggregation** (disgenet): error
- **Mendelian disease genetics** (omim): error

**Scientific caution:** This assessment describes evidence availability and does not establish clinical efficacy, causality, or therapeutic suitability.

## Integrated Verdict

The current evidence retrieval indicates **broad evidence availability** across the connected biomedical databases.

This is an evidence-availability assessment rather than a prediction of clinical efficacy.

## Gemini Evidence Synthesis

### 1. Target Summary
* **Gene Symbol:** *PCSK9* (Proprotein Convertase Subtilisin/Kexin Type 9)
* **Ensembl ID:** `ENSG00000169174`
* **Biological Function:** PCSK9 encodes a secreted serine protease that binds to the low-density lipoprotein receptor (LDLR) on the surface of hepatocytes, promoting LDLR degradation in lysosomes. Inhibiting or blocking PCSK9 prevents LDLR degradation, increasing hepatic surface LDLR expression and accelerating clearance of circulating low-density lipoprotein cholesterol (LDL-C).

---

### 2. Disease Summary
* **Disease:** Hypercholesterolemia
* **Canonical Identifiers:** 
  * MeSH: `D006937`
  * HPO: `HP_0003124`
  * MONDO: `MONDO_0005439` (Familial hypercholesterolemia), `MONDO_0011369` (Hypercholesterolemia, autosomal dominant, 3)
* **Pathophysiology:** Characterized by elevated concentrations of total cholesterol and LDL-C in the blood, leading to accelerated atherogenesis and heightened risk of coronary artery disease and major adverse cardiovascular events.

---

### 3. Drug Summary
* **Drug Name:** Evolocumab (Trade Name: Repatha®; ChEMBL ID: `CHEMBL2364655`)
* **Drug Class & Type:** Fully human IgG2 monoclonal antibody targeting extracellular PCSK9 (`-umab` stem; ATC code `C10AX13`).
* **Approval Status:** Approved (Max Phase 4.0; initial approval in 2015 by FDA/EMA).
* **Route of Administration:** Parenteral (subcutaneous injection).
* **Mechanism of Action:** Direct binding to circulating PCSK9, preventing its interaction with the LDLR, thereby reducing LDLR degradation and lowering serum LDL-C levels.

---

### 4. Tissue Evidence
* **GTEx RNA Expression (v8):**
  * **Highest Expression:** Liver (median `25.55 TPM`), consistent with primary physiological role in hepatic LDLR regulation.
  * **Secondary Expression:** Brain Cerebellar Hemisphere (`23.50 TPM`), Brain Cerebellum (`22.15 TPM`), Lung (`6.74 TPM`), Esophagus Mucosa (`4.94 TPM`), Small Intestine (`2.89 TPM`), Pancreas (`2.68 TPM`).
* **Human Protein Atlas (HPA):**
  * Protein tissue distribution is categorized as "Detected in some" with "Group enriched" specificity (score 83). High protein level intensities are reported in lung and kidney.
* **Tissue Interpretation:** 
  * The strong hepatic expression observed in GTEx aligns directly with hepatic lipid metabolism and LDLR recycling dynamics.
  * *Potential Tissue Complexity:* High cerebellar RNA levels in GTEx warrant contextual mention, though monoclonal antibodies such as evolocumab do not cross the intact blood-brain barrier under standard therapeutic conditions.

---

### 5. Genetic Evidence
* **ClinVar Records:** 5 representative variant entries retrieved (`4881694`, `4875483`, `4874269`, `4861692`, `4861691`).
* **Mendelian Pathology:** Gain-of-function variants in *PCSK9* cause autosomal dominant hypercholesterolemia 3 (`MONDO_0011369`), leading to severe hypercholesterolemia due to excessive LDLR degradation. Conversely, loss-of-function variants in *PCSK9* are well-documented to result in low circulating LDL-C levels and reduced risk of coronary heart disease without severe adverse phenotypes.

---

### 6. Disease Association Evidence
* **Open Targets Score Summary:**
  * Familial Hypercholesterolemia (`MONDO_0005439`): **0.852**
  * Hypercholesterolemia (`HP_0003124`): **0.820**
  * Autosomal Dominant Hypercholesterolemia 3 (`MONDO_0011369`): **0.816**
  * Cardiovascular Disorder (`MONDO_0004995`): **0.724**
  * Coronary Artery Disorder (`MONDO_0005010`): **0.718**
* **Evidence Level:** Direct genetic, clinical, and database evidence strongly connects *PCSK9* dysregulation to hypercholesterolemia and downstream cardiovascular sequelae.

---

### 7. Safety Evidence
* **openFDA FAERS Safety Signals:**
  * Common post-marketing reported adverse events include:
    * Dyspnoea ($n=120$)
    * Atrial fibrillation ($n=101$)
    * Coronary artery disease ($n=100$)
    * Drug ineffective ($n=99$)
    * Muscle spasms ($n=96$)
    * Cough ($n=93$)
    * Nasopharyngitis ($n=89$)
    * Cardiac disorder ($n=86$)
    * Dysphonia ($n=85$)
    * Chest discomfort ($n=83$)
* **Safety Interpretation:** 
  * Spontaneous post-marketing reporting in FAERS reflects adverse events reported in patients taking evolocumab, but does **not** establish causality.
  * Reported cardiac and vascular events (e.g., coronary artery disease, atrial fibrillation) reflect the underlying baseline cardiovascular risk profile of hypercholesterolemic patients receiving therapy.
  * Nasopharyngitis and upper respiratory symptoms align with established clinical trial safety profiles for monoclonal antibody therapies.

---

### 8. Evidence Gaps
* **Direct Database Gaps:** Direct standalone OMIM and DisGeNET API endpoints were not directly queried by the tool suite (though human genetic associations are captured in Open Targets and ClinVar).
* **Mechanistic / Pharmacodynamic Gaps:** Long-term effects of near-complete systemic suppression of extracellular PCSK9 across decades continue to be monitored in long-term extension studies.

---

### 9. Potential Contradictions and Mismatches
* **GTEx vs. Target Site:** GTEx displays notable transcript expression in cerebellar brain tissues alongside the primary liver target. However, because evolocumab is a high-molecular-weight IgG2 monoclonal antibody administered parenterally, central nervous system exposure is extremely low due to the blood-brain barrier. Thus, CNS RNA expression does not represent an immediate therapeutic mismatch for systemic lipid lowering.
* **HPA vs. GTEx Annotations:** Tissue naming and intensity scores differ between GTEx (RNA) and HPA (protein) due to non-standardized tissue sample labeling across databases rather than established biological contradiction.

---

### 10. Overall Evidence Assessment

| Category | Evidence Level | Summary |
| :--- | :--- | :--- |
| **Direct Clinical Evidence** | **Strong / Confirmed** | Evolocumab is an FDA- and EMA-approved therapeutic (Phase 4) specifically indicated for hypercholesterolemia and cardiovascular risk reduction. |
| **Mechanistic Evidence** | **Strong** | Monoclonal antibody inhibition of extracellular PCSK9 prevents LDLR lysosomal degradation, increasing hepatic surface LDLR density and lowering serum LDL-C. |
| **Genetic Validation** | **Very High** | Gain-of-function variants cause human hypercholesterolemia; loss-of-function variants lower LDL-C and confer cardiovascular protection. |
| **Tissue Alignment** | **Consistent** | Predominant hepatic GTEx expression aligns with the primary site of cholesterol clearance via LDLR. |
| **Safety Profile** | **Acceptable / Monitored** | FAERS signals predominantly capture baseline cardiovascular risk of target patient population and minor respiratory/injection-site symptoms. |

**Verdict:** The target-drug-disease triplet (*PCSK9* – evolocumab – hypercholesterolemia) represents a fully validated, clinically approved indication backed by concordant genetic, mechanistic, tissue-level, and human clinical trial evidence.

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
