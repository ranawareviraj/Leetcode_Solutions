class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_counter = Counter(s)
        steps = 0

        for ch in t:
            if s_counter[ch] > 0:
                s_counter[ch] -= 1
            else:
                steps += 1
        
        return steps