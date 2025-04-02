class Solution:
    def maximumTripletValue(self, nums:List[int]) -> int:
        result = 0
        N = len(nums)
        left = nums[0]
        for j in range(1, N):
            if nums[j] > left:
                left = nums[j]
                continue
            for k in range(j + 1, N):
                result = max(result, (left - nums[j]) * nums[k])
        return result