"""
DisGeNET wrapper.

Retrieves disease-gene associations from DisGeNET.

DisGeNET is treated as an optional evidence source because
API authentication may not be available in all environments.
"""

from shared.config import DISGENET_API_KEY
from shared.api_client import get_json
from .base import success_result, error_result


BASE_URL = "https://api.disgenet.com/api/v1"


def get_disgenet_associations(
    gene_or_disease: str,
    limit: int = 5,
) -> dict:
    """
    Retrieve disease-gene associations from DisGeNET.

    Returns a standardized OpenRepurpose response.
    """

    if not DISGENET_API_KEY:
        return error_result(
            source="DisGeNET",
            error=(
                "DISGENET_API_KEY is not configured. "
                "DisGeNET is unavailable for this run."
            ),
        )

    try:
        url = f"{BASE_URL}/gda/gene/{gene_or_disease}"

        params = {
            "limit": limit,
        }

        headers = {
            "Authorization": f"Bearer {DISGENET_API_KEY}",
        }

        result = get_json(
            url,
            params=params,
            headers=headers,
        )

        associations = result.get(
            "payload",
            result.get("data", []),
        )

        return success_result(
            source="DisGeNET",
            data={
                "query": gene_or_disease,
                "associations": associations,
                "count": (
                    len(associations)
                    if isinstance(associations, list)
                    else None
                ),
            },
        )

    except Exception as exc:
        return error_result(
            source="DisGeNET",
            error=str(exc),
        )