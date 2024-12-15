import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        
        pq = []
        
        for p, t in classes:
            heapq.heappush(pq, (p/t - (p + 1)/(t + 1), p, t))
            
        while extraStudents > 0:
            _, p, t = heapq.heappop(pq)
            
            p += 1
            t += 1
            
            heapq.heappush(pq, (p/t - (p + 1)/(t + 1), p, t))
            
            extraStudents -= 1
        
        n = len(classes)
        
        return sum([p/t for _, p, t in pq] / n)