from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        letter_to_indices = defaultdict(list)

        for index, ch in enumerate(t):
            letter_to_indices[ch].append(index)
        
        curr_match_index = -1
        for ch in s:
            if ch not in letter_to_indices:
                return False

            indices_list = letter_to_indices[ch]
            match_index = bisect.bisect_right(indices_list, curr_match_index)
            if match_index != len(indices_list):
                curr_match_index = indices_list[match_index]
            else:
                return False
            
        return True

