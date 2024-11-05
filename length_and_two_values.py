def alternate(n, first_value, second_value):
    arr = []
    for i in range(0, n, 1):
        if i % 2 == 0:
            arr.append(first_value)
        else:
            arr.append(second_value)
    return arr