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
        
        # Initialize BFS queue (row, col, level) and set of visited node
        queue = deque([(0, 0, 1)])
        seen = { (0, 0) }

        # BFS
        while queue:
            row, col, level = queue.popleft()

            # If this is bottom-right cell, return level
            if (row, col) == (m - 1, n - 1):
                return level

            # Add neighbors of the current node
            for dx, dy in directions:
                next_row = row + dy
                next_col = col + dx

                if is_valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, level + 1))
            
        return -1