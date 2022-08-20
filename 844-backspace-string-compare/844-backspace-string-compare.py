class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack, t_stack = [], []
        
        for char in s:
            if char == '#' and s_stack:
                s_stack.pop()
            else:
                if char != '#':
                    s_stack.append(char)
        
        for char in t:
            if char == '#' and t_stack:
                t_stack.pop()
            else:
                if char != '#':
                    t_stack.append(char)
        
        return s_stack == t_stack
        
            
            