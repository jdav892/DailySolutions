def build_suffix(s):
    n = len(s)
    k = 1
    rank = [ord(c) for c in s]
    tmp = [0] * n
    sa = list(range(n))

    while True:
        sa.sort(key=lambda x: (rank[x], rank[x + k] if x + k < n else -1))

        tmp[sa[0]] = 0
        for i in range(1 , n):
            tmp[sa[i]] = tmp[sa[i - 1]] + (
                (rank[sa[i]] != rank[sa[i - 1]] or
                (rank[sa[i] + k if sa[i] + k < n else -1]) != 
                (rank[sa[i - 1] + k] if sa[i - 1] + k < n else -1))
            )
        rank = tmp[:]
        if rank[sa[-1]] == n - 1:
            break
        k <<= 1
    return sa
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        N = len(word)
        L = N - (numFriends - 1)
        if numFriends == 1:
            return word
        
        suffix = build_suffix(word)
        start_index = suffix[-1]

        result = []
        for i in range(L):
            if i + start_index < N:
                result.append(word[i + start_index])
        return "".join(result)