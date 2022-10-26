class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        char_list, stack = list(s), []
        for i in range(len(char_list)):
            char = char_list[i]
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    char_list[i] = ''
        
        for i in stack:
            char_list[i] = ''
        return ''.join(char_list)