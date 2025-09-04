class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_diff = abs(z - x)
        y_diff = abs(z - y)
        
        if x_diff < y_diff:
            return 1
        elif y_diff < x_diff:
            return 2
        else:
            return 0