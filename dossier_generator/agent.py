import argparse

from shared.database_wrappers import (
    get_faers_events,
    get_gtex_expression,
    get_target_disease_associations,
)

from dossier_generator.formatter import save_results

def main():

    parser = argparse.ArgumentParser(
        description="OpenRepurpose Evidence Generator"
    )

    parser.add_argument("--target", required=True)
    parser.add_argument("--drug", required=True)
    parser.add_argument("--disease", required=True)

    args = parser.parse_args()

    print("\nOpenRepurpose")
    print("----------------------------")

    print("Target :", args.target)
    print("Drug   :", args.drug)
    print("Disease:", args.disease)

    faers = get_faers_events(args.drug)

    opentargets = get_target_disease_associations(
        args.target
    )

    print(get_gtex_expression("PCSK9"))

    print("\nFAERS Summary")
    print("----------------------------")

    print("Status:", faers["status"])
    print("Drug:", faers["data"]["drug"])
    print("Reports Retrieved:", faers["data"]["num_reports"])

    results = {
    "target": args.target,
    "drug": args.drug,
    "disease": args.disease,
    "faers": faers,
    "opentargets": opentargets,
    }

    json_path, md_path = save_results(
    args.target,
    args.drug,
    args.disease,
    results,
    )
    
    print("\nFiles Created")
    print("----------------------------")
    print(json_path)
    print(md_path)

    
    
if __name__ == "__main__":
    main()
