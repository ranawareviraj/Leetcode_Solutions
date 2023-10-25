class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [ False ] * (n + 1)
        dp[0] = True

        for i in range(n + 1):
            if dp[i] == True:
                for word in wordDict:
                    m = len(word)
                    new_target = s[i : i + m]
                    if new_target.startswith(word):
                        dp[i + m] = True
        
        return dp[n]