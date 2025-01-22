class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        q = deque()
        result = [[-1] * COLS for _ in range(ROWS)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c]:
                    q.append((r, c))
                    result[r][c] = 0
                    
        
        while q:
            r, c = q.popleft()
            h = result[r][c]
            
            adj = [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]
            
            for ar, ac in adj:
                if (ar < 0 or ac < 0 or ar == ROWS or ac == COLS or result[ar][ac] != -1):
                    continue
                q.append((ar, ac))
                result[ar][ac] = h + 1
            
        return result