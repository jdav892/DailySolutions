class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        line = [0] * (len(nums) + 1)
        decrement = 0
        result = 0
        
        for i, num in enumerate(nums):
            while decrement + line[i] < num:
                if result == len(queries):
                    return -1
                
                l, r, val = queries[result]
                result += 1
                if r < i:
                    continue
                line[max(l, i)] += val
                line[r + 1] -= val
            decrement += line[i]
        return result