# Python Refresher

This repository contains Python code for reading agricultural CO2 emissions data and printing forest fire emissions for a selected country.

## Environment Setup

Create the environment from `environment.yml`:

    mamba env create -f environment.yml

Activate the environment:

    conda activate swe4s_assignment2

The environment includes `pycodestyle` for checking Python style.

## Data File

The script expects `Agrofood_co2_emission.csv` to be present in the repository directory. The data file is not committed to Git.

## Running the Program

`print_fires.py` accepts four required command-line arguments:

- `--country`: country name
- `--country_column`: column containing country names
- `--fires_column`: column containing forest fire emissions
- `--file_name`: input CSV file

Example:

    python print_fires.py \
        --country "United States of America" \
        --country_column 0 \
        --fires_column 3 \
        --file_name Agrofood_co2_emission.csv

## Running the Examples

Run:

    ./run.sh

The script includes three examples:

1. A valid input example
2. A missing-file example
3. An invalid column argument example

## Style Checking

Check the Python files with:

    pycodestyle my_utils.py print_fires.py

No output from `pycodestyle` indicates that no style violations were found.
