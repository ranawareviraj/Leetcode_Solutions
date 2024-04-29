class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_counter = Counter(s)

        for ch in t:
            if ch in s:
                s_counter[ch] -= 1
                if s_counter[ch] == 0:
                    del s_counter[ch]
            else:
                return ch
        
        return [ch for ch in s_counter][0]