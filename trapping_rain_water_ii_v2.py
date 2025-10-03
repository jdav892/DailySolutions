class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        R = len(heightMap)
        C = len(heightMap[0])
        INF = 10 ** 20

        shortest = [[INF] * C for _ in range(R)]
        done = [[False] * C for _ in range(R)]

        h = []
        def enqueue(x, y, height):
            shortest[x][y] = height
            heapq.heappush(h, (height, x, y))

        for i in range(R):
            enqueue(i, 0, heightMap[i][0])
            enqueue(i, C - 1, heightMap[i][C - 1])
        for j in range(C):
            enqueue(0, j, heightMap[0][j])
            enqueue(R - 1, j, heightMap[R- 1][j])

        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        while len(h) > 0:
            height, x, y  = heapq.heappop(h)

            if done[x][y]:
                continue
            
            done[x][y] = True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C and shortest[nx][ny] > max(height, heightMap[nx][ny]):
                    enqueue(nx, ny, max(height, heightMap[nx][ny]))
        
        total = 0
        for i in range(R):
            for j in range(C):
                total += shortest[i][j] - heightMap[i][j]
        return total