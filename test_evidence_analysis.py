from dossier_generator.evidence_analysis import (
    calculate_evidence_score,
    identify_evidence_gaps,
    analyze_tissue_concordance,
    compare_tissue_expression,
    analyze_genetic_evidence,
    assess_rare_disease_relevance,
    analyze_evidence,
)


example_evidence = {
    "target": "PCSK9",
    "drug": "evolocumab",
    "disease": "hypercholesterolemia",

    "sources": {

        "gtex": {
            "status": "success",
            "data": {
                "results": [
                    {"tissue_name": "Liver"},
                    {"tissue_name": "Heart"},
                ]
            }
        },

        "hpa": {
            "status": "success",
            "data": {
                "results": [
                    {"tissue_name": "Liver"},
                    {"tissue_name": "Kidney"},
                ]
            }
        },

        "clinvar": {
            "status": "success",
            "data": {
                "count": 5
            }
        },

        "chembl": {
            "status": "success",
            "data": {}
        },

        "faers": {
            "status": "success",
            "data": {}
        },

        "ontology": {
            "status": "success",
            "data": {}
        },

        "opentargets": {
            "status": "success",
            "data": {}
        },

        "omim": {
            "status": "error",
            "data": {}
        },

        "disgenet": {
            "status": "error",
            "data": {}
        },
    }
}


print("=== Evidence Score ===")

print(
    calculate_evidence_score(
        example_evidence
    )
)


print("\n=== Evidence Gaps ===")

print(
    identify_evidence_gaps(
        example_evidence
    )
)


print("\n=== Tissue Concordance ===")

print(
    analyze_tissue_concordance(
        example_evidence
    )
)


print("\n=== Tissue Comparison ===")

print(
    compare_tissue_expression(
        example_evidence
    )
)


print("\n=== Genetic Evidence ===")

print(
    analyze_genetic_evidence(
        example_evidence
    )
)


print("\n=== Rare Disease ===")

print(
    assess_rare_disease_relevance(
        example_evidence
    )
)


print("\n=== Complete Analysis ===")

print(
    analyze_evidence(
        example_evidence
    )
)