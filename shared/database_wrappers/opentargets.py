"""
Open Targets Platform wrapper.

Retrieves disease associations for a target gene
using the Open Targets GraphQL API.
"""

from shared.api_client import post_json
from .base import success_result, error_result
from .gene_lookup import get_ensembl_id


BASE_URL = "https://api.platform.opentargets.org/api/v4/graphql"


QUERY = """
query TargetAssociations($ensemblId: String!) {
  target(ensemblId: $ensemblId) {
    approvedSymbol
    associatedDiseases(page: {index: 0, size: 5}) {
      count
      rows {
        score
        disease {
          id
          name
        }
      }
    }
  }
}
"""


def get_target_disease_associations(
    gene_symbol: str,
) -> dict:
    """
    Retrieve top disease associations for a target gene.

    Parameters
    ----------
    gene_symbol:
        Gene symbol, e.g. PCSK9.

    Returns
    -------
    dict
        Standardized OpenRepurpose wrapper response.
    """

    try:

        # --------------------------------------------------
        # Step 1: Convert gene symbol to Ensembl ID
        # --------------------------------------------------

        lookup = get_ensembl_id(gene_symbol)

        if lookup["status"] == "error":
            return error_result(
                source="Open Targets",
                error=lookup["error"],
            )

        ensembl_id = lookup["data"]["ensembl_id"]

        # --------------------------------------------------
        # Step 2: Build GraphQL request
        # --------------------------------------------------

        payload = {
            "query": QUERY,
            "variables": {
                "ensemblId": ensembl_id,
            },
        }

        # --------------------------------------------------
        # Step 3: Query Open Targets
        # --------------------------------------------------

        result = post_json(
            BASE_URL,
            json=payload,
        )

        # --------------------------------------------------
        # Step 4: Check GraphQL errors
        # --------------------------------------------------

        if result.get("errors"):
            return error_result(
                source="Open Targets",
                error=str(result["errors"]),
            )

        # --------------------------------------------------
        # Step 5: Extract target
        # --------------------------------------------------

        data = result.get(
            "data",
            {},
        )

        target = data.get("target")

        if target is None:
            return success_result(
                source="Open Targets",
                data={
                    "query": gene_symbol,
                    "ensembl_id": ensembl_id,
                    "results": [],
                    "count": 0,
                },
            )

        # --------------------------------------------------
        # Step 6: Extract disease associations
        # --------------------------------------------------

        disease_data = target.get(
            "associatedDiseases",
            {},
        )

        rows = disease_data.get(
            "rows",
            [],
        )

        associations = []

        for row in rows:

            disease = row.get(
                "disease",
                {},
            )

            associations.append(
                {
                    "disease_id": disease.get("id"),
                    "disease_name": disease.get("name"),
                    "association_score": row.get("score"),
                }
            )

        # --------------------------------------------------
        # Step 7: Return standardized response
        # --------------------------------------------------

        return success_result(
            source="Open Targets",
            data={
                "query": gene_symbol,
                "ensembl_id": ensembl_id,
                "results": associations,
                "count": len(associations),
            },
        )

    except Exception as exc:

        return error_result(
            source="Open Targets",
            error=str(exc),
        )