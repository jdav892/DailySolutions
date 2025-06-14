class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        
        def get_number_pairs(target):
            N = len(nums)
            
            pairs = 0
            i = 0
            while i + 1 < N:
                if nums[i + 1] - nums[i] <= target:
                    pairs += 1
                    i += 2
                else:
                    i += 1
            return pairs
        
        left = 0
        right = nums[-1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            
            if get_number_pairs(mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left