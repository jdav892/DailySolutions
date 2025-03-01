class Solution:
    def applyOperations(self, nums):
        new_list = []

        for i in range(len(nums)):
            if i != len(nums) - 1:
                if nums[i] == nums[i + 1]:
                    nums[i] *= 2
                    nums[i + 1] = 0
            new_list.append(nums[i])
        values = [num for num in new_list if num != 0]
        zeroes = [0] * (len(nums) - len(values))
        result = values + zeroes 
        return result
    