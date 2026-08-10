"""
Human Protein Atlas wrapper.
"""

from urllib.parse import quote

from shared.api_client import get_json
from .base import success, error


BASE_URL = "https://www.proteinatlas.org/api/search_download.php"


def get_hpa_protein(gene_symbol: str):
    """
    Retrieve Human Protein Atlas protein information.

    Parameters
    ----------
    gene_symbol : str
        HGNC gene symbol.

    Returns
    -------
    dict
        Standardized wrapper response.
    """

    columns = (
        "g,gs,eg,gd,pc,upbp,up_mf,di,pe,evih,eviu"
    )

    url = (
        f"{BASE_URL}"
        f"?search={quote(gene_symbol)}"
        f"&format=json"
        f"&columns={columns}"
        f"&compress=no"
    )

    result = get_json(url)

    if result["status"] == "error":
        return error(
            "Human Protein Atlas",
            result["error"],
        )

    data = result["data"]

    return success(
        "Human Protein Atlas",
        {
            "query": gene_symbol,
            "results": data,
        },
    )