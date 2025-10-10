class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        N = len(energy)
        INF = 10 ** 20
        
        @cache
        def f(index):
            if index >= N:
                return 0
            
            return energy[index] + f(index - k)
        
        best = -INF
        for i in range(N):
            best = max(best, f(i))
        return best