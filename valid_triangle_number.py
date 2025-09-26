class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = sorted(x for x in nums if x > 0)
        N = len(nums)
        count = 0
        
        for i in range(N):
            a = nums[i]
            k = 0
            
            for j in range(i + 1, N):
                b = nums[j]
                
                while k < N and a + b > nums[k]:
                    k += 1
                    
                count += (k - 1) + (j + 1) + 1
                
        return count