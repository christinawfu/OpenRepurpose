import argparse
from tools import get_target_summary

def main():

    parser = argparse.ArgumentParser(
        description="OpenRepurpose Evidence Generator"
    )

    parser.add_argument(
        "--target",
        required=True,
        help="Target gene"
    )

    parser.add_argument(
        "--drug",
        required=True,
        help="Drug name"
    )

    parser.add_argument(
        "--disease",
        required=True,
        help="Disease name"
    )

    args = parser.parse_args()

    summary = get_target_summary(args.target)

    print("OpenRepurpose")
    print("---------------------")
    print("Target:", args.target)
    print("Drug:", args.drug)
    print("Disease:", args.disease)

    print("\nTarget Summary")
    print(f"Target: {summary['target']}")
    print(f"Status: {summary['status']}")
    print(f"Message: {summary['message']}")

if __name__ == "__main__":
    main()