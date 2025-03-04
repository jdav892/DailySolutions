class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        i, j = 0, len(nums) - 1
        i2, j2 = 0, len(nums) - 1
        result = [0] * len(nums)
        
        while i < len(nums):
            if nums[i] < pivot:
                result[i2] = nums[i]
                i2 += 1
            if nums[j] > pivot:
                result[j2] = nums[j]
                j2 -= 1
            i, j = i + 1, j - 1
            
        while i2 <= j2:
            result[i2] = result[j2] = pivot
            i2, j2 = i2 + 1, j2 - 1
        return result