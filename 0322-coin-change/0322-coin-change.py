  
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dp(target):
            if target < 0:
                return -1
            if target == 0:
                return 0
            
            count = math.inf
            for coin in coins:
                new_count = dp(target - coin)
                if new_count != -1:
                    count = min(count, new_count + 1)

            return -1 if (count == math.inf) else count

        return dp(amount)


'''
        dp = [ math.inf ] * (amount + 1)
        dp[0] = 0 

        for i in range(amount + 1):
            for coin in coins:
                coint_count = dp[i] + 1
                if (i + coin) <= amount:
                    dp[i + coin] = min(coint_count, dp[i + coin])
        
        return dp[amount] if (dp[amount] != math.inf) else (-1)
'''