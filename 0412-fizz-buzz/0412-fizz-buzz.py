class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        
        for i in range(1, n + 1):
            message = []
            if i % 3 == 0:
                message.append("Fizz")
            if i % 5 == 0:
                message.append("Buzz")

            if len(message) == 0:
                message.append(str(i))

            result.append("".join(message))
        
        return result