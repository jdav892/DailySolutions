class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        diff = 0
        n = len(nums)
        for i in range(0, n):
            for j in range(1, n):
                if nums[j] - nums[i] > diff and i < j:
                    diff = nums[j] - nums[i]
                else:
                    continue
        
        if diff == 0:
            return -1
        else:
            return diff
        
        #return max(map(sub, nums, accumulate(nums, min))) or -1