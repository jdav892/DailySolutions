import heapq
class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        
        for i in range(k):
            max_gift = -heapq.heappop(max_heap)
            remaining = int(max_gift**0.5)
            heapq.heappush(max_heap, -remaining)
            
        return -sum(max_heap)