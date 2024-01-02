class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and log(num, 2) % 2 == 0