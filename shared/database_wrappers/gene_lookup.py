"""
Gene symbol → Ensembl ID lookup using the Ensembl REST API.
"""

from shared.api_client import get_json
from .base import success, error


BASE_URL = "https://rest.ensembl.org"


def get_ensembl_id(gene_symbol: str):
    """
    Convert a human gene symbol into an Ensembl gene ID.

    Parameters
    ----------
    gene_symbol : str
        Gene symbol, e.g. PCSK9.

    Returns
    -------
    dict
        Standardized wrapper response.
    """

    url = (
        f"{BASE_URL}/xrefs/symbol/homo_sapiens/"
        f"{gene_symbol}?content-type=application/json"
    )

    try:
        result = get_json(url)

    except Exception as exc:
        return error(
            "Ensembl",
            str(exc),
        )

    if not result:
        return error(
            "Ensembl",
            f"No Ensembl ID found for {gene_symbol}",
        )

    for item in result:

        if item.get("type") == "gene":

            return success(
                "Ensembl",
                {
                    "query": gene_symbol,
                    "ensembl_id": item["id"],
                },
            )

    return error(
        "Ensembl",
        f"No gene entry found for {gene_symbol}",
    )