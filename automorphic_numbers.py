def automorphic(n):
    square = n**2
    if str(square).endswith(str(n)):
        return "Automorphic"
    else:
        return "Not!!"
    