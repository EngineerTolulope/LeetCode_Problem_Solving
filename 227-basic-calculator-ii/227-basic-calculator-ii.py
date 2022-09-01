class Solution:
    def calculate(self, s: str) -> int: 
        if not s:
            return 0
        
        operators = {'+', '-', '*', '/'}
        current_num, previous_operator, stack = 0, '+', []
        for i in range(len(s)):
            char = s[i]
            if char == ' ' and i != len(s) - 1:
                continue
            
            if char.isdigit():
                current_num = current_num * 10 + int(char)
                
            if char in operators or i == len(s) - 1:
                if previous_operator == '+':
                    stack.append(current_num)
                elif previous_operator == '-':
                    stack.append(-current_num)
                elif previous_operator == '*':
                    stack[-1] *= current_num
                elif previous_operator == '/':
                    stack[-1] = int(stack[-1]/current_num)
                current_num = 0
                previous_operator = char
        return sum(stack)
            
            