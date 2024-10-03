def max_tri_sum(numbers):
    uniques = set(numbers)
    sorted_nums = sorted(uniques, reverse=True)
    max_trips_sum = sum(sorted_nums[:3])
    return max_trips_sum