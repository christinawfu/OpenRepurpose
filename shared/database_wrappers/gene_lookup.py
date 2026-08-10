"""
Gene symbol → Ensembl ID lookup using the Ensembl REST API.
"""

from shared.api_client import get_json
from .base import success, error

BASE_URL = "https://rest.ensembl.org"


def get_ensembl_id(gene_symbol: str):
    url = (
        f"{BASE_URL}/xrefs/symbol/homo_sapiens/"
        f"{gene_symbol}?content-type=application/json"
    )

    result = get_json(url)

    if result["status"] == "error":
        return error("Ensembl", result["error"])

    data = result["data"]

    if not data:
        return error(
            "Ensembl",
            f"No Ensembl ID found for {gene_symbol}",
        )

    for item in data:
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