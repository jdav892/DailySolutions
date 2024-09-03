def last_survivor(letters, coords):
    for coord in coords:
        letters = letters[:coord] + letters[coord + 1:]
    return letters