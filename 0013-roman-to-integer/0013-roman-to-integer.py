class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        prev_ch = s[-1]
        number = 0
        for ch in reversed(s):
            if map[ch] < map[prev_ch]:
                number -= map[ch]
            else:
                number += map[ch]
            prev_ch = ch
        
        return number
            
