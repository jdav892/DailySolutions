def flatten_and_sort(array):
    result = []
    for list in array:
        result = result + list
    return sorted(result)
