from shared.database_wrappers import (
    get_faers_events,
    get_gtex_expression,
)

print(get_gtex_expression("PCSK9"))

faers = get_faers_events("evolocumab")

print(faers["status"])
print(faers["source"])