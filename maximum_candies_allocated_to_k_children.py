class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0
        
        l, r = 1, sum(candies) // k
        result = 0
        
        while l <= r:
            m = (l + r) // 2
            count = 0
            
            for c in candies:
                if c >= m:
                    count += c // m
                if count >= k:
                    break
            if count >= k:
                result = m
                l = m + 1
            else:
                r = m - 1
        return result
    
    #O(1), O(n)