"""
Ontology normalization wrapper.

Uses the EMBL-EBI Ontology Lookup Service (OLS)
to identify canonical disease concepts.
"""

from shared.api_client import get_json
from .base import success_result, error_result


BASE_URL = "https://www.ebi.ac.uk/ols4/api/search"


def normalize_disease_name(name: str) -> dict:
    """
    Search OLS for a canonical ontology concept.

    Parameters
    ----------
    name:
        Disease or phenotype name.

    Returns
    -------
    dict
        Standardized OpenRepurpose response.
    """

    try:

        params = {
            "q": name,
            "rows": 10,
        }

        result = get_json(
            BASE_URL,
            params=params,
        )

        response = result.get(
            "response",
            {},
        )

        docs = response.get(
            "docs",
            [],
        )

        if not docs:
            return success_result(
                source="OLS",
                data={
                    "query": name,
                    "canonical_name": None,
                    "ontology_id": None,
                    "matches": [],
                },
            )

        best = docs[0]

        ontology_id = (
            best.get("obo_id")
            or best.get("short_form")
            or best.get("id")
        )

        canonical_name = (
            best.get("label")
            or best.get("prefLabel")
            or best.get("title")
        )

        return success_result(
            source="OLS",
            data={
                "query": name,
                "canonical_name": canonical_name,
                "ontology_id": ontology_id,
                "matches": docs,
            },
        )

    except Exception as exc:

        return error_result(
            source="OLS",
            error=str(exc),
        )