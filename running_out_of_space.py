def spacey(array):
    space = []
    combo = ""
    for word in array:
        combo += word
        space.append(combo)
    return space

    """
    from itertool import accumulate
    def spacey(array):
    return list(accumulate(array))
    """