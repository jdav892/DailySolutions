def largest(n, xs):
    if n == 0:
        return []
    else: 
        return sorted(xs)[-n:]