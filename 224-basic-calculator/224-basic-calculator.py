class Solution:
    def calculate(self, s: str) -> int:
        total, sign, stack = 0, 1, []
        
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + (ord(s[i]) - ord('0'))
                    i += 1
                total += num * sign
                i -= 1
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(total)
                stack.append(sign)
                total = 0
                sign = 1
            elif s[i] == ')':
                total = stack.pop() * total
                total += stack.pop()            
            i += 1

        return total