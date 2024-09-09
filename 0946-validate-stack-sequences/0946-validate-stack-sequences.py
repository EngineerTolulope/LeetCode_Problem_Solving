from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_index = 0
        
        for num in pushed:
            stack.append(num)
            
            # Pop from stack while the top of the stack matches the next element in popped
            while stack and pop_index < len(popped) and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        
        # If the stack is empty, all elements were matched correctly
        return not stack
