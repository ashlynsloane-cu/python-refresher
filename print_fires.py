import argparse

import my_utils


def main():
    parser = argparse.ArgumentParser(
        description="Print forest fire emissions for a country."
    )

    parser.add_argument(
        "--country",
        type=str,
        required=True,
        help="Country name"
    )

    parser.add_argument(
        "--country_column",
        type=int,
        required=True,
        help="Column containing country names"
    )

    parser.add_argument(
        "--fires_column",
        type=int,
        required=True,
        help="Column containing forest fire emissions"
    )

    parser.add_argument(
        "--file_name",
        type=str,
        required=True,
        help="Input CSV file"
    )

    parser.add_argument(
        "--operation",
        type=str,
        choices=["mean", "median", "stdev", "all"],
        required=False,
        help="Statistic to calculate"
    )

    args = parser.parse_args()

    fires = my_utils.get_column(
        args.file_name,
        args.country_column,
        args.country,
        result_column=args.fires_column
    )

    print(fires)

    if args.operation == "mean":
        print("Mean:", my_utils.mean(fires))

    elif args.operation == "median":
        print("Median:", my_utils.median(fires))

    elif args.operation == "stdev":
        print("Standard Deviation:", my_utils.stdev(fires))

    elif args.operation == "all":
        print("Mean:", my_utils.mean(fires))
        print("Median:", my_utils.median(fires))
        print("Standard Deviation:", my_utils.stdev(fires))


if __name__ == "__main__":
    main()
