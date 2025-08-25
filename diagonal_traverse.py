class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS = len(mat)
        COLS = len(mat[0])
        
        ND = ROWS + COLS - 1
        
        result = []
        
        for d in range(ND):
            if d % 2 == 0:
                for y in range(max(0, d - ROWS + 1), min(d + 1, COLS)):
                    x = d - y
                    result.append(mat[x][y])
                    
            else:
                for x in range(max(0, d - COLS + 1), min(d + 1, ROWS)):
                    y = d - x
                    result.append(mat[x][y])
                    
        return result