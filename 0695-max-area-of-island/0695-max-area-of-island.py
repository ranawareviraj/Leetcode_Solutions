class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: 
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        
        def is_valid(row, col):
            return row in range(rows) and col in range(cols) and grid[row][col] and (row, col) not in visited

        def bfs(row, column):
            queue = collections.deque()
            queue.append((row, column))
            visited.add((row, column))
            area = 1
            while queue: 
                current_row, current_column = queue.pop()
                for dx, dy in directions:
                    next_row, next_col = current_row + dy, current_column + dx
                    if is_valid(next_row, next_col):
                        queue.append((next_row, next_col))
                        visited.add((next_row, next_col))
                        area += 1
            return area
                
        visited = set()
        max_area = 0
        for row in range(rows):
            for column in range(cols):
                if grid[row][column] == 1 and (row, column) not in visited:
                    max_area = max(max_area, bfs(row, column))
                    
        return max_area