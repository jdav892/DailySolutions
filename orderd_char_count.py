from collections import Counter
def ordered_count(inp):
    counter = Counter(inp)
    occurrences = list(counter.items())
    
    return occurrences