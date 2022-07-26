class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1    # Starts left and right pointers at begining and end respectively
        max_area = 0    
        
        while left < right:
            area = (right - left) * min(height[left], height[right])    # Width multiplies by the minimum height
            max_area = max(area, max_area)  # Takes only the maximum area
            
            # Since we are trying to get the max height we move the one with the shortest height
            if height[left] < height[right]:    
                left += 1
            else:
                right -= 1
        return max_area
                
            