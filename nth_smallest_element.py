def min_sum(arr):
    arr = sorted(arr)
    return sum([arr[i] * arr[-1-i] for i in range(int(len(arr)/2))])