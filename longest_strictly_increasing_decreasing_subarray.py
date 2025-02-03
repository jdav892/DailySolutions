class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        current = 1
        result = 1
        increase = 0
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                if increase > 0:
                    current += 1
                else:
                    current = 2
                    increase = 1
            elif nums[i - 1] > nums[i]:
                if increase < 0:
                    current += 1
                else:
                    current = 2
                    increase = -1
            else:
                current = 1
                increase = 0
                
            result = max(result, current)
            
        return result