class Solution:
    def findLHS(self, nums: List[int]) -> int:
        result = 0
        vals = collections.Counter(nums)
        
        for i in vals.keys():
            if vals[i] > 0 and vals[i + 1] > 0:
                result = max(result, vals[i] + vals[i + 1])
        return result