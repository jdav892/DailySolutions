class Solution:
    def smallestNumber(self, n: int) -> int:
        current = 1
        
        while current < n:
            current = current * 2 + 1
        return current