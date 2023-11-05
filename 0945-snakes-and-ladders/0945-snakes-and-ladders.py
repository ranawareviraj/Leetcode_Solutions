class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        no_of_positions = n * n
        
        positions = [ -1 ] * (no_of_positions + 1)
        position = 1
        columns = [ col for col in range(n)]
        for row in range(n - 1, -1, -1):
            for col in columns:
                positions[position] = board[row][col]
                position += 1
            columns.reverse()
        
        visited = { 1 }
        queue = deque([ 1 ])
        level = 0
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                current_position = queue.popleft()
                
                if current_position == no_of_positions:
                    return level
                
                next_positions = [ current_position + i for i in range(1, 7) if current_position + i <= no_of_positions]
                for next_position in next_positions:
                    if positions[next_position] != -1:
                        next_position = positions[next_position]
                    
                    if next_position not in visited:
                        visited.add(next_position)
                        queue.append(next_position)
            level += 1
        
        return -1
            