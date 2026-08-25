"""
ChEMBL API wrapper.

Searches the ChEMBL database for drug/molecule information.
"""

from shared.api_client import get_json
from .base import success_result, error_result


BASE_URL = "https://www.ebi.ac.uk/chembl/api/data"


def get_chembl_drug_info(drug_name: str) -> dict:
    """
    Search ChEMBL for a drug or molecule.

    Parameters
    ----------
    drug_name:
        Drug or molecule name, e.g. evolocumab.

    Returns
    -------
    dict
        Standardized OpenRepurpose wrapper response.
    """

    try:

        # --------------------------------------------------
        # Step 1: Build ChEMBL request
        # --------------------------------------------------

        url = f"{BASE_URL}/molecule/search.json"

        params = {
            "q": drug_name,
        }

        # --------------------------------------------------
        # Step 2: Query ChEMBL
        # --------------------------------------------------

        result = get_json(
            url,
            params=params,
        )

        # --------------------------------------------------
        # Step 3: Extract results
        # --------------------------------------------------

        molecules = result.get(
            "molecules",
            [],
        )

        # --------------------------------------------------
        # Step 4: Return standardized response
        # --------------------------------------------------

        return success_result(
            source="ChEMBL",
            data={
                "query": drug_name,
                "count": len(molecules),
                "results": molecules,
            },
        )

    except Exception as exc:

        return error_result(
            source="ChEMBL",
            error=str(exc),
        )