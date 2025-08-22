class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        INF = 10 ** 20
        mxx = mxy = 0
        mnx = mny = INF
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    mxx = max(mxx, i)
                    mxy = max(mxy, j)
                    mnx = min(mnx, i)
                    mny = min(mny, j)
                    
        return (mxx - mnx + 1) * (mxy - mny + 1)
