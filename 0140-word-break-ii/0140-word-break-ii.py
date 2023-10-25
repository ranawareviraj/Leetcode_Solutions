class Solution:
    def wordBreak(self, sentence: str, word_dict: List[str]) -> List[str]:
        n = len(sentence)
        dp = [ None ] * (n + 1)
        dp[0] = [[]]

        for i in range(n + 1):
            if dp[i] != None:
                for word in word_dict:
                    m = len(word)
                    new_sentence = sentence[i : i + m]
                    if new_sentence.startswith(word):
                        new_combinations = []
                        for combination in dp[i]:
                            new_combination = combination[:]
                            new_combination.append(word)
                            new_combinations.append(new_combination)
                        if dp[i + m] == None:
                            dp[i + m] = new_combinations
                        else:
                            dp[i + m] += new_combinations
        result = []
        if dp[n] != None:
            for word_group in dp[n]:
                sentence_formed = " ".join(word_group)
                result.append(sentence_formed)
        
        return result