class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(i, cost, memo):
            if i in memo:
                return memo[i]
            if i <= 1:
                return 0
            
            cost = min((dp(i - 1, cost, memo) + cost[i - 1]), (dp(i - 2, cost, memo) + cost[i - 2]))
            memo[i] = cost
            return cost
            
        memo = {}
        return dp(len(cost), cost, memo)
