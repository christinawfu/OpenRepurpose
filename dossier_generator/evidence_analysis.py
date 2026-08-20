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


def _extract_tissue_names(data):
    """
    Extract tissue names from common biomedical API response structures.

    This function is intentionally defensive because different
    database wrappers may return slightly different structures.
    """

    tissues = set()

    if not data:
        return tissues

    # Case 1: dictionary containing a results list
    if isinstance(data, dict):

        results = data.get("results", [])

        if isinstance(results, list):

            for item in results:

                if not isinstance(item, dict):
                    continue

                possible_names = [
                    item.get("tissue"),
                    item.get("tissue_name"),
                    item.get("tissueName"),
                    item.get("organ"),
                    item.get("organ_name"),
                ]

                for name in possible_names:

                    if isinstance(name, str) and name.strip():
                        tissues.add(name.strip())


        # Case 2: dictionary containing a tissues list
        tissue_list = data.get("tissues", [])

        if isinstance(tissue_list, list):

            for item in tissue_list:

                if isinstance(item, str):
                    tissues.add(item.strip())

                elif isinstance(item, dict):

                    name = (
                        item.get("name")
                        or item.get("tissue")
                        or item.get("tissue_name")
                    )

                    if name:
                        tissues.add(str(name).strip())


    # Case 3: direct list
    elif isinstance(data, list):

        for item in data:

            if isinstance(item, str):
                tissues.add(item.strip())

            elif isinstance(item, dict):

                name = (
                    item.get("tissue")
                    or item.get("tissue_name")
                    or item.get("name")
                )

                if name:
                    tissues.add(str(name).strip())

    return tissues


def compare_tissue_expression(evidence):
    """
    Compare tissues reported by GTEx and HPA.

    This compares tissue names when the wrappers expose them.
    It does not claim biological equivalence merely because
    the same tissue appears in both sources.
    """

    sources = evidence.get(
        "sources",
        {}
    )

    gtex = sources.get(
        "gtex",
        {}
    )

    hpa = sources.get(
        "hpa",
        {}
    )

    gtex_status = gtex.get(
        "status",
        "unknown"
    )

    hpa_status = hpa.get(
        "status",
        "unknown"
    )

    gtex_tissues = set()

    hpa_tissues = set()

    if gtex_status == "success":

        gtex_tissues = _extract_tissue_names(
            gtex.get("data")
        )

    if hpa_status == "success":

        hpa_tissues = _extract_tissue_names(
            hpa.get("data")
        )

    shared = sorted(
        gtex_tissues.intersection(
            hpa_tissues
        )
    )

    gtex_only = sorted(
        gtex_tissues - hpa_tissues
    )

    hpa_only = sorted(
        hpa_tissues - gtex_tissues
    )

    if shared:

        interpretation = (
            "GTEx and HPA report overlapping tissues. "
            "This provides cross-database support for "
            "tissue-level evidence, although expression "
            "agreement does not establish target efficacy."
        )

        status = "overlap_detected"

        mismatch_flag = False

    elif gtex_tissues and hpa_tissues:

        interpretation = (
            "GTEx and HPA returned tissue-level information, "
            "but no directly matching tissue names were "
            "identified by the current comparison."
        )

        status = "different_tissue_sets"

        mismatch_flag = True

    elif gtex_tissues:

        interpretation = (
            "GTEx returned tissue information, but HPA "
            "did not expose comparable tissue information."
        )

        status = "gtex_only"

        mismatch_flag = True

    elif hpa_tissues:

        interpretation = (
            "HPA returned tissue information, but GTEx "
            "did not expose comparable tissue information."
        )

        status = "hpa_only"

        mismatch_flag = True

    else:

        interpretation = (
            "No directly comparable tissue names were "
            "available from the current GTEx/HPA responses."
        )

        status = "no_comparable_tissues"

        mismatch_flag = True

    return {
        "status": status,
        "mismatch_flag": mismatch_flag,
        "gtex_tissues": sorted(gtex_tissues),
        "hpa_tissues": sorted(hpa_tissues),
        "shared_tissues": shared,
        "gtex_only": gtex_only,
        "hpa_only": hpa_only,
        "interpretation": interpretation,
    }

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

    tissue_comparison = compare_tissue_expression(
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
        "tissue_comparison": tissue_comparison,
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