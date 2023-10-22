from collections import defaultdict

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def count_unique_paths(rows, cols, dp):
            if (rows == 0) or (cols == 0):
                return 0
            if (rows == cols == 1):
                return 1
            key = str(rows) + "-" + str(cols)
            if dp[key]:
                return dp[key]

            result = count_unique_paths(rows - 1, cols, dp) + count_unique_paths(rows, cols - 1, dp)
            dp[key] = result
            return result
        
        dp = defaultdict(str)
        dp[("1-1")] = 1
        return count_unique_paths(m, n, dp)