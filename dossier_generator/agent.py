import argparse


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

    print("OpenRepurpose")
    print("---------------------")
    print("Target:", args.target)
    print("Drug:", args.drug)
    print("Disease:", args.disease)


if __name__ == "__main__":
    main()