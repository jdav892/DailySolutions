class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        numbers = sorted(set(arr))
        
        rank = {num:i + 1 for i, num in enumerate(numbers)}
        
        return [rank[num] for num in arr]