class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                sub_string = ""
                while stack and stack[-1] != '[':
                    sub_string = stack.pop() + sub_string
                stack.pop() # removes the open parentheses
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * sub_string)
        return "".join(stack)