class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi = max(nums)
        
        streak = 0
        high = 0
        for x in nums:
            if x == maxi:
                streak += 1
            else:
                streak = 0
            
            high = max(high, streak)
        return high