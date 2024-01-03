class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total = prev = 0

        for i, row in enumerate(bank):
            curr = 0
            for cell in row:
                if cell == '1':
                    curr += 1
            
            if curr > 0:
                total += prev * curr
                prev = curr
        
        return total