import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        val = math.log10(n)/math.log10(4)
        
        return val.is_integer()