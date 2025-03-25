class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        previous = 0
        
        for start, end in meetings:
            start = max(start, previous + 1)
            length = end - start + 1
            days -= max(length, 0)
            previous = max(previous, end)
        return days