class Solution:
    def numOfSubArrays(self, arr: List[int]) -> int:
        current = 0
        odd = 0
        even = 0
        result = 0
        MOD = 10**9 + 7
        
        for n in arr:
            current += n
            
            if current % 2 != 0:
                result = (result + 1 + even) % MOD
                odd += 1
            else:
                result = (result + odd) % MOD
                even += 1
                
        return result