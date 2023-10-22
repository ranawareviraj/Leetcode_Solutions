class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def count_unique_paths(rows, cols, dp):
            if (rows == 0) or (cols == 0):
                return 0
            if (rows == cols == 1):
                return 1
            if dp[rows][cols]:
                return dp[rows][cols]
            result = count_unique_paths(rows - 1, cols, dp) + count_unique_paths(rows, cols - 1, dp)
            dp[rows][cols] = result
            return result
        
        dp = [[0] * (n + 1) for _ in range (m + 1)]
        dp[1][1] = 1
        return count_unique_paths(m, n, dp)