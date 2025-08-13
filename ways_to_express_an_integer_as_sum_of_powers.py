class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7

        ways = [0] * (n + 1)
        ways[0] = 1

        for i in range(1, int(pow(n, 1 / x)) + 2):
            c = pow(i, x)

            for j in range(n, -1, -1):
                if j - c >= 0:
                    ways[j] += ways[j - c]
                    ways[j] %= MOD

        return ways[n] % MOD