class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(i, current_sum):
            if i == nums:
                return 1 if current_sum == target else 0
            
            return (
                backtrack(i + 1, current_sum + nums[i])+
                backtrack(i + 1, current_sum - nums[i])
            )
        return backtrack(0, 0)