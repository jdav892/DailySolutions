class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        cons = len(set(nums))
        count = 0
        
        for i in range(N):
            s = set()
            
            for j in range(i, N):
                s.add(nums[j])
                
                if len(s) == cons:
                    count += 1
                elif len(s) > cons:
                    break
        return count