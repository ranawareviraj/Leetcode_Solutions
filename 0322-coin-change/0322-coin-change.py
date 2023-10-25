class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [ math.inf ] * (amount + 1)
        dp[0] = 0 

        for i in range(amount + 1):
            for coin in coins:
                coint_count = dp[i] + 1
                if (i + coin) <= amount:
                    dp[i + coin] = min(coint_count, dp[i + coin])
        
        return dp[amount] if (dp[amount] != math.inf) else (-1)
