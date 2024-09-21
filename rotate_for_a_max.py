def max_rot(n):
    num_str = str(n)
    max_num = n
    
    for num in range(len(n) - 1):
        num_str = num_str[:num] + num_str[num + 1:] + num_str[num]
        max_num = max(max_num, int(num_str))
    return max_num