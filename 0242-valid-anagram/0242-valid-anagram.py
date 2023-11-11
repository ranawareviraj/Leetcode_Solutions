class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(Counter(s) - Counter(t)) == 0 and len(Counter(t) - Counter(s)) == 0















"""
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        return len(s_counter - t_counter) == 0 and len(t_counter - s_counter) == 0
"""