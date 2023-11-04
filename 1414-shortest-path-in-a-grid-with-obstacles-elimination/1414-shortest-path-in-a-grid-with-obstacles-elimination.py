class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def in_bounds(row, col):
            return (-1 < row < m) and (-1 < col < n)

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])

        seen = [[[False] * (k + 1) for _ in range(n)] for j in range(m)]
        seen[0][0][k] = True

        queue = deque([(0, 0, k)])
        level = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                r, c, obstacles = queue.popleft()
    
                if (r, c) == (m - 1, n - 1):
                    return level 
                
                for dx, dy in directions:
                    nr, nc = r + dy, c + dx
                    if in_bounds(nr, nc):
                        next_obstacles = obstacles - grid[nr][nc] 

                        if (next_obstacles >= 0) and not seen[nr][nc][next_obstacles]:
                            seen[nr][nc][next_obstacles] = True
                            queue.append((nr, nc, next_obstacles))

            level += 1

        return -1