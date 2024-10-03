def sum_of_n(n):
    start = 0
    if n >= 0:
        start = 1
    else:
        start = -1
    return [start * (range(num + 1)) for num in range(abs(n) + 1)]