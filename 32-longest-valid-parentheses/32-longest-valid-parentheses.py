class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, result = [-1], 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    result = max(result, (i - stack[-1]))
        return result
        

        
#         if not s or len(s) == 1:
#             return 0
        
#         stack, result = [], 0
#         left, right = 0, 0
#         while left <= right and right != len(s):
#             if s[right] == '(':
#                 stack.append(right)
#                 right += 1
#             else:
#                 if stack and stack[-1] == '(':
#                     stack.pop()
#                     result = max(result, right - left + 1)
#                     right += 1
#                 else:
#                     left = right - 1
#                     right = right + 1
#         return result
                    