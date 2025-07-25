class Solution:
    def maxSum(self, nums: List[int]) -> int:
        new_nums = list(set(x for x in nums if x > 0))
        if len(new_nums) == 0:
            return max(nums)
        return sum(new_nums)