class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        result = [-1] * len(queries)
        groups = defaultdict(list)
        
        for i, query in enumerate(queries):
            left, right = sorted(query)
            
            if left == right or heights[right] > heights[left]:
                result[i] = right
            
            else:
                height = max(heights[left], heights[right])
                groups[right].append((height, i))
                
        
        min_heap = []
        for i, height in enumerate(heights):
            for q_h, q_i in groups[i]:
                heapq.heappush(min_heap, (q_h, q_i))
                
            while min_heap and height > min_heap[0][0]:
                q_h, q_i = heapq.heappop(min_heap)
                result[q_i] = i
                
        return result   