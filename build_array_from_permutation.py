class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = []
        for i, val in enumerate(nums):
            result.append(nums[val])
        return result