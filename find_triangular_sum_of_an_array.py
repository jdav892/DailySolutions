class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        result = nums[:]
        
        while len(result) > 1:
            new = []
            for x, y in zip(current, current[1:]):
                new.append((x + y) % 10)
            current = new
        return current[0]