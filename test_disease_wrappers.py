from shared.database_wrappers import (
    normalize_disease_name,
    get_disgenet_associations,
    get_omim_disease_genes,
)


print("\n=== Ontology ===")

ontology = normalize_disease_name(
    "hypercholesterolemia"
)

print("Status:", ontology["status"])
print("Source:", ontology["source"])

if ontology["status"] == "success":
    print(
        "Canonical ID:",
        ontology["data"]["canonical_id"],
    )

    print(
        "Canonical Name:",
        ontology["data"]["canonical_name"],
    )


print("\n=== DisGeNET ===")

disgenet = get_disgenet_associations("PCSK9")

print("Status:", disgenet["status"])
print("Source:", disgenet["source"])

if disgenet["status"] == "error":
    print(
        "Message:",
        disgenet["message"],
    )


print("\n=== OMIM ===")

omim = get_omim_disease_genes(
    "PCSK9"
)

print("Status:", omim["status"])
print("Source:", omim["source"])

if omim["status"] == "error":
    print(
        "Message:",
        omim["message"],
    )