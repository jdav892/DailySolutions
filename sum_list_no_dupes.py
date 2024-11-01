from collections import Counter

def sum_no_duplicates(l):
    counts = Counter(list)
    uniques = sum(num for num, count in counts.items() if count == 1)
    return uniques