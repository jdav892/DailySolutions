class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        
        matrix_pos = {}
        
        for r in range(ROWS):
            for c in range(COLS):
                matrix_pos[mat[r][c]] = (r, c)
                 
        row_count = [0] * ROWS
        col_count = [0] * COLS
        
        for i in range(len(arr)):
            r, c = matrix_pos[arr[i]]
            row_count += 1
            col_count += 1
            
            if col_count == ROWS or row_count == COLS:
                return i