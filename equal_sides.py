def find_even_index(arr):
    for index in range(len(arr)):
        l_sum = sum(arr[:index])
        r_sum = sum(arr[index+1:])
        
        if l_sum == r_sum:
            return index
        
    return -1