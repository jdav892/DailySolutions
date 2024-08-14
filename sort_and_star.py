def two_sort(array):
    sorted_string = sorted(array)
    first = sorted_string[0]
    formatted = "***".join(first)
    return formatted

# return "***".join(sorted(arr)[0]) also works, same with "***".join(min(lst))