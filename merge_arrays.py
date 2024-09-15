def merge_arrays(first, second):
    merged = set(first).union(second)
    return sorted(merged)