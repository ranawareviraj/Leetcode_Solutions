class Solution:
    def maxPower(self, s: str) -> int:
        count = max_count = 0
        prev_char = s[0]

        for ch in s:
            if ch == prev_char:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
                prev_char = ch
        
        return max_count
