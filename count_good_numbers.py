class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        odd = n // 2
        even = n - odd
        return (pow(5, even, MOD) * pow(4, odd, MOD)) % MOD