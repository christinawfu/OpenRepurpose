"""
OpenRepurpose dossier generator.

Collects evidence from multiple biomedical databases
and generates a unified evidence dossier.
"""

import argparse
import json
from dossier_generator.formatter import format_evidence_card
from pathlib import Path
from dossier_generator.gemini_agent import run_agent

from shared.database_wrappers import (
    get_ensembl_id,
    get_target_disease_associations,
    get_gtex_expression,
    get_hpa_protein,
    get_clinvar_variants,
    get_chembl_drug_info,
    get_faers_events,
    normalize_disease_name,
    get_disgenet_associations,
    get_omim_disease_genes,
)


def collect_evidence(
    target: str,
    drug: str,
    disease: str,
):
    """
    Collect evidence from all available database wrappers.
    """

    print("\nCollecting evidence...\n")

    evidence = {
        "target": target,
        "drug": drug,
        "disease": disease,
        "sources": {},
    }

    print("\nRunning Gemini evidence synthesis...\n")

    gemini_summary = run_agent(
        target,
        drug,
        disease,
    )

    evidence["gemini_summary"] = gemini_summary

    # --------------------------------------------------
    # 1. Ensembl gene lookup
    # --------------------------------------------------

    print("1/9 Ensembl gene lookup...")

    ensembl = get_ensembl_id(target)

    evidence["sources"]["ensembl"] = ensembl


    # --------------------------------------------------
    # 2. Open Targets
    # --------------------------------------------------

    print("2/9 Open Targets...")

    opentargets = get_target_disease_associations(
        target
    )

    evidence["sources"]["opentargets"] = opentargets


    # --------------------------------------------------
    # 3. GTEx
    # --------------------------------------------------

    print("3/9 GTEx...")

    gtex = get_gtex_expression(target)

    evidence["sources"]["gtex"] = gtex


    # --------------------------------------------------
    # 4. Human Protein Atlas
    # --------------------------------------------------

    print("4/9 Human Protein Atlas...")

    hpa = get_hpa_protein(target)

    evidence["sources"]["hpa"] = hpa


    # --------------------------------------------------
    # 5. ClinVar
    # --------------------------------------------------

    print("5/9 ClinVar...")

    clinvar = get_clinvar_variants(target)

    evidence["sources"]["clinvar"] = clinvar


    # --------------------------------------------------
    # 6. ChEMBL
    # --------------------------------------------------

    print("6/9 ChEMBL...")

    chembl = get_chembl_drug_info(drug)

    evidence["sources"]["chembl"] = chembl


    # --------------------------------------------------
    # 7. openFDA
    # --------------------------------------------------

    print("7/9 openFDA...")

    faers = get_faers_events(drug)

    evidence["sources"]["faers"] = faers


    # --------------------------------------------------
    # 8. Disease ontology
    # --------------------------------------------------

    print("8/9 Disease ontology...")

    ontology = normalize_disease_name(disease)

    evidence["sources"]["ontology"] = ontology


    # --------------------------------------------------
    # 9. Additional disease genetics
    # --------------------------------------------------

    print("9/9 Disease genetics...")

    disgenet = get_disgenet_associations(target)
    omim = get_omim_disease_genes(target)

    evidence["sources"]["disgenet"] = disgenet
    evidence["sources"]["omim"] = omim


    return evidence


def save_json(evidence, output_path):
    """
    Save unified evidence as JSON.
    """

    with open(
        output_path,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            evidence,
            file,
            indent=2,
        )

def summarize_sources(evidence):
    """
    Create a simple success/error summary for all sources.
    """

    summary = {}

    for source, result in evidence["sources"].items():

        summary[source] = result.get(
            "status",
            "unknown",
        )

    return summary

def main():

    parser = argparse.ArgumentParser(
        description="OpenRepurpose evidence dossier generator"
    )

    parser.add_argument(
        "--target",
        required=True,
        help="Target gene symbol",
    )

    parser.add_argument(
        "--drug",
        required=True,
        help="Drug name",
    )

    parser.add_argument(
        "--disease",
        required=True,
        help="Disease name",
    )

    args = parser.parse_args()

    evidence = collect_evidence(
        target=args.target,
        drug=args.drug,
        disease=args.disease,
    )

    source_summary = summarize_sources(
        evidence
    )

    print("\nSource summary:")

    for source, status in source_summary.items():
        print(
            f"  {source}: {status}"
        )

    output_directory = Path(
        "dossier_generator/cards"
    )

    output_directory.mkdir(
        parents=True,
        exist_ok=True,
    )


    output_path = (
        output_directory
        / f"{args.target}_{args.drug}_evidence.json"
    )


    save_json(
        evidence,
        output_path,
    )

    markdown = format_evidence_card(
        evidence
    )

    markdown_path = (
        output_directory
        / f"{args.target}_{args.drug}_evidence_card.md"
    )

    with open(
        markdown_path,
        "w",
        encoding="utf-8",
    ) as file:
        file.write(markdown)

    print("\nEvidence collection complete.")

    print(
        f"JSON saved to: {output_path}"
    )

    print(
        f"Markdown saved to: {markdown_path}"
    )


if __name__ == "__main__":
    main()