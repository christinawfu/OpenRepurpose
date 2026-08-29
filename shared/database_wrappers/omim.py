"""
OMIM wrapper.

Retrieves Mendelian disease-gene relationships from OMIM.
"""

from shared.config import OMIM_API_KEY
from shared.api_client import get_json
from .base import success_result, error_result


BASE_URL = "https://api.omim.org/api"


def get_omim_disease_genes(
    disease_or_gene: str,
    limit: int = 10,
) -> dict:
    """
    Retrieve Mendelian disease-gene relationships from OMIM.

    Parameters
    ----------
    disease_or_gene:
        Gene symbol or disease name.

    limit:
        Maximum number of gene-map results to request.

    Returns
    -------
    dict
        Standardized OpenRepurpose response.
    """

    if not OMIM_API_KEY:
        return error_result(
            source="OMIM",
            error="OMIM_API_KEY is not configured.",
        )

    try:
        url = f"{BASE_URL}/geneMap/search"

        params = {
            "search": disease_or_gene,
            "include": "geneMap",
            "apiKey": OMIM_API_KEY,
            "format": "json",
            "start": 0,
            "limit": limit,
        }

        result = get_json(
            url,
            params=params,
        )

        search_response = (
            result
            .get("omim", {})
            .get("searchResponse", {})
        )

        gene_map_list = search_response.get(
            "geneMapList",
            [],
        )

        associations = []

        for item in gene_map_list:

            gene_map = item.get(
                "geneMap",
                {},
            )

            gene = gene_map.get(
                "approvedGeneSymbols"
                or "geneSymbols"
            )

            gene_name = gene_map.get(
                "geneName"
            )

            gene_mim = gene_map.get(
                "mimNumber"
            )

            ensembl_ids = gene_map.get(
                "ensemblIDs"
            )

            phenotype_map_list = gene_map.get(
                "phenotypeMapList",
                [],
            )

            for phenotype_item in phenotype_map_list:

                phenotype = phenotype_item.get(
                    "phenotypeMap",
                    {},
                )

                associations.append(
                    {
                        "gene": gene,
                        "gene_name": gene_name,
                        "gene_mim_number": gene_mim,
                        "ensembl_ids": ensembl_ids,
                        "phenotype": phenotype.get(
                            "phenotype"
                        ),
                        "phenotype_mim_number": phenotype.get(
                            "phenotypeMimNumber"
                        ),
                        "inheritance": phenotype.get(
                            "phenotypeInheritance"
                        ),
                        "mapping_key": phenotype.get(
                            "phenotypeMappingKey"
                        ),
                    }
                )

        return success_result(
            source="OMIM",
            data={
                "query": disease_or_gene,
                "associations": associations,
                "count": len(associations),
            },
        )

    except Exception as exc:
        return error_result(
            source="OMIM",
            error=str(exc),
        )