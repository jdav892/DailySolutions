class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def calculate(edges):
            N = len(edges) + 1
            vals = [None] * N
            
            adj_list = collections.defaultdict(list)
            for u, v in edges:
                adj_list[u].append(v)
                adj_list[v].append(u)
                
            q = collections.deque()
            vals[0] = 0
            q.append(0)
            
            while len(q) > 0:
                current = q.popleft()
                
                for v in adj_list[current]:
                    if vals[v] is None:
                        vals[v] = (vals[current] + 1) % 2
                        q.append(v)
            return vals
        
        g1 = calculate(edges1)
        g2 = calculate(edges2)
        
        f1 = collections.Counter(g1)
        f2 = collections.Counter(g2)
        
        v = max(f2.values())
        
        result = []
        for i in range(len(g1)):
            result.append(f1[g1[i]] + v)
        return result