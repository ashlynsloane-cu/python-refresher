import csv
import os
import random
import statistics
import tempfile
import unittest

import my_utils


class TestMyUtils(unittest.TestCase):

    def setUp(self):
        random.seed(42)
        self.data = [
            random.randint(-100, 100)
            for _ in range(25)
        ]

    def test_get_column(self):
        with tempfile.NamedTemporaryFile(
            mode="w",
            newline="",
            delete=False
        ) as test_file:
            writer = csv.writer(test_file)
            writer.writerow(["USA", "10"])
            writer.writerow(["Canada", "20"])
            writer.writerow(["USA", "30"])
            file_name = test_file.name

        result = my_utils.get_column(
            file_name,
            0,
            "USA",
            result_column=1
        )

        os.remove(file_name)

        self.assertEqual(result, [10, 30])

    def test_get_column_missing_file(self):
        result = my_utils.get_column(
            "file_that_does_not_exist.csv",
            0,
            "USA",
            result_column=1
        )

        self.assertEqual(result, [])

    def test_mean(self):
        expected = statistics.mean(self.data)
        result = my_utils.mean(self.data)

        self.assertAlmostEqual(result, expected)

    def test_mean_empty_list(self):
        with self.assertRaises(ValueError):
            my_utils.mean([])

    def test_median(self):
        expected = statistics.median(self.data)
        result = my_utils.median(self.data)

        self.assertAlmostEqual(result, expected)

    def test_median_even_list(self):
        data = [1, 2, 3, 4]

        self.assertEqual(my_utils.median(data), 2.5)

    def test_median_empty_list(self):
        with self.assertRaises(ValueError):
            my_utils.median([])

    def test_stdev(self):
        expected = statistics.pstdev(self.data)
        result = my_utils.stdev(self.data)

        self.assertAlmostEqual(result, expected)

    def test_stdev_empty_list(self):
        with self.assertRaises(ValueError):
            my_utils.stdev([])


if __name__ == "__main__":
    unittest.main()
