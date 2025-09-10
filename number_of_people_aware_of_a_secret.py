class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10 ** 9 + 7
        
        dp = [0] * forget
        dp[forget - 1] = 1
        
        for _ in range(n - 1):
            ndp = [0] * forget
            
            for i in range(1, forget - delay + 1):
                ndp[forget - 1] += dp[i]
                
            for i in range(forget - 1):
                ndp[i] += dp[i + 1]
                
            for i in range(forget):
                ndp[i] %= MOD
        
        return sum(dp) %  MOD