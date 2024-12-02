class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse(word):
            reversed_word = []
            for ch in word:
                reversed_word.append(ch)
            return "".join(reversed(reversed_word))
        
        words = s.split(" ")
        result = []
        for word in words:
            result.append(reverse(word))
        
        return " ".join(result)