class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def find_min_cost(i, cost, dp):
            if i in dp:
                return dp[i]
            if i <= 1:
                return 0
            
            cost = min((find_min_cost(i - 1, cost, dp) + cost[i - 1]), 
                        (find_min_cost(i - 2, cost, dp) + cost[i - 2]))
            dp[i] = cost
            return cost
            
        dp = {}
        return find_min_cost(len(cost), cost, dp)
