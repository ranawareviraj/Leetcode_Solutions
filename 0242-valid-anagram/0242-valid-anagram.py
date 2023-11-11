class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = collections.Counter(s)

        for ch in t:
            if ch not in s_counter:
                return False

            s_counter[ch] -= 1

            if s_counter[ch] == 0:
                del s_counter[ch]

        return len(s_counter) == 0