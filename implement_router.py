from sortedcontainers import SortedList

class Router:
    
    def __init__(self, memoryLimit: int):
        self.sl = collections.deque()
        self.sl_by_dest = collections.defaultdict(SortedList)
        self.limit = memoryLimit
        
    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (timestamp, source) in self.sl_by_dest[destination]:
            return False
        
        self.sl.append((timestamp, source, destination))
        self.sl_by_dest[destination].add((timestamp, source))
        
        if len(self.sl) > self.limit:
            ts, src, dest = self.sl[0]
            self.sl.popleft()
            self.sl_by_dest[dest].remove((ts, src))
            
        return True
    
    def forwardPacket(self) -> List[int]:
        if len(self.sl) == 0:
            return []
        
        timestamp, source, destination = self.sl.popleft()
        self.sl_by_dest[destination].remove((timestamp, source))
        
        return [source, destination, timestamp]
    
    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        left = self.sl_by_dest[destination].bisect_left((startTime,))
        right = self.sl_by_dest[destination].bisect_right((endTime + 1,))
        
        return right - left