class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        streak = []
        count = 0
        last = -10000
        
        for x in nums:
            if x > last:
                count += 1
            else:
                count = 1
                
            last = x
            streak.append(count)
            
        for i in range(k, len(nums)):
            if streak[i] == k and streak[i - k] >= k:
                return True
            if streak[i] >= k * 2:
                return True
        return False