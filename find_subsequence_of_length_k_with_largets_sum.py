class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums2 = sorted(list((x, i) for i, x in enumerate(nums)), reverse=True)[:k]
        nums3 = sorted(list((i, x) for x, i in nums2))
        nums4 = list(x for i, x in nums3)

        return nums4