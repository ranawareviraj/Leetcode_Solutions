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
        ans = ""

        for i in range(n):
            ans = find_longest_palindrome(s, i, i, ans)
            ans = find_longest_palindrome(s, i, i + 1, ans)
        
        return ans

