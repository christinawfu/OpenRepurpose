from shared.database_wrappers import (
    get_target_disease_associations,
)

result = get_target_disease_associations("PCSK9")

assert result["status"] == "success"
assert len(result["data"]["results"]) > 0