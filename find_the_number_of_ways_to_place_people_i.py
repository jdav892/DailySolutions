class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        N = len(points)
        count = 0
        
        for i in range(N):
            ax, ay = points[i]
            for j in range(N):
                if i == j:
                    continue
                
                bx, by = points[j]
                
                if not by >= ay and ax >= bx:
                    continue
                
                found = False
                for k in range(N):
                    if k == i or k == j:
                        continue
                    
                    cx, cy = points[k]
                    if bx <= cx <= ax and by >= cy >= ay:
                        found = True
                if not found:
                    count += 1
                    
        return count