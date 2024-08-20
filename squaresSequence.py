def squares(x, n):
    if n <= 0:
        return []
    num_list = [x]
    for num in range(1, n):
        num_list.append(num_list[-1]**2)
    return num_list