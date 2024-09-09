from collections import Counter
def check_three_and_two(array):
    count = Counter(array).values()
    
    return sorted(count) == [2, 3]