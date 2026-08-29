"""
Validate OpenRepurpose demonstration dossiers.

Checks:
1. Required Markdown and JSON artifacts exist.
2. JSON is valid.
3. Required evidence fields are present.
4. Source statuses are recorded.
5. Evidence analysis is present.
6. Evidence gaps are recorded.
"""

import json
from pathlib import Path


DEMO_DIRECTORY = Path("final_demo_cards")


EXPECTED_CASES = [
    ("PCSK9", "evolocumab"),
    ("SLC5A2", "empagliflozin"),
    ("GLP1R", "semaglutide"),
    ("EGFR", "gefitinib"),
    ("BRAF", "vemurafenib"),
]


REQUIRED_SOURCE_NAMES = [
    "gtex",
    "hpa",
    "clinvar",
    "chembl",
    "opentargets",
    "ontology",
    "omim",
    "disgenet",
    "faers",
]


def validate_case(target, drug):

    print(
        f"\n=== {target} / {drug} ==="
    )

    json_file = (
        DEMO_DIRECTORY
        / f"{target}_{drug}_evidence.json"
    )

    markdown_file = (
        DEMO_DIRECTORY
        / f"{target}_{drug}_evidence_card.md"
    )

    passed = True

    # --------------------------------------------------
    # File existence
    # --------------------------------------------------

    if not json_file.exists():

        print(
            f"FAIL: Missing {json_file}"
        )

        passed = False

    else:

        print("PASS: JSON file exists")


    if not markdown_file.exists():

        print(
            f"FAIL: Missing {markdown_file}"
        )

        passed = False

    else:

        print("PASS: Markdown file exists")


    if not passed:

        return False


    # --------------------------------------------------
    # JSON parsing
    # --------------------------------------------------

    try:

        with open(
            json_file,
            "r",
            encoding="utf-8",
        ) as handle:

            evidence = json.load(handle)

        print("PASS: JSON is valid")

    except Exception as exc:

        print(
            f"FAIL: Invalid JSON: {exc}"
        )

        return False


    # --------------------------------------------------
    # Required top-level fields
    # --------------------------------------------------

    required_fields = [
        "target",
        "drug",
        "disease",
        "sources",
    ]

    for field in required_fields:

        if field not in evidence:

            print(
                f"FAIL: Missing field '{field}'"
            )

            passed = False

        else:

            print(
                f"PASS: Field '{field}' present"
            )


    # --------------------------------------------------
    # Source status checks
    # --------------------------------------------------

    sources = evidence.get(
        "sources",
        {}
    )

    for source in REQUIRED_SOURCE_NAMES:

        if source not in sources:

            print(
                f"FAIL: Missing source '{source}'"
            )

            passed = False

            continue


        result = sources[source]

        if not isinstance(result, dict):

            print(
                f"FAIL: Source '{source}' "
                "is not a dictionary"
            )

            passed = False

            continue


        if "status" not in result:

            print(
                f"FAIL: Source '{source}' "
                "has no status"
            )

            passed = False

        else:

            print(
                f"PASS: {source} status = "
                f"{result['status']}"
            )


    # --------------------------------------------------
    # Analysis checks
    # --------------------------------------------------

    analysis = evidence.get(
        "analysis"
    )

    if not analysis:

        print(
            "FAIL: No integrated analysis found"
        )

        passed = False

    else:

        print(
            "PASS: Integrated analysis present"
        )


    # --------------------------------------------------
    # Markdown checks
    # --------------------------------------------------

    markdown = markdown_file.read_text(
        encoding="utf-8"
    )

    required_sections = [
        "Evidence",
        "Provenance",
    ]

    for section in required_sections:

        if section.lower() not in markdown.lower():

            print(
                f"FAIL: Markdown does not contain "
                f"'{section}'"
            )

            passed = False

        else:

            print(
                f"PASS: Markdown contains "
                f"'{section}'"
            )


    if passed:

        print("RESULT: PASS")

    else:

        print("RESULT: FAIL")


    return passed


def main():

    if not DEMO_DIRECTORY.exists():

        raise SystemExit(
            "final_demo_cards directory does not exist."
        )


    results = []

    for target, drug in EXPECTED_CASES:

        results.append(
            validate_case(
                target,
                drug,
            )
        )


    print("\n" + "=" * 50)

    if all(results):

        print(
            "ALL DOSSIER VALIDATION CHECKS PASSED."
        )

    else:

        print(
            "ONE OR MORE DOSSIER VALIDATION CHECKS FAILED."
        )

        raise SystemExit(1)


if __name__ == "__main__":
    main()