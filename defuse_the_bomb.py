class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
    ##    N = len(code)
    ##    
    ##    res = [0] * N
    ##    
    ##    for i in range(N):
    ##        if k > 0:
    ##            for j in range(i + 1, i + 1 + k):
    ##                res[i] += code[j % N]
    ##        elif k < 0:
    ##            for j in range(i - 1, i - 1 - abs(k), -1):
    ##                res[i] += code[j % N]
    ##
    ##    return res
    
        N = len(code)
        res = [0] * N
        
        l = 0
        current = 0
        for i in range(N + abs(k)):
            current += code[i % N]
            
            if i - l + 1 > abs(k):
                current -= code[l % N]
                l = (l + 1) % N
            
            if i - l + 1 == abs(k):
                if k > 0:
                    res[(l - 1) % N] = current
                elif k < 0:
                    res[(i + 1) % N] = current    
            
        return res