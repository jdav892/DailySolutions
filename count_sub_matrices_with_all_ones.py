class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])

        prefix = [[0] * COLS for _ in range(ROWS + 1)]
        for r in range(ROWS):
            for c in range(COLS):
                prefix[r + 1][c] = prefix[r][c] + mat[r][c]

        def all(r1, r2, c):
            return (prefix[r2 + 1][c] - prefix[r1][c] == (r2 - r1 + 1))

        total = 0

        for r1 in range(ROWS):
            for r2 in range(r1, ROWS):
                count = 0
                streak = 0

                for c in range(COLS):
                    if (prefix[r2 + 1][c] - prefix[r1][c]) == (r2 - r1 + 1):
                        streak += 1

                    else:
                        streak = 0
                
                    count += streak

                total += count

        return total
 
