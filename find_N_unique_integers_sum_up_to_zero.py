class Solution:
    def sumZero(self, n: int) -> int:
        result = []
        
        if n % 2 != 0:
            result.append[0]
            
        new_nums = n // 2
        
        for i in range(1, new_nums + 1, 1):
           result.append(i) 
           result.append(-i)
        
        return result 
        