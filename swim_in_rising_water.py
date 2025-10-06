class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        INF = 10 ** 20
        R = len(grid)
        C = len(grid[0])

        distance = [[INF] * C for _ in range(R)]
        done = [[False] * C for _ in range(R)]
        h = []

        distance[0][0] = grid[0][0]
        heapq.heappush(h, (distance[0][0], 0, 0))

        directions = [
            (1, 0), (0, 1), (-1, 0), (0, -1) 
        ]

        while len(h) > 0:
            d, x, y = heapq.heappop(h)

            if done[x][y]:
                continue

            done[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C and distance[nx][ny] > max(d, grid[nx][ny]):
                    distance[nx][ny] = max(d, grid[nx][ny])
                    heapq.heappush(h, (distance[nx][ny], nx, ny))

                    if (nx, ny) == (R - 1, C - 1):
                        return distance[nx][ny]
        return (R * C) - 1
