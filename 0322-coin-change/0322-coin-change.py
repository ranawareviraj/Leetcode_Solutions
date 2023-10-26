  
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dp(target, memo):
            if target in memo:
                return memo[target]
            if target < 0:
                return -1
            if target == 0:
                return 0
            
            count = -1
            for coin in coins:
                new_count = dp(target - coin, memo)
                if new_count != -1:
                    new_count += 1
                    if count == -1 or new_count < count:
                        count = new_count   
                                 
            memo[target] = count
            return count
        
        memo = {}
        return dp(amount, memo)


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