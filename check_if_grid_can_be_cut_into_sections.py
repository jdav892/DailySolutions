class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x = [(r[0], r[2]) for r in rectangles]
        y = [(r[1], r[3]) for r in rectangles]
        
        x.sort()
        y.sort()
        
        def count_non_overlaps(intervals):
            count = 0
            previous_end = -1
            for start, end in intervals:
                if previous_end <= start:
                    count += 1
                previous_end = max(previous_end, end)
            return count
        
        return max(
            count_non_overlaps(x),
            count_non_overlaps(y)
        ) >= 3
            
                    