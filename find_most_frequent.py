from collections import Counter
def most_frequent_item_count(collection):
    if not collection:
        return 0
    count = Counter(collection)
    return max(count.values())