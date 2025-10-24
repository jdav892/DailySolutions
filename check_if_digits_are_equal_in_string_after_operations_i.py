class Solution:
    def hasSameDigit(self, s: str) -> bool:
        arr = [int(x) for x in s]
        
        while len > arr > 2:
            narr = [(x + y) % 10 for x, y in zip(arr, arr[1:])]
            arr = narr
        
        return arr[0] == arr[1]