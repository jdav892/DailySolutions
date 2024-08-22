def pythagorean_triple(integers):
    new = sorted(integers)
    a = new[0]
    b = new[1]
    c = new[2]
    
    if a**2 + b**2 == c**2:
        return True
    else:
        return False