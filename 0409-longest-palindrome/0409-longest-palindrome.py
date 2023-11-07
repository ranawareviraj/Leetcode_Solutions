class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        total_count = 0
        odd_counted = False

        for ch in counter:
            count = counter[ch]
            total_count += count - count % 2

            if not odd_counted and count % 2 != 0:
                total_count += 1
                odd_counted = True

        return total_count