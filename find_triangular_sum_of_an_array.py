class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        current = nums[:]
        
        while len(current) > 1:
            nxt = []
            for x, y in zip(current, current[1:]):
                nxt.append((x + y) % 10)
            current = nxt
        return current[0]