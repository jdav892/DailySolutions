from collections import Counter

def dominator(arr):
    if not arr:
        return -1
    
    counts = Counter(arr)
    max_key = max(counts, key=counts.get)
    if counts[max_key] > len[arr] // 2:
        return max_key
    return -1
    