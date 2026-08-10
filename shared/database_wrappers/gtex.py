"""
GTEx gene expression wrapper.
"""

from urllib.parse import quote

from shared.api_client import get_json
from .base import success, error


BASE_URL = "https://gtexportal.org/api/v2"


def get_gtex_expression(gene_symbol: str):
    """
    Retrieve median GTEx gene expression across tissues.

    Parameters
    ----------
    gene_symbol : str
        HGNC gene symbol, such as PCSK9.

    Returns
    -------
    dict
        Standardized wrapper response.
    """

    # Step 1: Find the GENCODE ID for the gene symbol.
    gene_url = (
        f"{BASE_URL}/reference/gene"
        f"?geneId={quote(gene_symbol)}"
        f"&page=0"
        f"&itemsPerPage=10"
    )

    gene_result = get_json(gene_url)

    if gene_result["status"] == "error":
        return error("GTEx", gene_result["error"])

    gene_data = gene_result["data"]

    genes = gene_data.get("data", [])

    if not genes:
        return error(
            "GTEx",
            f"No GTEx gene found for {gene_symbol}",
        )

    gencode_id = genes[0].get("gencodeId")

    if not gencode_id:
        return error(
            "GTEx",
            f"No GENCODE ID found for {gene_symbol}",
        )

    # Step 2: Retrieve median expression across tissues.
    expression_url = (
        f"{BASE_URL}/expression/medianGeneExpression"
        f"?gencodeId={quote(gencode_id)}"
        f"&datasetId=gtex_v10"
        f"&page=0"
        f"&itemsPerPage=250"
    )

    expression_result = get_json(expression_url)

    if expression_result["status"] == "error":
        return error(
            "GTEx",
            expression_result["error"],
        )

    expression_data = expression_result["data"]

    return success(
        "GTEx",
        {
            "query": gene_symbol,
            "gencode_id": gencode_id,
            "results": expression_data.get("data", []),
        },
    )