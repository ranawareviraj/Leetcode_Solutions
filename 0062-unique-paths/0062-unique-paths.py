class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Base condition: Fill first column and first row of dp with 1
        dp = [[0] * n for i in range(m)]
        dp[0][0] = 1

        for row in range(m):
            for col in range(n):
                if (row + 1 < m):
                    dp[row + 1][col] += dp[row][col]
                if (col + 1 < n):
                    dp[row][col + 1] += dp[row][col]
                
        return dp[m - 1][n - 1]