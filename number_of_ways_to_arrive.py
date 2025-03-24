class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        a = defaultdict(list)
        for u, v, w in roads:
            a[v].append((w, u))
            a[u].append((w, v))
        
        MOD = 10**9 + 7
        min_heap = [(0, 0)]
        min_cost = [float("inf")] * n
        path_count = [0] * n
        path_count[0] = 1

        while min_heap:
            cost, node = heappop(min_heap)

            for n_cost, neighbor in a[node]:
                if cost + n_cost < min_cost[neighbor]:
                    min_cost[neighbor] = cost + n_cost
                    path_count[neighbor] = path_count[node]
                    heappush(min_heap, (cost + n_cost , neighbor))
                elif cost + n_cost == min_cost[neighbor]:
                    path_count[neighbor] = (path_count[neighbor] + path_count[node]) % MOD
        return path_count[n - 1]
