class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        INF = 10 ** 20

        def get_interval(nums):
            zeroes = sum(1 for x in nums if x == 0)

            total = sum(nums)
            mn = total + zeroes

            mx = total
            if zeroes > 0:
                mx = INF
            
            return (mn, mx)

        int1 = get_interval(nums1)
        int2 = get_interval(nums2)

        if int2[1] < int1[0] or int1[1] < int2[0]:
            return -1

        return max(int1[0], int2[0])
    