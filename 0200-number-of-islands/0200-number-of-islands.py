class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"
        
        def bfs(r, c):
            queue = collections.deque([(r, c)])
            while queue:
                row, col = queue.popleft()
                for dx, dy in directions:
                    next_row, next_col = row + dy, col + dx
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        seen.add((next_row, next_col))
                        queue.append((next_row, next_col))

        m, n = len(grid), len(grid[0])        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        number_of_islands = 0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and (row, col) not in seen:
                    number_of_islands += 1
                    seen.add((row, col))
                    bfs(row, col)
        
        return number_of_islands