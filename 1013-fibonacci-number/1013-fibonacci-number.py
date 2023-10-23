class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(n + 1):
            if (i + 1) <= (n):
               dp[i + 1] += dp[i] 
            if (i + 2) <= (n):
                dp[i + 2] += dp[i]
        
        return dp[n]