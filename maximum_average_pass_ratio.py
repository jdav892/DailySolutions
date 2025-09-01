class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        n = len(classes)
        s = extraStudents
        
        def insert(p, t):
            gains = ((p + 1) / (t + 1) - (p / t))
            heapq.heappush(h, (-gains, p, t))
            
        
        h = []
        for p, t in classes:
            insert(p, t)
            
        for _ in range(s):
            _, p, t = heapq.heappop(h)
            insert(p + 1, t + 1)
            
        total = 0
        for _, p, t in h:
            total += (p / t)
            
        return total / n
            
            