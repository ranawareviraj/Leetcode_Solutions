class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        prev_one = 0  
        prev_two = 1

        for i in range(2, (n + 2)):
            prev_two, prev_one = prev_one, prev_one + prev_two
        return prev_one
