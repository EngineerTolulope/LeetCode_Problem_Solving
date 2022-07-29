class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '*':
                stack.append(stack.pop() * stack.pop())
            elif char == '-':
                num_1, num_2 = stack.pop(), stack.pop() # [5, 3] -> 5-3
                stack.append(num_2 - num_1)
            elif char == '/':
                num_1, num_2 = stack.pop(), stack.pop() # [5, 3] -> 5/3
                stack.append(int(num_2 / num_1))                
            else:
                stack.append(int(char))
        
        return stack.pop()