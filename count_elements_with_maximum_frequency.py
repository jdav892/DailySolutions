class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        result = []

        for k, v in c.items():
            if v == max(c.values()):
                result.append(v)
        return sum(result)