class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        evens = (((n + 1) // 2) * (m // 2))
        odds = (n // 2) * ((m + 1) // 2)
        
        return evens + odds