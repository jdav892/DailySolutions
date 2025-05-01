class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        T = len(tasks)
        W = len(workers)
        tasks.sort()
        workers.sort(reverse=True)
        
        left = 0
        right = min(T, W)
        
        def good(target):
            sl = SortedList(workers[:target])
            used = 0
            for i in range(target):
                if tasks[target - i - 1] <= sl[-1]:
                    sl.remove(sl[-1])
                else:
                    index = sl.bisect_left(tasks[target - i - 1] - strength)
                    if index >= len(sl):
                        return False
                    sl.remove(sl[index])
                    used += 1
                
                if used > pills:
                    return False
            return used <= pills
        while left < right:
            mid = (left + right + 1) // 2
            
            if good(mid):
                left = mid
            else:
                right = mid - 1
        return left