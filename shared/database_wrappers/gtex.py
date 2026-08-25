"""
GTEx database wrapper.

Retrieves median gene expression across tissues
from the GTEx Portal.
"""

from shared.api_client import get_json
from shared.database_wrappers.base import (
    success_result,
    error_result,
)


GTEX_API_URL = "https://gtexportal.org/api/v2"

# We explicitly use GTEx v8 because the GENCODE annotation
# returned by the current geneSearch endpoint is compatible
# with this dataset.
GTEX_DATASET = "gtex_v8"


def get_gtex_expression(
    gene_symbol: str,
) -> dict:
    """
    Retrieve median GTEx expression across tissues.

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

        # --------------------------------------------------
        # Step 1: Resolve gene symbol to GENCODE ID
        # --------------------------------------------------

        gene_response = get_json(
            f"{GTEX_API_URL}/reference/geneSearch",
            params={
                "geneId": gene_symbol,
            },
        )

        genes = gene_response.get(
            "data",
            []
        )

        if not genes:

            return error_result(
                source="GTEx",
                error=(
                    f"GTEx could not find gene "
                    f"{gene_symbol}."
                ),
            )

        gene_record = genes[0]

        gencode_id = gene_record.get(
            "gencodeId"
        )

        if not gencode_id:

            return error_result(
                source="GTEx",
                error=(
                    f"GTEx returned a gene record for "
                    f"{gene_symbol}, but no GENCODE ID "
                    f"was found."
                ),
                data=gene_record,
            )

        # --------------------------------------------------
        # Step 2: Retrieve median tissue expression
        # --------------------------------------------------

        expression_response = get_json(
            f"{GTEX_API_URL}/expression/medianGeneExpression",
            params={
                "gencodeId": gencode_id,
                "datasetId": GTEX_DATASET,
            },
        )

        expression_records = expression_response.get(
            "data",
            []
        )

        if not expression_records:

            return error_result(
                source="GTEx",
                error=(
                    f"GTEx returned no expression data "
                    f"for {gene_symbol} using "
                    f"{GTEX_DATASET}."
                ),
                data={
                    "gene": gene_symbol,
                    "gencode_id": gencode_id,
                },
            )

        # --------------------------------------------------
        # Step 3: Standardize tissue records
        # --------------------------------------------------

        tissues = []

        for record in expression_records:

            tissues.append(
                {
                    "tissue": record.get(
                        "tissueSiteDetailId"
                    ),
                    "median_tpm": record.get(
                        "median"
                    ),
                    "ontology_id": record.get(
                        "ontologyId"
                    ),
                    "unit": record.get(
                        "unit"
                    ),
                }
            )

        # --------------------------------------------------
        # Step 4: Determine highest-expression tissue
        # --------------------------------------------------

        valid_tissues = [
            tissue
            for tissue in tissues
            if isinstance(
                tissue.get("median_tpm"),
                (int, float),
            )
        ]

        highest_expression_tissue = None

        if valid_tissues:

            highest_expression_tissue = max(
                valid_tissues,
                key=lambda x: x["median_tpm"],
            )

        # --------------------------------------------------
        # Step 5: Return standardized result
        # --------------------------------------------------

        return success_result(
            source="GTEx",
            data={
                "gene": gene_symbol,
                "gencode_id": gencode_id,
                "dataset": GTEX_DATASET,
                "tissue_count": len(tissues),
                "tissues": tissues,
                "highest_expression_tissue": (
                    highest_expression_tissue
                ),
            },
        )

    except Exception as exc:

        return error_result(
            source="GTEx",
            error=str(exc),
        )