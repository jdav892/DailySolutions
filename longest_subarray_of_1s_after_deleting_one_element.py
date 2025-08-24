class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        best = 0
        zero = 0
        left = 0
        
        for right in range(n):
            if nums[right] == 0:
                zero += 1
            
                
            while zero > 1:
                if nums[left] == 0:
                    zero -= 1
                left += 1
                
            best = max(best, right - left) #should actually be right - left + 1 - 1 to include proper bounds
        return best