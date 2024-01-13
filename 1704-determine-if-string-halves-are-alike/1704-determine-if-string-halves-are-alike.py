class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        if len(s) %2 != 0:
            return False
        
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s) // 2
        count = 0

        for i in range(n):
            if s[i] in vowels:
                count += 1
        print(count)
        for i in range(n, len(s)):
            if s[i] in vowels:
                if count == 0:
                    return False
                count -= 1
   
        return count == 0

