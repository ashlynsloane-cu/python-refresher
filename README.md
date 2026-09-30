# Python Refresher

This repository contains Python code for reading agricultural CO2 emissions data and reporting forest fire emissions for a selected country. It can also calculate the mean, median, and population standard deviation of the selected values.

## Environment Setup

Create the environment from `environment.yml`:

```
mamba env create -f environment.yml
```

Activate the environment:

```
conda activate swe4s_assignment3
```

The environment includes `pycodestyle` for checking Python style.

## Data File

The main program expects `Agrofood_co2_emission.csv` to be present in the repository directory. The data file is not committed to Git.

A small test data file is included at:

```
test/functional/test_data.csv
```

## Running the Program

`print_fires.py` accepts four required command-line arguments:

* `--country`: country name
* `--country_column`: column containing country names
* `--fires_column`: column containing forest fire emissions
* `--file_name`: input CSV file

It also accepts one optional argument:

* `--operation`: `mean`, `median`, `stdev`, or `all`

Without `--operation`, the program prints the selected forest fire values.

Example:

```
python print_fires.py \
    --country "United States of America" \
    --country_column 0 \
    --fires_column 3 \
    --file_name Agrofood_co2_emission.csv
```

To calculate the mean:

```
python print_fires.py \
    --country "United States of America" \
    --country_column 0 \
    --fires_column 3 \
    --file_name Agrofood_co2_emission.csv \
    --operation mean
```

The other supported operations are:

```
--operation median
--operation stdev
--operation all
```

## Running the Examples

Run:

```
./run.sh
```

The script includes three examples:

1. A valid input example
2. A missing-file example
3. An invalid column argument example

## Unit Tests

Unit tests are located in:

```
test/unit/
```

Run all unit tests with:

```
python -m unittest discover -s test/unit -p "test_*.py" -v
```

The unit tests cover `get_column`, `mean`, `median`, and `stdev`, including normal and error cases. The statistical functions are also tested using reproducible random input.

## Functional Tests

Functional tests are located in:

```
test/functional/
```

Run them with:

```
bash test/functional/test_print_fires.sh
```

The functional tests use `ssshtest` to check command-line output and exit codes for the default behavior, each statistical operation, and invalid input.

## Style Checking

Check the Python files with:

```
pycodestyle my_utils.py print_fires.py test/unit/test_my_utils.py
```

No output from `pycodestyle` indicates that no style violations were found.

## Continuous Integration

GitHub Actions automatically runs the unit tests, functional tests, and `pycodestyle` checks whenever any branch is pushed and whenever a pull request is opened against `master`.

The workflow is defined in:

```
.github/workflows/test.yml
```
