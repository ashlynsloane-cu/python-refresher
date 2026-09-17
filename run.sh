#!/bin/bash

echo "Example 1: valid input"
python print_fires.py \
    --country "United States of America" \
    --country_column 0 \
    --fires_column 3 \
    --file_name Agrofood_co2_emission.csv

echo
echo "Example 2: missing file"
python print_fires.py \
    --country "United States of America" \
    --country_column 0 \
    --fires_column 3 \
    --file_name missing_file.csv

echo
echo "Example 3: invalid column argument"
python print_fires.py \
    --country "United States of America" \
    --country_column not_an_integer \
    --fires_column 3 \
    --file_name Agrofood_co2_emission.csv
