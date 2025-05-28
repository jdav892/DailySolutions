class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        INF = 10 ** 20
        def get(edges):
            e = collections.defaultdict(list)
            for u, v in edges:
                e[u].append(v)
                e[v].append(u)
            return e
            
        N1 = len(edges1) + 1
        N2 = len(edges2) + 1

        e1 = get(edges1)
        e2 = get(edges2)

        def calculate(N, e, node, k):
            q = collections.deque()
            q.append(node)

            distances = [INF] * N
            distances[node] = 0

            while len(q) > 0:
                current = q.popleft()

                if distances[current] > k:
                    continue

                for v in e[current]:                                                        
                    if distances[v] > distances[current] + 1:
                        distances[v] = distances[current] + 1
                        q.append(v)
            
            count = 0
            for i in range(N):
                if distances[i] <= k:
                    count += 1
            return count

        best2 = 0
        for node in range(N2):
            best2= max(best2, calculate(N2, e2, node, k - 1))

        answer = []
        for node in range (N1):
            answer.append(calculate(N1, e1, node, k) + best2)
        return answer