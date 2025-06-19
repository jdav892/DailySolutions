class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        
        result = []
        for i in range(0, N, 3):
            if nums[i + 2] - nums[i] > k:
                return []
            
            result.append(nums[i:i+3])
        return result