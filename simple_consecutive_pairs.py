def pairs(arr):
    count = 0
    for num in range(0, len(arr) - 1, 2):
        if abs(arr[num] - arr[num + 1]) == 1:
            count += 1
    return count
            