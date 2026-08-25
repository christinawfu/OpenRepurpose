"""
NCBI ClinVar wrapper.

Searches ClinVar through the NCBI E-utilities API.
"""

from shared.api_client import get_json
from .base import success_result, error_result


BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def get_clinvar_variants(
    gene_symbol: str,
    limit: int = 5,
) -> dict:
    """
    Search ClinVar for variants associated with a gene.

    Parameters
    ----------
    gene_symbol:
        Gene symbol, e.g. PCSK9.

    limit:
        Maximum number of ClinVar records to retrieve.

    Returns
    -------
    dict
        Standardized OpenRepurpose wrapper response.
    """

    try:

        # --------------------------------------------------
        # Step 1: Search ClinVar
        # --------------------------------------------------

        search_url = (
            f"{BASE_URL}/esearch.fcgi"
        )

        params = {
            "db": "clinvar",
            "term": f"{gene_symbol}[gene]",
            "retmax": limit,
            "retmode": "json",
        }

        search_data = get_json(
            search_url,
            params=params,
        )

        # --------------------------------------------------
        # Step 2: Extract ClinVar IDs
        # --------------------------------------------------

        search_result = search_data.get(
            "esearchresult",
            {},
        )

        ids = search_result.get(
            "idlist",
            [],
        )

        # --------------------------------------------------
        # Step 3: Return standardized result
        # --------------------------------------------------

        return success_result(
            source="ClinVar",
            data={
                "query": gene_symbol,
                "variant_ids": ids,
                "count": len(ids),
            },
        )

    except Exception as exc:

        return error_result(
            source="ClinVar",
            error=str(exc),
        )