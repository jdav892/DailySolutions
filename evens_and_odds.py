def evens_and_odds(n):
    if n % 2 == 0:
        return f"{n:0b}"
    else:
        return hex(n)[2:]