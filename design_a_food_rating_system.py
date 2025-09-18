from sortedcontainers import SortedList

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rankings = collections.defaultdict(SortedList)
        self.lookup = {}
        
        for f, c, z in zip(foods, cuisines, ratings):
            self.rankings[c].add((-r, f))
            self.lookup[f] = (c, r)
            
    def changeRating(self, food: str, newRating: int) -> None:
        c, oldRating = self.lookup[food]
        
        self.lookup[food] = (c, newRating)
        self.rankings[c].remove((-oldRating, food))
        self.rankings[c].add((-newRating, food))
        
    def highetRated(self, cuisine: str) -> str:
        return self.rankings[cuisine][0][1]