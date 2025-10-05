class Solution:
    def maxArea(self, height: List[int]) -> int:
        total = 0
        left = 0
        right = len(height) - 1
        
        total = (right - left) * min(height[left], height[right])
        
        while left < right:
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            total = max(total, (right - left) * min(height[left], height[right]))
        return total