from pathlib import Path
import json

def save_results(target, drug, disease, results):
    output_folder = Path("dossier_generator/cards")
    output_folder.mkdir(exist_ok=True)

    json_file = output_folder / f"{target}_{drug}_summary.json"

    with open(json_file, "w") as f:
        json.dump(results, f, indent=4)

    markdown_file = output_folder / f"{target}_{drug}_evidence_card.md"

    markdown = f"""# OpenRepurpose Evidence Card

## Input

- **Target:** {target}
- **Drug:** {drug}
- **Disease:** {disease}

---

## FAERS Summary

- Status: {results["faers"]["status"]}
- Reports Retrieved: {results["faers"]["num_reports"]}

---

## Current Verdict

This evidence card currently contains only FAERS data.

Additional evidence sources (GTEx, HPA, OMIM, DisGeNET, Ontology)
will be integrated in future development.
"""

    with open(markdown_file, "w") as f:
        f.write(markdown)

    return json_file, markdown_file