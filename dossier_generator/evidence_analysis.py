"""
Scientific evidence analysis utilities for OpenRepurpose.
"""


def get_source_status(evidence, source):
    """
    Return the status of a database source.
    """

    result = evidence.get("sources", {}).get(
        source
    )

    if not result:
        return "missing"

    return result.get(
        "status",
        "unknown"
    )


def count_successful_sources(evidence):
    """
    Count how many evidence sources successfully returned data.
    """

    sources = evidence.get(
        "sources",
        {}
    )

    successful = 0

    for result in sources.values():

        if result.get("status") == "success":
            successful += 1

    return successful


def count_failed_sources(evidence):
    """
    Count unavailable or failed evidence sources.
    """

    sources = evidence.get(
        "sources",
        {}
    )

    failed = 0

    for result in sources.values():

        if result.get("status") != "success":
            failed += 1

    return failed


def identify_evidence_gaps(evidence):
    """
    Identify evidence categories that are unavailable.
    """

    gaps = []

    source_categories = {
        "gtex": "RNA tissue expression",
        "hpa": "protein tissue expression",
        "opentargets": "target-disease association",
        "clinvar": "clinical genetic variation",
        "chembl": "drug information",
        "faers": "post-market safety",
        "ontology": "disease ontology",
        "disgenet": "disease-gene aggregation",
        "omim": "Mendelian disease genetics",
    }

    for source, description in source_categories.items():

        status = get_source_status(
            evidence,
            source
        )

        if status != "success":

            gaps.append({
                "source": source,
                "category": description,
                "status": status,
            })

    return gaps


def analyze_tissue_concordance(evidence):
    """
    Analyze whether GTEx and HPA both provide tissue evidence.
    """

    gtex_status = get_source_status(
        evidence,
        "gtex"
    )

    hpa_status = get_source_status(
        evidence,
        "hpa"
    )

    if (
        gtex_status == "success"
        and hpa_status == "success"
    ):

        return {
            "status": "concordant_available",
            "flag": False,
            "message": (
                "Both RNA-level and protein-level "
                "tissue evidence are available."
            ),
        }

    if (
        gtex_status == "success"
        and hpa_status != "success"
    ):

        return {
            "status": "partial",
            "flag": True,
            "message": (
                "RNA-level tissue evidence is available, "
                "but protein-level evidence is unavailable."
            ),
        }

    if (
        gtex_status != "success"
        and hpa_status == "success"
    ):

        return {
            "status": "partial",
            "flag": True,
            "message": (
                "Protein-level tissue evidence is available, "
                "but RNA-level evidence is unavailable."
            ),
        }

    return {
        "status": "unavailable",
        "flag": True,
        "message": (
            "Neither GTEx nor Human Protein Atlas "
            "returned usable tissue evidence."
        ),
    }


def analyze_genetic_evidence(evidence):
    """
    Analyze availability of genetic evidence.
    """

    clinvar_status = get_source_status(
        evidence,
        "clinvar"
    )

    omim_status = get_source_status(
        evidence,
        "omim"
    )

    disgenet_status = get_source_status(
        evidence,
        "disgenet"
    )

    available = []

    if clinvar_status == "success":
        available.append("ClinVar")

    if omim_status == "success":
        available.append("OMIM")

    if disgenet_status == "success":
        available.append("DisGeNET")

    if available:

        return {
            "status": "available",
            "sources": available,
            "message": (
                "Genetic evidence is available from: "
                + ", ".join(available)
            ),
        }

    return {
        "status": "limited",
        "sources": [],
        "message": (
            "No dedicated disease-genetics source "
            "returned usable evidence."
        ),
    }


def assess_rare_disease_relevance(evidence):
    """
    Assess whether rare-disease evidence is available.

    This does not determine whether a disease is rare.
    It identifies whether dedicated Mendelian or
    disease-gene evidence sources returned data.
    """

    omim = get_source_status(
        evidence,
        "omim"
    )

    disgenet = get_source_status(
        evidence,
        "disgenet"
    )

    clinvar = get_source_status(
        evidence,
        "clinvar"
    )

    sources = []

    if omim == "success":
        sources.append("OMIM")

    if disgenet == "success":
        sources.append("DisGeNET")

    if clinvar == "success":
        sources.append("ClinVar")

    if sources:

        return {
            "status": "evidence_available",
            "sources": sources,
            "message": (
                "Disease/genetic evidence relevant to "
                "rare-disease assessment is available."
            ),
        }

    return {
        "status": "insufficient_data",
        "sources": [],
        "message": (
            "Insufficient dedicated rare-disease evidence "
            "was retrieved."
        ),
    }
    

def calculate_evidence_score(evidence):
    """
    Calculate a simple reproducible evidence availability score.

    This is NOT a clinical validity score.
    It measures breadth of successfully retrieved evidence.
    """

    sources = evidence.get(
        "sources",
        {}
    )

    total_sources = len(sources)

    if total_sources == 0:
        return {
            "score": 0,
            "maximum": 0,
            "percentage": 0,
        }

    successful = count_successful_sources(
        evidence
    )

    percentage = round(
        (successful / total_sources) * 100,
        1
    )

    return {
        "score": successful,
        "maximum": total_sources,
        "percentage": percentage,
    }


def generate_integrated_verdict(evidence):
    """
    Generate a conservative evidence-availability verdict.
    """

    score = calculate_evidence_score(
        evidence
    )

    gaps = identify_evidence_gaps(
        evidence
    )

    tissue = analyze_tissue_concordance(
        evidence
    )

    genetic = analyze_genetic_evidence(
        evidence
    )

    rare_disease = assess_rare_disease_relevance(
        evidence
    )

    if score["percentage"] >= 80:
        strength = "broad"

    elif score["percentage"] >= 60:
        strength = "moderate"

    elif score["percentage"] >= 40:
        strength = "limited"

    else:
        strength = "insufficient"

    return {
        "evidence_availability": strength,
        "score": score,
        "tissue_assessment": tissue,
        "genetic_assessment": genetic,
        "rare_disease_assessment": rare_disease,
        "evidence_gaps": gaps,
        "caution": (
            "This assessment describes evidence availability "
            "and does not establish clinical efficacy, "
            "causality, or therapeutic suitability."
        ),
    }


def analyze_evidence(evidence):
    """
    Run the complete evidence analysis pipeline.
    """

    return generate_integrated_verdict(
        evidence
    )