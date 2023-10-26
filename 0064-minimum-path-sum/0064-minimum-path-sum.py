class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def dp(m, n, memo):
            if (m == n == 0):
                return grid[m][n]
            if (m, n) in memo:
                return memo[(m, n)]
            
            result = grid[m][n]

            up = dp(m - 1, n, memo) if m > 0 else math.inf
            left = dp(m, n - 1, memo) if n > 0 else math.inf
            memo[(m, n)] = result + min(left, up)
            return memo[(m, n)]

        rows, cols = len(grid), len(grid[0])
        return dp(rows - 1, cols - 1, {})