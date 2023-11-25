class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        def backtrack(target, curr):
            if target == '':
                result.append(curr[:])
                return
            
            for word in wordDict:
                if target.startswith(word):
                    curr.append(word)
                    backtrack(target[len(word) : ], curr)
                    curr.pop()

        result = []
        backtrack(s, [])
        
        sentences = []
        for word_list in result:
            sentence = " ".join(word_list)
            sentences.append(sentence)
        
        return sentences
        