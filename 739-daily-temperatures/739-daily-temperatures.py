class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stack_index, stack_temp = stack.pop()
                answer[stack_index] = index - stack_index
            stack.append((index, temp))
        return answer