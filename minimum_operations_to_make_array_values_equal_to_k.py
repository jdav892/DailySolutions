class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(i < k for i in nums):
            return -1
        return (len(set(i for i in nums if i > k)))