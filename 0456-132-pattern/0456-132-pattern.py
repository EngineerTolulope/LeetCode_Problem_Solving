class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # pair (num, min_left), mono decreasing
        current_min = sys.maxsize

        for num in nums:
            while stack and num >= stack[-1][0]:
                stack.pop()
            if stack and num > stack[-1][1]:
                return True
            
            stack.append((num, current_min))
            current_min = min(num, current_min)
        return False