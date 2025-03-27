class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        major = 0
        count = 0
        
        for n in nums:
            if count == 0:
                major = n
            if n == major:
                count += 1
            else:
                count -= 1
                
        left = 0
        right = nums.count(major)
        
        for i in range(len(nums)):
            if nums[i] == major:
                left += 1
                right -= 1
            
            left_len = i + 1
            right_len = len(nums) - i - 1
            
            if 2 * left > left_len and 2 * right > right_len:
                return i
        return -1