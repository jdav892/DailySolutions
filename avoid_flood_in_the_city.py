from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        N = len(rains)

        result = [-1] * N
        full = {}

        dry_indices = SortedList() 

        for index, lake in enumerate(rains):
            if lake == 0:
                dry_indices.add(index)
                continue
            
            if lake not in full:
                full[lake] = index
                continue

            sindex = dry_indices.bisect_left(full[lake])

            if sindex >= len(dry_indices):
                return []

            dry_day = dry_indices[sindex]
            result[dry_day] = lake
            dry_indices.remove(dry_day)
            full[lake] = index

        for x in dry_indices:
            result[x] = 100
        return result

