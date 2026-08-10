from shared.database_wrappers import get_ensembl_id

result = get_ensembl_id("PCSK9")

assert result["status"] == "success"
assert result["data"]["ensembl_id"].startswith("ENSG")