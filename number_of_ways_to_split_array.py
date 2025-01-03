class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count = 0
        sumNums = sum(nums)
        init_sum = 0
        for i in range(len(nums) - 1):
            init_sum += nums[i]
            comp_sum = sumNums - init_sum
            if init_sum >= comp_sum:
                count += 1
        return count