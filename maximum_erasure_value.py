class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = set()
        l = 0
        current = 0
        maximum = 0
        
        for r in range(len(nums)):
            while nums[r] in seen:
                seen.remove(nums[l])
                current -= nums[l]
                l += 1
            seen.add(nums[r])
            current += nums[r]
            maximum = max(maximum, current)
        return maximum
 


