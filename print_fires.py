import argparse

from my_utils import get_column


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

args = parser.parse_args()

fires = get_column(
    args.file_name,
    args.country_column,
    args.country,
    result_column=args.fires_column
)

print(fires)
