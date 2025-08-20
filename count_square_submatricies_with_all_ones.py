class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        dp = defaultdict(int)
        result = 0
        
        for r in range(ROWS):
            current = defaultdict(int)
            for c in range(COLS):
                if matrix[r][c]:
                    current[c] += 1 + min(
                        dp[c],
                        current[c - 1],
                        dp[c - 1]
                    )
                    result += current[c]
            dp = current
        return result