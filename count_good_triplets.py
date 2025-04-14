class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        result = 0
        N = len(arr)
        prefix = [0] * 1001
        
        for j in range(N - 1):
            for k in range(j + 1, N):
                if abs(arr[j] - arr[k]) <= b:
                    r = min(arr[j] + a, arr[k] + c)
                    l = max(arr[j] - a, arr[k] - c)
                    
                    l = max(l, 0)
                    r = min(r, 1000)
                    
                    if l <= r:
                        result += prefix[r] - (0 if l == 0 else prefix[l-1])
            for index in range(arr[j], 1001):
                prefix[index] += 1
        return result