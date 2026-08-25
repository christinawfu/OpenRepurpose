"""
openFDA FAERS wrapper.

Queries the FDA Adverse Event Reporting System through
the public openFDA API.
"""

from shared.api_client import get_json
from .base import success_result, error_result


BASE_URL = "https://api.fda.gov/drug/event.json"


def get_faers_events(
    drug_name: str,
    top_n: int = 10,
) -> dict:
    """
    Retrieve common adverse-event reports for a drug.

    Parameters
    ----------
    drug_name:
        Drug name, e.g. evolocumab.

    top_n:
        Number of adverse-event terms to return.

    Returns
    -------
    dict
        Standardized OpenRepurpose response.
    """

    try:

        # --------------------------------------------------
        # Step 1: Query openFDA
        # --------------------------------------------------

        params = {
            "search": f'patient.drug.medicinalproduct:"{drug_name}"',
            "count": "patient.reaction.reactionmeddrapt.exact",
            "limit": top_n,
        }

        result = get_json(
            BASE_URL,
            params=params,
        )

        # --------------------------------------------------
        # Step 2: Extract results
        # --------------------------------------------------

        events = result.get(
            "results",
            [],
        )

        # --------------------------------------------------
        # Step 3: Standardized response
        # --------------------------------------------------

        return success_result(
            source="openFDA FAERS",
            data={
                "drug": drug_name,
                "events": events,
                "count": len(events),
            },
        )

    except Exception as exc:

        return error_result(
            source="openFDA FAERS",
            error=str(exc),
        )