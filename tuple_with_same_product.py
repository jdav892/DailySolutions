class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        vals = defaultdict(int)
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                vals[product] += 1
                
        result = 0
        
        for c in vals.values():
            pairs = (c * (c - 1)) // 2
            result = 8 * pairs
            
        return result