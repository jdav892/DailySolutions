class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        row_count = [0] * ROWS
        col_count = [0] * ROWS
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1
                    
                    
        count = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] and max(row_count[r], col_count[r]) > 1:
                    count += 1
                    
        return count