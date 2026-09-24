import csv


def get_column(file_name, query_column, query_value, result_column=1):
    result = []

    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("Could not find " + file_name)
        return result
    except PermissionError:
        print("Could not open " + file_name)
        return result

    reader = csv.reader(file)

    for values in reader:
        try:
            if values[query_column] == query_value:
                value = int(float(values[result_column]))
                result.append(value)
        except ValueError:
            print(
                "Could not convert "
                + values[result_column]
                + " to an integer"
            )
        except IndexError:
            print("Column index is outside the available columns")

    file.close()

    return result


def mean(data):
    if len(data) == 0:
        raise ValueError("Cannot calculate mean of empty list")

    return sum(data) / len(data)


def median(data):
    if len(data) == 0:
        raise ValueError("Cannot calculate median of empty list")

    sorted_data = sorted(data)
    middle = len(sorted_data) // 2

    if len(sorted_data) % 2 == 1:
        return sorted_data[middle]

    return (
        sorted_data[middle - 1] + sorted_data[middle]
    ) / 2


def stdev(data):
    if len(data) == 0:
        raise ValueError(
            "Cannot calculate standard deviation of empty list"
        )

    data_mean = mean(data)

    squared_differences = [
        (value - data_mean) ** 2
        for value in data
    ]

    variance = sum(squared_differences) / len(data)

    return variance ** 0.5
