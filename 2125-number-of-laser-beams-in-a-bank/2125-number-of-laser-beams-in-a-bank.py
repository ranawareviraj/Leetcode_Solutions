class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m, n = len(bank), len(bank[0])
        row_wise_count = [0] * m

        for i, row in enumerate(bank):
            for cell in row:
                row_wise_count[i] += int(cell)
        
        total = 0
        prev_row_count = row_wise_count[0]
        for i in range(1, m):
            if row_wise_count[i] > 0:
                total += prev_row_count * row_wise_count[i]
                prev_row_count = row_wise_count[i]
        
        return total

'''        
row_count => security_devices
iterate if next one has security_devices => mul and add
'''