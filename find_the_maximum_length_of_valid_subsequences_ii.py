class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        def subset(c):
            m = collections.Counter()
            
            for x in nums:
                x %= k
                
                m[x] = max(m[x], m[(c - x) % k] + 1)
            return max(m.values())
        
        best = 0
        for i in range(k):
            best = max(best, subset(i))
        return best
                 