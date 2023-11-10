class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)

        for asteroid in asteroids:
            is_current_destroyed = False

            while stack and (stack[-1] > 0 and asteroid < 0):
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                    continue
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    is_current_destroyed = True
                    break
                else:
                    is_current_destroyed = True
                    break

            if not is_current_destroyed:
                stack.append(asteroid)
        
        return stack
                    