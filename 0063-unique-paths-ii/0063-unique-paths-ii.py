class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if (obstacleGrid[m - 1][n - 1] == 1) or (obstacleGrid[0][0] == 1):
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                if (row + 1) < m and obstacleGrid[row + 1][col] != 1:
                    dp[row + 1][col] += dp[row][col]
                if (col + 1) < n and obstacleGrid[row][col + 1] != 1:
                    dp[row][col + 1] += dp[row][col]
        
        return dp[m-1][n-1]



        