class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        mapping = {n:i for i, n in enumerate(arr)}
        result = 0
        dp = [[0] * len(arr) for _ in range(len(arr))]
        
        for i in reversed(range(len(arr))):
            for j in reversed(range(i + 1, len(arr))):
                prev, current = arr[i], arr[j]
                nxt = prev + current
                length = 2
                if nxt in mapping:
                    length = 1 + dp[j][mapping[nxt]]
                    result = max(result, length)
                dp[i][j] = length
        return result