class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        q = collections.deque(sorted(queries))
        
        good = []
        current = []
        
        count = 0
        for index, x in enumerate(nums):
            while len(q) > 0 and q[0][0] <= index:
                heapq.heappush(good, -q[0][1])
                q.popleft()
                
            while len(current) > 0:
                if current[0] < index:
                    heapq.heappush(current)
                else:
                    break
            
            while len(current) < x:
                if len(good) == 0:
                    return -1
                
                r = -heapq.heappop(good)
                if r < index:
                    continue
                heapq.heappush(current, r)
                count += 1
        return len(queries) - count