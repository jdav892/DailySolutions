class Solution:
    def soupServings(self, n: int) -> float:
        N = (n + 24) // 25
        
        @cache
        def getPour(A, B):
            if A <= 0 and B <= 0:
                return 0.5
            if A <= 0:
                return 1.0
            if B <= 0:
                return 0.0
            
            return (getPour(A - 4, B) + getPour(A - 3, B - 1) + getPour(A - 2, B - 2) + getPour(A - 1, B - 3)) / 4
        
        if N >= 200:
            return 1.0
        
        return getPour(N, N)