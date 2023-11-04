class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def is_valid(r, c):
            return 0 <= r < m and 0 <= c < n

        # DFS from boundaries marking all zeroes
        def dfs(row, col):
            if not is_valid(row, col) or board[row][col] != 'O':
                return

            board[row][col] = '#'

            for dx, dy in directions:
                nr, nc = row + dy, col + dx
                dfs(nr, nc)

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m, n = len(board), len(board[0])

        # Mark 'O's on the edges (and all zeroes of that connected component) with '#' 
        for row in range(m):
            for col in range(n):
                # Start DFS from edge cell with value 0
                if (row == 0 or col == 0 or row == m - 1 or col == n - 1) and board[row][col] == 'O':
                    dfs(row, col)

        # Convert remaining 'O's to 'X' and restore '#' to 'O'
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '#':
                    board[row][col] = 'O'
