class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteriod in asteroids:
            while stack and stack[-1] > 0 and asteriod < 0: # condition to have a collision
                difference = asteriod + stack[-1]
                if difference < 0:  # new asteriod won
                    stack.pop()
                elif difference > 0: # old asteriod won
                    asteriod = 0
                else:   # both asteriods are of equal size
                    asteriod = 0
                    stack.pop()
            if asteriod:    # negative numbers are truthy
                stack.append(asteriod)
        return stack
                
                    