class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        for d in range(-(COLS - 1), ROWS):
            arr = []
            for x in range(max(d, 0), min(ROWS, COLS + d)):
                y = x - d
                arr.append(grid[x][y])
                
                arr.sort(reverse=(not d < 0))
                
            for i, x in enumerate(range(max(d ,0), min(ROWS, COLS + d))):
                y = x - d
                grid[x][y] = arr[i]
                
        return grid