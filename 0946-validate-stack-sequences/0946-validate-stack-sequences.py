class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        index = 0

        for num in pushed:
            stack.append(num)

            if index < len(popped) and stack and stack[-1] == popped[index]:
                stack.pop()
                index += 1
        return len(stack) == 0