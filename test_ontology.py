from shared.database_wrappers import normalize_disease_name


result = normalize_disease_name(
    "hypercholesterolemia"
)

print("Status:", result["status"])
print("Source:", result["source"])

if result["status"] == "success":
    print(
        "Canonical ID:",
        result["data"]["canonical_id"]
    )

    print(
        "Canonical name:",
        result["data"]["canonical_name"]
    )
else:
    print(
        "Error:",
        result.get("message")
    )