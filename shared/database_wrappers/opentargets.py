from .base import not_implemented


def get_target_disease_associations(target):
    return not_implemented("Open Targets")

from shared.api_client import post_json
from shared.database_wrappers.base import success, error

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
    ):

    lookup = get_ensembl_id(gene_symbol)
    
    if lookup["status"] == "error":
        return lookup
    
    ensembl_id = lookup["data"]["ensembl_id"]

    """
    Retrieve top disease associations for a target.
    """

    payload = {
        "query": QUERY,
        "variables": {
            "ensemblId": ensembl_id
        }
    }

    result = post_json(BASE_URL, payload)

    if result["status"] == "error":
        return error(
            "Open Targets",
            result["error"]
        )

    data = result["data"]
    
    target = data["data"]["target"]
    
    rows = target["associatedDiseases"]["rows"]
    
    associations = []
    
    for row in rows:
        associations.append(
        {
            "disease_id": row["disease"]["id"],
            "disease_name": row["disease"]["name"],
            "association_score": row["score"],
        }
    )
    
    return success(
        "Open Targets",
    {
        "query": ensembl_id,
        "results": associations,
    },
)