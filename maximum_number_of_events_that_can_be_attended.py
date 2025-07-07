class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        INF = 10 ** 20
        event = collections.defaultdict(list)

        for s, e in events:
            event[s].append(e)

        count = 0

        lt = -INF
        h = []

        for t in sorted(event.keys()):
            while len(h) > 0 and lt < t:
                e = heapq.heappop(h)
                if e >= lt:
                    count += 1
                    lt += 1
                else:
                    pass
            lt = t

            for e in event[t]:
                heapq.heappush(h, e)

        t = INF
        while len(h) > 0 and lt < t:
            e = heapq.heappop(h)
            if e >= lt:
                count += 1
                lt += 1

        return count
