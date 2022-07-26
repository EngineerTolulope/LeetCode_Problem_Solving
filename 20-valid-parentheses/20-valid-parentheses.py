class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToopen = {")" : "(", "}" : "{", "]" : "["}     # Creates an hash mapping close parentheses  to open ones
        
        for part in s:
            if part not in closeToopen:     # If it is not a key in the hash then it's an open parentheses
                stack.append(part)
            else:
                if len(stack) != 0 and stack[-1] == closeToopen[part]:
                    stack.pop()
                else:
                    return False
                
        return True if len(stack) == 0 else False
                
            
            
        