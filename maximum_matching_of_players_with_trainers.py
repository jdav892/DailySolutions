class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        players = collections.deque(players)
        trainers.sort(reverse=True)
        
        c = 0
        for t in trainers:
            while len(players) > 0 and players[0] > t:
                players.popleft()
            if len(players) > 0 and players[0] <= t:
                c += 1
                players.popleft()
        return c