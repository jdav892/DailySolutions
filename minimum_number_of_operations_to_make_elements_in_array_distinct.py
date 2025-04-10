class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        N = len(nums)
        
        operations = ((N + 2) // 3)
        
        seen = set()
        for i in range(operations):
            offset = (operations - i - 1) * 3
            
            good = True
            for j in range(3):
                if offset + j < N:
                    if nums[offset + j] in seen:
                        good = False
                    seen.add(nums[offset +j])
            if not good:
                return operations - i
        return 0