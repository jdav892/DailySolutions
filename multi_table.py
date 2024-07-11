def multi_table(number):
    sequence = ""
    for num in range(1, 11):
        sequence += f"f{num} * {number} = {num * number}\n"
    return sequence.rstrip('\n')