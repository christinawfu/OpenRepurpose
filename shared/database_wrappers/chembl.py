"""
ChEMBL API wrapper.
"""

from shared.api_client import get_json
from .base import success, error


BASE_URL = "https://www.ebi.ac.uk/chembl/api/data"


def get_chembl_drug_info(drug_name: str):
    """
    Search ChEMBL for a drug or molecule.

    Parameters
    ----------
    drug_name : str
        Drug or molecule name.

    Returns
    -------
    dict
        Standardized wrapper response.
    """

    url = (
        f"{BASE_URL}/molecule/search.json"
        f"?q={drug_name}"
    )

    result = get_json(url)

    if result["status"] == "error":
        return error("ChEMBL", result["error"])

    return success(
        "ChEMBL",
        {
            "query": drug_name,
            "results": result["data"],
        },
    )