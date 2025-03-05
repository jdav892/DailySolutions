class Solution:
    def coloredCells(self, n: int) -> int:
        result = 1
        for i in range(n):
            result += (4 * i)
        
        return result
    
    
        """
        return 1 + 2 * (n (n - 1))
        """