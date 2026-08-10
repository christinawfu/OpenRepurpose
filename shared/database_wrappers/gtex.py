"""
GTEx gene expression wrapper.
"""

from shared.api_client import get_json
from .base import success, error


BASE_URL = "https://gtexportal.org/api/v2"


def get_gtex_expression(gene_symbol: str):
    """
    Retrieve GTEx tissue expression information for a gene.

    Parameters
    ----------
    gene_symbol : str
        HGNC gene symbol, such as PCSK9.

    Returns
    -------
    dict
        Standardized wrapper response.
    """

    url = (
        f"{BASE_URL}/geneExpression"
        f"?gencodeId={gene_symbol}"
    )

    result = get_json(url)

    if result["status"] == "error":
        return error("GTEx", result["error"])

    return success(
        "GTEx",
        {
            "query": gene_symbol,
            "results": result["data"],
        },
    )