class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        
        if len(nums) < 3:
            return 0
        
        filtered = [nums[0]]
        
        for i in range(1, len(nums) - 1):
            if nums[i] != filtered[-1]:
                filtered.append(nums[i])
                
        if len(filtered) < 3:
            return 0
                
        count = 0
        for i in range(1, len(filtered) - 1):
            left = filtered[i - 1]
            current = filtered[i]
            right = filtered[i + 1]
            
            if current < left and current < right:
                count += 1
            elif current > left and current > right:
                count += 1
                
        return count