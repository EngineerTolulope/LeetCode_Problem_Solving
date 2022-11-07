class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dx, dy = 0, 1   # direction x, y
        x, y = 0, 0
        for i in instructions:
            if i == 'G':
                x, y = x + dx, y + dy
            elif i == 'L':
                dx, dy = -1 * dy, dx
            else:
                dx, dy = dy, -1 * dx
                
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)