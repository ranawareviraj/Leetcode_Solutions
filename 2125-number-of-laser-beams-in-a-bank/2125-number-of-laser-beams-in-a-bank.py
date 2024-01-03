class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = prev_row_count = curr_row_count = 0

        for i, row in enumerate(bank):
            for cell in row:
                curr_row_count += int(cell)
            
            if curr_row_count > 0:
                total += prev_row_count * curr_row_count
                prev_row_count = curr_row_count
                curr_row_count = 0
        
        return total