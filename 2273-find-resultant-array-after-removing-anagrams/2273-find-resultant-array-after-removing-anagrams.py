from collections import Counter

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def is_anagram(word1, word2):
            return Counter(word1) == Counter(word2)

        stack = [words[0]]
        for i, word in enumerate(words, 1):
            if not is_anagram(word, stack[-1]):
                stack.append(word)

        return stack
        