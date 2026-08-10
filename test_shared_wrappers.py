from shared.database_wrappers import (
    get_gtex_expression,
    get_hpa_protein,
    get_clinvar_variants,
    get_chembl_drug_info,
)


print("\n=== GTEx ===")

gtex = get_gtex_expression("PCSK9")

print("Status:", gtex["status"])
print("Source:", gtex["source"])


print("\n=== Human Protein Atlas ===")

hpa = get_hpa_protein("PCSK9")

print("Status:", hpa["status"])
print("Source:", hpa["source"])


print("\n=== ClinVar ===")

clinvar = get_clinvar_variants("PCSK9")

print("Status:", clinvar["status"])
print("Source:", clinvar["source"])

if clinvar["status"] == "success":
    print(
        "Variants:",
        clinvar["data"]["count"]
    )


print("\n=== ChEMBL ===")

chembl = get_chembl_drug_info("evolocumab")

print("Status:", chembl["status"])
print("Source:", chembl["source"])