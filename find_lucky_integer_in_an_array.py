class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counted = collections.Counter(arr)
        counted_list = [val for val, count in counted.items() if val == count]
        return max(counted_list) if counted_list else -1