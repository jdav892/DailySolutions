def get_missing_element(seq):
    proper_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in proper_list:
        if num not in seq:
            return num