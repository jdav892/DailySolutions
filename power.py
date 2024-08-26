def number_to_pwr(number, p):
    new_total = 1
    while p > 0:
        new_total *= number
        p -= 1
    return new_total