def arr_check(arr):
    result = True
    for el in arr:
        if type(el) != list:
            result = False
    return result


#return all(isinstance(el, list) for el in arr)