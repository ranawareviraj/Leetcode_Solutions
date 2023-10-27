class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find_longest_palindrome(s, left, right, longest_so_far):
            while (left >= 0 and right < n) and s[left] == s[right]:
                if (right - left + 1) > len(longest_so_far):
                    longest_so_far = s[left : right + 1]
                left -= 1
                right += 1
            return longest_so_far

        n = len(s)
        longest_palindrome = ""
        for i in range(n):
            longest_palindrome = find_longest_palindrome(s, i, i, longest_palindrome)
            longest_palindrome = find_longest_palindrome(s, i, i + 1, longest_palindrome)
        
        return longest_palindrome
