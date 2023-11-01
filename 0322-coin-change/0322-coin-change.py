  
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1
        dp = [ math.inf ] * (n)
        dp[0] = 0 

        for i in range(n - 1):
            if dp[i] != math.inf:
                coin_count = dp[i] + 1
                for coin in coins:
                    next_amount = i + coin
                    if (next_amount) <= amount:
                        dp[next_amount] = min(dp[next_amount], coin_count)
        
        return dp[amount] if (dp[amount] != math.inf) else (-1)
