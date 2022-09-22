class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for char in operations:
            if char == '+':
                sum_ = stack[-1] + stack[-2]
                stack.append(sum_)
            elif char == 'D':
                double = 2 * stack[-1]
                stack.append(double)
            elif char == 'C':
                stack.pop()
            else:
                stack.append(int(char))
        return sum(stack)