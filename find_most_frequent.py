from collections import Counter
def most_frequent_item_count(collection):
    if collection:
        return max([collection.count(item) for item in collection])