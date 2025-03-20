class Solution:
    def longestNiceSubarray(self, nums: List[int]) ->  int:
        result = 0
        current = 0
        l = 0
        for r in range(len(nums)):
            while current & nums[r]:
                current = current ^ nums[l]
                l += 1
            result = max(result, r - l + 1)
            current = current ^ nums[r]
        return result
                