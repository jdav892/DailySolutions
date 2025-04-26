class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        N = len(nums)
        
        prev = collections.Counter()
        prev[0] = 1
        total = 0
        current = 0
        
        for i in range(N):
            if nums[i] % modulo == k:
                current += 1
            total += prev[(current - k) % modulo]
            prev[current % modulo] += 1
        return total