class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7
        N = len(s)

        sec = [ord(c) - ord('a') for c in s]
        f = [0] * 26
        for c in sec:
            f[c] += 1

        for _ in range(t):
            nf = [0] * 26
            for c in range(26 - 1):
                nf[c + 1] += f[c]
            nf[0] += f[25]
            nf[1] += f[25]

            for c in range(26):
                nf[c] %= MOD
            f = nf
        return sum(f) % MOD