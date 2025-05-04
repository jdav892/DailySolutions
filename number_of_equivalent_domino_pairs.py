class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        ht = collections.Counter()
        for i, j in dominoes:
            if i > j:
                i, j = j, i
            count += ht[(i, j)]
            ht[(i, j)] += 1
        return count