class Solution:
    def isPowerOfTwo(self, n):
        if n == 0: return False
        if n == 1: return True
        if n % 2 != 0: return False

        x = n // 2
        return self.isPowerOfTwo(x)