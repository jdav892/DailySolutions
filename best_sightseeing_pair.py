class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        score = 0
        
        current = values[0] - 1
        
        for i in range(1, len(values)):
            score = max(score, values[i] + current)
            current = max(current - 1, values[i] - 1)
            
        return score