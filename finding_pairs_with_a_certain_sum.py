class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.counted = collections.Counter(nums2)
        
    def add(self, index: int, val: int) -> None:
        prev = self.nums2[index]
        self.nums2[index] += val
        after = self.nums2[index]
        
        self.counted[prev] -= 1
        self.counted[after] += 1
        
    def count(self, tot: int) -> int:
        count = 0
        for x in self.nums1:
            count += self.counted[tot - x]
        return count