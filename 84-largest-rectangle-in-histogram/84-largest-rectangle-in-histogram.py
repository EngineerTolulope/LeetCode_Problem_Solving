class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []  # (index, height)
        
        for i, current_height in enumerate(heights):
            start_index = i
            while stack and stack[-1][1] > current_height:
                index, height = stack.pop()
                area = height * (i - index)
                max_area = max(max_area, area)
                start_index = index
            stack.append((start_index, current_height))
            
        for i, height in stack:
            area = height * (len(heights) - i)
            max_area = max(max_area, area)
        return max_area
            
            