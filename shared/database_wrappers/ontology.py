"""
Disease ontology normalization using EMBL-EBI Ontology Lookup Service.
"""

from urllib.parse import quote

from shared.api_client import get_json
from .base import success, error


BASE_URL = "https://www.ebi.ac.uk/ols4/api"


def normalize_disease_name(name: str):
    """
    Search OLS for a disease name and return a canonical ontology ID.

    Parameters
    ----------
    name : str
        Disease name, such as "hypercholesterolemia".

    Returns
    -------
    dict
        Standardized wrapper response.
    """

    url = (
        f"{BASE_URL}/search"
        f"?q={quote(name)}"
        f"&ontology=mondo"
        f"&rows=5"
    )

    result = get_json(url)

    if result["status"] == "error":
        return error(
            "OLS/MONDO",
            result["error"],
        )

    data = result["data"]

    docs = data.get("response", {}).get("docs", [])

    if not docs:
        return error(
            "OLS/MONDO",
            f"No MONDO disease found for '{name}'.",
        )

    first_match = docs[0]

    disease_id = (
        first_match.get("obo_id")
        or first_match.get("id")
    )

    label = (
        first_match.get("label")
        or first_match.get("title")
        or name
    )

    return success(
        "OLS/MONDO",
        {
            "query": name,
            "canonical_id": disease_id,
            "canonical_name": label,
            "results": docs[:5],
        },
    )