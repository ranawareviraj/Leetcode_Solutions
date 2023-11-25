class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dp(target, word_dict, memo = {}):
            if target in memo:
                return memo[target]
            
            if target == '':
                return True
            
            for word in word_dict:
                if target.startswith(word):
                    remaining = target[len(word) : ]
                    if dp(remaining, word_dict, memo):
                        memo[target] = True
                        return memo[target]
            
            memo[target] = False
            return False
        
        return dp(s, wordDict)