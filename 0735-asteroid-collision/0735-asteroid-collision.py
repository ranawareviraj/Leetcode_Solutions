class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)

        for asteroid in asteroids:
            is_current_destroyed = False

            while stack and (stack[-1] > 0 and asteroid < 0):
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                # If current asteroid is destroyed, break out of the loop
                elif abs(asteroid) <= abs(stack[-1]):
                    is_current_destroyed = True
                    # Before breaking, check if top us same as current,
                    # If yes, destroy top as well
                    if abs(asteroid) == abs(stack[-1]):
                        stack.pop()
                    break

            # If current asteroid is not yet destroyed push it onto stack
            if not is_current_destroyed:
                stack.append(asteroid)
        
        return stack
                    