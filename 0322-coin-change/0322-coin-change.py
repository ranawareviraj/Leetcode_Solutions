class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [ None ] * (amount + 1)
        dp[0] = [[]] # [[], None, None, None]
        # [1,2,5]

        for i in range(amount + 1):
            if dp[i] != None:
                for coin in coins:
                    new_combination = dp[i][:]
                    new_combination.append(coin)
                    if (i + coin) <= amount:
                        if dp[i + coin] == None:
                            dp[i + coin] = new_combination
                        elif len(new_combination) < len(dp[i + coin]):
                            dp[i + coin] = new_combination
        
        return len(dp[amount]) - 1 if dp[amount] != None else (-1)

