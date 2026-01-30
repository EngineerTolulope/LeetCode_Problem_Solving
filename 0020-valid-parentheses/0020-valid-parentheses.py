class Solution:
    def isValid(self, s: str) -> bool:
        closeToopen = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []
        for char in s:
            if char in closeToopen: #close bracket
                if stack and closeToopen[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:   #open bracket
                stack.append(char)
    
        return not stack