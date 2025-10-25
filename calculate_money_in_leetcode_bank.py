class Solution:
    def totalMoney(self, n: int) -> int:
        
        full = n // 7
        total = 28 * full + (7 * (full - 1) * (full - 1 + 1)) // 2
        
        leftover = n % 7
        total += leftover * full + (leftover * (leftover + 1)) // 2
        
        return total