class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)







"""
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        return len(s_counter - t_counter) == 0 and len(t_counter - s_counter) == 0
"""