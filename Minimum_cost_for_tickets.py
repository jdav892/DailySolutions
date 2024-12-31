class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dp = { len(days): 0}
        
        def bt(i):
            if i in dp:
                return dp[i]
            
            dp[i] = float("inf")
            j = i
            for cost, duration in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + duration:
                    j += 1
                dp[i] = min(dp[i], cost + bt(j))
            
            return dp[i]
        return bt(0)