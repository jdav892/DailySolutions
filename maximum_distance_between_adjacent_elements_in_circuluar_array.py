class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diffs = []
        for i in range(len(nums)):
            if i != len(nums) - 1:
                diffs.append(abs(nums[i] - nums[i + 1]))
            else:
                diffs.append(abs(nums[-1] - nums[0]))   
        return max(diffs)
