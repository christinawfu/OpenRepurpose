"""
Human Protein Atlas database wrapper.

Retrieves protein and tissue expression information
for a human gene.
"""

from shared.api_client import get_json

from shared.database_wrappers.base import (
    success_result,
    error_result,
)


HPA_URL = (
    "https://www.proteinatlas.org/api/search_download.php"
)


def get_hpa_protein(
    gene_symbol: str,
) -> dict:
    """
    Retrieve Human Protein Atlas protein/tissue information.

    Parameters
    ----------
    gene_symbol:
        HGNC gene symbol, e.g. PCSK9.

    Returns
    -------
    dict
        Standardized OpenRepurpose result.
    """

    try:

        params = {
            "search": gene_symbol,
            "format": "json",

            # Requested HPA fields.
            #
            # g     = gene
            # eg    = Ensembl gene ID
            # prts  = protein tissue specificity
            # prtd  = protein tissue distribution
            # prtss = protein tissue specificity score
            # prtsm = protein tissue-specific intensity
            #
            "columns": (
                "g,eg,prts,prtd,prtss,prtsm"
            ),

            "compress": "no",
        }

        data = get_json(
            HPA_URL,
            params=params,
        )

        return success_result(
            source="Human Protein Atlas",
            data={
                "gene": gene_symbol,
                "results": data,
            },
        )

    except Exception as exc:

        return error_result(
            source="Human Protein Atlas",
            error=str(exc),
        )