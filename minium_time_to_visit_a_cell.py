class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if min(grid[0][1], grid[1][0]) > 1:
            return -1
        
        
        min_heap = [(0, 0, 0)]
        
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        
        while min_heap:
            x, y, z = heapq.heappop(min_heap)
            
            if (y, z) == (ROWS - 1, COLS - 1):
                return x
            
            neighbor = [(y + 1, z), (y - 1, z), (y, z + 1), (y, z - 1)]
            for new_y, new_z in neighbor:
                if new_y < 0 or new_z < 0 or new_y == ROWS or new_z == COLS or (new_y, new_z) in visit:
                    continue
                wait = 0
                if abs(grid[new_y][new_z] - t) % 2 == 0:
                    wait = 1
                n_time = max(grid[new_y][new_z] + wait, x + 1)
                heapq.heappush(min_heap,(n_time,new_y, new_z))
                visit.add((new_y, new_z))
                