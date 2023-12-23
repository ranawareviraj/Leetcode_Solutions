class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        result = []
        for ch in s:
            if ch not in vowels:
                result.append(ch)
        
        return "".join(result)