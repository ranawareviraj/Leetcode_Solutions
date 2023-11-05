class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        no_of_positions = n * n

        #Pre-Processing
        # Create position array of size n^2 and update row, col no for each position
        positions = [None] * (no_of_positions + 1)
        position = 1
        columns = list(range(n))
        for row in range(n - 1, -1, -1):
            for col in columns:
                positions[position] = (row, col)
                position += 1
            columns.reverse()

        # Initialize queue with start position (pos = 0)
        queue = deque([1])
        level = 0
        seen =  {1}

        # BFS
        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                current_position = queue.popleft()

                if current_position == no_of_positions:
                    return level

                for next in range(1, 7):
                    next_position = current_position + next
                    if next_position <= no_of_positions:
                        next_row, next_col = positions[next_position]
                        if board[next_row][next_col] != -1:
                            next_position = board[next_row][next_col]
                            # next_row, next_col = positions[next_position]
                        if next_position not in seen:
                            seen.add(next_position)
                            queue.append(next_position)
                
            level += 1
            # For each level
            #   - if current is in bound
            #   - Get the next position => row, col on the board
            #   - If snake or ladder => move to next position
            #   - If reached target, return current level
            # If position not visited, add it to visited set
            # Increment level
        return -1
'''        
[
    [-1,-1],
    [-1,3]
]
'''
