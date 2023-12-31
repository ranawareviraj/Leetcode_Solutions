class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        points_with_current = points_without_current = 0
        
        dp = [0] * n
        dp[-1] = questions[-1][0]

        for i in range(n - 2, -1, -1):
            points_without_curr = dp[i + 1]

            points_with_curr = questions[i][0]
            j = i + questions[i][1] + 1
            if j < n:
                points_with_curr += dp[j]
            
            dp[i] = max(points_with_curr, points_without_curr)
            
        return dp[0]
        