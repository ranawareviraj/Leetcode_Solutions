class Solution:
    def isPowerOfTwo(self, n):
        if n == 0: return False
        
        return n & (-n) == n