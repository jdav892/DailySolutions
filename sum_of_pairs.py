def sum_pairs(ints, s):
    new_set = set()
    for num in ints:
        adder = s - num
        if adder in new_set:
            return [adder, num]
        new_set.add(num)
    return None