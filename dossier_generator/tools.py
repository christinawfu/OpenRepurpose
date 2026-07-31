import requests

def get_target_summary(target):
    """
    Returns a simple placeholder summary for a target gene.
    """

    return {
        "target": target,
        "status": "Placeholder",
        "message": f"{target} lookup has not been implemented yet."
    }

def get_faers_events(drug_name):
    """
    Retrieves a few FAERS reports mentioning a drug.
    """

    url = (
        "https://api.fda.gov/drug/event.json"
        f"?search=patient.drug.medicinalproduct:{drug_name}"
        "&limit=3"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return {
            "status": "error",
            "message": "Unable to retrieve FAERS data."
        }

    return response.json()