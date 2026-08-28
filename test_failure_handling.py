from dossier_generator.evidence_analysis import (
    analyze_evidence,
)


def main():

    evidence = {
        "target": "TEST",
        "drug": "TEST_DRUG",
        "disease": "TEST_DISEASE",

        "sources": {

            "gtex": {
                "status": "error",
                "source": "GTEx",
                "data": None,
                "error": "Simulated API failure.",
            },

            "hpa": {
                "status": "error",
                "source": "Human Protein Atlas",
                "data": None,
                "error": "Simulated API failure.",
            },

            "clinvar": {
                "status": "success",
                "source": "ClinVar",
                "data": {
                    "count": 5,
                },
                "error": None,
            },

        },
    }

    result = analyze_evidence(
        evidence
    )

    print(
        "Analysis completed successfully."
    )

    print(
        result
    )


if __name__ == "__main__":
    main()