class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        def is_valid(row, col):
            return (-1 < row < m) and (-1 < col < n) and (grid[row][col] == 0)

        # Base case: If start val is 1, we can't reach the end
        if grid[0][0] == 1:
            return -1
        
        m = len(grid)
        n = len(grid[0])
        # Possible neighbors if they in bounds
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, 1), (1, -1), (-1, -1), (1, 1)]
        
        # Initialize BFS queue and set of visited node
        queue = deque([(0, 0)])
        seen = [ [False] * n for _ in range(m)]
        seen[0][0] = True
        level = 0

        # BFS
        while queue:
            level += 1
            level_size = len(queue)
            for _ in range(level_size):
                row, col = queue.popleft()

                if (row, col) == (m - 1, n - 1):
                    return level

                for dx, dy in directions:
                    next_row = row + dy
                    next_col = col + dx

                    if is_valid(next_row, next_col) and not seen[next_row][next_col]:
                        seen[next_row][next_col] = True
                        queue.append((next_row, next_col))
            
        return -1