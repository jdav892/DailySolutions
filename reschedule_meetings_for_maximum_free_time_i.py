class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        INF = 10 ** 20
        startTime = [-INF] + startTime + [eventTime]
        endTime = [0] + endTime + [INF]
        N = len(startTime)

        prefix = [0]
        for i in range(1, N - 1):
            prefix.append(prefix[-1] + (endTime[i] - startTime[i]))

        
        best = 0
        for i in range(1, N - 1):
            if i + k >= N:
                break

            total = startTime[i + k] - endTime[i - 1]
            best = max(best, total - (prefix[i + k - 1] - prefix[i - 1]))
        return best