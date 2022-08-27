class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix) - 1
        
        while left < right:
            top, bottom = left, right
            for i in range(right - left):
                top_left_value = matrix[top][left + i]
                
                matrix[top][left + i] = matrix[bottom - i][left]    # replace top left
                matrix[bottom - i][left] = matrix[bottom][right - i]    # replace bottom left
                matrix[bottom][right - i] = matrix[top + i][right]  # replace bottom right
                matrix[top + i][right] = top_left_value # replace top right        
            left += 1
            right -= 1
        return matrix