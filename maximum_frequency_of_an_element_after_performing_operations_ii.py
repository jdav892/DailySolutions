class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        N = len(nums)
        nums.sort()
        best = 0
        
        f = collections.Counter(nums)

        for current in nums:
            for x in [current, current + k, current - k]:
                left = bisect.bisect_left(nums, x - k)
                right = bisect.bisect_right(nums, x + k)

                count = right - left
                best = max(best, f[x] + min(numOperations, count - f[x]))
        return best