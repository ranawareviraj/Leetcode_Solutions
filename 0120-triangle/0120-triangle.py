class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def dp(index, row, grid, memo):
            if (index, row) in memo:
                return memo[(index, row)]
            if row == 0:
                return grid[0][0]
            if index < 0:
                return math.inf
            
            up = dp(index, row - 1, grid, memo)
            diagonal = dp(index - 1, row - 1, grid, memo)

            memo[(index, row)] = grid[row][index] + min(up, diagonal)
            return memo[(index, row)]

        m = len(triangle)
        n = len(triangle[m - 1])
        grid = [[math.inf] * n for _ in range(m)]
        
        for row in range(m):
            for col in range(len(triangle[row])):
                grid[row][col] = triangle[row][col]
        
        ans = math.inf
        for index in range(n):
            ans = min(ans, dp(index, m - 1, grid, {}))
        return ans

'''
[
    [2],       [0][0]
    [3,4],     [1][0], [1][1]    
    [6,5,7],   [2][0], [2][1], [2][2]
    [4,1,8,3]  [3][0]
]

[
    [inf, inf, inf, inf], 
    [inf, inf, inf, inf], 
    inf, inf, inf, inf], 
    [inf, inf, inf, inf]]

[
    [2, inf, inf, inf], 
    [3, 4, inf, inf], 
    [6, 5, 7, inf], 
    [4, 1, 8, 3]]
'''