class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_longest_palindrome(s, left, right, longest_palindrome):
            while (left >= 0 and right < n) and s[left] == s[right]:
                if (right - left + 1) > len(longest_palindrome):
                    longest_palindrome = s[left : right + 1]
                left -= 1
                right += 1
            return longest_palindrome

        n = len(s)
        longest_palindrome = ""
        for i in range(n):
            # Find all odd length palindromes centered at i th character
            # left =  right = i
            longest_palindrome = find_longest_palindrome(s, i, i, longest_palindrome)

            # Find all even length palindromes centered at i th and (i + 1) th characteres
            # left = i, right = i + 1
            longest_palindrome = find_longest_palindrome(s, i, i + 1, longest_palindrome)
        
        return longest_palindrome

# https://www.youtube.com/watch?v=XYQecbcd6_c&ab_channel=NeetCode