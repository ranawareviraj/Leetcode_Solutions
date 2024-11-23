class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def cound_negative_numbers(row):
            left, right = 0, len(row) - 1
            while left < right:
                mid = (left + right) // 2
                if row[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid
            return (len(row) - right) if row[right] < 0 else 0

        result = 0
        for row in grid:
            result += cound_negative_numbers(row)

        return result
