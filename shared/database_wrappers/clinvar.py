"""
NCBI ClinVar wrapper.
"""

from shared.api_client import get_json
from .base import success, error


BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def get_clinvar_variants(gene_symbol: str, limit: int = 5):
    """
    Search ClinVar for variants associated with a gene.

    Parameters
    ----------
    gene_symbol : str
        Gene symbol.

    limit : int
        Maximum number of records to retrieve.

    Returns
    -------
    dict
        Standardized wrapper response.
    """

    search_url = (
        f"{BASE_URL}/esearch.fcgi"
        f"?db=clinvar"
        f"&term={gene_symbol}[gene]"
        f"&retmax={limit}"
        f"&retmode=json"
    )

    result = get_json(search_url)

    if result["status"] == "error":
        return error("ClinVar", result["error"])

    search_data = result["data"]

    ids = search_data.get(
        "esearchresult",
        {}
    ).get(
        "idlist",
        []
    )

    return success(
        "ClinVar",
        {
            "query": gene_symbol,
            "variant_ids": ids,
            "count": len(ids),
        },
    )