"""
Evidence dossier Markdown formatter.
"""


def format_evidence_card(evidence):
    """
    Convert unified evidence into a Markdown evidence card.
    """

    target = evidence["target"]
    drug = evidence["drug"]
    disease = evidence["disease"]

    sources = evidence["sources"]

    markdown = []

    markdown.append(
        f"# OpenRepurpose Evidence Card"
    )

    markdown.append("")

    markdown.append(
        f"**Target:** {target}"
    )

    markdown.append(
        f"**Drug:** {drug}"
    )

    markdown.append(
        f"**Disease:** {disease}"
    )

    markdown.append("")


    # --------------------------------------------------
    # Source status
    # --------------------------------------------------

    markdown.append(
        "## Evidence Sources"
    )

    markdown.append("")

    markdown.append(
        "| Source | Status |"
    )

    markdown.append(
        "|---|---|"
    )

    for source, result in sources.items():

        status = result.get(
            "status",
            "unknown",
        )

        markdown.append(
            f"| {source} | {status} |"
        )

    markdown.append("")


    # --------------------------------------------------
    # Open Targets
    # --------------------------------------------------

    opentargets = sources.get(
        "opentargets"
    )

    if (
        opentargets
        and opentargets.get("status") == "success"
    ):

        results = (
            opentargets["data"]
            .get("results", [])
        )

        markdown.append(
            "## Open Targets Disease Associations"
        )

        markdown.append("")

        markdown.append(
            "| Disease | Score |"
        )

        markdown.append(
            "|---|---:|"
        )

        for association in results:

            disease_name = association.get(
                "disease_name",
                "Unknown",
            )

            score = association.get(
                "association_score",
                0,
            )

            markdown.append(
                f"| {disease_name} | {score:.3f} |"
            )

        markdown.append("")


    # --------------------------------------------------
    # GTEx
    # --------------------------------------------------

    gtex = sources.get("gtex")

    if gtex and gtex.get("status") == "success":

        results = (
            gtex["data"]
            .get("results", [])
        )

        markdown.append(
            "## GTEx Tissue Expression"
        )

        markdown.append("")

        markdown.append(
            f"GENCODE ID: "
            f"{gtex['data'].get('gencode_id', 'Unknown')}"
        )

        markdown.append("")

        markdown.append(
            f"Expression records returned: "
            f"{len(results)}"
        )

        markdown.append("")


    # --------------------------------------------------
    # HPA
    # --------------------------------------------------

    hpa = sources.get("hpa")

    if hpa and hpa.get("status") == "success":

        results = (
            hpa["data"]
            .get("results", [])
        )

        markdown.append(
            "## Human Protein Atlas"
        )

        markdown.append("")

        markdown.append(
            f"Protein records returned: "
            f"{len(results)}"
        )

        markdown.append("")


    # --------------------------------------------------
    # ClinVar
    # --------------------------------------------------

    clinvar = sources.get("clinvar")

    if (
        clinvar
        and clinvar.get("status") == "success"
    ):

        data = clinvar["data"]

        markdown.append(
            "## ClinVar"
        )

        markdown.append("")

        markdown.append(
            f"ClinVar records identified: "
            f"{data.get('count', 0)}"
        )

        markdown.append("")


    # --------------------------------------------------
    # ChEMBL
    # --------------------------------------------------

    chembl = sources.get("chembl")

    if (
        chembl
        and chembl.get("status") == "success"
    ):

        markdown.append(
            "## ChEMBL"
        )

        markdown.append("")

        markdown.append(
            "Drug/molecule information retrieved "
            "from ChEMBL."
        )

        markdown.append("")


    # --------------------------------------------------
    # openFDA
    # --------------------------------------------------

    faers = sources.get("faers")

    if (
        faers
        and faers.get("status") == "success"
    ):

        markdown.append(
            "## FAERS Safety Signals"
        )

        markdown.append("")

        data = faers.get(
            "data",
            {},
        )

        markdown.append(
            f"Drug: {data.get('drug', drug)}"
        )

        markdown.append("")


    # --------------------------------------------------
    # Disease ontology
    # --------------------------------------------------

    ontology = sources.get(
        "ontology"
    )

    if (
        ontology
        and ontology.get("status") == "success"
    ):

        data = ontology["data"]

        markdown.append(
            "## Disease Ontology"
        )

        markdown.append("")

        markdown.append(
            f"Canonical disease: "
            f"{data.get('canonical_name', disease)}"
        )

        markdown.append("")

        markdown.append(
            f"Canonical ID: "
            f"{data.get('canonical_id', 'Unknown')}"
        )

        markdown.append("")


    return "\n".join(markdown)