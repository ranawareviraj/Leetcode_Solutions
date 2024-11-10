class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(sub_str):
            left = 0
            right = len(sub_str) - 1

            while left < right:
                if sub_str[left] != sub_str[right]:
                    return False
                left += 1
                right -= 1
            
            return True

        n = len(s)
        max_length = 0
        max_str = ""
        for start in range(n):
            for end in range(start, n):
                sub_str = s[start : end + 1]
                if len(sub_str) > max_length and is_palindrome(sub_str):
                    max_length, max_str = max(0, end - start + 1), sub_str
        
        return max_str