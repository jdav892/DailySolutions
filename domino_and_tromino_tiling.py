class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        @cache
        def get_odd(N):
            if N <= 0:
                return 0
            
            one_vert = get_odd(N - 1)
            tromino = get_even(N - 1)
            
            return (one_vert + tromino) % MOD
        
        @cache 
        def get_even(N):
            if N == 0:
                return 1
            
            if N < 0:
                return 0
            
            one_vert = get_even(N - 1)
            two_hori = get_even(N - 2)
            
            tromino = 2 * get_odd(N - 2)
            
            return(one_vert + two_hori + tromino) % MOD
        
        return get_even(n) % MOD
        