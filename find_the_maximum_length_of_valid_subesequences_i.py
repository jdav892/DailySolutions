class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        N = len(nums)
        
        m = collections.Counter()
        for x in nums:
            x %= 2
            m[x] = m[x] + 1
            
        g = max(m.values())
        
        m = collections.Counter()
        for x in nums:
            x %= 2
            m[x] = m[1 - x] + 1
            
        return max(max(m.values()), g)