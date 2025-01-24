class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        n = len(graph)
        
        safe = {}
        
        def dfs(i):
            if i in safe:
                return safe[i]

            safe[i] = False
            for nb in graph[i]:
                if not dfs(nb):
                    return safe[i]
            
            safe[i] = True
            return safe[i]
        
        result = []
        
        for i in range(n):
            if dfs(i):
                result.append(i)
        return result