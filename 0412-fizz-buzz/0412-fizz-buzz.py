class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        
        for i in range(1, n + 1):
            message = ""
            
            if i % 3 == 0: message += "Fizz"
            if i % 5 == 0: message += "Buzz"
            
            if not message: message += str(i)

            result.append(message)
        
        return result