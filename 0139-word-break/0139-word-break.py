class Solution:
    def wordBreak(self, s: str, word_dict: List[str]) -> bool:
        def can_construct(s, word_dict, memo):
            if s == "":
                return True
            if s in memo:
                return memo[s]
            
            for word in word_dict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if can_construct(new_s, word_dict, memo):
                        memo[new_s] =  True
                        return True
            
            memo[s] = False
            return False

        memo = {}
        return can_construct(s, word_dict, memo)
        