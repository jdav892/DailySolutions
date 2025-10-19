class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        INF = 10 ** 20
        nums.sort()
        
        count = 0
        next_avail = INF
        
        for x in nums:
            if x - k >= next_avail:
                next_avail = x - k + 1
                count += 1
                continue
            
            if x - k < next_avail <= x + k:
                next_avail += 1
                count += 1
                
        return count