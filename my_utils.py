def get_column(file_name, query_column, query_value, result_column):
    result = []
    
    with open(file_name, "r") as file:
        for line in file:
            values = line.strip().split(",")
            if values[query_column] == query_value:
                result.append(values[result_column])
    return result
