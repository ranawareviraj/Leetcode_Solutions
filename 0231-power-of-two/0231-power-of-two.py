class Solution:
    def isPowerOfTwo(self, n):
        if n == 0: return False
        if n % 2 == 0:
            n = self.isPowerOfTwo(n // 2)
        return n == 1