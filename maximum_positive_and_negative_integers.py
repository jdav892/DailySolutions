class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = self.binary_search(nums, 0)
        pos = len(nums) - self.binary_search(nums, 1)
        return max(neg, pos)
    
    
    def binary_search(self, nums, target):
        left, right = 0, len(nums) - 1
        result = len(nums)
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                result = mid
                right = mid - 1
        
        return result 