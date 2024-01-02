class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        row = [1]
        ans.append(row)
        row_num = 1

        while row_num < numRows:
            next_row = [0] * (len(row) + 1)
            row = [0] + row + [0]

            for i in range(len(next_row)):
                next_row[i] = row[i] + row[i + 1]
                
            ans.append(next_row)
            row = next_row
            row_num += 1    
        return ans
        