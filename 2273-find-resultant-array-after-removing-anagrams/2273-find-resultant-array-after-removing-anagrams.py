from collections import Counter

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def is_anagram(word1, word2):
            return Counter(word1) == Counter(word2)

        stack = [words[0]]
        for i in range(1, len(words)):
            if not is_anagram(words[i], stack[-1]):
                stack.append(words[i])

        return stack
        