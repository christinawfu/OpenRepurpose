"""
DisGeNET disease-gene association wrapper.
"""

from urllib.parse import quote

from shared.api_client import get_json
from shared.config import DISGENET_API_KEY
from .base import success, error


BASE_URL = "https://api.disgenet.com/api/v1"


def get_disgenet_associations(
    gene_or_disease: str,
    limit: int = 5,
):
    """
    Retrieve DisGeNET gene-disease associations.

    Parameters
    ----------
    gene_or_disease : str
        Gene symbol or disease identifier.

    limit : int
        Maximum number of results.

    Returns
    -------
    dict
        Standardized wrapper response.
    """

    if not DISGENET_API_KEY:
        return error(
            "DisGeNET",
            (
                "DISGENET_API_KEY is not configured. "
                "Add it to your .env file."
            ),
        )

    encoded_query = quote(gene_or_disease)

    url = (
        f"{BASE_URL}/gda/gene/{encoded_query}"
        f"?limit={limit}"
    )

    # DisGeNET requires authentication.
    # get_json() currently handles GET requests without headers,
    # so this wrapper will be updated to use the authenticated
    # request helper once the shared client supports headers.

    return error(
        "DisGeNET",
        (
            "DisGeNET authentication requires an API request "
            "with the configured API key. Authentication support "
            "will be added to the shared API client."
        ),
    )