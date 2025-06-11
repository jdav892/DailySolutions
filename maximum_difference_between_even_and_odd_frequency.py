class Solution:
    def maxDifference(self, s: str) -> int:
        letters = collections.Counter(s)
        sorted_vals = sorted(letters.values(), reverse=True)

        even = [x for x in sorted_vals if x % 2 == 0]
        odd = [x for x in sorted_vals if x % 2 != 0]

        return max(odd) - min(even)
       