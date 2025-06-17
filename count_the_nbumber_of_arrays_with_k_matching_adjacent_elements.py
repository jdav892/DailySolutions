MAX = 100005
MOD = 10 ** 9 + 7
fact = [1]
ifact = [1]
for i in range(1, MAX):
    fact.append((fact[-1] * i) % MOD)
    ifact.append(pow(fact[-1], -1, MOD))

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        return (m * pow(m - 1, n - 1 - k, MOD) * fact[n - 1] * ifact[k] * ifact[n - 1 - k]) % MOD

