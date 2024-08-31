def jumping_number(number):
    num_str = str(number)
    for num in range(len(num_str) - 1):
        if abs(int(num_str[num]) - int(num_str[num + 1])) != 1:
            return "Not!!"
    return "Jumping!!"