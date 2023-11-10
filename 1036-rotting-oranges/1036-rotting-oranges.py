class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def is_valid(r, c):
            return (0 <= r < m) and (0 <= c < n) and grid[r][c] == 1

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        seen = set()

        m, n = len(grid), len(grid[0])
        fresh_oranges = 0
        queue = deque()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                if grid[row][col] == 2:
                    queue.append((row, col))
                    seen.add((row, col))
        
        minutes = 0
        while queue:
            level_size = len(queue)
            is_infected = False

            for _ in range(level_size):
                row, col = queue.popleft()
                
                for dx, dy in directions:
                    next_row, next_col = row + dy, col + dx
                    if is_valid(next_row, next_col) and (next_row, next_col) not in seen:
                        # There might be no infected oranges in current round
                        # Use is_infected flag to increment minutes if we add new oranges in this round 
                        is_infected = True
                        fresh_oranges -= 1
                        queue.append((next_row, next_col))
                        seen.add((next_row, next_col))

            if is_infected:
                minutes += 1
        
        return minutes if fresh_oranges == 0 else -1