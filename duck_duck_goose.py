def duck_duck_goose(players, goose):
    for i in range(len(players)):
        if (goose - 1) % len(players) == i:
            return players[i].name