def arr_check(arr):
    result = True
    for el in arr:
        if type(el) != list:
            result = False
    return result


