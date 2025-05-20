class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        f = [0] * (N + 1)
        
        for s, e in queries:
            f[s] += 1
            f[e + 1] -= 1
            
        for i in range(1, N + 1):
            f[i] += f[i - 1]
        
        for i in range(N):
            if nums[i] > f[i]:
                return False
        return True