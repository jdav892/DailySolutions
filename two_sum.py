class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hashmap:
                return i, hashmap[val]
            hashmap[nums[i]] = i