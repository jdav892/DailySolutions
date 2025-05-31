class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        R = len(board)
        C = len(board[0])
        INF = 10 ** 20
        
        arr = []
        for i in range(R - 1, -1, -1):
            for j in range(C):
                nj = j
                if i % 2 == R % 2:
                    nj = C - j - 1
                arr.append(board[i][nj] - 1)
        
        q = collections.deque()
        q.append(0)
        
        distances = [INF] * (R * C)
        distances[0] = 0
        
        while len(q) > 0:
            current = q.popleft()
            
            for i in range(1, 7):
                if current + i < (R * C):
                    nxt = current + i
                
                if distances[nxt] == INF:
                    distances[nxt] = distances[current] + 1
                    q.append(nxt)
                    
        if distances[R * C - 1] >= INF:
            return -1
        return distances[R * C - 1]