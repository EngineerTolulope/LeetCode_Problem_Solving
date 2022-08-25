class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, stack = [], []
        
        def backtracking(open_count, closed_count):
            if open_count == closed_count == n:
                result.append("".join(stack))
                return
            
            if open_count < n:
                stack.append('(')
                backtracking(open_count + 1, closed_count)
                stack.pop()
            if closed_count < open_count:
                stack.append(')')
                backtracking(open_count, closed_count + 1)
                stack.pop()
        
        
        backtracking(0, 0)
        return result
        