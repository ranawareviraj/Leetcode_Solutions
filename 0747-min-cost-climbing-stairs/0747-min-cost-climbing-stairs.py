class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev_one = 0
        prev_two = 0
        n = len(cost)

        for i in range(2, n + 1):
            ans = min(cost[i - 1]+ prev_one, cost[i - 2] + prev_two)
            prev_two, prev_one = prev_one, ans

        return ans
