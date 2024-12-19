class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        current_max = -1
        
        result = 0
        
        for i, n in enumerate(arr):
            current_max = max(n, current_max)
            if current_max == i:
                result += 1
                
        return result