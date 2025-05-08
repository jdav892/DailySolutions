class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        R = len(moveTime)
        C = len(moveTime[0])
        INF = 10 ** 20

        h = []
        heapq.heappush(h, (0, 0, 0))
        best = [[INF] * C for _ in range(R)]
        best[0][0]

        dirs = [
            (1,0), (0, 1), (-1, 0), (0, -1)
        ]

        while len(h) > 0:
            d, x, y = heapq.heappop(h)

            if best[x][y] < d:
                continue

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                p = 2 - ((nx + ny) % 2)

                if 0 <= nx < R and 0 <= ny < C and best[nx][ny] > max(d, moveTime[nx][ny]) + p:
                    best[nx][ny] = max(d, moveTime[nx][ny]) + p
                    heapq.heappush(h, (best[nx][ny], nx, ny))

        return best[R - 1][C - 1]