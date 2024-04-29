class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) - Counter(t) == Counter(t) - Counter(s) == {}
