fmin = lambda x, y: x if x < y else y 

class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])

        INF = 10 ** 20

        @cache
        def go(x1, y1, x2, y2, left):
            if left == 0:
                return 0

            if left == 1:
                mxx = mxy = 0
                mnx = mny = INF

                for i in range(x1, x2 + 1):
                    for j in range(y1, y2 + 1):
                        if grid[i][j] == 1:
                            mxx = max(mxx, i)
                            mnx = min(mnx, i)
                            mxy = max(mxy, j)
                            mny = min(mny, j)

                if mnx == INF:
                    return 0

                return (mxx - mnx + 1) * (mxy - mny + 1)

            best = INF

            for t in range(1, left):
                for i in range(x1, x2 + 1):
                    best = fmin(best, go(x1, y1, i, y2, t) + go(i + 1, y1, x2, y2, left - t))

            for t in range(1, left):
                for i in range(y1, y2 + 1):
                    best = fmin(best, go(x1, y1, x2, i, t) + go(x1, i + 1, x2, y2, left - t))
            return best

        return go(0, 0, ROWS - 1, COLS - 1, 3)