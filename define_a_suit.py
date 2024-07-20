def define_suit(card):
    spade_check = "S"
    diamond_check = "D"
    heart_check = "H"
    club_check = "C"
    for char in card:
        if spade_check in char:
            return "spades"
        elif diamond_check in char:
            return "diamonds"
        elif heart_check in char:
            return "hearts"
        elif club_check in char: 
            return "clubs"
        
# d = {'C': 'clubs', 'S':'spades', 'D':'diamonds','H':'hearts'}
#    return d[card[-1]]
        