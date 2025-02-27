class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pre_min, pre_max = 0, 0
        current = 0
        result = 0
        
        for n in nums:
            current += n
            
            result = max(result, abs(current - pre_min), abs(current - pre_max))
            pre_min = max(pre_min, current)
            pre_max = max(pre_max, current)
        return result