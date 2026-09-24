test -e ssshtest || wget -q \
    https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest


run test_default_output \
    python print_fires.py \
    --country USA \
    --country_column 0 \
    --fires_column 1 \
    --file_name test/functional/test_data.csv

assert_exit_code 0
assert_in_stdout "[10, 30, 50]"


run test_mean \
    python print_fires.py \
    --country USA \
    --country_column 0 \
    --fires_column 1 \
    --file_name test/functional/test_data.csv \
    --operation mean

assert_exit_code 0
assert_in_stdout "[10, 30, 50]"
assert_in_stdout "Mean: 30.0"


run test_median \
    python print_fires.py \
    --country USA \
    --country_column 0 \
    --fires_column 1 \
    --file_name test/functional/test_data.csv \
    --operation median

assert_exit_code 0
assert_in_stdout "[10, 30, 50]"
assert_in_stdout "Median: 30"


run test_stdev \
    python print_fires.py \
    --country USA \
    --country_column 0 \
    --fires_column 1 \
    --file_name test/functional/test_data.csv \
    --operation stdev

assert_exit_code 0
assert_in_stdout "[10, 30, 50]"
assert_in_stdout "Standard Deviation: 16.32993161855452"


run test_all \
    python print_fires.py \
    --country USA \
    --country_column 0 \
    --fires_column 1 \
    --file_name test/functional/test_data.csv \
    --operation all

assert_exit_code 0
assert_in_stdout "[10, 30, 50]"
assert_in_stdout "Mean: 30.0"
assert_in_stdout "Median: 30"
assert_in_stdout "Standard Deviation: 16.32993161855452"


run test_invalid_operation \
    python print_fires.py \
    --country USA \
    --country_column 0 \
    --fires_column 1 \
    --file_name test/functional/test_data.csv \
    --operation banana

assert_exit_code 2
assert_in_stderr "invalid choice"
