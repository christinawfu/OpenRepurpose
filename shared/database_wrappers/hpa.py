"""
Human Protein Atlas wrapper.
"""

from shared.api_client import get_json
from .base import success, error


BASE_URL = "https://www.proteinatlas.org"


def get_hpa_protein(gene_symbol: str):
    """
    Retrieve Human Protein Atlas information for a gene.

    Parameters
    ----------
    gene_symbol : str
        HGNC gene symbol.

    Returns
    -------
    dict
        Standardized wrapper response.
    """

    url = (
        f"{BASE_URL}/api/search_download.php"
        f"?search={gene_symbol}"
        f"&format=json"
    )

    result = get_json(url)

    if result["status"] == "error":
        return error(
            "Human Protein Atlas",
            result["error"],
        )

    return success(
        "Human Protein Atlas",
        {
            "query": gene_symbol,
            "results": result["data"],
        },
    )