class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        
        return 3 ** int(log(2**31, 3)) % n == 0