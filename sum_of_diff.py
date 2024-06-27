def sum_of_differences(arr):
    if len(arr) < 2:
        return 0
    
    arr.sort(reverse=True)
    new_arr = []
    for i in range (len(arr) - 1):
        diff = abs(arr[i] + arr[i+1])
        new_arr.append(diff)
    return new_arr 