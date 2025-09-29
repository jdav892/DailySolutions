class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        INF = 10 ** 20
        
        @cache
        def f(left, right):
            points = right - left + 1
            
            if points <= 2:
                return 0
            
            if points == 3:
                return values[left] * values[left + 1] * values[left + 2]
            
            best = INF
            
            for mid in range(left + 1, right):
                best = min(best, values[left] * values[right] * values[mid] + f(left, mid) + f(mid, right))
            
            return best
        return f(0, N - 1)
            