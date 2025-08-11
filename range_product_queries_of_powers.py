class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7

        r = []
        for i in range(32):
            if (n & (1 << i)) > 0:
                r.append(1 << i)

        result = []
        for s, e in queries:
            j = 1
            for i in range(s, e + 1):
                j *= r[i]
                j %= MOD
            result.append(j)
        return result