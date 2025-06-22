class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        N = len(s)
        #N % k to determine if there are any fills
        #If there are fills, perform slice, and add fill to last group
        result = [s[i:i+k] for i in range(0, N, k)]
        if len(result[-1]) < k:
                result[-1] += fill * (k - len(result[-1])) 
        return result 
    
    
 