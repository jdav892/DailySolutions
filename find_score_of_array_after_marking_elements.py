class Solution:
    def findScore(self, nums: List[int]) -> int:
        marked = {}
        score = 0
        indices = sorted(range(len(nums)), key=lambda x: nums[x])
        
        for idx in indices:
            if idx not in marked:
                score += nums[idx]
                marked[idx] = True
                if idx > 0:
                    marked[idx - 1] = True
                if idx < len(nums) - 1:
                    marked[idx + 1] = True
                    
        return score 