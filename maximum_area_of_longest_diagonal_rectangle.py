class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0
        max_area = 0
        
        for w, h in dimensions:
            d = w ** 2 + h ** 2
            if d > max_diag:
                max_diag = d
                max_area = w * h
            elif d == max_diag and max_area < w * h:
                max_area = w * h
        return max_area