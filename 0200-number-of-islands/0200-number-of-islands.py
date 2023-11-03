class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def is_valid(row, col):
            return (-1 < row < m) and (-1 < col < n) and grid[row][col] == '1'

        def bfs(row, col, visited):
            queue = collections.deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                visited.add((r, c))

                for dx, dy in directions:
                    next_row, nex_col = r + dy, c + dx
                    if is_valid(next_row, nex_col) and (next_row, nex_col) not in visited:
                        queue.append((next_row, nex_col))

        def dfs(row, col, visited):
            stack = [(row, col)]
            while stack:
                r, c = stack.pop()
                visited.add((r, c))

                for dx, dy in directions:
                    next_row, nex_col = r + dy, c + dx
                    if is_valid(next_row, nex_col) and (next_row, nex_col) not in visited:
                        stack.append((next_row, nex_col))

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])

        visited = set()
        connected_components = 0
        for row in range(m):
            for col in range(n):
                if (row, col) not in visited and grid[row][col] == '1':
                    dfs(row, col, visited)
                    connected_components += 1
        
        return connected_components


