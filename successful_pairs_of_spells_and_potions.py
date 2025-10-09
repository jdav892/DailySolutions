class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        P = len(potions)
        potions.sort()
        
        result = []
        for s in spells:
            index = bisect.bisect_left(potions, True, key=lambda p: p * s >= success)
            result.append(P - index)
        return result 