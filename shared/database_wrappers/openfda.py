"""
openFDA FAERS wrapper
"""

import requests


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

    try:

        response = requests.get(url, timeout=15)

        response.raise_for_status()

        data = response.json()

        return {
            "status": "success",
            "drug": drug_name,
            "num_reports": len(data.get("results", [])),
            "raw_results": data.get("results", [])
        }

    except requests.exceptions.RequestException as error:

        return {
            "status": "error",
            "drug": drug_name,
            "message": str(error),
            "num_reports": 0,
            "raw_results": []
        }