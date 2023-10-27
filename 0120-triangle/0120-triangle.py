class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        def dp(row, col, memo):
            if (row, col) in memo:
                return memo[(row, col)]
            
            min_path_sum = triangle[row][col]
            if row < m - 1:
                min_path_sum += min(dp(row + 1, col, memo), dp(row + 1, col + 1, memo))
            
            memo[(row, col)] = min_path_sum
            return min_path_sum
        
        m = len(triangle)
        return dp(0, 0, {})
