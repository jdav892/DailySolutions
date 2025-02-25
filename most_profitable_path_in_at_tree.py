class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
            
        
        times = {}
        def dfs(src, prev, time):
            if src == 0:
                times[src] = time
                return True
            
            for n in adj[src]:
                if n == prev:
                    continue
                if dfs(n, src, time + 1):
                    times[src] = time
                    return True
                
            return False
        dfs(bob, -1, 0)
        
        q = deque([(0, 0, -1, amount[0])])
        result = float("-inf")
        while q:
            node, time, parent, profit = q.popleft()
            
            for n in adj[node]:
                if n == parent:
                    continue
                n_profit = amount[n]
                n_time = time + 1
                if n in times:
                    if n_time > times[n]:
                        n_profit = 0
                    if n_time == times[n]:
                        n_profit = n_profit // 2
                        
                q.append((n, n_time, node, profit + n_profit))
                if len(adj[n]) == 1:
                    result = max(result, profit + n_profit)
        return result