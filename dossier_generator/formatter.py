from pathlib import Path
import json

def save_results(target, drug, disease, results):
    output_folder = Path("dossier_generator/cards")
    output_folder.mkdir(exist_ok=True)

    # Save JSON
    json_file = output_folder / f"{target}_{drug}_summary.json"

    with open(json_file, "w") as f:
        json.dump(results, f, indent=4)

    # Build Markdown
    markdown_file = output_folder / f"{target}_{drug}_evidence_card.md"

    markdown = f"""# OpenRepurpose Evidence Card

## Input

- **Target:** {target}
- **Drug:** {drug}
- **Disease:** {disease}

---

## FAERS Summary

- Status: {results["faers"]["status"]}
- Reports Retrieved: {results["faers"]["data"]["num_reports"]}

---

## Current Verdict

This evidence card currently contains only FAERS data.

Additional evidence sources (GTEx, HPA, OMIM, DisGeNET, Ontology)
will be integrated in future development.

---

## Open Targets Associations

| Disease | Association Score |
|---------|-------------------|
"""

    for association in results["opentargets"]["data"]["results"]:
        markdown += (
            f"| {association['disease_name']} "
            f"| {association['association_score']:.3f} |\n"
    )

    # Write Markdown file
    with open(markdown_file, "w") as f:
        f.write(markdown)

    return json_file, markdown_file