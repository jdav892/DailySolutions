def elevator_distance(array):
    num = 0
    for i in range(len(array) - 1):
        num += abs(array[i] - array[i + 1])
    return num

    """def elevator_distance(array):
    return sum([abs(array[i] - array[i + 1]) for i in range(len(array) - 1)])
    """