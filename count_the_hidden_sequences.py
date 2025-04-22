class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        current = 0
        high = 0
        low = 0
        for d in differences:
            current += d 
            high = max(high, current)
            low = min(low, current)
        shift = (upper - high)
        low += shift

        return max(low - lower + 1, 0)