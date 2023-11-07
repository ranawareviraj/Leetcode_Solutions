class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(col, diagonals, anti_diagonals, rows):
            if col == n:
                return 1
            
            solutions = 0

            for row in range(n):
                diagonal = (row - col)
                anti_diagonal = (row + col)

                if ((row not in rows) and 
                    (diagonal not in diagonals) and 
                    (anti_diagonal not in anti_diagonals)):

                    rows.add(row)
                    diagonals.add(diagonal)
                    anti_diagonals.add(anti_diagonal)

                    solutions += backtrack(col + 1, diagonals, anti_diagonals, rows)

                    rows.remove(row)
                    diagonals.remove(diagonal)
                    anti_diagonals.remove(anti_diagonal)
            
            return solutions
        
        return backtrack(0, set(), set(), set())
