class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        op = 0
        for n in nums: 
            op ^= n
        
        sub = (1 << maximumBit) - 1
        answer = []
        for n in reversed(nums):
            answer.append(op ^ sub)
            op ^= n
        return answer