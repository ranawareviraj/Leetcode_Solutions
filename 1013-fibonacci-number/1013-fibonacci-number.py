class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[0] = 0   # explicit 0 assignment for redability
        dp[1] = 1

        for i in range(2, (n + 1)):
            # Recurrence Relation
            # F(n) = F(n - 1) + F(n - 2), for n > 1
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
