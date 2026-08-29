# OpenRepurpose — Evidence & Validation Module

**AI-assisted biomedical evidence dossier generator for drug repurposing and target validation**

OpenRepurpose is a Python-based CLI tool that integrates evidence from multiple public biomedical databases and uses a Gemini-powered agent to organize and synthesize that evidence into reproducible Markdown and JSON dossiers.

The project was developed as part of the **CABS ds4cabs 2026 intern cohort**.

---

## Project Overview

Drug repurposing and target validation require evidence from many different biological and clinical data sources. Relevant information is distributed across databases covering gene expression, protein expression, genetic variation, disease-gene relationships, drug information, ontology mappings, and post-market safety.

OpenRepurpose addresses this fragmentation by providing an automated evidence-collection and synthesis workflow.

A user supplies:

```text
Target + Drug + Disease
```

For example:

```bash
python3 dossier_generator/agent.py \
  --target PCSK9 \
  --drug evolocumab \
  --disease hypercholesterolemia
```

The system collects evidence from multiple biomedical APIs, performs structured evidence analysis, invokes Gemini for synthesis, and produces:

```text
Markdown evidence card
+
JSON evidence record
```

---

## Architecture

```text
                    User Query
                        │
                        ▼
              Target + Drug + Disease
                        │
                        ▼
                OpenRepurpose CLI
                        │
                        ▼
                 Evidence Agent
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
        GTEx           HPA        Open Targets
          │             │             │
          ▼             ▼             ▼
       ClinVar        ChEMBL       Ontology
          │             │             │
          └─────────────┼─────────────┘
                        │
             ┌──────────┴──────────┐
             ▼                     ▼
         OMIM /                    FAERS
        DisGeNET
             │                     │
             └──────────┬──────────┘
                        ▼
               Evidence Analysis
                        │
            ┌───────────┼───────────┐
            ▼           ▼           ▼
        Evidence      Tissue      Evidence
          Score      Comparison      Gaps
            │           │           │
            └───────────┼───────────┘
                        ▼
                 Gemini Synthesis
                        │
                 ┌──────┴──────┐
                 ▼             ▼
             Markdown         JSON
               Dossier       Record
```

---

## Core Capabilities

### Multi-source evidence collection

The evidence module integrates information from public biomedical databases including:

* **GTEx** — tissue-level gene expression
* **Human Protein Atlas** — protein expression
* **ClinVar** — clinically interpreted genetic variants
* **ChEMBL** — drug and bioactivity information
* **Open Targets** — target-disease evidence
* **Ontology services** — disease-name normalization
* **OMIM** — Mendelian disease-gene relationships
* **DisGeNET** — aggregated disease-gene associations
* **openFDA FAERS** — post-market adverse-event signals

Individual API failures are captured as structured evidence metadata rather than terminating the entire dossier-generation workflow.

---

## Evidence Workflow

For each target-drug-disease query, OpenRepurpose:

1. Accepts structured CLI input.
2. Queries available biomedical databases.
3. Normalizes and stores returned evidence.
4. Records API failures and unavailable sources.
5. Compares tissue evidence across databases.
6. Identifies evidence gaps.
7. Calculates a structured evidence score.
8. Evaluates genetic and disease-association evidence.
9. Passes the collected evidence to Gemini for synthesis.
10. Produces Markdown and JSON output.

---

## Example

### PCSK9 / Evolocumab / Hypercholesterolemia

```bash
python3 dossier_generator/agent.py \
  --target PCSK9 \
  --drug evolocumab \
  --disease hypercholesterolemia
```

The resulting dossier includes:

* target and drug identifiers
* tissue-expression evidence
* cross-database tissue comparison
* disease-gene evidence
* genetic evidence
* safety signals
* evidence gaps
* integrated assessment
* source/provenance information

Output:

```text
PCSK9_evolocumab_evidence_card.md
PCSK9_evolocumab_evidence.json
```

---

## Repository Structure

```text
openrepurpose/
│
├── dossier_generator/
│   ├── agent.py
│   ├── evidence_analysis.py
│   ├── formatter.py
│   ├── system_prompt.md
│   └── cards/
│
├── shared/
│   ├── api_client.py
│   ├── config.py
│   └── database_wrappers/
│       ├── base.py
│       ├── gtex.py
│       ├── hpa.py
│       ├── clinvar.py
│       ├── chembl.py
│       ├── opentargets.py
│       ├── ontology.py
│       ├── omim.py
│       ├── disgenet.py
│       └── openfda.py
│
├── test_shared_wrappers.py
├── test_evidence_analysis.py
├── test_failure_handling.py
├── test_wrapper_base.py
├── test_agent_smoke.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository and enter the project directory:

```bash
git clone <repository-url>
cd openrepurpose
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

The Gemini agent requires an API key.

Create a `.env` file in the repository root:

```text
GEMINI_API_KEY=your_api_key_here
```

Do **not** commit `.env` or API keys to GitHub.

The repository should contain a `.gitignore` entry for:

```text
.env
```

---

## Running the Dossier Generator

Basic usage:

```bash
python3 dossier_generator/agent.py \
  --target PCSK9 \
  --drug evolocumab \
  --disease hypercholesterolemia
```

Specify a custom output directory:

```bash
python3 dossier_generator/agent.py \
  --target PCSK9 \
  --drug evolocumab \
  --disease hypercholesterolemia \
  --output final_demo_cards
```

Enable verbose diagnostic output:

```bash
python3 dossier_generator/agent.py \
  --target PCSK9 \
  --drug evolocumab \
  --disease hypercholesterolemia \
  --verbose
```

---

## Testing

Run the wrapper tests:

```bash
python3 test_shared_wrappers.py
```

Run evidence-analysis tests:

```bash
python3 test_evidence_analysis.py
```

Run API failure-handling tests:

```bash
python3 test_failure_handling.py
```

Run the wrapper-base tests:

```bash
python3 test_wrapper_base.py
```

Run the end-to-end smoke test:

```bash
python3 test_agent_smoke.py
```

---

## Reproducibility

OpenRepurpose produces versionable artifacts in two formats:

### Markdown

Human-readable evidence dossier suitable for inspection, sharing, and presentation.

### JSON

Machine-readable evidence record suitable for downstream analysis or future integration with dashboards and computational workflows.

The generated dossier preserves source-level status information so that unavailable APIs are distinguishable from negative biological evidence.

---

## MVP Validation

The MVP was evaluated using five representative
target-drug-disease queries:

| Target | Drug | Example indication |
|---|---|---|
| PCSK9 | Evolocumab | Hypercholesterolemia |
| SLC5A2 | Empagliflozin | Type 2 diabetes |
| GLP1R | Semaglutide | Fatty liver |
| EGFR | Gefitinib | Non-small cell lung cancer |
| BRAF | Vemurafenib | Melanoma |

Validation checks include:

- successful generation of Markdown and JSON artifacts
- valid JSON serialization
- standardized database-source status reporting
- integrated evidence analysis
- evidence-gap reporting
- source provenance
- resilience to individual API failures
- cautious interpretation of incomplete evidence

The validation suite is implemented in:

```bash
validate_dossiers.py
```

and can be run with:

```bash
python3 validate_dossiers.py
```

The five examples are demonstration cases rather than clinical validation studies. Their purpose is to test the reproducibility and behavior of the evidence-generation workflow across different biomedical queries.

## Scientific Interpretation

OpenRepurpose is an **evidence aggregation and synthesis tool**, not a clinical decision-support system.

The presence of an association, expression pattern, genetic relationship, or safety signal does not establish:

* clinical efficacy
* causal biological mechanism
* therapeutic suitability
* clinical safety
* regulatory approval

Automated tissue comparisons should also be interpreted cautiously because different databases may use different tissue naming conventions.

Gemini-generated synthesis should be treated as an interpretation layer over retrieved evidence rather than as an independent biomedical source.

---

## Current MVP Scope

The current MVP focuses on:

* target-drug-disease queries
* multi-source biomedical evidence retrieval
* evidence normalization
* tissue-expression cross-checking
* disease-gene evidence
* genetic evidence
* post-market safety signals
* structured evidence scoring
* Gemini-assisted synthesis
* Markdown and JSON dossier generation

---

## Future Work

Potential extensions include:

* additional biomedical databases
* improved tissue-name normalization
* automated evidence citation and source URLs
* richer genetic evidence interpretation
* rare-disease resources such as Orphanet
* dependency/essentiality data from resources such as DepMap
* visualization dashboards
* longitudinal evidence tracking
* automated benchmark datasets for evidence extraction and entity linking

---

## Project Context

**Project:** OpenRepurpose — Evidence & Validation Module
**Program:** CABS ds4cabs 2026
**Paradigm:** Dossier Generator
**Technology:** Python, Gemini, REST APIs, biomedical databases

The broader cohort project uses a shared starter repository containing three computational paradigms:

1. Dossier Generator
2. Dashboard
3. Computation Engine

This module implements the dossier-generator paradigm while contributing shared API infrastructure to the cohort repository.

---

## Authors

**Christina Fu**
OpenRepurpose Evidence & Validation Module

CABS ds4cabs 2026 Intern Cohort
