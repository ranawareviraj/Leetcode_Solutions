class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def count_unique_paths(rows, cols, dp):
            if (rows == 0) or (cols == 0):
                return 0
            if (rows == cols == 1):
                return 1
            if dp[rows - 1][cols - 1]:
                return dp[rows - 1][cols - 1]
            result = count_unique_paths(rows - 1, cols, dp) + count_unique_paths(rows, cols - 1, dp)
            dp[rows - 1][cols - 1] = result
            return result
        
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        return count_unique_paths(m, n, dp)