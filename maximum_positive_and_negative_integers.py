class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive = []
        negative = []

        for num in nums:
            if num < 0:
                negative.append(num)
            elif num > 0:
                positive.append(num)
            else:
                continue
        
        result = max(len(negative), len(positive))
        return result