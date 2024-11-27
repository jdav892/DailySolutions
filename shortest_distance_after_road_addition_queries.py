class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i + 1] for i in range(n)]
        
        def shortest_path():
            q = deque()
            q.append((0, 0))
            visit = set()
            visit.add((0, 0))
        
            while q:
                curr, length = q.popleft()
                if curr == n - 1:
                    return length
                for neighbor in adj[curr]:
                    if neighbor not in visit:
                        q.append((neighbor, length + 1))
                        visit.add(neighbor)
            
        
        res = []
        for src, dest, in queries:
            adj[src].append(dest)
            res.append(shortest_path())
        return res