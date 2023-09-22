class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # Stack to store tuples of (character, count)
    
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1] = (char, stack[-1][1] + 1)  # Update count for the top element
            else:
                stack.append((char, 1))  # Add a new tuple to the stack
            
            if stack[-1][1] == k:
                stack.pop()  # Remove the top element if count reaches k
        
        result = ""
        for char, count in stack:
            result += char * count
        
        return result