class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        S_BOUND, T_BOUND = len(s), len(t)
        
        def is_subsequence(s_index, t_index):
            if s_index == S_BOUND:
                return True
            if t_index == T_BOUND:
                return False
            
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1

            return is_subsequence(s_index, t_index)
        
        return is_subsequence(0, 0)