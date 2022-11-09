class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for char in num:
            while k > 0 and stack and stack[-1] > char:
                stack.pop()
                k -= 1
            stack.append(char)
            
        stack = stack[:len(stack) - k]
        result = ''.join(stack)
        return str(int(result)) if result else '0'
        