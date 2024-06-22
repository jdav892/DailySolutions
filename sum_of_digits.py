def sum_digits(number):
    total = 0
    for digit in str(number):
        if digit.isdigit():
            total += digit
    return total