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
