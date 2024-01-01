class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x = y = direction = 0
        
        for instruction in instructions:
            # Anti-clockwise by 1 = clockwise 3
            if instruction == 'L':
                direction = (direction + 3) % 4
            # Go clockwise by 1
            elif instruction == 'R':
                direction = (direction + 1) % 4
            else:
                x += directions[direction][0]
                y += directions[direction][1]

        # After 4 cycles, check if either
        # - ROBOT return to original position or
        # - it changes its direction
        return (x == y == 0) or (direction != 0)