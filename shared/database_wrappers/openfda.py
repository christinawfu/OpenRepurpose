"""
openFDA FAERS wrapper
"""

from shared.database_wrappers.base import success, error
from shared.api_client import get_json

BASE_URL = "https://api.fda.gov/drug/event.json"


def get_faers_events(drug_name, limit=3):
    """
    Retrieve a small summary of FAERS reports for a drug.

    Parameters
    ----------
    drug_name : str
        Drug to search.

    limit : int
        Maximum reports.

    Returns
    -------
    dict
    """

    url = (
        f"{BASE_URL}"
        f"?search=patient.drug.medicinalproduct:{drug_name}"
        f"&limit={limit}"
    )

    result = get_json(url)

    if result["status"] == "error":
        return error(
            "openFDA",
            result["error"],
            )

    data = result["data"]

    return success(
        "openFDA",
        {
        "drug": drug_name,
        "num_reports": len(data.get("results", [])),
        "raw_results": data.get("results", []),
        },
        )