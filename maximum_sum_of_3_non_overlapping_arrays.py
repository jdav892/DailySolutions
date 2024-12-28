class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        maximum, result = 0, []

        def backtrack(i , chosen):
            if len(chosen) == 3 or i >= len(nums) - 1:
                nonlocal maximum, result
                current_sum = 0
                for j in chosen:
                    current_sum += sum(nums[j:j+k])
                if current_sum > maximum:
                    maximum = current_sum
                    result = chosen[:]
                return

            chosen.append(i)
            backtrack(i + k, chosen)
            chosen.pop()

            backtrack(i + 1, chosen)

        backtrack(0, [])
        return result