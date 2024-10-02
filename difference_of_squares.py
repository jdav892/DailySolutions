def difference_of_squares(n):
    sum_of_nums = sum(range(1, n + 1))
    square_of_sum = sum_of_nums**2
    sum_of_squares = sum(num ** 2 for num in range(1, n + 1))
    return square_of_sum - sum_of_squares