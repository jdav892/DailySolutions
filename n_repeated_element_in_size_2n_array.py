from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        
        numbers = Counter(nums)
        n = len(nums) / 2
        
        for key, value in numbers.items():
            if value == n:
                return key
        return None