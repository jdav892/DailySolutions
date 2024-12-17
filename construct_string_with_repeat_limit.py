class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s)
        
        max_heap = [(-ord(c), cnt) for c, cnt, in count.items()]
        heapq.heapify(max_heap)
        
        result = []
        
        while max_heap:
            char, cnt = heapq.heappop(max_heap)
            char = chr(-char) 
            current = min(cnt, repeatLimit)
            result.append(char * current)
            
            if cnt - current > 0 and max_heap:
                next_char, next_count = heapq.heappop(max_heap)
                next_char = chr(-next_char)
                result.append(next_char)
                if next_count > 1:
                    heapq.heappush(max_heap, (-ord(next_char)), next_count - 1)
                    
                heapq.heappush(max_heap, (-ord(char)), cnt - current)
                    
        return "".join(result)