class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = collections.Counter(nums)
        
        for k, v in c.items():
            return max(c, key=c.get)