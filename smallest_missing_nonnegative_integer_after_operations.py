class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        f = collections.Counter(n % value for n in nums)
        
        current = 0
        
        while f[current % value] > 0:
            f[current % value] -= 1
            current += 1
            continue
        
        return current