"""
Integration tests for OpenRepurpose database wrappers.
"""

import json

from shared.database_wrappers import (
    get_gtex_expression,
    get_hpa_protein,
    get_clinvar_variants,
    get_chembl_drug_info,
)


def print_result(
    name: str,
    result: dict,
):
    """
    Print a standardized wrapper result.
    """

    print(
        f"\n=== {name} ==="
    )

    print(
        f"Status: {result.get('status')}"
    )

    print(
        f"Source: {result.get('source')}"
    )

    if result.get("status") == "success":

        print("Result: SUCCESS")

    else:

        print(
            "Error:",
            result.get("error")
        )


def main():

    print_result(
        "GTEx",
        get_gtex_expression("PCSK9"),
    )

    print_result(
        "Human Protein Atlas",
        get_hpa_protein("PCSK9"),
    )

    print_result(
        "ClinVar",
        get_clinvar_variants("PCSK9"),
    )

    print_result(
        "ChEMBL",
        get_chembl_drug_info("evolocumab"),
    )


if __name__ == "__main__":
    main()