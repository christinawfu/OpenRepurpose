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

Here is a structured, evidence-based biomedical synthesis investigating **empagliflozin** targeting **SLC5A2** (SGLT2) for **type 2 diabetes mellitus**.

---

### 1. Target Summary
* **Gene Symbol:** `SLC5A2`
* **Gene Name:** Solute Carrier Family 5 Member 2
* **Gene Synonyms:** `SGLT2` (Sodium-Glucose Cotransporter 2)
* **Ensembl Identifier:** `ENSG00000140675`
* **Biological Function:** `SLC5A2` encodes a membrane-bound, sodium-dependent glucose symporter responsible for reabsorbing the majority of filtered glucose from the lumen of the renal proximal tubule back into circulation.

---

### 2. Disease Summary
* **Canonical Disease Name:** Type 2 Diabetes Mellitus
* **Monarch/MONDO Identifier:** `MONDO:0005148`
* **Disease Characteristics:** A chronic metabolic disorder characterized by systemic insulin resistance, impaired insulin secretion, and persistent hyperglycemia leading to vascular and organ complications over time.

---

### 3. Drug Summary
* **Drug Name:** Empagliflozin (Brand Name: *Jardiance*)
* **ChEMBL Identifier:** `CHEMBL2107830`
* **ATC Classification:** `A10BK03` (Sodium-glucose co-transporter 2 [SGLT2] inhibitors)
* **Approval Status:** First approved in 2014; Phase 4 clinical status.
* **Mechanism of Action:** Direct inhibition of SGLT2 (`SLC5A2`) in the renal proximal tubule. By blocking renal glucose reabsorption, empagliflozin promotes urinary glucose excretion (glucosuria), thereby lowering plasma blood glucose levels independently of insulin action.

---

### 4. Tissue Evidence
* **Human Protein Atlas (HPA):** Confirms `SLC5A2` as a predicted membrane transporter and established FDA-approved drug target with protein-level validation (`Evidence at protein level`). High expression is historically localized to renal proximal tubular epithelial cells.
* **GTEx Expression Data:** The GTEx query returned empty records (`results: []`) for `SLC5A2` during this retrieval attempt.
* **Tissue Interpretation:** Physiological target localization is highly concentrated in the kidney (specifically S1/S2 proximal tubule segments) rather than major insulin-responsive metabolic tissues (such as skeletal muscle, liver, or endocrine pancreas).

---

### 5. Genetic Evidence
* **ClinVar Data:** Identified 5 clinically classified variant records (`4879630`, `4864643`, `4857303`, `4857297`, `4857271`). 
* **Mendelian Associations:** Inactivating loss-of-function variants in `SLC5A2` cause *Familial Renal Glucosuria* (`MONDO:0009297`), a hereditary trait characterized by persistent urinary glucose loss in the absence of systemic hyperglycemia or renal dysfunction.
* **Genetic Relevance:** Loss of function in human genetics mimics the pharmacological action of SGLT2 inhibitors (glucosuria without gross toxicity), offering strong genetic phenocopy support for drug safety and targeted mechanism.

---

### 6. Disease Association Evidence
* **Open Targets Score:** Strong association score between `SLC5A2` and Type 2 Diabetes Mellitus (`MONDO:0005148`, score: `0.6366`).
* **Related Phenotypic Associations:**
  * Familial Renal Glucosuria (`MONDO:0009297`, score: `0.7038`)
  * Heart Failure (`MONDO:0005252`, score: `0.6310`)
  * Chronic Kidney Disease (`MONDO:0005300`, score: `0.6264`)
* **Evidence Classification:**
  * *Direct Clinical Target Evidence:* Approved therapeutic indication with established clinical efficacy.
  * *Indirect/Secondary Evidence:* Cardiorenal protective associations reflected in secondary disease scoring (heart failure, chronic kidney disease).

---

### 7. Safety Evidence (Post-Market Signals)
* **FAERS Database Query:** A sample query of post-market reports for empagliflozin highlighted cases involving polypharmacy (e.g., concomitant administration with metformin, dulaglutide, or linagliptin).
* **Observed Adverse Event Terms in Sample Records:** Dyspepsia, flatulence, weight changes, injection-site reactions (associated with co-medications), headache, and ear/tooth discomfort.
* **Safety Interpretation:** FAERS signals reflect post-market observational reporting in complex, real-world clinical populations and **do not establish direct causality**. Standard clinical safety profiles for SGLT2 inhibitors typically monitor for mycotic genital infections, urinary tract infections, volume depletion, and rare euglycemic ketoacidosis.

---

### 8. Evidence Gaps
* **Tissue Expression Retrieval:** RNA-level tissue breakdown via GTEx was unavailable/unreturned in the current tool response.
* **Secondary Target Profiles:** Specific off-target binding affinity matrices (e.g., selectivity ratio over SGLT1/`SLC5A1`) were not quantified in the retrieved database subset.

---

### 9. Potential Mismatches
* **Physiological Localization vs. Primary Pathology:** `SLC5A2` is expressed primarily in the kidney rather than in the primary sites of Type 2 Diabetes pathophysiology (pancreatic beta-cells, liver, or adipose tissue). 
* **Mismatch Context:** This represents an *advantageous physiological divergence*: lowering blood glucose via renal clearance bypassed insulin-resistance pathways and avoids direct pancreatic stimulation, minimizing hypoglycemia risk.

---

### 10. Integrated Assessment

| Evidence Category | Status / Findings |
| :--- | :--- |
| **Direct Target Evidence** | Direct drug-target interaction confirmed (`empagliflozin` $\rightarrow$ `SLC5A2`). |
| **Genetic Phenocopy** | `SLC5A2` loss-of-function variants in human genetics (Familial Renal Glucosuria) support mechanism safety and efficacy. |
| **Database Association** | Strong Open Targets scoring for T2D (`0.6366`) and related cardiorenal conditions (`0.62`–`0.63`). |
| **Tissue Alignment** | Kidney-specific protein expression aligns with renal glucose reabsorption physiology. |
| **Safety Signals** | FAERS adverse event reports reflect real-world polypharmacy; requires conservative interpretation. |

**Overall Conclusion:**
The retrieved evidence strongly supports the biological mechanism and clinical validity of targeting `SLC5A2` with empagliflozin for Type 2 Diabetes Mellitus. The mechanism operates through an extra-pancreatic, renal-clearance pathway that is supported by human genetic knockouts (Familial Renal Glucosuria) and robust direct database associations.
