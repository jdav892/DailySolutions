class Solution:
    def fib(self, n: int, memo={}) -> int:
        if n <= 1:
            return n
        
        if n in memo:
            return memo[n]
        
        memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)
        return memo[n] #Time: O(n), Space: O(n)
    
    
    
    def fib2(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n] #Time: O(n), Space: O(n)
    
    def fib3(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b #Time: O(n), Space: O(1)